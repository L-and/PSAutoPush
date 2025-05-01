#include <iostream>

int main()
{
	int arr[5];
	int total=0;
	int avg;
	
	for(int i=0;i<5;i++)
	{
	std::cin>>arr[i];
	
	if(arr[i]<=40) total+=40;
	else total+=arr[i];
	}
	
	avg=total/5;
	
	std::cout<<avg;
	
	return 0;
}