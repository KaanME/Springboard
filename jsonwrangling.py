# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:52:56 2018

@author: Kaan
"""
import pandas as pd
import json
from pandas.io.json import json_normalize
import numpy as np

# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]

json_normalize(data, 'counties')

json_normalize(data, 'counties',['state','shortname',['info','governor']])

json.load((open('data/world_bank_projects_less.json')))

sample_json_df = pd.read_json('data/world_bank_projects_less.json')
sample_json_df


#JSON Exercises
json.load((open('data/world_bank_projects.json')))          #load file
worldBanks = pd.read_json('data/world_bank_projects.json')  #load file in pandas

worldBanks.info()       #see the column names and content of worldBanks
worldBanks.columns()    #identify column names of worldBanks

#EXERCISE 1
#count the number of times each country apears in 'countryname', take top 10
mostProjects = worldBanks['countryname'].value_counts().head(10)    
mostProjects

#EXERCISE 2
worldBanks['mjtheme_namecode'].head()                       #analyze the column in question
mjthemes = worldBanks['mjtheme_namecode']                   #assign column to a variable

json_normalize(worldBanks['mjtheme_namecode'][0])           #json_normalize list of dicts, or each row of column

mjthemesdf = pd.DataFrame()                                 #create empty dataset
for project in worldBanks['mjtheme_namecode']:              #append each mini data frame obtained from normalizing each row
    mjthemesdf = mjthemesdf.append(json_normalize(project))
mjthemesdf = mjthemesdf.reindex(range(len(mjthemesdf)))     #reset the index

topthemes = mjthemesdf['name'].value_counts().head(10)      #count each unique theme name return top 10
topthemes

#EXERCISE 3

mjthemesdf['code'] = pd.to_numeric(mjthemesdf['code'])      #convert number strings into integers
mjthemesdf['code'].max()

themesfilled = pd.DataFrame()                               #create empty datafram
for code in range(mjthemesdf.code.max()):                   #for each code number, fill in empty strings with corresponding name
    codedf = mjthemesdf.loc[mjthemesdf['code'] == code+1].copy()
    namecol = mjthemesdf.loc[mjthemesdf['code'] == code+1]['name'].replace('', np.nan).ffill().bfill()
    codedf['name'] = namecol
    themesfilled = themesfilled.append(codedf)
themesfilled = themesfilled.sort_index()                    #rested order of index

topthemesfilled = themesfilled['name'].value_counts().head(10)  #count each unique theme name and return top 10
topthemesfilled















