#include <stdio.h>
#include <time.h>

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    int iterations = 100000000;
    double number = 1.00000065;
    for (int i = 0; i < iterations; i++) {
        number *= 1.000000045;
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    printf("Execution time: %f seconds\n", cpu_time_used);
    
    return 0;
}