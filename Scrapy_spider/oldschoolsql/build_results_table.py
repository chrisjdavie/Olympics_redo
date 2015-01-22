'''
Created on 18 Dec 2014

@author: chris
'''
def main():
    
    from build_countries_table import get_info
    
    # year, country, rank, golds, silvers, bronzes
    def what_info_fn(rank,fname):
        return int(fname[-6:-2]), rank
    
    results = get_info(what_info_fn)
    

    
    from login import login
    
    cur, mysql_cn = login()   
    
    drop_table_str = 'DROP TABLES results'
    cur.execute(drop_table_str)
    
    create_table_str = ' CREATE TABLE results( ' +\
                         ' country_id INT NOT NULL, ' +\
                         ' year_id INT NOT NULL, ' +\
                         ' rank INT, ' +\
                         ' golds INT, ' +\
                         ' silvers INT, ' +\
                         ' bronzes INT, ' +\
                         ' PRIMARY KEY (country_id,year_id), ' +\
                         ' FOREIGN KEY (country_id) REFERENCES countries (id), ' +\
                         ' FOREIGN KEY (year_id) REFERENCES dates (id) ' +\
                       ' ) '
                       
    cur.execute(create_table_str)
    
    for year, result in results:
        print result.name, year
        
        search_str = ' SELECT id FROM countries WHERE name = \'' + result.name + '\''
        cur.execute(search_str)
        c_id = cur.fetchone()[0]
        
        search_str = ' SELECT id FROM dates WHERE year = ' + str(year) + ''
        cur.execute(search_str)
        y_id = cur.fetchone()[0]
        
        insert_str = ' INSERT INTO results ' +\
                       ' ( country_id, year_id, rank, golds, silvers, bronzes ) ' +\
                       ' VALUES ( ' +\
                           str(c_id) + ', ' + str(y_id) + ', ' + str(result.rank) + ', ' + str(result.golds) + ', ' + str(result.silvers) + ', ' + str(result.bronzes) +\
                       ' ) '
        
        cur.execute(insert_str)
    
    mysql_cn.commit()
    mysql_cn.close()         

if __name__ == '__main__':
    main()