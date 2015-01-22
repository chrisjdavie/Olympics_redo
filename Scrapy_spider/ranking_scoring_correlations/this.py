'''
Created on 21 Dec 2014

@author: chris
'''
def main():
    
    year_0 = '2014'
    
    from get_rankings import get_results
    
    results = get_results(year_0)
    
    ranks = []
    scores = []    
    
    for result in results:
        print result[0]
        scores.append(result[1]*3 + result[2]*2 + result[3]*1)
        print scores[-1]
        print result[4]
        ranks.append(result[4])
    
    import numpy as np
    
    ranks  = np.array(ranks)
    ranks = np.max(ranks) - ranks + 1
    
    i_ranks = np.argsort(ranks)
    ranks  = np.array(ranks)[i_ranks]
    scores = np.array(scores)[i_ranks]    
    
    from scipy.stats import spearmanr
    
    rho, pval = spearmanr(ranks,scores)
    
    print rho, pval
    
    from shared_pltj import scatter_plot
    
    from scipy import stats
    
    D, p = stats.ks_2samp(ranks,scores)
    
    print D, p
    
    p = scatter_plot(ranks,scores)
    p.show()
    
if __name__ == '__main__':
    main()