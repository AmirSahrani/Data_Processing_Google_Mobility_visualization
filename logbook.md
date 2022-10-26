Date: 15/10

Task: Find dataset / Get Idea about final project 

Problems: Choosing between datasets/topics, Hard to find an interesting data set that would be feasible to fully grasp in 2 week + learn new python libraries needed

Solutions: Decided to do a data visualization using the Dash python library, on the google mobility report

Resources: 

Kaggle: [https://www.kaggle.com/datasets/bigquery/covid19-google-mobility](https://www.kaggle.com/datasets/bigquery/covid19-google-mobility)

Dash:   [https://www.youtube.com/watch?v=hSPmj7mK6ng](https://www.youtube.com/watch?v=hSPmj7mK6ng)
------
Date: 16/10

Task: Learning Git

Problems: —

Solutions: — 

Resources: cs50 lecture

Date:17/10
------
Task: Meeting 

Problems: How big should this assignment be, is using dash and this data feasible 

Solutions: find minimum viable product, try to get that working, everything else is extra

Resources: Meeting

Date:18/10
------
Task: Clean data

Problems: CSV file big, lots of missing data points because of privacy, data is all compared to a baseline, not in absolute numbers, therefore it is hard to make initially intended bubble map

Solutions: For now just compare changes compared to base line in different countries

Resources:

Date:20/10
------
Task: make polts

Problems: very long compute times

Solutions: possible using Dask to create more efficient dataframes, otherwise I’ll have to use biqquery

Resources:

Date: 21/10
------
Task: Dealing with the large amount of data

Problems: Dask did not improve my issue/too difficult to implement, and biqquery is a paid google service :(

Solutions: I can create a local sql database using sqlite, and a plotly post explaining how it works

Resources:[https://plotly.com/python/v3/ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/#data-analysis-of-82-million-rows-with-python-and-sqlite](https://plotly.com/python/v3/ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/#data-analysis-of-82-million-rows-with-python-and-sqlite)

Date:23/10
------
Task: Increase performance, put figure into dash app

Problems: Data files too big, animation can’t get smooth, I also wanted to give every category a different symbol in order to have a visual differentiation, can’t push any git commits 

Solutions: Instead of sampling everyday, I took the average per week, also instead of a csv I used a parquet file, couldn’t get the symbols to work yet. For Git I removed all my commits that included the files that were too larger, and pushed the new changes

Resources: [https://plotly.com/python/bubble-charts/](https://plotly.com/python/bubble-charts/)

Date: 25/10
------
Task: add GDP data

Problems: can’t extract the current date in the animation frame, so I can’t automatically change the year

Solutions: Instead of automatically changing the year, give people option to change it manually, since the GPD does not really change in 3 years it doesn’t not have a large impact on the plot

Resources:

[https://www.imf.org/en/Publications/WEO/weo-database/2022/October/weo-report?c=512,914,612,171,614,311,213,911,314,193,122,912,313,419,513,316,913,124,339,638,514,218,963,616,223,516,918,748,618,624,522,622,156,626,628,228,924,233,632,636,634,238,662,960,423,935,128,611,321,243,248,469,253,642,643,939,734,644,819,172,132,646,648,915,134,652,174,328,258,656,654,336,263,268,532,944,176,534,536,429,433,178,436,136,343,158,439,916,664,826,542,967,443,917,544,941,446,666,668,672,946,137,546,674,676,548,556,678,181,867,682,684,273,868,921,948,943,686,688,518,728,836,558,138,196,278,692,694,962,142,449,564,565,283,853,288,293,566,964,182,359,453,968,922,714,862,135,716,456,722,942,718,724,576,936,961,813,726,199,733,184,524,361,362,364,732,366,144,146,463,528,923,738,578,537,742,866,369,744,186,925,869,746,926,466,112,111,298,927,846,299,582,487,474,754,698,&s=NGDPDPC,&sy=2020&ey=2022&ssm=0&scsm=1&scc=0&ssd=1&ssc=0&sic=0&sort=country&ds=.&br=1](https://www.imf.org/en/Publications/WEO/weo-database/2022/October/weo-report?c=512,914,612,171,614,311,213,911,314,193,122,912,313,419,513,316,913,124,339,638,514,218,963,616,223,516,918,748,618,624,522,622,156,626,628,228,924,233,632,636,634,238,662,960,423,935,128,611,321,243,248,469,253,642,643,939,734,644,819,172,132,646,648,915,134,652,174,328,258,656,654,336,263,268,532,944,176,534,536,429,433,178,436,136,343,158,439,916,664,826,542,967,443,917,544,941,446,666,668,672,946,137,546,674,676,548,556,678,181,867,682,684,273,868,921,948,943,686,688,518,728,836,558,138,196,278,692,694,962,142,449,564,565,283,853,288,293,566,964,182,359,453,968,922,714,862,135,716,456,722,942,718,724,576,936,961,813,726,199,733,184,524,361,362,364,732,366,144,146,463,528,923,738,578,537,742,866,369,744,186,925,869,746,926,466,112,111,298,927,846,299,582,487,474,754,698,&s=NGDPDPC,&sy=2020&ey=2022&ssm=0&scsm=1&scc=0&ssd=1&ssc=0&sic=0&sort=country&ds=.&br=1)
------
Date: 26/10

Task: Styling

Problems: plotly natural earth projection has a border that is white, and can’t be changed through plot_bgcolor Also styling is hard, so it took me a while to figure it out.

Solutions: Instead of the natural earth projection I used the default projection.

Resources:
