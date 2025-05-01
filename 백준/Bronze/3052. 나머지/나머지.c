#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)    // 오름차순 비교 함수 구현
{
    int num1 = *(int *)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
    int num2 = *(int *)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

    if (num1 < num2)    // a가 b보다 작을 때는
        return -1;      // -1 반환
    
    if (num1 > num2)    // a가 b보다 클 때는
        return 1;       // 1 반환
    
    return 0;    // a와 b가 같을 때는 0 반환
}

int main(){
	int i,j;
	int input[10];
	int remainder[10];
	int total_same=0;
	int num;
	
	for(i=0;i<10;i++){
	scanf("%d",&input[i]);
	remainder[i]=input[i]%42;
	}
	
	qsort(remainder,sizeof(remainder)/sizeof(int),sizeof(int),compare);
	
	num=remainder[0];
	
	i=1;
	
	while(1){
	
	while(num==remainder[i]) i++;
	
	num=remainder[i];
	
	total_same++;
	
	if(i==10) break;
	}
	
	printf("%d",total_same);
	return 0;
}

