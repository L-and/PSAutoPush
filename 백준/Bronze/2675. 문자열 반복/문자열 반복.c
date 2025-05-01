#include <stdio.h>
#include <ctype.h>
#include <string.h>

int cheak(char c)
{
	char *cheak_string="\$%*+-./:";
	
	for(int i=0;i<9;i++)
	{
		if(c==cheak_string[i])
		return 1;
	}
	return 0;
 } 

int main()
{
	int casenum;
	int loop;
	char input[21];
	int i,j,k;
	
	scanf("%d",&casenum);
	
	for(i=0;i<casenum;i++)		//케이스 반복  
	{
		scanf("%d",&loop);
		scanf("%s",&input);

			for(k=0;k<strlen(input);k++)	//문자열에서 각 문자 하나씩  
			{
				if(isalnum(input[k])!=0||cheak(input[k])!=0)
				{
				
					for(j=0;j<loop;j++)	//루프횟수만큼 출력반복 
					{
					printf("%c",input[k]);
				
					}
				}

			}
			printf("\n");
	
	}	
	
	
	
	
	return 0;
}