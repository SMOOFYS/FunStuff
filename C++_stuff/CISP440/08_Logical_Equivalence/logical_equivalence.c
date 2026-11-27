// CISP 440 - HW 8.42 Logical Equivalence IMPLEMENTATION
// Aditya Shinde
// March 22, 2026

#include <stdio.h>
#include <stdbool.h>

// logical functions
bool Implication(bool a, bool b) { return !a || b; }
bool Bicondition(bool a, bool b) { return a == b; }
bool Maybe(bool a, bool b) { return !a || b; } // i jus did smth random
bool Because(bool a, bool b) { return a && !b; } // i jus did smth random
bool And(bool a, bool b) { return a && b; }
bool Or(bool a, bool b) { return a || b; }
bool Xor(bool a, bool b) { return a != b; }
bool Not(bool a) { return !a; }

int main()
{

    int p, q, r;
    bool equiv;

    // a
    printf("p q | p | q | ~(~p & ~q)\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {

            bool left = Or(p, q);
            bool right = Not(And(Not(p), Not(q)));

            if (left != right)
                equiv = false;

            printf("%d %d | %d | %d\n", p, q, left, right);
        }
    }
    if (equiv)
        printf("Equivalent\n\n");
    else
        printf("Not Equivalent\n\n");

    // b
    printf("p q r | p & (q -> r) | (p & q) ^ r\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {

            for (r = 0; r < 2; r++)
            {

                bool left = And(p, Implication(q, r));
                bool right = Xor(And(p, q), r);

                if (left != right)
                    equiv = false;

                printf("%d %d %d | %d | %d\n", p, q, r, left, right);
            }
        }
    }
    if (equiv)

        printf("Equivalent\n\n");
    else

        printf("Not Equivalent\n\n");

    // c
    printf("p q | p <-> q | ~(p ^ q)\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {

            bool left = Bicondition(p, q);
            bool right = Not(Xor(p, q));

            if (left != right)
                equiv = false;

            printf("%d %d | %d | %d\n", p, q, left, right);
        }
    }
    if (equiv)
        printf("Equivalent\n\n");
    else
        printf("Not Equivalent\n\n");

    // d
    printf("p q r | (p <-> q) -> r | p & (~q | r)\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {
            for (r = 0; r < 2; r++)
            {

                bool left = Implication(Bicondition(p, q), r);
                bool right = And(p, Or(Not(q), r));

                if (left != right)
                    equiv = false;

                printf("%d %d %d | %d | %d\n", p, q, r, left, right);

            }
        }
    }
    if (equiv)
        printf("Equivalent\n\n");
    else
        printf("Not Equivalent\n\n");

    // e
    printf("p q r | ~(p -> (q & r)) | p & ~(q & r)\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {

            for (r = 0; r < 2; r++)
            {

                bool left = Not(Implication(p, And(q, r)));
                bool right = And(p, Not(And(q, r)));

                if (left != right)
                    equiv = false;

                printf("%d %d %d | %d | %d\n", p, q, r, left, right);
            }
        }
    }
    if (equiv)

        printf("Equivalent\n\n");
    else

        printf("Not Equivalent\n\n");

    // f
    printf("p q | p | (p ? q) | p & (p @ q)\n");
    equiv = true;
    for (p = 0; p < 2; p++)
    {

        for (q = 0; q < 2; q++)
        {

            bool left = Or(p, Maybe(p, q));
            bool right = And(p, Because(p, q));

            if (left != right)
                equiv = false;

            printf("%d %d | %d | %d\n", p, q, left, right);
        }
    }
    if (equiv)
        printf("Equivalent\n\n");
    else
        printf("Not Equivalent\n\n");

    return 0;
}
