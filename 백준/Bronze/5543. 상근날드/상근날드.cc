#include <iostream>

int main()
{
	int set[3];
	int juice[2];
	
	int cheapset=0,cheapjuice=0;
	
	for(int i=0;i<3;i++)
	std::cin>>set[i];
	
	for(int i=0;i<2;i++)
	std::cin>>juice[i];
	
	cheapset=set[0],cheapjuice=juice[0];
	
	for(int i=0;i<3;i++)
	{
		if(cheapset>set[i]) cheapset=set[i];
	}
	
	for(int i=0;i<2;i++)
	{
		if(cheapjuice>juice[i]) cheapjuice=juice[i];
	}
	
	std::cout<<cheapset+cheapjuice-50;
	
}