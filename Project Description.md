# Project Description
## Goals
The main goal of this project was to familiarize myself with using Dash, Plotly, and a bit of CSS. I found a google data set (which you can find in the README file in the repository) containing a lot of data about people’s daily locations during the pandemic, this was saved a changes in % as compared to a base line (presumably before the pandemic), I later combined the data with GDP data which helped make the plots a bit more informative. The question I hoped to be able to answer was whether you would be able to see a difference in trends between the countries with higher vs lower GDP’s, I don’t think you can clearly see it in this bubble plot, looking at the line graph we can see that for example parks had peaks of popularity after during summer and work places drop in popularity in January in countries with a high GDP.  Another interesting things to note it that there are more countries with a GDP per capita between 0 and 1000 USD than between 60k and 120k USD. 

## What I learned
As for the things I ended up learning during this project, the biggest things I’ve learned are the things I initially  set out to learn, I’ve learned quit a bit about dash components, HTML, different Plotly plots and CSS. Somethings I had to learn along the way which I did not anticipate were writing SQL files (even though I did not create new tables), which I needed to be able to select data from the large data file without memory issues, and using python to query SQL databases, I learned a bit about files types, e.g. parquet files can only read entire columns, but you can select which columns you want the computer to read, where as CSV files can select the first N rows, but you have to read all the columns, and discard the ones you don’t need after having read them to memory.  Finally I learned quite a bit about git, and why you should not try to push a 3gb file to GitHub and commit a few more times after that, since you will have to revert your repository to fix it. 

## Future improvements
Improvements for the future would to make sure my process is more efficient, currently I’m reading a very large CSV files, writing it to a database, extracting data from that data base, manipulating that data, and saving it to a parquet files which undergoes further processing in the Dash app, this could of course be made a lot more efficient, but due to time constraints I cannot change that anymore.  Although I do like that I’ve kind of used the “benefits” of each file type during this project

Further more it would probably be a good idea to implement some kind of statistical analysis next time, because even though this is a visualization it would be very useful to not have to eye ball all the conclusions.