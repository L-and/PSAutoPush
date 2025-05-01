#include <stdio.h>
#include <stdbool.h>

int main()
    {
    int alphabet[26]={0,};
    bool havethis[26]={false,};
    char s[101];
    int i;
    
    scanf("%s",s);
    
    for(i=0;s[i]!='\0';i++)
        {
                if(alphabet[s[i]-97]==0&&havethis[s[i]-97]==false)

        {
		havethis[s[i]-97]=true;
		alphabet[s[i]-97]=i;
	}
		
        }

    for(i=0;i<26;i++)
        {
        if(havethis[i]==false)
           {
            alphabet[i]=-1;
            }
        }
    
    for(i=0;i<26;i++)
        {
        
        printf("%d ",alphabet[i]);
          
        }
    
    return 0;
    }