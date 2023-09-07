#include <iostream>


int main()
{
    // do while loop = do some block of code first,
    //                 THEN repeat again if condition is true
    
    std::string name;

    while(1==1)
    {
        std::cout << "Enter your name: ";
        std::getline(std::cin, name);
    }

    std::cout << "Hello " << name;

    return 0;
}