#include <iostream>
#include <string.h>

int check_croatia(char *str,int *add,int i)
{
	if(str[i]=='c')
	{
		if(str[i+1]=='=')
		{
			*add+=1;
			return 1;
		}
		else if(str[i=1]=='-')
		{
			*add+=1;
			return 1;
		}
		else return 1;
	}
	else if(str[i]=='d')
	{
		if(str[i+1]=='z'&&str[i+2]=='=')
		{
			*add+=2;
			return 1;
		}
		else if(str[i+1]=='-')
		{
			*add+=1;
			return 1;
		}
		else return 1;
	}
	else if(str[i]=='l'&&str[i+1]=='j')
	{
		*add+=1;
		return 1;
	}
	else if(str[i]=='n'&&str[i+1]=='j')
	{
		*add+=1;
		return 1;
	}
	else if(str[i]=='s'&&str[i+1]=='=')
	{
		*add+=1;
		return 1;	
	}
	else if(str[i]=='z'&&str[i+1]=='=')
	{
		*add+=1;
		return 1;	
	}
	else
	{
		if(str[i]>='a'&&str[i]<='z')
		{
			*add+=0;
			return 1;
		}
		else 
		{
			*add+=0;
			return 0;
		}	
	}
}

int main()
{
	char input[103];
	int add=0;
	int croatia=0;
	
	std::cin>>input;
	
	for(int i=0;i<strlen(input);i++)
	{
		croatia+=check_croatia(input,&i,i);
		

	}

	std::cout<<croatia;
	return 0;
}