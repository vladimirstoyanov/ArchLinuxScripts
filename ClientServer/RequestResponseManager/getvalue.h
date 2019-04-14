#ifndef GETVALUE_H
#define GETVALUE_H

#include "request.h"
#include "command.h"
#include "parameters.h"

class getValue: public Command
{
public:
    getValue(Request *request, const std::string &path, const std::string &key) :
        mRequest(request),
        path(path),
        key(key)
    {}
    void execute(){
        mRequest->getValue(path, key);
    }
    void result (Parameters parameters)
    {
        switch(parameters.getType())
        {
            case INTEEGER:
            {
                std::cout<<"Result integeer: "<<parameters.getIntValue()<<std::endl;
                break;
            }
            case DOUBLE:
            {
                std::cout<<"Result double: "<<parameters.getDoubleValue()<<std::endl;
                break;
            }
            case STRING:
            {
                std::cout<<"Result string: "<<parameters.getStringValue()<<std::endl;
                break;
            }
            case BOOLEAN:
            {
                std::cout<<"Result bool: "<<parameters.getBoolValue()<<std::endl;
                break;
            }
            default:
            {
                std::cout<<"There isn't such type"<<std::endl;
            }

        }

    }
private:
    Request *mRequest;
    std::string path;
    std::string key;
};

#endif // GETVALUE_H
