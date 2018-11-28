#include <iostream>
#include <stdexcept>
using namespace std;


void write (int amount)
{
	if (amount > 10)
	{
		throw logic_error("Error");
	}
}

int main ()
{
	try
	{
		write(100);
	}
	catch (std::logic_error)
	{
		cout<<"Amount is biggest than 10"<<endl;
	}
	return 0;
}
