#ifndef ADDDAILYTASKWINDOW_H
#define ADDDAILYTASKWINDOW_H

#include <QCloseEvent>
#include <QDebug>
#include <QMessageBox>
#include <QWidget>
#include <memory>

#include "database.h"

namespace Ui {
class AddDailyTaskWindow;
}

class AddDailyTaskWindow : public QWidget
{
    Q_OBJECT

public:
    explicit AddDailyTaskWindow(QWidget *parent = nullptr);
    ~AddDailyTaskWindow();

signals:
    void updateTableView ();

private slots:
        void on_addButton_clicked ();
        void on_cancelButton_clicked ();
private:
        QString getItemText (const int &index);
private:
         void closeEvent (QCloseEvent *);
         void showEvent(QShowEvent *);

private:
    std::shared_ptr<DataBase> mDataBase;
    std::shared_ptr<Ui::AddDailyTaskWindow> mUi;
};

#endif // ADDDAILYTASKWINDOW_H
