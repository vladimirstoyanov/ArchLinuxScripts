#include <iostream>
#include <typeinfo>
using namespace std;

int main ()
{
        struct A { double x; };
        const A* a;
        decltype(a->x) y; //y bocomes double type

        cout<<typeid(y).name()<<endl; //result: d (double)
        return 0;
}
