#include "database.h"

DataBase::DataBase()
{
    //open db
    //openDB();
    //createTables(); //it creates RSS data necessary tables if they don't exist
}

DataBase::~DataBase ()
{
    //closeDB();
}

void DataBase::createTables()
{
    createDailyTasksTable ();
    createYkzaTasksTable ();
    createUsernameDataTable ();
    createHistoryTable ();
    createAccountsTable ();
}

void DataBase::openDB()
{
    //qDebug()<<__PRETTY_FUNCTION__;
    //open db
    q_sql_data_base_ = QSqlDatabase::addDatabase("QSQLITE");
    q_sql_data_base_.setDatabaseName("data.db3");
    q_sql_data_base_.open();
}

void DataBase::closeDB()
{
    //qDebug()<<__PRETTY_FUNCTION__;
    //q_sql_data_base_.close();
    QSqlDatabase db = QSqlDatabase::database();
    db.close();
    q_sql_data_base_.close();

    QSqlDatabase::removeDatabase( QSqlDatabase::defaultConnection );
    //QSqlDatabase::removeDatabase("QSQLITE");
    //  'qt_sql_default_connection'
    QSqlDatabase::removeDatabase("qt_sql_default_connection");
    //qDebug()<<__PRETTY_FUNCTION__<<": END";
}

void DataBase::insertIntoDailyTasks (const QString &username,
                              const QString &task,
                              const QString &type_entry,
                              const QString &points,
                              const QString &points_for_amount)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);
        query.prepare("insert into daily_tasks (username, task, type_entry, points, points_for_amount) values (?,?,?,?,?)");
        query.addBindValue(username);
        query.addBindValue(task);
        query.addBindValue(type_entry);
        query.addBindValue(points);
        query.addBindValue(points_for_amount);

        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError();
        }
    }
    closeDB();
}

//-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
void DataBase::insertIntoYkzaTasks (const QString &username,
                              const QString &task,
                              const QString &points)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);
        query.prepare("insert into ykza_tasks (username, task, points) values (?,?,?)");
        query.addBindValue(username);
        query.addBindValue(task);
        query.addBindValue(points);

        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError();
        }
    }
    closeDB();
}

//-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
void DataBase::insertIntoUsernameData (const QString &username,
                              const QString &budget,
                              const QString &level,
                              const QString &points)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);
        query.prepare("insert into username_data (username, budget, level, points) values (?,?,?,?)");
        query.addBindValue(username);
        query.addBindValue(budget);
        query.addBindValue(level);
        query.addBindValue(points);

        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError();
        }
    }
    closeDB();
}

//    -'hostory' slite database should contains - 'username', 'date', 'points'
void DataBase::insertIntoHistory (const QString &username,
                              const QString &date,
                              const QString &points)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);
        query.prepare("insert into history (username, date, points) values (?,?,?)");
        query.addBindValue(username);
        query.addBindValue(date);
        query.addBindValue(points);

        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError();
        }
    }
    closeDB();
}

//-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
void DataBase::insertIntoAccounts (const QString &username,
                              const QString &password)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);
        query.prepare("insert into accounts (username, password) values (?,?)");
        query.addBindValue(username);
        query.addBindValue(password);

        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError();
        }
    }
    closeDB();
}

void DataBase::removeTaskFromDailyTasks(const QString &username, const QString &task)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("delete from daily_tasks where username=\"%1\" and task=\"%2\"").arg(username, task));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

//-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
void    DataBase::removeTaskFromYkzaTasks(const QString &username, const QString &task)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("delete from ykza_tasks where username=\"%1\" and task=\"%2\"").arg(username, task));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

//-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
void    DataBase::removeUsernameData(const QString &username)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("delete from username_data where username=\"%1\"").arg(username));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<" Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

//    -'hostory' slite database should contains - 'username', 'date', 'points'
void    DataBase::removeHistory(const QString &username)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("delete from history where username=\"%1\"").arg(username));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<" Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

//-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
void  DataBase::removeAccount(const QString &username)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("delete from accounts where username=\"%1\"").arg(username));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<" Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

void DataBase::updatePointsByTaksName (const QString &username, const QString &task, const QString &points)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        query.prepare(QString("update daily_tasks set points=\"%1\" where username=\"%2\" and task=\"%3\"").arg(
                          points, username, task));
        if (!query.exec())
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error:"<<query.lastError().text();
        }
    }
    closeDB();
}

int DataBase::dropTable(const QString &table_name)
{
    int result = 0;
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (!query.exec("drop table " + table_name))
        {
            qDebug()<<__PRETTY_FUNCTION__<<"Error drop table: "  + table_name;
        }
        result = 1;
    }
    closeDB();

    return result;
}

DailyTasksStructure DataBase::getDailyTasksData (const QString &username)
{
    DailyTasksStructure dailyTasksStructure;
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM daily_tasks WHERE username=\"%1\"").arg(username));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return dailyTasksStructure;
            }
            while(query.next())
            {
                DailyTask dailyTask;
                QString task = query.value( 2 ).toByteArray().data();
                QString typeEntry = query.value( 3 ).toByteArray().data();
                QString points = query.value( 4 ).toByteArray().data();
                QString amountPoints = query.value( 5 ).toByteArray().data();

                dailyTask.setTask(task);
                dailyTask.setTypeEntry(typeEntry);
                dailyTask.setPoints(points);
                dailyTask.setAmountPoints(amountPoints);
                dailyTasksStructure.addDailyTask(dailyTask);
            }
        }
    }
    closeDB();

    return dailyTasksStructure;
}

//-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
QString DataBase::getYkzaTasks (const QString &username)
{
    QString result = "";
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM ykza_tasks WHERE username=\"%1\"").arg(username));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return "";
            }
            while(query.next())
            {
                //-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
                result += "username:";
                result += query.value( 2 ).toByteArray().data();
                result +=",";
                result += "task:";
                result += query.value( 3 ).toByteArray().data();
                result +=",";
                result += "points:";
                result += query.value( 4 ).toByteArray().data();
                result +="\n";
            }
        }
    }
    closeDB();
    return "";
}

//-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
QString DataBase::getUsernameData (const QString &username)
{
    QString result = "";
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM username_data WHERE username=\"%1\"").arg(username));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return "";
            }
            while(query.next())
            {
                //-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
                result += "username:";
                result += query.value( 2 ).toByteArray().data();
                result +=",";
                result += "budget:";
                result += query.value( 3 ).toByteArray().data();
                result +=",";
                result += "level:";
                result += query.value( 4 ).toByteArray().data();
                result +=",";
                result += "points:";
                result += query.value( 5 ).toByteArray().data();
                result +="\n";
            }
        }
    }
    closeDB();
    return "";
}

//    -'hostory' slite database should contains - 'username', 'date', 'points'
QString DataBase::getHistory (const QString &username)
{
    QString result = "";
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM history WHERE username=\"%1\"").arg(username));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return "";
            }
            while(query.next())
            {
                //    -'hostory' slite database should contains - 'username', 'date', 'points', 'notes'
                result += "username:";
                result += query.value( 2 ).toByteArray().data();
                result +=",";
                result += "date:";
                result += query.value( 3 ).toByteArray().data();
                result +=",";
                result += "points:";
                result += query.value( 4 ).toByteArray().data();
                result +=",";
                result += "notes:";
                result += query.value( 5 ).toByteArray().data();
                result +="\n";
            }
        }
    }
    closeDB();
    return "";
}

bool DataBase::getPasswordByUsername (const QString &username, QString &password)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM accounts"));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return false;
            }
            while(query.next())
            {
                if (username == query.value( 1 ).toByteArray().data())
                {
                    password = query.value( 2 ).toByteArray().data();
                    closeDB();
                    return true;
                }
            }
        }
    }
    closeDB();
    return false;
}
//-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
bool DataBase::checkUsernameAvailable(const QString &username)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM accounts"));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return false;
            }
            while(query.next())
            {

                if (username == query.value( 1 ).toByteArray().data())
                {
                    closeDB();
                    return false;
                }
            }
        }
    }
    closeDB();
    return true;
}

bool DataBase::checkTaskExistInDailyTasks (const QString &task)
{
    {
        openDB();
        QSqlQuery query(q_sql_data_base_);

        if (q_sql_data_base_.isOpen())
        {
            query.prepare(QString("SELECT * FROM daily_tasks"));
            if (!query.exec())
            {
                qDebug()<<"Fail:" + query.lastError().text();
                closeDB();
                return false;
            }
            while(query.next())
            {
                if (task == query.value( 2 ).toByteArray().data())
                {
                    closeDB();
                    return false;
                }
            }
        }
    }
    closeDB();
    return true;
}

void DataBase::createDailyTasksTable ()
{
    createTable ("daily_tasks",
                 "create table daily_tasks "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "task varchar, "
                 "type_entry varchar, " //textbox, checkbox
                 "points varchar, "
                 "points_for_amount varchar)");
}

void DataBase::createYkzaTasksTable ()
{
    //-'ykza_tasks' sqlite table should contains - 'username', 'task', 'points'
    createTable ("ykza_tasks",
                 "create table ykza_tasks "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "task varchar, "
                 "points varchar)");
}

void DataBase::createUsernameDataTable ()
{
    //-'username_data' sqlite table should contains - 'username', 'budget', 'level', 'points'
    createTable ("username_data",
                 "create table username_data "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "budget varchar, "
                 "level varchar, "
                 "points varchar)");
}
void DataBase::createHistoryTable ()
{
    //    -'hostory' slite database should contains - 'username', 'date', 'points'
    createTable ("history",
                 "create table history "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "date varchar, "
                 "points varchar,"
                 "notes varchar)");
}
void DataBase::createAccountsTable ()
{
    //-'accounts' sqlite database should contains - 'username', 'password' (sha265 hash)
    createTable ("accounts",
                 "create table accounts "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "password varchar)");
}

void DataBase::createTable (const QString &table_name, const QString &query_string)
{
    qDebug()<<__PRETTY_FUNCTION__<<": query:"<<query_string;
    {
        openDB();
        if (!q_sql_data_base_.tables().contains(table_name)) //if the table doesn't exist
        {
            //create 'table'
            if (q_sql_data_base_.isOpen())
            {
                    QSqlQuery query;
                    if (!query.exec(query_string))
                    {
                        qDebug()<<__PRETTY_FUNCTION__<<":"<<query.lastError()<<" : query_string: "<<query_string;
                    }
            }
        }
    }
    closeDB();
}
