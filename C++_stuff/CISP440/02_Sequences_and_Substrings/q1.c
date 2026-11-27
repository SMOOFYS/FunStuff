#include <stdio.h>

int main() {
    printf("First 55 terms of tn = n^2 - 1 (n starting from 2):\n\n");

    for (int n = 2; n <= 56; n++) {
        long long term = (long long)n * n - 1;
        printf("n=%2d  tn = %lld\n", n, term);

    }

    return 0;
}
