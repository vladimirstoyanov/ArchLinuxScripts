#ifndef ADDDAILYTASKWINDOW_H
#define ADDDAILYTASKWINDOW_H

#include <QCloseEvent>
#include <QWidget>
#include <memory>

namespace Ui {
class AddDailyTaskWindow;
}

class AddDailyTaskWindow : public QWidget
{
    Q_OBJECT

public:
    explicit AddDailyTaskWindow(QWidget *parent = nullptr);
    ~AddDailyTaskWindow();

private:
         void closeEvent (QCloseEvent *);
         void showEvent(QShowEvent *);

private:
    std::shared_ptr<Ui::AddDailyTaskWindow> mUi;
};

#endif // ADDDAILYTASKWINDOW_H
