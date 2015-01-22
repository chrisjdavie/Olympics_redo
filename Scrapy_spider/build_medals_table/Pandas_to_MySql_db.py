'''
Created on 24 Oct 2014

@author: chris
'''
from sqlalchemy.orm.session import sessionmaker
def main():
    
    import sqlalchemy as sa
    
    conn_str = "mysql://chris:pythonaccess@localhost/winter_olympics"
    engine = sa.create_engine(conn_str,echo=True) 
#     metadata = sa.MetaData(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    
    for a in sess.query(Dates):
        print a.id, a.year
        
    for a in sess.query(Country):
        print a.id, a.name
    
#     raw_input()    
    
    from os import listdir
    pickle_files = [ f for f in listdir('.') if f[-2:] == '.p' ]
    
    for fname in pickle_files[:1]:
        year = int(fname[:-2])
        
        year_q = sess.query(sa.exists().where(Dates.year == year)).scalar()
        print year_q
        if not year_q:
            this_year = Dates(year=year)
            sess.add(this_year)
            sess.commit()
            year_id = this_year.id
#             raw_input()
            
            import pickle
            with open(fname) as f:
                medals_table = pickle.load(f)
                
            print len(medals_table)
            raw_input()
            for rank in medals_table:
                country_name = rank.name
                country_q = sess.query(sa.exists().where(Country.name == country_name)).scalar()
                if not country_q:
                    country = Country(name=country_name)
                    sess.add(country)
                    sess.commit()
                county_id = sess.query(Country.id).filter(Country.name==country_name).first()
                
                rank_tmp = Results(country_id=county_id,year_id=year_id,rank=rank.rank,golds=rank.golds,silvers=rank.silvers,bronzes=rank.bronzes)
                ''''So, this is where I got to.  Put this in the db, check the db is working, and it's all golden?'''
                sess.add(country)
                sess.commit()
                
    for a in sess.query(Dates):
        print a.id, a.year
        
    for a in sess.query(Country):
        print a.id, a.name
           
    sess.query(Dates).delete()
    sess.query(Country).delete()
    sess.query(Results).delete() 
    sess.commit()
        
#     import pickle
#     with open(fname) as f:
#         yr_medals=pickle.load(f)
#         
#     print yr_medals[0].name
#     
# #     from pandas.io import sql
# #     import MySQLdb
# #     
# #     con = MySQLdb.connect(user="chris",passwd="pythonaccess")
#     import sqlalchemy as sa
#     print sa.__version__
#     
#     conn_str = "mysql://chris:pythonaccess@localhost/winter_olympics"
#     engine = sa.create_engine(conn_str,echo=True)
#     metadata = sa.MetaData(engine)
# #     conn = engine.connect()
#     metadata.reflect(engine)
#     
#     print metadata.tables.keys()
#     
#     Session = sessionmaker(bind=engine)
#     sess = Session()
#     print 'sam'
#     bob = sess.query(sa.exists().where(Country.name == 'United States')).scalar()  #Country).filter_by(name='can').exists().scalar()
#     print bob
    
    '''Add a row'''
#     US_country = Country(name='United States')
#     sess.add(US_country)
#     sess.commit()
    '''Create table line'''
#     Country.metadata.create_all(engine)    
    '''Create db lines (requires appropriate privaledges, did it but don't know which line did that)'''
#     conn.execute("commit")
#     conn.execute("create database winter_olympics")
#     conn.close()


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Country(Base):
    __tablename__ = 'country'
    
    id   = Column(Integer,primary_key=True)
    name = Column(String(32))
     
class Results(Base):
    __tablename__ = 'results'
    
    id          = Column(Integer,primary_key=True)
    country_id  = Column(Integer)
    year_id     = Column(Integer)
    rank        = Column(Integer)
    golds       = Column(Integer)
    silvers     = Column(Integer)
    bronzes     = Column(Integer)
    
class Dates(Base):
    __tablename__ = 'dates'
    id      = Column(Integer,primary_key=True)
    year    = Column(Integer)
    
    
if __name__ == '__main__':
    main()