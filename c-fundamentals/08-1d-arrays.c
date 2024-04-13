#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n, tot = 0;
    scanf("%d", &n);
    while(n--) {
        int x;
        scanf("%d", &x);
        tot += x;
    }
    printf("%d", tot);
    return 0;
}