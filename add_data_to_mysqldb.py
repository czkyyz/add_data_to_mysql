import MySQLdb
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='alex3714',db='python')
    #conn.select_db('python')
    cur =conn.cursor()
    cur.execute("select * from host_list")
    v_list = []
    for i in range(0,100):
        v_list.append(("testServer%s"%i,"192.169.0.%s"%i,"Ubuntu"))
    #print(v_list)
    cur.scroll(4,mode="relative")
    #print(cur.fetchall())
    cur.executemany("insert into host_list values(%s,%s,%s)",v_list)
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
    print("MysqlError%d:%s"%(e.args[0],e.args[1]))