#include <iostream>
#include <ctime>


int main()
{
    srand(time(0));
    int randNum = rand() % 5 +1;
    
    switch(randNum)
    {
        case 1: std::cout << "You win a sun blade!\n";
                break;
        case 2: std::cout << "You win a sword!\n";
                break;
        case 3: std::cout << "You win a helm!\n";
                break;
        case 4: std::cout << "You win a staff of the magi!\n";
                break;
        case 5: std::cout << "You win a mastodon halberd!\n";
                break;

    }
    
    return 0;
    
    
    
}