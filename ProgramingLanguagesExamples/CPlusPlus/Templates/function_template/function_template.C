#include <iostream>
using namespace std;


template <typename T>
void test (T argument)
{
	cout<<argument<<endl;
}

int main ()
{
	test(10);
	test("some string");
	test(10.1);
	return 0;
}
