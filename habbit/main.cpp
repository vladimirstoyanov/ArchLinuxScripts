#include <QApplication>

#include "login_window.h"
#include "main_window.h"
#include "database.h"
/*
    - 'main window' it will contains:
        - make the widget to resize correctly;
        - make totalLabel to resize dynamicly;
        - current amount should be updated with amount data from sunday to this day for weekly tasks;
            - it will get the current amount from previous day, if the privous day is not sunday and current day is equal to zero;

    - a gui window that can be added weekly tasks
        - when resize the window, then resize the widget and positioning them;

    - a gui window that can be added yakuza tasks (simillar to daily tasks window);
         - create gui;
    - a window with the current budget, ykza level, ykza points, list of ranks
            - create gui;
    - graphic with history of earned points;
            - create gui;
    - create a backup of the sqlite data base of an enternal hard drive;
    - sqlite data is encypted, using a password stored like a sha256 hash;
    - option to open a data base, a text box will appear with a password field;
        -'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
            - add account;
            - remove account;
            - update data;

    - a window that can be added notes, like a diary;

    Database:
        - create a baseClass - database and subclasses for every table. Also create a folder to store them;


    Type of points type: "checkbox", "textbox", "incrementJudgeAfter", "incrementGainAfter";
 */
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DataBase dataBase;
    dataBase.createTables();

    MainWindow w;
    w.show();

    //LoginWindow l;
    //l.show();

    return a.exec();
}
