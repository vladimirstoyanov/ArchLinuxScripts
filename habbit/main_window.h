#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QDate>
#include <QDebug>
#include <QLayout>
#include <QMainWindow>

#include <memory>

#include "daily_tasks_structure.h"
#include "database.h"
#include "manage_daily_tasks_window.h"


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


public slots:
    void changeDailyTasksMenuClicked();
    void notesMenuClicked();
    void backUpMenuClicked();
    void budgetMenuClicked();
    void levelsMenuClicked();
    void addNotesMenuClicked();
    void addTaskMenuClicked();
    void showHistoryMenuClicked();
    void changeDailyTaskMenuClicked();
    void markTaskAsFinishedMenuClicked();
    void onUpdateTableViewMainWindow ();
    void itemChanged (QStandardItem*);

private slots:
    void on_submitButton_clicked();

private:
    void closeEvent (QCloseEvent *);
    void showEvent(QShowEvent *);

private:
    void addDataInTableView(const QString &task,
                            const QString &points,
                            const QString &currentAmount,
                            const QString &amountToEarnLose,
                            const QString &type,
                            const QString &time);

    QString calculateEarnedPoints (const QString &points,
                               const QString &amountToEarnLose,
                               const QString &currentAmount,
                               const QString &type,
                               const QString &time);

    QString getPreviousAmountOfTheCurrentWeek (const QString &task);
    void getCurrentDate (int &day, int&month, int &year, int &dayOfTheWeek);
    void getDateBeforeCurrent (const int &dayBeforeCurrent, int &day, int&month, int &year, int &dayOfTheWeek);
    void initActions ();
    void initModelTableView();
    QString getDataFromModelByIndex (const int &index, const int &column);
    void reloadTableViewData ();
    void resetCurrentAmount ();
    void splitDate (QString &day, QString &month, QString &year, QString &dayOfTheWeek);



private:
    std::shared_ptr<DataBase> mDatabase;
    std::shared_ptr<ManageDailyTasks> mManageDailyTasks;
    std::shared_ptr<QStandardItemModel> mModel;
    int mTotalPoints;
    std::shared_ptr<Ui::MainWindow> mUi;

};

#endif // MAINWINDOW_H
