#include <iostream>
#include <string>

int main()
{
	std::string input;
	
	std::cin>>input;
	
	int time=0;
	
	for(int i=0;i<input.length();i++)
	{
		if(input.at(i)>='A'&&input.at(i)<='C')		time+=3;
		else if(input.at(i)>='D'&&input.at(i)<='F')		time+=4;
		else if(input.at(i)>='G'&&input.at(i)<='I')		time+=5;
		else if(input.at(i)>='J'&&input.at(i)<='L')		time+=6;
		else if(input.at(i)>='M'&&input.at(i)<='O')		time+=7;
		else if(input.at(i)>='P'&&input.at(i)<='S')		time+=8;
		else if(input.at(i)>='T'&&input.at(i)<='V')		time+=9;
		else if(input.at(i)>='W'&&input.at(i)<='Z')		time+=10;
	}
	
	std::cout<<time;
	
	return 0;
}