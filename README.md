# Doughboys Data Table
Michael Nolan

2023-02-01

### Description
python script to scrape and extend the data table found on the Doughboys podcast wiki: https://doughboys.fandom.com/wiki/Episodes

### Requirements
This script requires the `numpy` and `pandas` packages.

### Running
To generate the most recent version of the data table, run the following command from wherever you've cloned the repo:

```python generate_doughboys_data.py```

The table file `doughboys_episode_data.csv` will then be updated to include all information on the website page listed at the top of the README.

### Table Format
The data table contains all the information listed on the wiki. It also contains broken-out columns for each individual guest and a separate column named "Topic" which is a short description of the restaurant discussed or the overall topic of the episode. This could be further refined, please feel free to contribute.
