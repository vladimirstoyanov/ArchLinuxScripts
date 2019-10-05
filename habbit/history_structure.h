#ifndef HISTORYSTRUCTURE_H
#define HISTORYSTRUCTURE_H

#include <QString>

#include <memory>
#include <vector>

/*
 *     createTable ("history",
                 "create table history "
                 "(id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "
                 "username varchar, "
                 "date varchar, "
                 "points varchar,"
                 "notes varchar,"
                 "task varchar, "
                 "type_entry varchar, "
                 "task_points varchar, "
                 "amount_earn_lose varchar, "
                 "time varchar, " //daily, mouthly
                 "current_amount varchar)");
                 */
class History
{
public:
     History ():
        mTask (""),
        mTypeEntry (""),
        mTaskPoints (""),
        mCurrentAmount (""),
        mAmountEarnLosePoints (""),
        mTime (""),
        mDate (""),
        mPoints (""),
        mNotes ("")
    {
    }
    virtual ~History () = default;

    void setTask (const QString & task) { this->mTask = task; }
    void setTypeEntry (const QString &typeEntry) { this->mTypeEntry = typeEntry; }
    void setTaskPoints (const QString &taskPoints) { this->mTaskPoints = taskPoints; }
    void setAmountEarnLosePoints (const QString &amountEarnLosePoints) { this->mAmountEarnLosePoints = amountEarnLosePoints; }
    void setTime (const QString &time) { this->mTime = time; }
    void setCurrentAmount (const QString &currentAmount) { this->mCurrentAmount = currentAmount; }
    void setDate (const QString &date) { this->mDate = date; }
    void setPoints (const QString &points) { this->mPoints = points; }
    void setNotes (const QString &notes) { this->mNotes = notes; }

    QString getTask () { return this->mTask; }
    QString getTypeEntry () { return this->mTypeEntry; }
    QString getTaskPoints () { return this->mTaskPoints; }
    QString getCurrentAmount () { return this->mCurrentAmount; }
    QString getAmountEarnLosePoints () { return this->mAmountEarnLosePoints; }
    QString getTime () { return this->mTime; }
    QString getDate () { return this->mDate; }
    QString getPoints () { return this->mPoints; }
    QString getNotes () { return this->mNotes; }

private:
    QString mTask;
    QString mTypeEntry;
    QString mTaskPoints;
    QString mCurrentAmount;
    QString mAmountEarnLosePoints;
    QString mTime;
    QString mDate;
    QString mPoints;
    QString mNotes;
};

class HistoryStructure
{
public:
    HistoryStructure();
    virtual ~HistoryStructure ()=default;

    std::vector<History> getHistoryItem ();
    void addHistoryItem (History history);

private:
    std::vector<History> mHistory;
};

#endif // HISTORYSTRUCTURE_H
