// CISP 440 - HW 12.42 Natural Language Generator Implementation
// Aditya Shinde
// April 25th, 2026

#include <iostream>
#include <string.h>
#include <time.h>
#pragma warning( disable : 4996 )
using namespace std;

//---------------------------------------------------------------------------
// Global string buffers (shared across all CFG runs)
//---------------------------------------------------------------------------
#define SIZE 10000
char w[SIZE];
char buf[SIZE];

//===========================================================================
// PRODUCTION TABLES P[nonterminal_row][alternative_col][production_string]
// Each row = one nonterminal (A=0, B=1, C=2, ...)
// Each column = one alternative; empty string "" terminates the list
//===========================================================================

// --- CFG 0 ------------------------------------------------------------------
char P0[][5][20] = {
    {"Bc", "", "", "", ""},   // A(0) -> Bc
    {"Cb", "l", "", "", ""},  // B(1) -> Cb | lambda
    {"Ba", "l", "", "", ""},  // C(2) -> Ba | lambda
};
char tTable0[][30] = {
    "he said ",   // a
    "she said ",  // b
    "you lie.",   // c
};
const char* start0 = "A";
const char* label0 = "CFG 0 (Part 1) - He Said / She Said";

// --- CFG 1 ------------------------------------------------------------------
char P1[][5][20] = {
    {"aBCoDF", "", "", "", ""},        // A(0) -> aBCoDF
    {"Bb",     "Bc", "Bd", "l", ""},   // B(1) -> Bb | Bc | Bd | lambda
    {"e",      "f", "g", "", ""},      // C(2) -> e | f | g
    {"E",      "EE", "EEE", "l", ""},  // D(3) -> E | EE | EEE | lambda
    {"h",      "i", "j", "", ""},      // E(4) -> h | i | j
    {"k",      "m", "n", "", ""},      // F(5) -> k | m | n
};

char tTable1[][30] = {
    "My ",            // a (index 0)
    "brother's ",     // b
    "uncle's ",       // c
    "sister's ",      // d
    "boss ",          // e
    "sorcerer ",      // f
    "hairdresser ",   // g
    "world-famous ",  // h
    "excellent ",     // i
    "hairy ",         // j
    "rockstar",       // k
    "",               // l = lambda
    "noodlehead",     // m
    "astronaut",      // n
    "is a ",          // o
};

const char* start1 = "A";
const char* label1 = "CFG 1 (Part 2) - My Brother's Boss";

// --- CFG 2 ------------------------------------------------------------------
char P2[][5][20] = {
    {"aBCDE", "", "", "", ""},        // A(0) -> aBCDE
    {"bc", "bd", "cb", "cd",""},      // B(1) -> bc | bd | cb | cd
    {"e",      "f", "g", "", ""},     // C(2) -> e | f | g
    {"h",      "i", "j", "", ""},     // D(3) -> h | i | j
    {"k",      "m", "l", "", ""},     // E(4) -> k | m | lambda
};

char tTable2[][30] = {
    "The ",     // a
    "brown ",   // b
    "lazy ",    // c
    "fat ",     // d
    "cow ",     // e
    "fish ",    // f
    "liger ",   // g
    "ran ",     // h
    "swam ",    // i
    "jumped ",  // j
    "high",     // k
    "",         // l = lambda
    "fast",     // m
};

const char* start2 = "A";
const char* label2 = "CFG 2 (Part 2) - The Brown Cow Jumped";

// --- CFG 3 (tTable needs 40 chars for long strings) -------------------------
// We use a separate expand function for this one (see below).
char P3[][5][20] = {
    {"Bmbnaoap", "", "", "", ""},  // A(0) -> Bmbnaoap
    {"Cmcnb", "l", "", "", ""},    // B(1) -> Cmcnb | lambda
    {"Dmdnc", "l", "", "", ""},    // C(2) -> Dmdnc | lambda
    {"Emend", "l", "", "", ""},    // D(3) -> Emend | lambda
    {"FmFne", "l", "", "", ""},    // E(4) -> FmFne | lambda
    {"mgnf",    "l", "", "", ""},  // F(5) -> mgnf | lambda
};

char tTable3[][40] = {
    "fly ",                                 // a
    "spider ",                              // b
    "mouse ",                               // c
    "cat ",                                 // d
    "dog ",                                 // e
    "liger ",                               // f
    "T-Rex ",                               // g
    "", "", "", "",                         // h i j k (unused)
    "",                                     // l = lambda
    "She swallowed the ",                   // m
    "to catch the ",                        // n
    "I don't know why she swallowed the ",  // o
    "perhaps she'll die.",                  // p
};

const char* start3 = "A";
const char* label3 = "CFG 3 (Part 2) - She Swallowed the Fly";

// --- CFG 4 (Part 3 - Original; tTable needs 50 chars) ----------------------
char P4[][5][20] = {
    {"BCD", "", "", "", ""},      // A(0) -> BCD
    {"a", "b", "c", "d", ""},     // B(1) -> a | b | c | d
    {"Ee", "Ef", "Eg", "", ""},   // C(2) -> Ee | Ef | Eg
    {"h", "Di", "Dj", "", ""},    // D(3) -> h | Di | Dj  (recursive)
    {"k", "m", "", "", ""},       // E(4) -> k | m
};

char tTable4[][50] = {
    "Scientists ",            // a
    "Astronomers ",           // b
    "NASA ",                  // c
    "Researchers ",           // d
    "discover ",              // e
    "confirm ",               // f
    "photograph ",            // g
    "a black hole",           // h
    ", 10 light-years away",  // i
    " in our galaxy",         // j
    "may have ",              // k
    "",                       // l = lambda (unused)
    "finally ",               // m
};

const char* start4 = "A";
const char* label4 = "CFG 4 (Part 3 - Original) - Space News Headlines";

//===========================================================================
// HELPER FUNCTIONS
//===========================================================================

// Returns the number of alternatives (cardinality) for one nonterminal row.
int Cardinality(char P[][5][20], int row)
{
    int col = 0;
    while (P[row][col][0])  // stop at first empty string
        col++;
    return col;
}

// Returns true if the string s still contains any Nonterminals (A-Z).
bool gotNs(char* s)
{
    for (int i = 0; s[i]; i++)
        if (s[i] >= 'A' && s[i] <= 'Z')
            return true;
    return false;
}

// Expands each terminal symbol in w to its human-readable string (30-char tTable).
void expand30(char* w, char tTable[][30])
{
    int i = 0;
    buf[0] = 0;
    while (w[i])
    {
        int index = w[i] - 'a';
        strcat(buf, tTable[index]);
        i++;
    }
    strcpy(w, buf);
}

// Overload for CFG3's 40-char tTable.
void expand40(char* w, char tTable[][40])
{
    int i = 0;
    buf[0] = 0;
    while (w[i])
    {
        int index = w[i] - 'a';
        strcat(buf, tTable[index]);
        i++;
    }
    strcpy(w, buf);
}

// Overload for CFG4's 50-char tTable.
void expand50(char* w, char tTable[][50])
{
    int i = 0;
    buf[0] = 0;
    while (w[i])
    {
        int index = w[i] - 'a';
        strcat(buf, tTable[index]);
        i++;
    }
    strcpy(w, buf);
}

//===========================================================================
// GENERALIZED CFG PROCESSOR
//
// runCFG drives the iterative production-replacement loop using the
// supplied tables. It does NOT need to change between CFGs.
// The only differences between CFG runs are the table arguments passed in.
//===========================================================================
void runCFG(char P[][5][20], char tTable[][30],
            const char* start, const char* label)
{
    strcpy(w, start);
    buf[0] = 0;

    cout << "\n========================================\n";
    cout << label << "\n";
    cout << "========================================\n";
    cout << "w = " << w << "\n";

    while (gotNs(w))
    {
        int i = 0;
        buf[0] = 0;

        while (w[i])                        // for each char in w
        {
            if (w[i] >= 'A' && w[i] <= 'Z')
            {
                // --- THE THREE FIXES FROM PART 1 ---
                int row = w[i] - 'A';         // index into P table
                int C = Cardinality(P, row);  // number of alternatives
                int col = rand() % C;         // pick one at random
                // -----------------------------------
                cout << " " << w[i] << " -> " << P[row][col] << "\n";
                strcat(buf, P[row][col]);     // copy chosen production
            }
            else                              // Terminal pass through
            {
                char lilbuf[3] = {w[i], 0};
                strcat(buf, lilbuf);
            }
            i++;
        }

        strcpy(w, buf);
        cout << "w = " << w << "\n";
    }

    expand30(w, tTable);
    cout << "\n>>> " << w << "\n";
}

// Variant for CFG 3 (40-char tTable)
void runCFG3(char P[][5][20], char tTable[][40],
             const char* start, const char* label)
{
    strcpy(w, start);
    buf[0] = 0;

    cout << "\n========================================\n";
    cout << label << "\n";
    cout << "========================================\n";
    cout << "w = " << w << "\n";

    while (gotNs(w))
    {
        int i = 0;
        buf[0] = 0;

        while (w[i])
        {
            if (w[i] >= 'A' && w[i] <= 'Z')
            {
                int row = w[i] - 'A';
                int C = Cardinality(P, row);
                int col = rand() % C;
                cout << " " << w[i] << " -> " << P[row][col] << "\n";
                strcat(buf, P[row][col]);
            }
            else
            {
                char lilbuf[3] = {w[i], 0};
                strcat(buf, lilbuf);
            }
            i++;
        }

        strcpy(w, buf);
        cout << "w = " << w << "\n";
    }

    expand40(w, tTable);
    cout << "\n>>> " << w << "\n";
}

// Variant for CFG 4 (50-char tTable)
void runCFG4(char P[][5][20], char tTable[][50],
             const char* start, const char* label)
{
    strcpy(w, start);
    buf[0] = 0;

    cout << "\n========================================\n";
    cout << label << "\n";
    cout << "========================================\n";
    cout << "w = " << w << "\n";

    while (gotNs(w))
    {
        int i = 0;
        buf[0] = 0;

        while (w[i])
        {
            if (w[i] >= 'A' && w[i] <= 'Z')
            {
                int row = w[i] - 'A';
                int C = Cardinality(P, row);
                int col = rand() % C;
                cout << " " << w[i] << " -> " << P[row][col] << "\n";
                strcat(buf, P[row][col]);
            }
            else
            {
                char lilbuf[3] = {w[i], 0};
                strcat(buf, lilbuf);
            }
            i++;
        }

        strcpy(w, buf);
        cout << "w = " << w << "\n";
    }

    expand50(w, tTable);
    cout << "\n>>> " << w << "\n";
}

// MAIN - Runs each CFG several times to show variety

int main(void)
{
    srand((unsigned)time(0));

    const int RUNS = 4;

    cout << "\n\n*** CISP 440 HW 12.42 - Natural Language CFG Generator ***\n";

    // Part 1 - CFG 0
    cout << "\n\n--- PART 1 ---\n";
    for (int r = 0; r < RUNS; r++)
        runCFG(P0, tTable0, start0, label0);

    // Part 2 - CFG 1, 2, 3
    cout << "\n\n--- PART 2 ---\n";
    for (int r = 0; r < RUNS; r++)
        runCFG(P1, tTable1, start1, label1);

    for (int r = 0; r < RUNS; r++)
        runCFG(P2, tTable2, start2, label2);

    for (int r = 0; r < RUNS; r++)
        runCFG3(P3, tTable3, start3, label3);

    // Part 3 - CFG 4
    cout << "\n\n--- PART 3 ---\n";
    for (int r = 0; r < RUNS; r++)
        runCFG4(P4, tTable4, start4, label4);

    return 0;
}
