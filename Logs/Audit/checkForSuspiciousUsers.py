from AuditLog import AuditLog

auditLog = AuditLog ()
users = auditLog.getUsers ()

for i in range (len(users)):
    print (users[i])
