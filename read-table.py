#!/usr/bin/python3

TABLE_FILE = "table.txt"
IP_FILE = "ip-list.txt"

table = []
iplist = []

tf = open(TABLE_FILE)

for line in tf:
    table.append(line)

tf.close()

begin = -1
end = -1

for i in range(0, len(table)):
    if table[i].find("Chain f2b-SSH") != -1:
        begin = i+1
        print(i)
    if begin != -1:
        if table[i].find("RETURN") != -1:
            end = i

j = 0
for i in range(0, len(table)):
    if i > begin and i < end:
        iplist.append(table[i][:-1])
        j+=1

ipf = open(IP_FILE, 'w')

for item in iplist:
    splite = item.split(' ')
    ip = splite[9]
    ipf.write(ip + "\n")

ipf.close()
