'''
Created on 21 Dec 2014

@author: chris
'''
def main():
    
    year_0 = '2014'
    
    results = get_results(year_0)
    
    ranks = []
    scores = []
    
    for result in results:
#         print result[0]
        scores.append(result[1]*3 + result[2]*2 + result[3]*1)
#         print result[4]
        ranks.append(result[4])    
        
    import numpy as np
    
    i_ranks = np.argsort(ranks)
    ranks  = np.array(ranks)[i_ranks]
    scores = np.array(scores)[i_ranks]
    
    for rank, score in zip(ranks,scores):
        print rank, score
    

def get_results(year_0):
    from oldschoolsql import login
    
    cur, mysql_cn = login()
    
    search_str = ' SELECT countries.name, results.golds, results.silvers, results.bronzes, results.rank ' +\
                   ' FROM dates ' +\
                   ' JOIN results ON results.year_id = dates.id ' +\
                   ' JOIN countries ON results.country_id = countries.id ' +\
                 ' WHERE year = ' + year_0
                 
    cur.execute(search_str)
#     print dir(cur)
    results = cur.fetchall()

    mysql_cn.commit()
    mysql_cn.close()         
        
    return results

if __name__ == '__main__':
    main()