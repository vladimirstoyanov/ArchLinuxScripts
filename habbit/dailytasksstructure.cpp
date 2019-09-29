#include "dailytasksstructure.h"

DailyTasksStructure::DailyTasksStructure()
{

}


std::vector<DailyTask> DailyTasksStructure::getDailyTasks ()
{
    return mDailyTasks;
}

void DailyTasksStructure::addDailyTask (DailyTask dailyTask)
{
    mDailyTasks.push_back(dailyTask);
}
