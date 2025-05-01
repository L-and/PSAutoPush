#include <stdio.h>

int main()
{
    int total=0;
    int n;
    int temp;
    
    scanf("%d",&n); 
    
    
    getchar();
    for(int i=0;i<n;i++)
    {
        temp=getchar()-48;
        
        total+=temp;
    }
    
    printf("%d",total);
    
    return 0;
}