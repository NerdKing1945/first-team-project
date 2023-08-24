#include <iostream>

namespace first
{
    int x = 1;
}
namespace second
{
    int x = 2;
}


int main()
{
    using namespace second;

    std::cout << first::x;

    

    // Namespace = provide a solution for preventing name conflicts
    //            in large projects. Each entity needs a unique name.
    //            A namespace allows for identically name entities
    //            as long as the namespaces are different.

    return 0;
}