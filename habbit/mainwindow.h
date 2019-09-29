#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QDebug>
#include <QMainWindow>

#include <memory>

#include "dailytasksstructure.h"
#include "database.h"
#include "managedailytasks.h"


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

private:
    void closeEvent (QCloseEvent *);
    void showEvent(QShowEvent *);

private:
    void addDataInTableView(const QString &task, const QString &points, const QString &amount, const QString &type);
    void initActions ();
    void initModelTableView();
    void reloadTableViewData ();


private:
    std::shared_ptr<DataBase> mDatabase;
    std::shared_ptr<ManageDailyTasks> mManageDailyTasks;
    std::shared_ptr<QStandardItemModel> mModel;
    std::shared_ptr<Ui::MainWindow> mUi;

};

#endif // MAINWINDOW_H
