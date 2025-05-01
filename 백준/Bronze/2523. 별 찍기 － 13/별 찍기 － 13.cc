#include <iostream>

int main()
{
	int i;
	int max;
	int now_max=1;
	int count=1;
	
	std::cin>>max;
	
	int loop=max*2-1;
	
	for(i=1;i<=loop;i++)
	{
		count=1;
		while(count<=now_max)
		{
			std::cout<<'*';
			count++;
		}
		std::cout<<std::endl;
		
		if(now_max<max) now_max++;
		else {max=-1; now_max--;}
	}
	
	
	return 0;
}