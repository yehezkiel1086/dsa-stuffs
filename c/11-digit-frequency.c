#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    char str[1010];
    scanf("%s", str);
    
    for(int i = 0; i < strlen(str); i++) {
        switch (str[i]) {
            case '0':
                arr[0]++;
                break;
            case '1':
                arr[1]++;
                break;
            case '2':
                arr[2]++;
                break;
            case '3':
                arr[3]++;
                break;
            case '4':
                arr[4]++;
                break;
            case '5':
                arr[5]++;
                break;
            case '6':
                arr[6]++;
                break;
            case '7':
                arr[7]++;
                break;
            case '8':
                arr[8]++;
                break;
            case '9':
                arr[9]++;
                break;
        }
    }
    
    for(int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
