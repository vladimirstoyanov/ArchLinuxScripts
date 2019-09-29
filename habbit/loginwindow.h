#ifndef LOGINWINDOW_H
#define LOGINWINDOW_H

#include <QCryptographicHash>
#include <QDebug>
#include <QWidget>
#include <memory>

#include "createaccountwindow.h"
#include "database.h"
#include "mainwindow.h"

namespace Ui {
class LoginWindow;
}

class LoginWindow : public QWidget
{
    Q_OBJECT
public:
    explicit LoginWindow(QWidget *parent = nullptr);
     ~LoginWindow();
signals:


private slots:
     void on_cancelButton_clicked();
     void on_createAccountButton_clicked();
     void on_loginButton_clicked();

private:
        std::shared_ptr<Ui::LoginWindow> mUi;
        std::shared_ptr<CreateAccountWindow> mCreateAccountWindow;
        std::shared_ptr<MainWindow> mMainWindow;
};

#endif // LOGINWINDOW_H
