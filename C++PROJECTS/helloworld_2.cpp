#include <iostream>


int main()
{
    //if statement = do something if a condition is true.
    //                 if not, then don't do it.

    int age;

    std::cout << "Enter your age: ";
    std::cin >> age;

    if(age >= 18)
    {
        std::cout << "Welcome to the site!";
    }
    else if(age >= 100)
    {
        std::cout << "You are too old to enter this site!";
    }
    else
    {
        std::cout << "You are not old enough to enter!";
    }

    return 0;
}