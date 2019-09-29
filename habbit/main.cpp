#include <QApplication>

#include "loginwindow.h"
#include "mainwindow.h"
#include "database.h"
/*
    - 'main window' it will contains:
        [- daily tasks getted from 'daily_task' sqlite table; - task (text cannot be edited), amount or checkbox (it can be enter text here), and points (can't be edited)]
        [- a menu with different options;]
        - load daily tasks from 'daily_tasks' sqlite database;
        - show the daily tasks to 'main window':
                - task: label
                - points: edit box, checkbox or increment;
                - amount: label
        - make the widget to resize correctly;
        - calculate daily points and show them like a label;
        - create a submit button;
            - when click it it will add the points in history with current date. If there is a hole between current and
             previous day, then it will set them to 0;
        - it should remember progress of weekly tasks in the database and load it after a new day (the tasks with
        type - increment*

    [- a gui window that can be added weekly tasks]
        [- the new window should contain a table with data from 'daily_task', table data can be edited, buttons - 'add', 'remove', 'OK', 'Cancel']
            [- when click add a new window-'daily task' will appear]
                [-'daily task' should contain 'text box' - task name, 'combobox' - type, 'textbox' - points, 'amount', 'amount type' (cannot be eddited), 'OK', 'Cancel' buttons]
            [- when click on remove button it will remove marked rows (tasks);]
            [- when click on 'OK' button:]
                [-it will change 'Main window' tasks;]
            [- when click on 'Cancel' button it will close the window]
        [- 'daily task' should contains - username, task, type (textbox, checkbox), points, amount, amount type (time, steps, etc)]

    - a gui window that can be added yakuza tasks (simillar to daily tasks window);
        [-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points']
            [-add data;]
            [-remove data;]
            [-update data;]
         - create gui;
    - a window with the current budget, ykza level, ykza points, list of ranks
        [-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points']
            [-add data;]
            [-remove data;]
            [-update data;]
            - create gui;
    - graphic with history of earned points;
        [-'hostory' slite database should contains - 'username', 'date', 'points', 'notes']
            [- add data;]
            [- remove data;]
            [- update data;]
            - create gui;
    - create a backup of the sqlite data base of an enternal hard drive;
    - sqlite data is encypted, using a password stored like a sha256 hash;
    - option to open a data base, a text box will appear with a password field;
        -'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
            - add account;
            - remove account;
            - update data;

    - a window that can be added notes, like a diary;


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
