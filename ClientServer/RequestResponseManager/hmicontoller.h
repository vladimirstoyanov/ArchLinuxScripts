#ifndef HMICONTOLLER_H
#define HMICONTOLLER_H

#include <QObject>
#include "command.h"
#include "parameters.h"

class HMIContoller
{
public:
    HMIContoller();

    void setCommand(Command *cmd) {
        mCmd = cmd;
    }

    void executeRequest() {
        mCmd->execute();
    }

    void handleResponse(Parameters parameters)
    {
        mCmd->result(parameters);
    }
private:
    Command *mCmd;
};

#endif // HMICONTOLLER_H
