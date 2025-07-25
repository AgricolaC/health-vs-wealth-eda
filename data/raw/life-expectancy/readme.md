# Life expectancy - Data package

This data package contains the data that powers the chart ["Life expectancy"](https://ourworldindata.org/grapher/life-expectancy?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on July 25, 2025.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Life expectancy at birth – period tables – Various sources
The period life expectancy at birth, in a given year.
Last updated: December 3, 2024  
Next update: December 2025  
Date range: 1543–2023  
Unit: years  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
UN WPP (2024); HMD (2024); Zijdeman et al. (2015); Riley (2005) – with minor processing by Our World in Data

#### Full citation
UN WPP (2024); HMD (2024); Zijdeman et al. (2015); Riley (2005) – with minor processing by Our World in Data. “Life expectancy at birth – Various sources – period tables” [dataset]. Human Mortality Database, “Human Mortality Database”; United Nations, “World Population Prospects”; Zijdeman et al., “Life Expectancy at birth 2”; James C. Riley, “Estimates of Regional and Global Life Expectancy, 1800-2001” [original data].
Source: UN WPP (2024); HMD (2024); Zijdeman et al. (2015); Riley (2005) – with minor processing by Our World In Data

### What you should know about this data
* Period life expectancy is a metric that summarizes death rates across all age groups in one particular year.
* For a given year, it represents the remaining average lifespan for a hypothetical group of people, if they experienced the same age-specific death rates throughout the rest of their lives as the age-specific death rates seen in that particular year.
* Prior to 1950, we use HMD (2024) data combined with Zijdeman (2015). From 1950 onwards, we use UN WPP (2024) data. For old regional data, we use Riley (2005) estimates.

### Sources

#### Human Mortality Database
Retrieved on: 2024-11-27  
Retrieved from: https://www.mortality.org/Data/ZippedDataFiles  

#### United Nations – World Population Prospects
Retrieved on: 2024-12-02  
Retrieved from: https://population.un.org/wpp/Download/  

#### Zijdeman et al. – Life Expectancy at birth
Retrieved on: 2023-10-10  
Retrieved from: https://clio-infra.eu/Indicators/LifeExpectancyatBirthTotal.html  

#### James C. Riley – Estimates of Regional and Global Life Expectancy, 1800-2001
Retrieved on: 2023-10-10  
Retrieved from: https://doi.org/10.1111/j.1728-4457.2005.00083.x  


    