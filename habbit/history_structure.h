#ifndef HISTORYSTRUCTURE_H
#define HISTORYSTRUCTURE_H

#include <QString>

#include <memory>
#include <vector>

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
        mDay (""),
        mMonth (""),
        mYear (""),
        mDayOfWeek (""),
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
    void setDay (const QString &day) { this->mDay = day; }
    void setMonth (const QString &month) { this->mMonth = month; }
    void setYear (const QString &year) { this->mYear = year; }
    void setDayOfWeek (const QString &dayOfWeek) { this->mDayOfWeek = dayOfWeek; }
    void setPoints (const QString &points) { this->mPoints = points; }
    void setNotes (const QString &notes) { this->mNotes = notes; }

    QString getTask () { return this->mTask; }
    QString getTypeEntry () { return this->mTypeEntry; }
    QString getTaskPoints () { return this->mTaskPoints; }
    QString getCurrentAmount () { return this->mCurrentAmount; }
    QString getAmountEarnLosePoints () { return this->mAmountEarnLosePoints; }
    QString getTime () { return this->mTime; }
    QString getDay () { return this->mDay; }
    QString getMonth () { return this->mMonth; }
    QString getYear () { return this->mYear; }
    QString getDayOfWeek () { return this->mDayOfWeek; }
    QString getPoints () { return this->mPoints; }
    QString getNotes () { return this->mNotes; }

private:
    QString mTask;
    QString mTypeEntry;
    QString mTaskPoints;
    QString mCurrentAmount;
    QString mAmountEarnLosePoints;
    QString mTime;
    QString mDay;
    QString mMonth;
    QString mYear;
    QString mDayOfWeek;
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
