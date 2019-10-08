#include "main_window.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    mDatabase (std::make_shared<DataBase> ()),
    mManageDailyTasks (std::make_shared<ManageDailyTasks> ()),
    mModel (std::make_shared<QStandardItemModel> ()),
    mTotalPoints(0),
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
    mTotalPoints = 0;
    for (int i=0; i<mModel->rowCount(); ++i)
    {
        QString task = getDataFromModelByIndex (i, 0);
        QString points = mDatabase->getPointsByDailyTask("vlado", task);
        QString amountToEarnLose = getDataFromModelByIndex (i, 3); //ToDo: get it from the database
        QString currentAmount = getDataFromModelByIndex(i, 2);
        QString type = mDatabase->getTypeByDailyTask("vlado", task);
        QString time = mDatabase->getTimeByDailyTask("vlado", task);

        if (type == "checkbox")
        {
            QStandardItem *standardItem = mModel->item(i, 2);
            if (standardItem!=nullptr && standardItem->checkState() == Qt::Checked)
            {
                currentAmount = "1";
            }
            else
            {
                currentAmount = "0";
            }
        }

        QString earnedPoints = calculateEarnedPoints(points,
                                                     amountToEarnLose,
                                                     currentAmount,
                                                     type,
                                                     time);
        mTotalPoints+=earnedPoints.toInt();
        mModel->setData(mModel->index(i,1),earnedPoints);
        mDatabase->updateCurrentAmount("vlado", getDataFromModelByIndex (i, 0), currentAmount);
    }
    mUi->totalLablel->setText("Total: " + QString::number(mTotalPoints));
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
                            listDailyTask[i].getTypeEntry (),
                            listDailyTask[i].getTime());
    }
}

void MainWindow::closeEvent (QCloseEvent *)
{
    qDebug () <<__PRETTY_FUNCTION__;
    this->close();
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
                                       const QString &time)
{
    int resultInt = 0;
    int pointsInt = points.toInt();
    int amountToEarnLoseInt = amountToEarnLose.toInt();
    int currentAmountInt = currentAmount.toInt();

    int day=0, month =0, year = 0, dayOfWeek=0;
    getCurrentDate(day, month, year, dayOfWeek);

    if (type == "checkbox")
    {
        if (currentAmountInt == 1)
        {
            resultInt = pointsInt;
        }
        else
        {
            resultInt = -pointsInt;
        }
    }
    else if (type == "incrementJudgeAfter")
    {
        if ((currentAmountInt/double(amountToEarnLoseInt)) > 1.0)
        {
            resultInt = (pointsInt * (currentAmountInt/amountToEarnLoseInt)) * -1;
        }
        if (time == "weekly" && dayOfWeek == 7 && (currentAmountInt/double(amountToEarnLoseInt)) > 1.0)
        {
            resultInt = (pointsInt * (currentAmountInt/amountToEarnLoseInt)) * -1;
        }
        else if (time == "weekly" && dayOfWeek == 7 && (currentAmountInt/double(amountToEarnLoseInt)) <= 1.0)
        {
            resultInt = pointsInt;
        }
        else if (time == "weekly" && dayOfWeek !=7)
        {
            resultInt = 0;
        }
    }
    else if (type == "incrementGainAfter" || type =="textbox")
    {
        //ToDo if a weekly task and it's a sunday
        if (currentAmountInt/amountToEarnLoseInt < 1)
        {
            resultInt = - pointsInt;
        }
        else
        {
            resultInt = currentAmountInt/amountToEarnLoseInt * pointsInt;
        }
        if (time == "weekly" && dayOfWeek == 7 && currentAmountInt/amountToEarnLoseInt < 1)
        {
            resultInt = -pointsInt;
        }
        else if (time == "weekly" && dayOfWeek == 7 && currentAmountInt/amountToEarnLoseInt >= 1)
        {
            resultInt = currentAmountInt/amountToEarnLoseInt * pointsInt;
        }
        else if (time == "weekly" && dayOfWeek != 7)
        {
            resultInt = 0;
        }
    }
    QString result = QString::number(resultInt);
    return result;
}

void MainWindow::addDataInTableView(const QString &task,
                                    const QString &points,
                                    const QString &currentAmount,
                                    const QString &amountToEarnLose,
                                    const QString &type,
                                    const QString &time)
{

    mModel->setRowCount(mModel->rowCount()+1);

    QString earnedPoints = calculateEarnedPoints(points, amountToEarnLose,currentAmount,type, time);
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
        QString time = mDatabase->getTimeByDailyTask ("vlado", task);
        if (currentAmount=="0" && time == "weekly")
        {
            QString previousAmount = getPreviousAmountOfTheCurrentWeek(task);
            mModel->setData(mModel->index(mModel->rowCount()-1,2),previousAmount);
        }
        else
        {
            mModel->setData(mModel->index(mModel->rowCount()-1,2),currentAmount);
        }
        mModel->item(mModel->rowCount()-1,2)->setEditable(true);
    }

}

void MainWindow::onUpdateTableViewMainWindow ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    reloadTableViewData();
}

void MainWindow::resetCurrentAmount ()
{
    for (int i=0; i<mModel->rowCount(); ++i)
    {
        QString task = getDataFromModelByIndex (i, 0);
        QString type = mDatabase->getTypeByDailyTask("vlado", task);
        if (type == "checkbox")
        {
            QStandardItem *standardItem = mModel->item(i, 2);
            if (standardItem!=nullptr && standardItem->checkState() == Qt::Checked)
            {
                standardItem->setCheckState(Qt::Unchecked);
            }

        }
        else
        {
            QString time = mDatabase->getTimeByDailyTask("vlado", task);
            int day=0, month=0, year=0, dayOfWeek = 0;
            getCurrentDate(day,month,year, dayOfWeek);
            if (time == "weekly" && dayOfWeek!=7)
            {
                qDebug ()<<__PRETTY_FUNCTION__<<": do nothing for task: "<<task;
            }
            else
            {
                mModel->setData(mModel->index(mModel->rowCount()-1,2),"0");
            }

        }
        mDatabase->updateCurrentAmount("vlado", task, "0");
    }
}

QString MainWindow::getPreviousAmountOfTheCurrentWeek (const QString &task)
{
    int day=0, month = 0, year = 0, dayOfWeek = 0, dayBeforeCurrent = -1;
    getCurrentDate(day, month, year, dayOfWeek);

    //until found a day of the week with currentAmount value
    while (dayOfWeek==1)
    {
        QString amount = mDatabase->getAmountFromHistory("vlado",
                                    task,
                                    QString::number(day),
                                    QString::number(month),
                                    QString::number(year));

        if (amount != "0")
        {
            return amount;
        }
        --dayBeforeCurrent;
        getDateBeforeCurrent(dayBeforeCurrent, day, month, year, dayOfWeek);
    }

    return "0";
}

void MainWindow::getDateBeforeCurrent (const int &dayBeforeCurrent, int &day, int&month, int &year, int &dayOfTheWeek)
{
    QDate date(QDate::currentDate());
    QDate yesterday = date.addDays(dayBeforeCurrent);
    day = yesterday.day();
    month = yesterday.month();
    year = yesterday.year();
    dayOfTheWeek = yesterday.dayOfWeek();
}

void MainWindow::getCurrentDate (int &day, int &month, int &year, int &dayOfTheWeek)
{
    QDate date(QDate::currentDate());
    day = date.day();
    month = date.month();
    year = date.year();
    dayOfTheWeek = date.dayOfWeek();
}

void MainWindow::on_submitButton_clicked ()
{
    qDebug () <<__PRETTY_FUNCTION__;

    //get current date
    QString date = QDate::currentDate().toString();

    int day, month, year, dayOfWeek = 0;
    getCurrentDate(day, month, year, dayOfWeek);
    //get notes by date
    QString notes = mDatabase->getNotesByDate("vlado",
                                              QString::number(day),
                                              QString::number(month),
                                              QString::number(year));

    //remove the history data by date
    mDatabase->removeHistoryByDate("vlado",
                                   QString::number(day),
                                   QString::number(month),
                                   QString::number(year));

    //add the new data
    DailyTasksStructure dailyTaskStructure;
    dailyTaskStructure = mDatabase->getDailyTasksData("vlado");
    QString points = QString::number(mTotalPoints);
    //FIXME
    std::vector<DailyTask> dailyTasks = dailyTaskStructure.getDailyTasks();
    for (unsigned int i=0; i<dailyTasks.size(); ++i)
    {
        mDatabase->insertIntoHistory("vlado",
                                     QString::number(day),
                                     QString::number(month),
                                     QString::number(year),
                                     QString::number(dayOfWeek),
                                     points,
                                     notes,
                                     dailyTasks[i].getTask(),
                                     dailyTasks[i].getTypeEntry(),
                                     dailyTasks[i].getPoints(),
                                     dailyTasks[i].getAmountEarnLosePoints(),
                                     dailyTasks[i].getTime(),
                                     dailyTasks[i].getCurrentAmount());
    }

    resetCurrentAmount();
}
