#include <iostream>

int main()
{
	int a,b,c; // a:고정비용 b:노트북생산비용 c:노트북가격 
	int cost;
	int i=0; //손익분기점
	int add;
	
	std::cin>>a>>b>>c;
	
	add=c-b;
	
	if(add==0)
	{
		std::cout<<-1;
		return 0;
	}
	
	cost=a+add;
	
	i=cost/add;	
	
	if(i<0) std::cout<<-1;
	else std::cout<<i;
	
	return 0;
}