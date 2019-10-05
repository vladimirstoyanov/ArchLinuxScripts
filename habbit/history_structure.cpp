#include "history_structure.h"

HistoryStructure::HistoryStructure()
{

}

std::vector<History> HistoryStructure::getHistoryItem()
{
    return mHistory;
}

void HistoryStructure::addHistoryItem (History history)
{
    mHistory.push_back(history);
}
