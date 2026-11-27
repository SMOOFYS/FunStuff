/*
 * CISP 440 - Spring 2026
 * Homework 5.42 - Matrix Implementation of Properties of Relations
 *
 * Student implementation in pure C
 * Reads R1.bin through R7.bin and reports reflexive/symmetric/transitive
 * and equivalence classes (if applicable)
 *
 * Format of .bin files:
 * first byte = n (size)
 * next n×n bytes = matrix entries (0 or 1), row-major order
 */

// Aditya Shinde
// 03/02/2026

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 40

int R[MAX][MAX];
int R2[MAX][MAX];
int captain[MAX];
int n;
void printMatrix(const int mat[MAX][MAX]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");

}

int isReflexive(const int mat[MAX][MAX]) {
    for (int i = 0; i < n; i++) {
        if (mat[i][i] == 0) return 0;
    }
    return 1;

}

int isSymmetric(const int mat[MAX][MAX]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[j][i]) return 0;
        }
    }
    return 1;

}

/* calc boolean matrix square */
void squareMatrix(const int mat[MAX][MAX], int result[MAX][MAX])
{

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n; k++) {
                if (mat[i][k] && mat[k][j]) {
                    result[i][j] = 1;
                    break;
                }
            }
        }
    }
}

int isTransitive(const int mat[MAX][MAX], const int sq[MAX][MAX])
{

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (sq[i][j] && !mat[i][j]) {
                return 0;
            }
        }

    }
    return 1;
}

/* Find equiv. class representatives ("captains")
   The cap'n of a class is the smallest-indexed member.
   Use fwd pass: if i is related to any j < i, then i is not cap'n.
 */

void findCaptains(const int mat[MAX][MAX]) {
    memset(captain, 0, sizeof(captain));

    for (int i = 0; i < n; i++) {

        int is_capt = 1;

        for (int j = 0; j < i; j++) {

            if (mat[i][j]) {             /* i ~ j and j < i  demote i */

                is_capt = 0;

                break;

            }

        }

        if (is_capt) captain[i] = 1;

    }

}
void printEquivalenceClasses(const int mat[MAX][MAX]) {
    printf("This is an equivalence relation\n");
    printf("The equivalence classes are:\n");

    for (int i = 0; i < n; i++) {
        if (captain[i]) {
            printf("{ ");
            for (int j = 0; j < n; j++) {
                if (mat[i][j]) {
                    printf("%d ", j);
                }
            }
            printf("}\n");
        }

    }
    printf("\n");
}

int main(void) {
    const char *files[] = {
        "R1.bin", "R2.bin", "R3.bin", "R4.bin", "R5.bin", "R6.bin", "R7.bin"
    };
    int num_files = 7;

    for (int f = 0; f < num_files; f++) {
        FILE *fp = fopen(files[f], "rb");
        if (!fp) {
            fprintf(stderr, "Cannot open %s\n", files[f]);
            continue;
        }

        unsigned char size_byte;
        if (fread(&size_byte, 1, 1, fp) != 1) {

            fprintf(stderr, "Cannot read size from %s\n", files[f]);
            fclose(fp);
            continue;
        }
        n = size_byte;

        if (n < 1 || n > MAX) {
            fprintf(stderr, "Invalid size %d in %s\n", n, files[f]);
            fclose(fp);
            continue;

        }

        /* Read n×n matrix */
        for (int i = 0; i < n; i++) {

            for (int j = 0; j < n; j++) {
                unsigned char val;
                if (fread(&val, 1, 1, fp) != 1) {
                    fprintf(stderr, "Incomplete read in %s\n", files[f]);
                    goto next_file;

                }
                R[i][j] = val; /* assume 0 or 1 */
            }
        }

    next_file:
        fclose(fp);

        printf("File: %s (n = %d)\n", files[f], n);
        printMatrix(R);

        int ref = isReflexive(R);
        int sym = isSymmetric(R);

        squareMatrix(R, R2);

        printf("The Product is:\n");
        printMatrix(R2);

        int tra = isTransitive(R, R2);

        if (ref)  printf("Reflexive\n");
        if (sym)  printf("Symmetric\n");
        if (tra)  printf("Transitive\n");

        if (ref && sym && tra) {
            findCaptains(R);
            printEquivalenceClasses(R);

        } else {
            printf("Not an equivalence relation\n\n");

        }
    }

    printf("Fin.\n");
    return 0;
}
