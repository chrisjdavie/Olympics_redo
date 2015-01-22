'''
testing pickling

Created on 23 Oct 2014

@author: chris
'''
import pickle

class Integer(object):
    def __init__(self, x):
        self.x = x

i = Integer(7)

f = open('test.p','w+')

pickle.dump(i,f)

f.close()