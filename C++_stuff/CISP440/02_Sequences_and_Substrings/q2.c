#include <stdio.h>

int main() {
    printf("CISP 440 Homework 2.42 - Part 2\n");
    printf("Nilakantha series (double & float) + Leibniz comparison\n\n");

    double piNilakanthaDouble = 3.0;
    float piNilakanthaFloat = 3.0f;
    int currentSign = 1;
    double currentDenom = 2.0;

    double piLeibnizQuarter = 0.0;
    int leibnizSign = 1;

    printf(" iter    Nilkantha double    Nilkantha float    Leibniz\n");
    printf("~~~~~~ ~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~ ~~~~~~~~~\n");

    int iteration;
    int floatWarningShown = 0;

    for (iteration = 1; iteration <= 1000000; iteration++) {
        double termValue = 4.0 / (currentDenom * (currentDenom + 1.0) * (currentDenom + 2.0));
        piNilakanthaDouble += currentSign * termValue;
        piNilakanthaFloat += (float)(currentSign * termValue);

        double leibnizDenom = 2.0 * iteration - 1.0;
        piLeibnizQuarter += leibnizSign * (1.0 / leibnizDenom);
        leibnizSign = -leibnizSign;
        if (iteration == 1 || iteration == 5 || iteration == 20 || iteration == 100 ||
            iteration == 1000 || iteration == 10000 || iteration == 100000 || iteration == 1000000) {

            printf("%6d %.10f         %.10f       %.10f\n",
                   iteration, piNilakanthaDouble, piNilakanthaFloat, piLeibnizQuarter * 4.0);

        }

        if (!floatWarningShown && iteration > 200) {
            double difference = piNilakanthaDouble - (double)piNilakanthaFloat;
            if (difference > 0.000005 || difference < -0.000005) {
                printf("\n>>> Float starts deviating noticeably around iteration %d <<<\n", iteration);
                floatWarningShown = 1;

            }
        }

        currentSign = -currentSign;
        currentDenom += 2.0;
    }

    printf("\nObservations:\n");
    printf("a) Float usually begins losing accuracy vs double around 100,000–600,000 iterations\n");
    printf("b) Nilakantha converges much faster than Leibniz\n");
    printf(" (good accuracy in <50 terms vs millions needed for Leibniz)\n\n");

    return 0;
}
