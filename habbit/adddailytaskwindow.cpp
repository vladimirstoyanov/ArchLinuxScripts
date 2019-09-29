#include "adddailytaskwindow.h"
#include "ui_adddailytaskwindow.h"

AddDailyTaskWindow::AddDailyTaskWindow(QWidget *parent) :
    QWidget(parent),
    mUi(std::make_shared<Ui::AddDailyTaskWindow> ()),
    mDataBase (std::make_shared<DataBase> ())
{
    mUi->setupUi(this);

    mUi->comboBox->addItem(tr("checkbox"));
    mUi->comboBox->addItem(tr("textbox"));
    mUi->comboBox->addItem(tr("incrementJudgeAfter"));
    mUi->comboBox->addItem(tr("incrementGainAfter"));
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

QString AddDailyTaskWindow::getItemText (const int &index)
{
    switch (index)
    {
        case 0:
            return "checkbox";
        case 1:
            return "textbox";
        case 2:
            return "incrementJudgeAfter";
        case 3:
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
                                    getItemText(mUi->comboBox->currentIndex()),
                                    mUi->pointsEdit->text(),
                                    mUi->amountEdit->text());

    emit (updateTableView());
    this->hide();
}
