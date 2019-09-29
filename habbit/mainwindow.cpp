#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    mDatabase (std::make_shared<DataBase> ()),
    mManageDailyTasks (std::make_shared<ManageDailyTasks> ()),
    mModel (std::make_shared<QStandardItemModel> ()),
    mUi(std::make_shared<Ui::MainWindow> ())
{
    mUi->setupUi(this);
    initActions ();
    initModelTableView ();

    connect( mManageDailyTasks.get()
            , SIGNAL(updateTableViewMainWindow())
            , this
            , SLOT(onUpdateTableViewMainWindow())
            , Qt::QueuedConnection);
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
    QLabel *label = new QLabel(this);
    label->setText("test");
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

void MainWindow::reloadTableViewData ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    //remove all data from tableView
    mModel->removeRows(0, mModel->rowCount());

    DailyTasksStructure dailyTaskStructure = mDatabase->getDailyTasksData("vlado");
    std::vector<DailyTask> listDailyTask = dailyTaskStructure.getDailyTasks();
    for (unsigned int i = 0; i<listDailyTask.size(); ++i)
    {
        addDataInTableView (listDailyTask[i].getTask (),
                            listDailyTask[i].getPoints (),
                            listDailyTask[i].getAmountPoints (),
                            listDailyTask[i].getTypeEntry ());
    }
}

void MainWindow::closeEvent (QCloseEvent *)
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void MainWindow::showEvent(QShowEvent *)
{
    qDebug () <<__PRETTY_FUNCTION__;

    reloadTableViewData();
}


void MainWindow::initModelTableView()
{
    mModel->setHorizontalHeaderItem(0, new QStandardItem(QString("Task")));
    mModel->setHorizontalHeaderItem(1, new QStandardItem(QString("Earned Points")));
    mModel->setHorizontalHeaderItem(2, new QStandardItem(QString("Amount")));
    mUi->tableView->setModel(mModel.get());
}

void MainWindow::addDataInTableView(const QString &task,
                                    const QString &points,
                                    const QString &amount,
                                    const QString &type)
{

    mModel->setRowCount(mModel->rowCount()+1);

    mModel->setData(mModel->index(mModel->rowCount()-1,0),task);
    mModel->setData(mModel->index(mModel->rowCount()-1,1),points);
    mModel->setData(mModel->index(mModel->rowCount()-1,2),amount);
    //mModel->setData(mModel->index(mModel->rowCount()-1,3),type);

    //set data to be not editable
    mModel->item(mModel->rowCount()-1,0)->setEditable(false);
    //"checkbox", "textbox", "incrementJudgeAfter", "incrementGainAfter";
    if ("checkbox" == type)
    {
        //ToDo: create a check box
        QStandardItem* item0 = new QStandardItem(true);
        item0->setCheckable(true);
        item0->setCheckState(Qt::Unchecked);
        item0->setText(" Finished");
        mModel->setItem(mModel->rowCount()-1, 2, item0);
        mModel->item(mModel->rowCount()-1,2)->setEditable(false);
    }
    else
    {
        mModel->item(mModel->rowCount()-1,2)->setEditable(true);
    }

    mModel->item(mModel->rowCount()-1,1)->setEditable(false);
}

void MainWindow::onUpdateTableViewMainWindow ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    reloadTableViewData();
}
