#ifndef DAILYTASKSSTRUCTURE_H
#define DAILYTASKSSTRUCTURE_H

#include <QCheckBox>
#include <QLabel>
#include <QLineEdit>
#include <QString>

#include <memory>
#include <vector>

class DailyTaskWidgets
{
public:
    DailyTaskWidgets (QWidget *parent, const QString &typeEntry, const QString &taskName):
        mTaskLabel(std::make_shared<QLabel> (parent)),
        mEntryCheckBox (std::make_shared<QCheckBox> (parent)),
        mEntryLineEdit (std::make_shared<QLineEdit> (parent)),
        mPoints (std::make_shared<QLabel> (parent)),
        mAmount (std::make_shared<QLabel> (parent)),
        mTypeEntry (typeEntry)

    {
        mTaskLabel->setText(taskName);

    }
    virtual ~DailyTaskWidgets () = default;

    /*
    std::shared_ptr<QLabel> getTaskLabel () { return this->mTaskLabel; }
    std::shared_ptr<QLabel> getEntryCheckBox () { return this->mEntryCheckBox; }
    std::shared_ptr<QLabel> getEntryLineEdit () { return this->mEntryLineEdit; }
    std::shared_ptr<QLabel> getPoints () { return this->mPoints; }
    std::shared_ptr<QLabel> getAmount () { return this->mAmount; }
    */

    //positioning and show
    //

private:
    std::shared_ptr<QLabel> mTaskLabel;
    std::shared_ptr<QCheckBox> mEntryCheckBox;
    std::shared_ptr<QLineEdit> mEntryLineEdit;
    std::shared_ptr<QLabel> mPoints;
    std::shared_ptr<QLabel> mAmount;
    QString mTypeEntry;
};

class DailyTask
{
public:
    DailyTask ():
        mTask (""),
        mTypeEntry (""),
        mPoints (""),
        mCurrentAmount (""),
        mAmountEarnLosePoints (""),
        mTime ("")
    {
    }
    virtual ~DailyTask () {}

    void setTask (const QString & task) { this->mTask = task; }
    void setTypeEntry (const QString &typeEntry) { this->mTypeEntry = typeEntry; }
    void setPoints (const QString &points) { this->mPoints = points; }
    void setAmountEarnLosePoints (const QString &amountEarnLosePoints) { this->mAmountEarnLosePoints = amountEarnLosePoints; }
    void setTime (const QString &time) { this->mTime = time; }
    void setCurrentAmount (const QString &currentAmount) { this->mCurrentAmount = currentAmount; }

    QString getTask () { return this->mTask; }
    QString getTypeEntry () { return this->mTypeEntry; }
    QString getPoints () { return this->mPoints; }
    QString getCurrentAmount () { return this->mCurrentAmount; }
    QString getAmountEarnLosePoints () { return this->mAmountEarnLosePoints; }
    QString getTime () { return this->mTime; }

private:
    QString mTask;
    QString mTypeEntry;
    QString mPoints;
    QString mCurrentAmount;
    QString mAmountEarnLosePoints;
    QString mTime;
};

class DailyTasksStructure
{
public:
    DailyTasksStructure();
    virtual ~DailyTasksStructure () {}

    std::vector<DailyTask> getDailyTasks ();
    void addDailyTask (DailyTask dailyTask);

private:
    std::vector<DailyTask> mDailyTasks;
};

#endif // DAILYTASKSSTRUCTURE_H
