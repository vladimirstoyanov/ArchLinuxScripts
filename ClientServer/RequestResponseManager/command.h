#ifndef COMMABD_H
#define COMMABD_H

#include "parameters.h"

class Command
{
public:
    Command () {}
    virtual ~Command () {}
    virtual void execute() = 0;
    virtual void result (Parameters parameters) = 0;
};


#endif // COMMABD_H
