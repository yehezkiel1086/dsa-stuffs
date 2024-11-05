#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int tot = 0;
    while(n) {
        tot += n % 10;
        n /= 10;
    }
    printf("%d", tot);
    return 0;
}