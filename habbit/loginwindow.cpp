#include "loginwindow.h"
#include "ui_loginwindow.h"

LoginWindow::LoginWindow(QWidget *parent) :
        QWidget(parent),
        mUi(std::make_shared<Ui::LoginWindow> ()),
        mCreateAccountWindow (std::make_shared<CreateAccountWindow> ()),
        mMainWindow (std::make_shared<MainWindow> ())
{
    mUi->setupUi(this);
    mUi->passwordEdit->setEchoMode(QLineEdit::Password);
}

LoginWindow::~LoginWindow()
{
}

void LoginWindow::on_cancelButton_clicked()
{
    qDebug()<<__PRETTY_FUNCTION__;
    this->hide();
}

void LoginWindow::on_createAccountButton_clicked()
{
    qDebug()<<__PRETTY_FUNCTION__;
    mCreateAccountWindow->show();
}

void LoginWindow::on_loginButton_clicked()
{
    qDebug()<<__PRETTY_FUNCTION__;
    QString username = mUi->usernameEdit->text();
    QString password = mUi->passwordEdit->text();

    //check is username exist in the database
    DataBase database;
    QString passwordDataBase;
    if (!database.getPasswordByUsername(username, passwordDataBase))
    {
        QMessageBox::critical(this, tr("Error!"),
                                       tr("There isn't such username!"),
                                       QMessageBox::Ok);
        return;
    }

    QString passwordHesh;
    QCryptographicHash cryptographicHash (QCryptographicHash::Sha256);
    passwordHesh=QString(cryptographicHash.hash(password.toLatin1(), QCryptographicHash::Sha256).toHex());

    if (passwordHesh!=passwordDataBase)
    {
        QMessageBox::critical(this, tr("Error!"),
                                       tr("The password doesn't match!"),
                                       QMessageBox::Ok);
        return;
    }

    mMainWindow->show();
    this->hide();
}
