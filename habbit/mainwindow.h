#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QDebug>
#include <QMainWindow>

#include <memory>

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

private:
    void initActions ();

private:
    std::shared_ptr<Ui::MainWindow> mUi;
    std::shared_ptr<ManageDailyTasks> mManageDailyTasks;
};

#endif // MAINWINDOW_H
