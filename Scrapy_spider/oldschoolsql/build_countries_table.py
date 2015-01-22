'''
Created on 18 Dec 2014

@author: chris
'''
import sys
sys.path.append('../build_medals_table/')


def main():
    
    def what_info_fn(rank,fname):
        return rank.name
#     country_names
    country_names = get_info(what_info_fn)
        
    import numpy as np
    country_names = np.unique(country_names)
    
    print 'db stuff'
    
    from login import login
    
    cur, mysql_cn = login()
    
    drop_table_str = 'DROP TABLE countries'
    cur.execute(drop_table_str)
    
    build_table_str = 'CREATE TABLE countries( ' +\
                        ' id INT NOT NULL AUTO_INCREMENT, ' +\
                        ' name VARCHAR(32), ' +\
                        ' PRIMARY KEY(id) ' +\
                        ' ) '
    
    cur.execute(build_table_str)
    
    print 'insert stuff'
    
    for country_name in country_names:
        print country_name
        insert_str = ' INSERT INTO countries (name) ' +\
                        ' VALUES ( \'' + country_name + '\') '
        cur.execute(insert_str)
        
    mysql_cn.commit()
    mysql_cn.close()    
    
def get_info(what_info_fn):
                        
    dat_dir = '/home/chris/Projects/Olympics/data/'
    
    from os import listdir
    pickle_files = [ f for f in listdir(dat_dir) if f[-2:] == '.p' ]
    
    dats_out = []
    
    for fname in pickle_files:
        
        fname = dat_dir + fname
        
        import pickle
        with open(fname) as f:
            medals_table = pickle.load(f)
            
            for rank in medals_table:
                dat_out = what_info_fn(rank,fname)
                dats_out.append(dat_out)      
    return dats_out 

if __name__ == '__main__':
    main()