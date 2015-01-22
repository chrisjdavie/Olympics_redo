'''
Created on 20 Nov 2014

@author: chris
'''

import matplotlib.pyplot as pl
import numpy as np

class scatter_plot:
    
    def __init__(self,xx,yy,xlabel='',ylabel='',s=20.0,title='',label='',marker='x',fig_i=1,colour='Maroon'):
        self.fig = pl.figure(fig_i)
        
        self.xx = xx
        self.yy = yy
#         print s
        self.ps = []
        p = pl.scatter(xx,yy,s=s,label=label,marker=marker,color=colour)#, edgecolors=None)
        self.ps.append(p)
        
        pl.xlabel(xlabel, fontweight='bold')
        pl.ylabel(ylabel, fontweight='bold')
        pl.title(  title, fontweight='bold')        
        
        ax = pl.gca()
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()   
#         ax.xaxis.set_ticks_position('none')         
        
    def lin_reg(self):
        from scipy import stats
        
        slope, intercept, r_value, _, _ = stats.linregress(self.xx,self.yy)
        
#         import numpy as np
        xx_lin = np.linspace(np.min(self.xx), np.max(self.xx), 2)
        yy_lin = xx_lin*slope + intercept       
        
        self.lin(xx_lin,yy_lin,label='Lin. reg., R$^\mathrm{2}$=' + str(r_value**2)[:4], colour='blue', linestyle='--')
                 
        
    def lin(self,xx,yy,label='',colour='green',linestyle=':'):
        p = pl.plot(xx,yy,linestyle=linestyle,label=label,color=colour)
#         print type(p[0])
        self.ps.append(p[0])    
        
    def leg(self,loc='upper left',box_q=False):
#         for P in self.ps:
#             print type(P)
#             print P.get_label()
        
        lg = pl.legend(self.ps,[ P.get_label() for P in self.ps ],loc=loc)
        lg.draw_frame(box_q)
        ltext = lg.get_texts()
        pl.setp(ltext, fontweight='bold')
        
    def show(self):
        pl.show()