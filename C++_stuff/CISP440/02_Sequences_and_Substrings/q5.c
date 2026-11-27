#include <stdio.h>
#include <string.h>

int main() {
    printf("All contiguous substrings - longest first from each starting position\n\n");

    char *testWords[] = {
        "aabbb",
        "supercalifragilisticexpialidocious"

    };

    int wordCount = 2;
    int wordIndex;

    for (wordIndex = 0; wordIndex < wordCount; wordIndex++) {
        char *currentString = testWords[wordIndex];
        int stringLength = strlen(currentString);

        printf("Input: \"%s\" (length %d)\n", currentString, stringLength);

        int startPos;
        for (startPos = 0; startPos < stringLength; startPos++) {

            int subLength;
            for (subLength = stringLength - startPos; subLength >= 1; subLength--) {

                printf(" ");
                int charIndex;
                for (charIndex = startPos; charIndex < startPos + subLength; charIndex++) {

                    printf("%c", currentString[charIndex]);
                }
                printf(",");
            }
            printf("\n");
        }
        printf("\n");
    }

    return 0;
}
