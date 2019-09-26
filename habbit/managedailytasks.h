#ifndef MANAGEDAILYTASKS_H
#define MANAGEDAILYTASKS_H

#include <QCloseEvent>
#include <QtDebug>
#include <QWidget>

#include <memory>

#include "adddailytaskwindow.h"

namespace Ui {
class ManageDailyTasks;
}

class ManageDailyTasks : public QWidget
{
    Q_OBJECT


public:
    explicit ManageDailyTasks(QWidget *parent = nullptr);
    ~ManageDailyTasks();

private slots:
    void on_addButton_clicked ();
    void on_removeButton_clicked ();

private:
         void closeEvent (QCloseEvent *);
         void showEvent(QShowEvent *);
private:
    std::shared_ptr<AddDailyTaskWindow> mAddDailyTaskWindow;
    std::shared_ptr<Ui::ManageDailyTasks> mUi;
};

#endif // MANAGEDAILYTASKS_H
