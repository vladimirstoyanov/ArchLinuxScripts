#include <QCoreApplication>

#include "request.h"
#include "getvalue.h"
#include "hmicontoller.h"
int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);


        Request *request = new Request;

        std::string path = "/RemoteUI";
        std::string key = "Press_exec_button";
        // concrete Command objects
        getValue *getValue_ = new getValue(request, path, key);

        // invoker objects
        HMIContoller *control = new HMIContoller;

        // execute
        control->setCommand(getValue_);
        control->executeRequest();
        Parameters parameters(6);
        control->handleResponse(parameters);
        Parameters parameters1(false);
        control->handleResponse(parameters1);
        Parameters parameters2("Test");
        control->handleResponse(parameters2);
        Parameters parameters3(3.14);
        control->handleResponse(parameters3);


        delete request, getValue_, control;
    return a.exec();
}
