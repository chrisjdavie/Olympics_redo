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

Copyright (C) 2015  Christopher Joseph Davie

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
