#include <stdio.h>
#include <math.h>

int main() {
    double x, s = 0.0, term;
    int n;

    printf("Enter the value of x (in radians): ");
    scanf("%lf", &x);

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int power = 2 * i + 1;
        
        long fact = 1;
        for (int j = 1; j <= power; j++) {
            fact *= j;
        }

        term = pow(-1, i) * pow(x, power) / fact;

        s += term;
    }

    printf("sin(%lf) ≈ %lf\n", x, s);

    return 0;
}
