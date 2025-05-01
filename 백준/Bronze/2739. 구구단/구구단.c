#include <stdio.h>

int main(void){
    int N=0;
    int i=0;
    
    scanf("%d",&N);
    
    for(i=1;i<=9;i++){
        printf("%d * %d = %d",N,i,N*i);
        printf("\n");
    }
    return 0;
}