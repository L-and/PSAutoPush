#include <iostream>

int main()
{
	int input;
	int loop;
	int i,j;
	
	std::cin>>input;
	
	for(i=1;i<=input*2;i++)
	{
		for(j=1;j<=input;j++)
		{
			if(i%2!=0)
			{
				if(j%2!=0) std::cout<<'*';
				else if(j%2==0) std::cout<<' ';
			}
			else if(i%2==0)
			{
				if(j%2!=0) std::cout<<' ';
				else if(j%2==0) std::cout<<'*';
			}
		}
		std::cout<<std::endl;
	}
	
	return 0;
}