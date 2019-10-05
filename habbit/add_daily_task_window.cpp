#include "add_daily_task_window.h"
#include "ui_adddailytaskwindow.h"

AddDailyTaskWindow::AddDailyTaskWindow(QWidget *parent) :
    QWidget(parent),
    mUi(std::make_shared<Ui::AddDailyTaskWindow> ()),
    mDataBase (std::make_shared<DataBase> ())
{
    mUi->setupUi(this);

    mUi->comboBox->addItem(tr("checkbox"));
    mUi->comboBox->addItem(tr("incrementJudgeAfter"));
    mUi->comboBox->addItem(tr("incrementGainAfter"));

    mUi->timeComboBox->addItem(tr("daily"));
    mUi->timeComboBox->addItem(tr("weekly"));
}

AddDailyTaskWindow::~AddDailyTaskWindow()
{
}


void AddDailyTaskWindow::closeEvent (QCloseEvent *)
{
    qDebug()<<__PRETTY_FUNCTION__;
}

void AddDailyTaskWindow::showEvent(QShowEvent *)
{
    qDebug()<<__PRETTY_FUNCTION__;
}

void AddDailyTaskWindow::on_cancelButton_clicked ()
{
    qDebug()<<__PRETTY_FUNCTION__;
    this->hide();
}

QString AddDailyTaskWindow::getItemTextByTimeCombobox(const int &index)
{
    switch (index)
    {
        case 0:
            return "daily";
        case 1:
            return "weekly";
        default:
            return "";
    }
}

QString AddDailyTaskWindow::getItemTextByTypeCombobox (const int &index)
{
    switch (index)
    {
        case 0:
            return "checkbox";
        case 1:
            return "incrementJudgeAfter";
        case 2:
            return "incrementGainAfter";
        default:
            return "";
    }
    return "";
}

void AddDailyTaskWindow::on_addButton_clicked ()
{
    qDebug()<<__PRETTY_FUNCTION__;
    QString comboboxSelectedItem = "";
    qDebug()<<"AddDailyTaskWindow::on_addButton_clicked:"<<comboboxSelectedItem<<", current index: "<<mUi->comboBox->currentIndex();

    //validate fields
    if ((mUi->taskEdit->text()=="") ||
        (mUi->pointsEdit->text()=="") ||
        (mUi->amountEdit->text()=="" && mUi->comboBox->currentIndex()!=0))
    {
        QMessageBox::critical(this, tr("Error!"),
                                    tr("Fill all values, please!"),
                                    QMessageBox::Ok);
        return;
    }

    //check if the task exist in the data base
    if (!mDataBase->checkTaskExistInDailyTasks(mUi->taskEdit->text()))
    {
        QMessageBox::critical(this, tr("Error!"),
                                    tr("Task exist in the database!"),
                                    QMessageBox::Ok);
        return;
    }

    //add data to the database
    //ToDo: change this hardcoded username with someone getted from the database
    mDataBase->insertIntoDailyTasks("vlado",
                                    mUi->taskEdit->text(),
                                    getItemTextByTypeCombobox(mUi->comboBox->currentIndex()),
                                    mUi->pointsEdit->text(),
                                    mUi->amountEdit->text(),
                                    getItemTextByTimeCombobox(mUi->timeComboBox->currentIndex()),
                                    "0"); //current_amount is 0 when add a daily task

    emit (updateTableView());
    this->hide();
}
