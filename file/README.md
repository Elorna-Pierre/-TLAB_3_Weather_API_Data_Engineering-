# Weather API Data Engineering

You are a data engineer at a Brazil-based weather prediction startup called Curu-SightLinks to an external site.. The goal of this startup is to analyze weather trends in Brazil and predict the output of non-durable consumer goods at harvest time.

One major threat to Brazil's biggest export, coffee, is leaf rust (barring tariffs). This fungus thrives in humid environments and causes plants to wither. Your company recently won a contract with the local government of Minas Gerais to analyze how humidity (and auxiliary measures) determine the yearly output of coffee.

You will collect data on relative humidity, precipitation, temperature, surface pressure, soil temperature, and soil moisture in Minas Gerais using the open-meteoLinks to an external site. weather API. After transforming this dataset into a CSV file, you will perform exploratory data analysis to discover how yearly weather trends influence harvest outcomes.

## Instructions

There are three Python files which you will create in this repository to complete this project:
* weather_api.py
* data_transform.ipynb
* explore_weather.ipynb

Further directions for each file are listed below: 

**weather_api.py**

Create a file called `weather_api.py`

Access the website https://open-meteo.com/en/docs and generate historical hourly data on Minais Gerais (lat: -21.72,  long: -45.39) from Jan 1 2022 to Dec 31 2023. Generate data on `temperature`, `relative humidity`, `precipitation`, and `surface pressure`.

Use this URL to pull your JSON data programmatically into your Python program, and save this object into the path `data/json`.

Remove all the meta-data from this resultant JSON file and keep only the data that describes the time and the variables listed above. Convert this modified JSON file into a CSV file and save it to the path `data/CSV/`. 

**Note** You are only limited to 1000 API calls per day. If you use any more, you must wait for this limit to be reset tomorrow.

**data_transform.ipynb**

Create a jupyter notebook in the folder titled `notebooks` called `data_transform.py`. Within this file you will be create the following dataframes and save them as a csv files into your folder `data/csv`.

* monthly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available months
* yearly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available years
* yearly medians on `temperature`, `relative humidity`, `precipitation`, and `surface pressure` for all available years along with harvest data (`million_60kgs_bag`, `nonbear_mill_trees`, `bear_mill_trees`, `avg_unemp_perc`) for each respective year present for Minas Gerais

Be sure to drop rows that contain missing values as you perform these data transformations.

**explore_weather.ipynb**

After creating these CSV files, you will then perform exploratory data analysis on the data file that describes historical yearly weather data and crop output. As exploratory data analysis should entail a variety of data visualizations to determine patterns and relationships, we welcome you to perform your own EDA to determine trends.

At the minimum, however, you should be generating visualizations that explore the following questions and patterns:

* How have harvest outcomes changed for Minas Gerais throughout the years?  
    * Are these harvest outcomes similar to other regions in Brazil?  
    * Which region produces the most coffee (by sub-category) in Brazil?  
* How has unemployment changed in the various coffee-producing regions of Brazil?  
* How have weather outcomes changed for Minas Gerais throughout the years?  
* Does it seem that coffee harvest is dependent on weather? If so, which specific variable seems to "coffee" harvest. If not, which variable might appear to be correlated with harvest outcomes instead?   

For each of these questions and subsequent visualizations, be sure to include a markdown block in your jupyter notebook explaining which trends you see.

To form visualizations that answer these analytical questions, utilize your knowledge of appropriate visualizations for categorical and quantitative variables.

## Submission 

The due date for this project is `01/17`.

To begin work on this project, you will create a repository in your GitHub and copy all these template files into your repo.

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

