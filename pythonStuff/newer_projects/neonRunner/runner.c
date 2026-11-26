#include <stdio.h>
#include <string.h>

#define MAX_STATES 100
#define MAX_PAT_LEN 50

int state_table[MAX_STATES][2];
char pattern[MAX_PAT_LEN];
int m;

void generate_state_table() {
    for (int k = 0; k <= m; k++) {
        for (int idx = 0; idx < 2; idx++) {
            char c = 'a' + idx;
            char temp[MAX_PAT_LEN + 2];
            strncpy(temp, pattern, k);
            temp[k] = c;
            temp[k + 1] = '\0';

            int next_st = 0;
            int max_l = (k + 1 <= m) ? k + 1 : m;
            for (int l = max_l; l >= 0; l--) {
                if (l == 0 || strncmp(pattern, temp + (k + 1 - l), l) == 0) {
                    next_st = l;
                    break;
                }
            }
            state_table[k][idx] = next_st;
        }
    }
}

void print_generating() {
    printf("Generating state table for %s...\n", pattern);
    for (int k = 0; k <= m; k++) {
        printf("state %d ", k);
        for (int idx = 0; idx < 2; idx++) {
            char c = 'a' + idx;
            char temp[MAX_PAT_LEN + 2];
            strncpy(temp, pattern, k);
            temp[k] = c;
            temp[k + 1] = '\0';
            printf("%s goto %d  ", temp, state_table[k][idx]);
        }
        printf("\n");
    }
}

void print_complete_table() {
    printf("\nComplete state table for %s...\n", pattern);
    printf("s\ta\tb\n\n");
    for (int s = 0; s <= m; s++) {
        printf("%d\t%d\t%d\n", s, state_table[s][0], state_table[s][1]);
    }
}

void search_in_file(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Cannot open file %s\n", filename);
        return;
    }
    printf("\nThe string %s was found at locations: ", pattern);
    int state = 0;
    long pos = 0;
    int ch;
    int first = 1;
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == 'a' || ch == 'b') {
            pos++;
            state = state_table[state][ch - 'a'];
            if (state == m) {
                if (!first) printf(", ");
                printf("%ld", pos);
                first = 0;
            }
        }
    }
    fclose(fp);
    if (first) printf("none");
    printf("\n");
}

int main() {
    /* Sample (exactly matches the assignment sample output) */
    strcpy(pattern, "abab");
    m = strlen(pattern);
    generate_state_table();
    print_generating();
    print_complete_table();
    search_in_file("abab.txt");

    /* The 5 required strings in monkeydata.txt */
    char patterns[5][MAX_PAT_LEN] = {
        "abbbbbbaaaaaba",
        "abbbbaabbbbaaa",
        "aaaaaaabaaaaaaa",
        "aabbbababaaababbaaaa",
        "aaaabababaaaaabbaaaa"
    };

    for (int i = 0; i < 5; i++) {
        strcpy(pattern, patterns[i]);
        m = strlen(pattern);
        generate_state_table();
        print_generating();
        print_complete_table();
        search_in_file("monkeydata.txt");
    }

    return 0;
}