#include <stdio.h>
#include <string.h>

int main()
{
	char str[1000001];
	int i=0;
	char* word;
	int wordnum=0;

	scanf("%[^\n]s",str);
	
	word=strtok(str," ");
	
	
	if(word!=NULL) wordnum++;
	
	while(word!=NULL)
	{
		word=strtok(NULL," ");

		if(word!=NULL) wordnum++;
	}
	
	printf("%d",wordnum);
	
	return 0;
}
