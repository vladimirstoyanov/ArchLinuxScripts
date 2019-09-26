#ifndef CREATEACCOUNTWINDOW_H
#define CREATEACCOUNTWINDOW_H

#include <QCloseEvent>
#include <QCryptographicHash>
#include <QDebug>
#include <QMessageBox>
#include <QWidget>

#include <memory>

#include "database.h"

namespace Ui {
class CreateAccountWindow;
}

class CreateAccountWindow : public QWidget
{
    Q_OBJECT

public:
    explicit CreateAccountWindow(QWidget *parent = nullptr);
    ~CreateAccountWindow();

private slots:
        void on_okButton_clicked ();
        void on_cancelButton_clicked();

private:
         void closeEvent (QCloseEvent *);
         void showEvent(QShowEvent *);

private:
    std::shared_ptr<Ui::CreateAccountWindow> mUi;
    QCryptographicHash mQCryptographicHash;
    std::shared_ptr<DataBase> mDataBase;
};

#endif // CREATEACCOUNTWINDOW_H
