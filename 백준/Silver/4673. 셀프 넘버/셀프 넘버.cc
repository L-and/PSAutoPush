#include <stdio.h>
#include <stdlib.h>


void deletesamenum(int *mary,int *dary)
{
	int i,j;
	for(i=0;i<10000;i++)
	{
		for(j=i;j<10000;j++)
		{
			if(mary[i]==dary[j]) {mary[i]=10001; break;}
		}
	}
}


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


int getaddnum(int n)
{
	int addnum;
	
	addnum=n%10;
	
	return addnum;
}

int getnotselfnum(int n)
{
	int num;
	
	num=n;
	for(int i=0;i<5;i++)
	{
		num+=getaddnum(n);
		n/=10;
	}
	
	return num;
}

int main(void)
{
	int i=1,j=0;
	int ary[10000];
	int numary[10000];
	
	for(i=1;i<=10000;i++)
	{
		numary[i]=i;
	}
	
	i=1;
	
	while(getnotselfnum(i)<=10000)
	{
		ary[j]=getnotselfnum(i);
		i++;
		j++;
	}
	
	qsort(ary,10000,sizeof(int),compare);
	
	deletesamenum(numary,ary);
	
	qsort(numary,10000,sizeof(int),compare);
	
	for(i=0;i<983;i++)
	{
		printf("%d\n",numary[i]);
	}
	

}