#include <iostream>

int main()
{
	int i,j;
	int input;
	
	std::cin>>input;
	
	int out_loop=input*2-1;
	int star_loop,space_loop;
	
	for(i=1;i<=out_loop;i++)
	{	
		if(i<=input) space_loop=i-1;
		else space_loop=-i+out_loop;
		for(j=1;j<=space_loop;j++)	std::cout<<' ';
		
		if(i<=input) star_loop=-2*(i-1)+out_loop;
		else star_loop=2*(i-input)+1;
		for(j=1;j<=star_loop;j++)	std::cout<<'*';

		std::cout<<std::endl;
	}
	return 0;
} 