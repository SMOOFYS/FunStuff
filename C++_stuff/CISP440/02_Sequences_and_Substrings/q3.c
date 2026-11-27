#include <stdio.h>

int main() {
    printf("All strings of length 3 over alphabet {a, b, c}\n\n{\n");

    char firstChar, secondChar, thirdChar;
    int totalCount = 0;

    for (firstChar = 'a'; firstChar <= 'c'; firstChar++) {
        for (secondChar = 'a'; secondChar <= 'c'; secondChar++) {
            for (thirdChar = 'a'; thirdChar <= 'c'; thirdChar++) {
                printf(" %c%c%c", firstChar, secondChar, thirdChar);
                totalCount++;
                if (totalCount % 9 == 0) {
                    printf("\n");
                } else {
                    printf(", ");
                }

            }
        }
    }

    printf("\n}\n");
    printf("(27 total combinations)\n");

    return 0;
}
