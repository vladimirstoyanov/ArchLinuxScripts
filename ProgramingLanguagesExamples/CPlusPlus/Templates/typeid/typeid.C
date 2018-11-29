#include <iostream>
using namespace std;

template <typename T>
void test (T argument)
{
	cout<<typeid(T).name()<<endl;
}

int main ()
{
	test(10); //result: i (like integer)
	test("some string"); //result: 
	test(10.1); //result d (like double)
	return 0;
}
