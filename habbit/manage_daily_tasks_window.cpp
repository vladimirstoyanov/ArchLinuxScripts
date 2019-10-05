#include "manage_daily_tasks_window.h"
#include "ui_managedailytasks.h"

ManageDailyTasks::ManageDailyTasks(QWidget *parent) :
    QWidget(parent),
    mAddDailyTaskWindow(std::make_shared<AddDailyTaskWindow> ()),
    mDatabase (std::make_shared<DataBase> ()),
    mModel (std::make_shared<QStandardItemModel>(0,4,this)),
    mUi(std::make_shared<Ui::ManageDailyTasks> ())
{
    mUi->setupUi(this);
    initModelTableView ();

    connect( mAddDailyTaskWindow.get()
            , SIGNAL(updateTableView())
            , this
            , SLOT(onUpdateTableView())
            , Qt::QueuedConnection);
}

ManageDailyTasks::~ManageDailyTasks()
{
}

void ManageDailyTasks::on_addButton_clicked ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    mAddDailyTaskWindow->show();
    //this->hide();
}

QString ManageDailyTasks::getDataFromModelByIndex (const int &index, const int &column)
{
    QModelIndex modelIndex;
    QVariant variant;
    modelIndex = mModel->index(index,column);
    variant=modelIndex.data();

    return variant.toString();
}

void ManageDailyTasks::on_removeButton_clicked ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    //get selected rows
    QModelIndexList indexes = mUi->tableView->selectionModel()->selectedRows();

    qSort(indexes.begin(), indexes.end());

    //remove last index in list
    while (!indexes.isEmpty())
    {
        //ToDo: remove from database
        QString task = getDataFromModelByIndex(indexes.last().row(), 0);
        mDatabase->removeTaskFromDailyTasks("vlado", task);

        mModel->removeRows(indexes.last().row(), 1);
        indexes.removeLast();
    }
}

void ManageDailyTasks::closeEvent (QCloseEvent *)
{
    qDebug () <<__PRETTY_FUNCTION__;
    emit(updateTableViewMainWindow());
}

void ManageDailyTasks::reloadDailyTasks ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    //remove all data from tableView
    mModel->removeRows(0, mModel->rowCount());
    //load data from sqlite database
    DailyTasksStructure dailyTasksStructure;
    dailyTasksStructure = mDatabase->getDailyTasksData("vlado");
    //fill tableView with the data from the database
    std::vector<DailyTask> dailyTasks = dailyTasksStructure.getDailyTasks();

    for (unsigned int i = 0; i<dailyTasks.size(); ++i)
    {
        addDataInTableView(dailyTasks[i].getTask(),
                           dailyTasks[i].getPoints(),
                           dailyTasks[i].getAmountEarnLosePoints(),
                           dailyTasks[i].getTypeEntry());
    }
}

void ManageDailyTasks::showEvent(QShowEvent *)
{
    reloadDailyTasks ();
}


void ManageDailyTasks::initModelTableView()
{
    mModel->setHorizontalHeaderItem(0, new QStandardItem(QString("Task")));
    mModel->setHorizontalHeaderItem(1, new QStandardItem(QString("Earned Points")));
    mModel->setHorizontalHeaderItem(2, new QStandardItem(QString("Amount")));
    mModel->setHorizontalHeaderItem(3, new QStandardItem(QString("Type")));
    mUi->tableView->setModel(mModel.get());
}

void ManageDailyTasks::addDataInTableView(const QString &task, const QString &points, const QString &amountEarnLose, const QString &type)
{
    mModel->setRowCount(mModel->rowCount()+1);

    mModel->setData(mModel->index(mModel->rowCount()-1,0),task);
    mModel->setData(mModel->index(mModel->rowCount()-1,1),points);
    mModel->setData(mModel->index(mModel->rowCount()-1,2),amountEarnLose);
    mModel->setData(mModel->index(mModel->rowCount()-1,3),type);

    //set data to be not editable
    mModel->item(mModel->rowCount()-1,0)->setEditable(false);
    mModel->item(mModel->rowCount()-1,1)->setEditable(false);
    mModel->item(mModel->rowCount()-1,2)->setEditable(false);
    mModel->item(mModel->rowCount()-1,3)->setEditable(false);
}

void ManageDailyTasks::onUpdateTableView ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    reloadDailyTasks ();
}
