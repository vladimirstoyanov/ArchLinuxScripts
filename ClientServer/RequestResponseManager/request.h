#ifndef REQUEST_H
#define REQUEST_H

#include <iostream>
#include <string>

class Request
{
public:
    Request();

    void setValue(const std::string &path, const std::string &key, const std::string &value) {
        std::cout << "set value\n";
    }
    void getValue(const std::string &path, const std::string &key) {
        std::cout << "[get value] path="<<path<<" key="<<key<<"\n";
    }

    void getMenu (const std::string menu)
    {
        std::cout << "get menu \n";
    }


};

#endif // REQUEST_H
