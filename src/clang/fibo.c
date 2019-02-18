#include <stdio.h>

int main() {
    int pre=1, preBeforePre=0, number;
    printf ("please input number:");
    scanf("%d", &number);
    int count = 0,result=0, total=1;;
    while (count < number) {
        result = pre + preBeforePre;
        total += result;
        preBeforePre = pre;
        pre = result;
        count ++;
    }
    printf("fibo result is %d and calculation result is %d\n", result, total);
    return 0;
}
