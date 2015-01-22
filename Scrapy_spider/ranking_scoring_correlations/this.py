'''
Compares a ranking based on number of golds for 2014 to
a score given 3 points for a gold, 2 for a silver and 1
for bronze.  A points based system makes some of the 
subsequent tests more doable using commonly-understood
techniques, but needs to be shown to be broadly comparable
to the well-accepted 'more gold!' system.

This uses the spearmanr, the Spearman's rank correlation
coefficient, the which is a non-parametric analogue of 
the Pearson correlation coefficient (often 'the correlation
coefficient').  While this is probably not as good as the
Kendall tau, it is quicker to explain.

rho = 0.956, with a p = 2.75e-14

It is probably significant, but the test employed here 
assumes a student's t distribution, which might be valid
for a test comparison if I had a few hundred points.  I 
don't here, but if there's a more accurate way of testing 
this with these few points I couldn't find it quickly.

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
    
    print 'Spearman', rho, pval
    
    from shared_pltj import scatter_plot
    
    from scipy import stats
    
    D, p = stats.ks_2samp(ranks,scores)
    
    print D, p
    
    p = scatter_plot(ranks,scores)
    p.show()
    
if __name__ == '__main__':
    main()