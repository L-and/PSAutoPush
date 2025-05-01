#include <iostream>

int main()
{
    int num = 0;
    int count = 0;
    std::cin >> num;

    while (num != 0)
    {
        if (num % 5 == 0)
        {
            num -= 5;
            count++;
        }
        else if (num % 3 == 0)
        {
            num -= 3;
            count++;
        }
        else if(num > 5)
        {
        	num-=5;
        	count++;
		}
        else
        {
            count = -1;
            break;
        }
    }

    std::cout << count;

    return 0;
}