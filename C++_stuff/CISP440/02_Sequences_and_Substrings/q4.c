#include <stdio.h>

int main() {
    printf("Convert sentences to acronyms\n\n");

    char *testSentences[] = {
        "All the world is indeed a stage, and we are merely players.",
        "as soon as possible right now",
        "central processing unit",
        "do it yourself today",
        "laugh out loud my friend"

    };

    int testIndex;
    for (testIndex = 0; testIndex < 5; testIndex++) {

        char *currentSentence = testSentences[testIndex];
        int position = 0;

        printf("\"%s\"\n -> ", currentSentence);

        // First character
        if (currentSentence[0] != '\0') {

            char letter = currentSentence[0];
            if (letter >= 'a' && letter <= 'z') letter -= 32;
            if (letter >= 'A' && letter <= 'Z') printf("%c", letter);
        }

        while (currentSentence[position] != '\0') {
            if (currentSentence[position] == ' ' || currentSentence[position] == ',' ||
                currentSentence[position] == ';' || currentSentence[position] == '!') {

                position++;
                while (currentSentence[position] == ' ') position++;
                if (currentSentence[position] != '\0') {

                    char letter = currentSentence[position];
                    if (letter >= 'a' && letter <= 'z') letter -= 32;
                    if (letter >= 'A' && letter <= 'Z') printf("%c", letter);
                }
            }
            position++;
        }
        printf("\n\n");
    }

    return 0;
}
