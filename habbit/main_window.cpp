#include "main_window.h"
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

    connect(mModel.get(), SIGNAL(itemChanged(QStandardItem*)), this, SLOT(itemChanged(QStandardItem*)), Qt::QueuedConnection);
}

MainWindow::~MainWindow()
{
}

void MainWindow::itemChanged (QStandardItem*item)
{
    //Qt::CheckState checkState = item->checkState();

    qDebug()<<__PRETTY_FUNCTION__;
    //FIXME: it should update only a row that 'current amount' field has changed
    for (int i=0; i<mModel->rowCount(); ++i)
    {
        QString points = mDatabase->getPointsByDailyTask("vlado", getDataFromModelByIndex (i, 0));
        QString amountToEarnLose = getDataFromModelByIndex (i, 3);
        QString currentAmount = getDataFromModelByIndex(i, 2);
        if (item->isCheckable())
        {
            if (item->checkState() == Qt::Unchecked)
            {
                currentAmount = "0";
            }
            else
            {
                currentAmount = "1";
            }
        }
        QString type = mDatabase->getTypeByDailyTask("vlado", getDataFromModelByIndex (i, 0));
        QString earnedPoints = calculateEarnedPoints(points,
                                                     amountToEarnLose,
                                                     currentAmount,
                                                     type,
                                                     item->checkState());

        //update earned points
        mModel->setData(mModel->index(i,1),earnedPoints);
        mDatabase->updateCurrentAmount("vlado", getDataFromModelByIndex (i, 0), currentAmount);
    }

}

QString MainWindow::getDataFromModelByIndex (const int &index, const int &column)
{
    QModelIndex modelIndex;
    QVariant variant;
    modelIndex = mModel->index(index,column);
    variant=modelIndex.data();

    return variant.toString();
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
                            listDailyTask[i].getCurrentAmount(),
                            listDailyTask[i].getAmountEarnLosePoints (),
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
    mModel->setHorizontalHeaderItem(2, new QStandardItem(QString("Current Amount")));
    mModel->setHorizontalHeaderItem(3, new QStandardItem(QString("Amount to Earn Lose Points")));
    mUi->tableView->setModel(mModel.get());
}

QString MainWindow::calculateEarnedPoints (const QString &points,
                                       const QString &amountToEarnLose,
                                       const QString &currentAmount,
                                       const QString &type,
                                       Qt::CheckState checkState)
{
    int resultInt = 0;
    int pointsInt = points.toInt();
    int amountToEarnLoseInt = amountToEarnLose.toInt();
    int currentAmountInt = currentAmount.toInt();

    if (type == "checkbox")
    {
        if (checkState == Qt::Checked)
        {
            resultInt = pointsInt;
        }
    }
    else if (type == "incrementJudgeAfter")
    {
        if ((currentAmountInt/double(amountToEarnLoseInt)) > 1.0)
        {
            resultInt = (pointsInt * (currentAmountInt/amountToEarnLoseInt)) * -1;
        }
    }
    else if (type == "incrementGainAfter" || type =="textbox")
    {
        resultInt = currentAmountInt/amountToEarnLoseInt * pointsInt;
    }
    QString result = QString::number(resultInt);
    return result;
}

void MainWindow::addDataInTableView(const QString &task,
                                    const QString &points,
                                    const QString &currentAmount,
                                    const QString &amountToEarnLose,
                                    const QString &type)
{

    mModel->setRowCount(mModel->rowCount()+1);

    //calculate earned points
    Qt::CheckState checkState =Qt::Unchecked;
    if (currentAmount == "1")
    {
        checkState = Qt::Checked;
    }
    QString earnedPoints = calculateEarnedPoints(points, amountToEarnLose,currentAmount,type, checkState);
    mModel->setData(mModel->index(mModel->rowCount()-1,0),task);
    mModel->setData(mModel->index(mModel->rowCount()-1,1),earnedPoints);
    mModel->setData(mModel->index(mModel->rowCount()-1,3),amountToEarnLose);

    //set data to be not editable
    mModel->item(mModel->rowCount()-1,0)->setEditable(false);
    mModel->item(mModel->rowCount()-1,1)->setEditable(false);
    mModel->item(mModel->rowCount()-1,3)->setEditable(false);

    //"checkbox", "textbox", "incrementJudgeAfter", "incrementGainAfter";
    if ("checkbox" == type)
    {
        //ToDo: create a check box
        QStandardItem* item0 = new QStandardItem(true);
        item0->setCheckable(true);
        if (currentAmount == "0")
        {
            item0->setCheckState(Qt::Unchecked);
        }
        else
        {
            item0->setCheckState(Qt::Checked);
        }
        item0->setText(" Finished");
        mModel->setItem(mModel->rowCount()-1, 2, item0);
        mModel->item(mModel->rowCount()-1,2)->setEditable(false);
    }
    else
    {
        mModel->setData(mModel->index(mModel->rowCount()-1,2),currentAmount);
        mModel->item(mModel->rowCount()-1,2)->setEditable(true);
    }

}

void MainWindow::onUpdateTableViewMainWindow ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    reloadTableViewData();
}
