#include <iostream>
using namespace std;

class Test1
{
        public:
                Test1(){}
                void test () { cout<<"Test1::test"<<endl;}


};

class Test2
{
        public:
                Test2() {}
                void test () {cout<<"Test2::test"<<endl;}

};

int main ()
{
        std::pair<Test1, Test2> test1AndTest2;

        Test1 test1;
        Test2 test2;

        test1AndTest2.first = test1;
        test1AndTest2.second = test2;

        test1AndTest2.first.test(); //it will print Test1::test
        test1AndTest2.second.test(); //it will print Test2::test
        return 0;
}
