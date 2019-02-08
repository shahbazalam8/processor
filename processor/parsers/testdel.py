dbtype='mysql'
dbuser='root'
dbpasswd='testing'
server='localhost'

dburi = dbtype + "://" + dbuser + ":" + dbpasswd + "@" + server + "/mysql"
print(dburi)