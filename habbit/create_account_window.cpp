#include "create_account_window.h"
#include "ui_createaccountwindow.h"
#include <QString>
CreateAccountWindow::CreateAccountWindow(QWidget *parent) :
    QWidget(parent),
    mUi(std::make_shared<Ui::CreateAccountWindow> ()),
    mQCryptographicHash(QCryptographicHash::Sha256),
    mDataBase (std::make_shared<DataBase> ())
{
    mUi->setupUi(this);
    mUi->passwordEdit->setEchoMode(QLineEdit::Password);
    mUi->repeatPasswordEdit->setEchoMode(QLineEdit::Password);
}

CreateAccountWindow::~CreateAccountWindow()
{
}

void CreateAccountWindow::closeEvent (QCloseEvent *)
{
    this->hide();
}

void  CreateAccountWindow::showEvent(QShowEvent *)
{
    //clear edit boxes
    mUi->usernameEdit->setText("");
    mUi->passwordEdit->setText("");
    mUi->repeatPasswordEdit->setText("");
}

void CreateAccountWindow::on_okButton_clicked ()
{
    qDebug()<<__PRETTY_FUNCTION__;
    QString username = mUi->usernameEdit->text();
    QString password = mUi->passwordEdit->text();
    QString repatedPassword = mUi->repeatPasswordEdit->text();
    if (password!=repatedPassword)
    {
        QMessageBox::critical(this, tr("Error!"),
                                       tr("Passwords don't match!"),
                                       QMessageBox::Ok);
        return;
    }

    //check is username exists in the data base
    if (!mDataBase->checkUsernameAvailable (username))
    {
        QMessageBox::critical(this, tr("Error!"),
                                       tr("The username is used. Please try with another username!"),
                                       QMessageBox::Ok);
        return;
    }

    QString passwordHash;
    QCryptographicHash cryptographicHash (QCryptographicHash::Sha256);
    passwordHash=QString(cryptographicHash.hash(password.toLatin1(), QCryptographicHash::Sha256).toHex());

    mDataBase->insertIntoAccounts(username, passwordHash);
    this->hide();
}

void CreateAccountWindow::on_cancelButton_clicked()
{
    qDebug()<<__PRETTY_FUNCTION__;
    this->hide();
}
