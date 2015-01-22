'''
I really ought to do this class-based, but I'd have to think
quite hard and then that wouldn't be right, I just don't have
the time right now to start the itterative process.

Created on 21 Nov 2014

@author: chris
'''
import numpy as np 
import fiona
from matplotlib.patches import Polygon as Polygon_m    
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as pl
from matplotlib import font_manager

def draw_london_map(locn_count,cbar_label,cmap='gist_heat_r'):
    
    ''' locn_count, dict, { postcode_str, counts_int } '''
    
    ax, p, pcc_new, xyy = setup_map(cmap)
    
    cts_map = []
    
    for map_pc in pcc_new:
        try:
#         if map_pc == 'SW3':
            cts_map.append(locn_count[map_pc])
#             else:
#                 cts_map.append(1)
        except(KeyError):
            print "No sales in ", map_pc
            cts_map.append(0)
            
#         raw_input()
    cts_map = np.array(cts_map)
    print locn_count['SW3']
#     raw_input()
    
    
    p.set_array(cts_map)
    p.set_clim(0,np.max(np.array(cts_map)))
    ax.add_collection(p)
    cb = pl.colorbar(p,label=cbar_label)
    cb_ax = cb.ax
    text = cb_ax.yaxis.label
    font = font_manager.FontProperties(weight='bold')
    text.set_font_properties(font)
#     cbtext=cb.get_texts()
#     pl.setp(cbtext)
    
    put_Thames_on(ax)
#     
    return pcc_new, xyy, ax, cts_map
#         

def put_Thames_on(ax):
    shp_fname = '/home/chris/Projects/Tutorfair/drawing_a_map/Rivers_in_europe/Thames_ish2'
    
    with fiona.open(shp_fname + '.shp') as shps:
        for i, shp in enumerate(shps):
            print i
#             map_pc  = shp['properties']['name']
            xy = shp.items()[0][1]['coordinates'][0]

#     m.readshapefile(shp_fname,'waters')    
#     for shapedict, xy in zip(m.waters_info,m.waters):
            poly = Polygon_m(xy, facecolor='blue', alpha=1.0)
            ax.add_patch(poly)    
            

def setup_map(cmap='gist_heat_r'):
        
    shp_fname = '/home/chris/Projects/Tutorfair/drawing_a_map/postcode_shapefiles/London_only/postcode'
    
    with fiona.open(shp_fname + '.shp') as shps:
        bds = shps.bounds
    
    extra = 0.01
    ll = (bds[0], bds[1])
    ur = (bds[2], bds[3])
    
    from itertools import chain
    coords = list(chain(ll, ur))
    w, h = coords[2] - coords[0], coords[3] - coords[1]
    
    xlims = [ coords[0] - extra * w, coords[2] + extra * w ]
    ylims = [ coords[1] - extra + 0.01 * h, coords[3] + extra + 0.01 * h ]
    
    
    '''Here I'm trying to merge all the EC and WC areas'''
    from shapely.geometry import Polygon, LinearRing
     
    xyy_new  = [ None, None ]
    pcc_new  = [ 'EC', 'WC' ]
     
    EC_pgs = []
    WC_pgs = []
    
    with fiona.open(shp_fname + '.shp') as shps:
        
        for i, shp in enumerate(shps):
            print i
            map_pc  = shp['properties']['name']
            xy = shp.items()[0][1]['coordinates'][0]
            
            if len(np.shape(xy)) == 3 and len(xy) == 1:
                xy = xy[0]
            elif len(np.shape(xy[0])) == 2 and len(xy) == 2:
                '''This is not general and should be fixed if I extend this to outside London'''
                xy0 = xy[0]
                xy1 = xy[1]
                xy = xy0
                if len(xy1[0]) > len(xy0[1]):
                    xy = xy1 
                    
            if map_pc[:2] == 'EC':
                EC_pgs.append(Polygon(xy))
            elif map_pc[:2] == 'WC':
                WC_pgs.append(Polygon(xy))
            else:
                pcc_new.append(map_pc)
                xyy_new.append(xy)
             
    from shapely.ops import cascaded_union
    WC_pg = cascaded_union(WC_pgs)
    EC_pg = cascaded_union(EC_pgs)
    
    xyy_new[0] = np.array(LinearRing(EC_pg.exterior.coords).xy).transpose()
     
    xyy_new[1] = np.array(LinearRing(WC_pg.exterior.coords).xy).transpose()
    
    
    pl.xlim(xlims)
    pl.ylim(ylims)
    
    ax = pl.gca()
    
    patches = []
    
    for i, (map_pc, xy) in enumerate(zip(pcc_new,xyy_new)):
        
        xy = np.array(xy)
        
        poly = Polygon_m(xy, True) 
        
        patches.append(poly)

    p = PatchCollection(patches,cmap=cmap)
    
    return ax, p, pcc_new, xyy_new


if __name__ == '__main__':
    pass