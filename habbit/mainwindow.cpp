#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    mUi(std::make_shared<Ui::MainWindow> ()),
    mManageDailyTasks (std::make_shared<ManageDailyTasks> ())
{
    mUi->setupUi(this);
    initActions ();
}

MainWindow::~MainWindow()
{
}

void MainWindow::initActions()
{
    connect(mUi->actionChange_daily_tasks, SIGNAL(triggered()), this, SLOT(changeDailyTasksMenuClicked()));
    connect(mUi->actionNotes, SIGNAL(triggered()), this, SLOT(notesMenuClicked()));
    connect(mUi->actionBackUp, SIGNAL(triggered()), this, SLOT(backUpMenuClicked()));
    connect(mUi->actionBudget, SIGNAL(triggered()), this, SLOT(budgetMenuClicked()));
    connect(mUi->actionLevels, SIGNAL(triggered()), this, SLOT(levelsMenuClicked()));
    connect(mUi->actionAdd_notes, SIGNAL(triggered()), this, SLOT(addNotesMenuClicked()));
    connect(mUi->actionadd_a_task, SIGNAL(triggered()), this, SLOT(addTaskMenuClicked()));
    connect(mUi->actionShow_history, SIGNAL(triggered()), this, SLOT(showHistoryMenuClicked()));
    connect(mUi->actionChange_daily_tasks, SIGNAL(triggered()), this, SLOT(changeDailyTaskMenuClicked()));
    connect(mUi->actionMark_task_as_finished, SIGNAL(triggered()), this, SLOT(markTaskAsFinishedMenuClicked()));
}

void MainWindow::changeDailyTasksMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
    mManageDailyTasks->show();
}

void MainWindow::notesMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::backUpMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::budgetMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::levelsMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::addNotesMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::addTaskMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::showHistoryMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::changeDailyTaskMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::markTaskAsFinishedMenuClicked()
{
    qDebug () <<__PRETTY_FUNCTION__;
}
