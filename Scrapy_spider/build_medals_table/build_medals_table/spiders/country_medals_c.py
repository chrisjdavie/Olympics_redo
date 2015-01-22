'''
Created on 23 Oct 2014

@author: chris
'''
class country_medals:
    def __init__(self,rank,name):
        self.rank = rank
        self.name = name
        
    def golds_in(self,no):
        self.golds = no
        
    def silvers_in(self,no):
        self.silvers = no 
        
    def bronzes_in(self,no):
        self.bronzes = no 
        
    def medals_in(self,medals):
        self.golds_in(medals[0])
        self.silvers_in(medals[1])
        self.bronzes_in(medals[2])