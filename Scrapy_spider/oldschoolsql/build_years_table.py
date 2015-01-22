'''
Created on 18 Dec 2014

@author: chris
'''
def main():
    
    from build_countries_table import get_info
    
    def what_info_fn(rank,fname):
        return int(fname[-6:-2])
    
    years = get_info(what_info_fn)
    
    import numpy as np
    years = np.unique(years)
    
    from login import login
    
    cur, mysql_cn = login()
        
    drop_table_str = 'DROP TABLES dates'
    cur.execute(drop_table_str)
    
    create_table_str = ' CREATE TABLE dates( ' +\
                         ' id INT NOT NULL AUTO_INCREMENT, ' +\
                         ' year INT, ' +\
                         ' PRIMARY KEY(id) ' +\
                       ' ) '
                       
    cur.execute(create_table_str)
    
    for year in years:
        insert_str = ' INSERT INTO dates (year) ' +\
                       ' VALUES ( ' + str(year) + ' ) '
        cur.execute(insert_str) 
    
    mysql_cn.commit()
    mysql_cn.close()        

if __name__ == '__main__':
    main()