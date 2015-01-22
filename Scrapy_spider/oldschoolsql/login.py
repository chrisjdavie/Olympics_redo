'''
Created on 18 Dec 2014

@author: chris
'''
def login():
    import MySQLdb
    mysql_cn= MySQLdb.connect(host='localhost', 
                    user='pyuser', passwd='pythonaccess', 
                    db='winter_olympics')
    cur = mysql_cn.cursor()
    
    return cur, mysql_cn