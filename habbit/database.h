#ifndef YKZA_DB_H
#define YKZA_DB_H

#include <map>
#include <vector>

#include <QtSql/QtSql>

#include "daily_tasks_structure.h"

class DataBase
{
public:
    DataBase();
    virtual ~DataBase ();

    void    createTables();

    bool    checkUsernameAvailable (const QString &username);
    bool    checkTaskExistInDailyTasks (const QString &task);


    void    insertIntoDailyTasks (const QString &username,
                                  const QString &task,
                                  const QString &type_entry,
                                  const QString &points,
                                  const QString &amount_earn_lose,
                                  const QString &time,
                                  const QString &current_amount);

    //-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
    void    insertIntoYkzaTasks (const QString &username,
                                  const QString &task,
                                  const QString &points);
    //-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
    void    insertIntoUsernameData (const QString &username,
                                  const QString &budget,
                                  const QString &level,
                                  const QString &points);

    void    insertIntoHistory (const QString &username,
                                  const QString &date,
                                  const QString &points,
                                  const QString &notes,
                                  const QString &task,
                                  const QString &typeEntry,
                                  const QString &taskPoints,
                                  const QString &amountEarnlose,
                                  const QString &time,
                                  const QString &currentAmount);

    //-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
    void    insertIntoAccounts (const QString &username,
                                  const QString &password);

    DailyTasksStructure getDailyTasksData (const QString &username);
    QString getPointsByDailyTask (const QString &username, const QString &dailyTask);
    QString getTypeByDailyTask (const QString &username, const QString &dailyTask);

    //-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
    QString getYkzaTasks (const QString &username);
    //-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
    QString getUsernameData (const QString &username);
    //    -'hostory' slite database should contains - 'username', 'date', 'points'
    QString getHistory (const QString &username);
    bool getPasswordByUsername (const QString &username, QString &password);

    void    removeTaskFromDailyTasks(const QString &username, const QString &task);
    //-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
    void    removeTaskFromYkzaTasks(const QString &username, const QString &task);
    //-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
    void    removeUsernameData(const QString &username);
    //    -'hostory' slite database should contains - 'username', 'date', 'points'
    void    removeHistory(const QString &username);
    //-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
    void    removeAccount(const QString &username);

    void    updatePointsByTaksName (const QString &username, const QString &task, const QString &points);
    void    updateCurrentAmount (const QString &username, const QString &task, const QString &currentAmount);
private:
    void closeDB();
    void createDailyTasksTable ();
    void createYkzaTasksTable ();
    void createUsernameDataTable ();
    void createHistoryTable ();
    void createAccountsTable ();
    void createTable (const QString &table_name, const QString &query_string);
    int  dropTable(const QString &table_name);
    void openDB();
private:
    QSqlDatabase q_sql_data_base_;
};

#endif // YKZA_DB_H
