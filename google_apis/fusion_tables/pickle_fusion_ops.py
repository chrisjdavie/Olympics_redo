'''
Created on 5 Jan 2015

@author: chris
'''
from googleapiclient import sample_tools

def main(argv):
    print argv 
    print __file__
    print __doc__
    
# Authenticate and construct service.
    service, _ = sample_tools.init(
        argv, 'fusiontables', 'v2', __doc__, __file__)    
    
    tableid = "1N2LBk4JHwWpOY4d9fobIn27lfnZ5MDy-NoqqRpk"
#     api_key = "AIzaSyBk8sImslk8jvVZcJ8Le_Y4aqHox_TFA4I"
    
    get_op = service.table().get(tableId=tableid)
    
#     print dir(service)
    
    get_tbl = get_op.execute()
    
#     print dir(bob)
    print get_tbl['columns']
    
    select_details = service.query().sql(sql='SELECT \'Name\', \'geometry\' FROM ' + tableid)
    
    dets = select_details.execute()
    
    import pickle
    
    with open('/tmp/fusion_op.p','w+') as f:
        pickle.dump(dets,f)
    
#     extract_most_notherly_point(dets)
    

    
import sys

if __name__ == '__main__':
    main(sys.argv)