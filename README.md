# Olympics_redo
Statistical analysis of the winter olympics.

2015-01-22

This intends to compare the medals results of the Winter Olympics to
various factors, including GDP; health, sports spending, etc; lattitude
and longitute; previous winter olympics results; if the country is host
or not.

The flow for recreating this is:

'Scrapy_spider/build_medals_table/build_medals_table/'

Where the winter olympics results are scraped and pickled.

'Scrapy_spider/build_medals_table/oldschoolsql'

Where these results are put into a database.

'Scrapy_spider/ranking_scoring_correlations'

Where it is verified that the ranking-by-golds won correlates
with awarding points to medals won.

'google_apis/'

Is an attempt to get the lattitude and longitude of countries and
comparing this to medals won.  This is not completed yet

Copyright (C) 2015  Christopher Joseph Davie, MIT License
