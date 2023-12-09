from AuditLog import AuditLog

auditLog = AuditLog ()
exes = auditLog.getExecutables ()

for i in range (len(exes)):
    print (exes[i])
