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
        mAmountPoints ("")
    {
    }
    virtual ~DailyTask () {}

    void setTask (const QString & task) { this->mTask = task; }
    void setTypeEntry (const QString &typeEntry) { this->mTypeEntry = typeEntry; }
    void setPoints (const QString &points) { this->mPoints = points; }
    void setAmountPoints (const QString &amountPoints) { this->mAmountPoints = amountPoints; }

    QString getTask () { return this->mTask; }
    QString getTypeEntry () { return this->mTypeEntry; }
    QString getPoints () { return this->mPoints; }
    QString getAmountPoints () { return this->mAmountPoints; }

private:
    QString mTask;
    QString mTypeEntry;
    QString mPoints;
    QString mAmountPoints;

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
