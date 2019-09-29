#ifndef MANAGEDAILYTASKS_H
#define MANAGEDAILYTASKS_H

#include <QCloseEvent>
#include <QLineEdit>
#include <QLabel>
#include <QStandardItemModel>
#include <QtDebug>
#include <QWidget>

#include <memory>
#include <vector>

#include "adddailytaskwindow.h"
#include "dailytasksstructure.h"
#include "database.h"

namespace Ui {
class ManageDailyTasks;
}

class ManageDailyTasks : public QWidget
{
    Q_OBJECT


public:
    explicit ManageDailyTasks(QWidget *parent = nullptr);
    ~ManageDailyTasks();

    void reloadDailyTasks();

public slots:
    void onUpdateTableView ();

private slots:
    void on_addButton_clicked ();
    void on_removeButton_clicked ();

private:
    void closeEvent (QCloseEvent *);
    void showEvent(QShowEvent *);

signals:
    void updateTableViewMainWindow ();

private:
    void addDataInTableView(const QString &task, const QString &points, const QString &amount, const QString &type);
    QString getDataFromModelByIndex (const int &index, const int &column);
    void initModelTableView();


private:
    std::shared_ptr<AddDailyTaskWindow> mAddDailyTaskWindow;
    std::shared_ptr<DataBase> mDatabase;
    std::shared_ptr<QStandardItemModel> mModel;
    std::shared_ptr<Ui::ManageDailyTasks> mUi;
    std::vector<std::shared_ptr<QLabel>> mLabelList;
    std::vector<std::shared_ptr<QLineEdit>> mLineEditList;
};

#endif // MANAGEDAILYTASKS_H
