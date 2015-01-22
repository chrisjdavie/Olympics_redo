2015-01-22

Assumes a 'winter_olympics' MySQL database hosted on the local computer,
with a user satisfying "user='pyuser', passwd='pythonaccess'", which has 
pretty complete access rights to the 'winter_olympics' db.

Also assumes a data directory - in build_countries_table.py, variable named
'dat_dir', needs to point to where the output of scrapy is.

Order of execution -
    build_countries_table.py
    build_years_table.py
    build_results_table.py

The next stage is '../ranking_scoring_correlation/'
    
