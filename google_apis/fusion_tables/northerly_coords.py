'''
Created on 9 Jan 2015

@author: chris
'''
def main():
    
    most_northerly_coords = extract_most_notherly_point()
    
    for m in most_northerly_coords:
        print m
    
def extract_most_notherly_point():    
#     print 'a'
    import pickle
    
    with open('/tmp/fusion_op.p','rb') as f:
        dets = pickle.load(f)
    
    import numpy as np
    
    most_northerly_coords = []
    
    for det in dets['rows']: 
#         if det[0] == test_name:
#         print det[0]
        northerly_coords = []
        
#         print det[1].keys()
        geo_key = 'geometries'
        if geo_key in det[1].keys():
            for geo in det[1][geo_key]:
                for coords in geo['coordinates']:
                    coords = np.array(coords)
                    i_northerly = np.argmax(coords[:,1])
                    northerly_coords.append(coords[i_northerly])
#     print 'b'
            northerly_coords = np.array(northerly_coords)
#         print northerly_coords
            i_northerly = np.argmax(northerly_coords[:,1])
            
            most_north_coords = northerly_coords[i_northerly]
            
        else:
            geo_key = 'geometry'
#                 print type(det[1][geo_key])
#                 print det[1][geo_key].keys()
            coords = np.array(det[1][geo_key]['coordinates'][0])
            
#             print coords
            i_northerly = np.argmax(coords[:,1])
            most_north_coords = coords[i_northerly]
            
#         if det[0] == test_name:
        most_northerly_coords.append({'country name':det[0],'most north coords':most_north_coords})
    
    return most_northerly_coords
    
if __name__ == '__main__':
    main()