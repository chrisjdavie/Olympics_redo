2015-01-22

Run from terminal.

$ scrapy crawl medals

should make pickle files of the medal record in the above directory.

Eg. 2006.p - Golds, silvers, bronzes, country names from 2006.

The next stage for this is '../../oldschoolsql/' to build the tables
in the database.  This assumes that these *.p files have been copied
to a data directory.
