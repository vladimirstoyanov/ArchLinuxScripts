date -d "$(</proc/uptime awk '{print $1}') seconds ago"
