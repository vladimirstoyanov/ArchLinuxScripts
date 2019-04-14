#ifndef PARAETERS_H
#define PARAETERS_H


#include <string>

enum TypeVar
{
    INTEEGER,
    DOUBLE,
    STRING,
    BOOLEAN
};

class Parameters
{
public:
    Parameters(int intValue1): intValue1(intValue1), typeVar1(INTEEGER) {}
    Parameters (bool boolValue1): boolValue1(boolValue1), typeVar1(BOOLEAN) {}
    Parameters (const std::string &stringValue1): stringValue1(stringValue1), typeVar1(STRING) {}
    Parameters (double doubleValue1): doubleValue1(doubleValue1), typeVar1(DOUBLE) {}
    int getIntValue() { return this->intValue1; }
    bool getBoolValue() { return this->boolValue1; }
    std::string getStringValue() { return this->stringValue1; }
    double getDoubleValue() { return this->doubleValue1; }
    TypeVar getType () { return this->typeVar1; }
private:
    int intValue1;
    bool boolValue1;
    std::string stringValue1;
    double doubleValue1;
    TypeVar typeVar1;
};

#endif // PARAETERS_H
