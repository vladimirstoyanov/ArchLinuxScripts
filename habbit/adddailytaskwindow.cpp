#include "adddailytaskwindow.h"
#include "ui_adddailytaskwindow.h"

AddDailyTaskWindow::AddDailyTaskWindow(QWidget *parent) :
    QWidget(parent),
    mUi(std::make_shared<Ui::AddDailyTaskWindow> ())
{
    mUi->setupUi(this);
}

AddDailyTaskWindow::~AddDailyTaskWindow()
{
}
