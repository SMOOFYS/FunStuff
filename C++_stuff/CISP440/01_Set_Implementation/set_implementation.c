// Aditya Shinde
// CISP 440 - Set Implementation
// 02/01/2026

#include <stdio.h>
#include <string.h>

// Universe for parts 3 & 4 (8 elements)
const char *universe[8] = {
    "Bat", "Cat", "Chimp", "Dog", "Fish", "Liger", "Snake", "Turtle"
};

// Universe for part 5 (12 elements)
const char *universe32[12] = {
    "Bat", "Dragon", "Hippopotamus", "Gecko", "Sloth", "Deer",
    "Kangaroo", "Rhinoceros", "Squirrel", "Platypus", "Horse", "Donkey"
};

void print_set(unsigned int s, const char **univ, int univ_size)
{
    int first = 1;
    printf("{");
    for (int i = 0; i < univ_size; i++) {
        if (s & (1u << i)) {
            if (!first) printf(", ");
            printf("%s", univ[i]);
            first = 0;
        }
    }
    printf("}");
}

unsigned int make_set(const char **names, int count, const char **univ, int univ_size) {
    unsigned int result = 0;
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < univ_size; j++) {
            if (strcmp(names[i], univ[j]) == 0) {
                result |= (1u << j);
                break;
            }
        }
    }
    return result;
}

unsigned int set_union(unsigned int a, unsigned int b)        { return a | b; }
unsigned int set_intersection(unsigned int a, unsigned int b) { return a & b; }
unsigned int set_difference(unsigned int a, unsigned int b)   { return a & ~b; }
unsigned int set_complement(unsigned int a, unsigned int mask) { return (~a) & mask; }

int is_subset(unsigned int a, unsigned int b) {
    return (a & ~b) == 0;
}

int is_proper_subset(unsigned int a, unsigned int b) {
    return is_subset(a, b) && a != b;
}

int cardinality(unsigned int s) {
    int count = 0;
    while (s) {
        count += s & 1;
        s >>= 1;
    }
    return count;
}

// Power set printer
void print_power_set(unsigned int target, const char **univ, int univ_size, const char *label) {
    int n = cardinality(target);
    int total = 1 << n;
    printf("%s:\n", label);

    int indices[32];
    int k = 0;
    for (int i = 0; i < univ_size; i++) {
        if (target & (1u << i)) indices[k++] = i;
    }

    for (int i = 0; i < total; i++) {
        int first = 1;
        printf("{");
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                if (!first) printf(", ");
                printf("%s", univ[indices[j]]);
                first = 0;
            }
        }
        printf("}\n");
    }
}

// Print subset relations
void print_subset_info(const char *nameA, unsigned int A,
                       const char *nameB, unsigned int B) {
    printf("%s C= %s : %s\n", nameA, nameB, is_subset(A, B) ? "true" : "false");
    printf("%s C= %s (proper) : %s\n", nameA, nameB, is_proper_subset(A, B) ? "true" : "false");
}

// Part 3
void do_part3() {
    unsigned int mask = (1u << 8) - 1;

    const char *a_names[] = {"Cat", "Dog", "Fish"};
    const char *b_names[] = {"Cat", "Dog", "Liger"};
    const char *c_names[] = {"Dog", "Liger", "Snake", "Turtle"};

    unsigned int A = make_set(a_names, 3, universe, 8);
    unsigned int B = make_set(b_names, 3, universe, 8);
    unsigned int C = make_set(c_names, 4, universe, 8);

    printf("\n=== Part 3 ===\n");
    printf("Set A: "); print_set(A, universe, 8); printf("\n");
    printf("Set B: "); print_set(B, universe, 8); printf("\n");
    printf("Set C: "); print_set(C, universe, 8); printf("\n\n");

    unsigned int res;
    res = set_intersection(set_union(A, B), set_complement(C, mask));
    printf("(A U B) N ~C: "); print_set(res, universe, 8); printf("\n");

    res = set_union(A, set_intersection(B, C));
    printf("A U (B N C): "); print_set(res, universe, 8); printf("\n");

    res = set_complement(set_intersection(A, B), mask);
    printf("~ (A N B): "); print_set(res, universe, 8); printf("\n");

    res = set_union(set_complement(A, mask), set_complement(B, mask));
    printf("~A U ~B: "); print_set(res, universe, 8); printf("\n");

    res = set_difference(A, B);
    printf("A - B: "); print_set(res, universe, 8); printf("\n");

    printf("\n");
    print_power_set(A, universe, 8, "PowerSet(A)");
    printf("\n");

    print_subset_info("A", A, "B", B);
    printf("\n");

    // my own two expressions
    res = set_union(set_intersection(A, C), B);
    printf("(A N C) U B: "); print_set(res, universe, 8); printf("\n");

    res = set_intersection(set_complement(A, mask),
                           set_intersection(set_complement(B, mask),
                                            set_complement(C, mask)));
    printf("~A N ~B N ~C: "); print_set(res, universe, 8); printf("\n");
}

// Part 4
void do_part4() {
    unsigned int mask = (1u << 8) - 1;

    const char *a_names[] = {"Bat", "Chimp", "Liger", "Snake", "Turtle"};
    const char *b_names[] = {"Bat", "Cat", "Chimp", "Dog", "Fish"};
    const char *c_names[] = {"Dog", "Fish", "Liger", "Snake", "Turtle"};

    unsigned int A = make_set(a_names, 5, universe, 8);
    unsigned int B = make_set(b_names, 5, universe, 8);
    unsigned int C = make_set(c_names, 5, universe, 8);

    printf("\n=== Part 4 ===\n");
    printf("Set A: "); print_set(A, universe, 8); printf("\n");
    printf("Set B: "); print_set(B, universe, 8); printf("\n");
    printf("Set C: "); print_set(C, universe, 8); printf("\n\n");

    unsigned int res;
    res = set_intersection(set_union(A, B), set_complement(C, mask));
    printf("(A U B) N ~C: "); print_set(res, universe, 8); printf("\n");

    res = set_union(A, set_intersection(B, C));
    printf("A U (B N C): "); print_set(res, universe, 8); printf("\n");

    res = set_complement(set_intersection(A, B), mask);
    printf("~ (A N B): "); print_set(res, universe, 8); printf("\n");

    res = set_union(set_complement(A, mask), set_complement(B, mask));
    printf("~A U ~B: "); print_set(res, universe, 8); printf("\n");

    res = set_difference(A, B);
    printf("A - B: "); print_set(res, universe, 8); printf("\n");

    printf("\n");
    print_power_set(A, universe, 8, "PowerSet(A)");
    printf("\n");

    print_subset_info("A", A, "B", B);
    print_subset_info("B", B, "C", C);
    printf("\n");

    // Two more original expressions
    res = set_difference(set_union(A, C), B);
    printf("(A U C) - B: "); print_set(res, universe, 8); printf("\n");

    res = set_intersection(set_union(A, B), set_complement(C, mask));
    printf("(A U B) N ~C (again): "); print_set(res, universe, 8); printf("\n");
}

// Part 5 — 32-bit demonstration
void do_part5() {
    unsigned int mask = (1u << 12) - 1;

    const char *a_names[] = {"Bat", "Dragon", "Hippopotamus", "Gecko", "Sloth", "Deer", "Kangaroo"};
    const char *b_names[] = {"Hippopotamus", "Gecko", "Sloth", "Bat", "Rhinoceros", "Squirrel", "Platypus"};
    const char *c_names[] = {"Gecko", "Sloth", "Bat", "Rhinoceros", "Horse", "Donkey"};

    unsigned int A = make_set(a_names, 7, universe32, 12);
    unsigned int B = make_set(b_names, 7, universe32, 12);
    unsigned int C = make_set(c_names, 6, universe32, 12);

    printf("\n=== Part 5 — 32-bit universe ===\n");
    printf("Set A: "); print_set(A, universe32, 12); printf("\n");
    printf("Set B: "); print_set(B, universe32, 12); printf("\n");
    printf("Set C: "); print_set(C, universe32, 12); printf("\n\n");

    unsigned int res = set_intersection(set_union(A, B), set_complement(C, mask));
    printf("(A U B) N ~C: "); print_set(res, universe32, 12); printf("\n");

    res = set_union(A, set_intersection(B, C));
    printf("A U (B N C): "); print_set(res, universe32, 12); printf("\n");

    res = set_difference(A, B);
    printf("A - B: "); print_set(res, universe32, 12); printf("\n");

    printf("\nCardinality A: %d\n", cardinality(A));
    printf("Cardinality B: %d\n", cardinality(B));
    printf("Cardinality C: %d\n\n", cardinality(C));

    print_subset_info("A", A, "B", B);
    print_subset_info("C", C, "B", B);

    printf("\nPowerSet(A) has 128 elements — not printed (2^7).\n");
}

int main(void) {
    printf("Quick FYI: This program uses simplified notation for set operations:\n");
    printf(" N = intersection\n");
    printf(" U = union\n");
    printf(" ~ = complement\n");
    printf(" C= = subset or equal / is a subset (including improper)\n");
    printf(" - = difference\n");
    printf("These symbols are used over special math characters simply for convenience.\n\n");

    printf("CISP 440 Homework 1.42 — Set Operations with Bit Vectors\n\n");

    do_part3();
    do_part4();
    do_part5();

    printf("\nAll tests completed.\n");
    return 0;
}
