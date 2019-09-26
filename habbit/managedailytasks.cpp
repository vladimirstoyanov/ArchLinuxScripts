#include "managedailytasks.h"
#include "ui_managedailytasks.h"

ManageDailyTasks::ManageDailyTasks(QWidget *parent) :
    QWidget(parent),
    mAddDailyTaskWindow(std::make_shared<AddDailyTaskWindow> ()),
    mUi(std::make_shared<Ui::ManageDailyTasks> ())
{
    mUi->setupUi(this);
}

ManageDailyTasks::~ManageDailyTasks()
{
}

void ManageDailyTasks::on_addButton_clicked ()
{
    qDebug () <<__PRETTY_FUNCTION__;
    mAddDailyTaskWindow->show();
    this->hide();
}
void ManageDailyTasks::on_removeButton_clicked ()
{
    qDebug () <<__PRETTY_FUNCTION__;
}

void ManageDailyTasks::closeEvent (QCloseEvent *)
{

}
void ManageDailyTasks::showEvent(QShowEvent *)
{
    //ToDo: load data from 'daily_tasks'
}
