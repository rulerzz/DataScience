# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:47:45 2023

@author: admin
"""

import pandas as pd
import numpy as np

df = pd.read_csv("./lecture-notes/mckinsey.csv")
print(df)

"""
Prints pandas.core.frame.DataFrame
"""
print(type(df))

"""
Prints summary
"""
print(df.info())

"""
Prints rows,columns
"""
print(df.shape)

"""
Prints first 5 by default if given args may edftend

default:  df.head()
       country  year  population continent  life_edfp     gdp_cap
0  Afghanistan  1952     8425333      Asia    28.801  779.445314
1  Afghanistan  1957     9240934      Asia    30.332  820.853030
2  Afghanistan  1962    10267083      Asia    31.997  853.100710
3  Afghanistan  1967    11537966      Asia    34.020  836.197138
4  Afghanistan  1972    13079460      Asia    36.088  739.981106

df.head(15)
        country  year  population continent  life_edfp      gdp_cap
0   Afghanistan  1952     8425333      Asia    28.801   779.445314
1   Afghanistan  1957     9240934      Asia    30.332   820.853030
2   Afghanistan  1962    10267083      Asia    31.997   853.100710
3   Afghanistan  1967    11537966      Asia    34.020   836.197138
4   Afghanistan  1972    13079460      Asia    36.088   739.981106
5   Afghanistan  1977    14880372      Asia    38.438   786.113360
6   Afghanistan  1982    12881816      Asia    39.854   978.011439
7   Afghanistan  1987    13867957      Asia    40.822   852.395945
8   Afghanistan  1992    16317921      Asia    41.674   649.341395
9   Afghanistan  1997    22227415      Asia    41.763   635.341351
10  Afghanistan  2002    25268405      Asia    42.129   726.734055
11  Afghanistan  2007    31889923      Asia    43.828   974.580338
12      Albania  1952     1282697    Europe    55.230  1601.056136
13      Albania  1957     1476505    Europe    59.280  1942.284244
14      Albania  1962     1728137    Europe    64.820  2312.888958
"""
print(df.head())
print(df.head(15))

print(df.tail())
"""
Prints last records
default:  df.tail()
       country  year  population continent  life_edfp     gdp_cap
1699  Zimbabwe  1987     9216418    Africa    62.351  706.157306
1700  Zimbabwe  1992    10704340    Africa    60.377  693.420786
1701  Zimbabwe  1997    11404948    Africa    46.809  792.449960
1702  Zimbabwe  2002    11926563    Africa    39.989  672.038623
1703  Zimbabwe  2007    12311143    Africa    43.487  469.709298
"""

print(df.tail(14))
"""
df.tail(14)
       country  year  population continent  life_edfp      gdp_cap
1690    Zambia  2002    10595811    Africa    39.193  1071.613938
1691    Zambia  2007    11746035    Africa    42.384  1271.211593
1692  Zimbabwe  1952     3080907    Africa    48.451   406.884115
1693  Zimbabwe  1957     3646340    Africa    50.469   518.764268
1694  Zimbabwe  1962     4277736    Africa    52.358   527.272182
1695  Zimbabwe  1967     4995432    Africa    53.995   569.795071
1696  Zimbabwe  1972     5861135    Africa    55.635   799.362176
1697  Zimbabwe  1977     6642107    Africa    57.674   685.587682
1698  Zimbabwe  1982     7636524    Africa    60.363   788.855041
1699  Zimbabwe  1987     9216418    Africa    62.351   706.157306
1700  Zimbabwe  1992    10704340    Africa    60.377   693.420786
1701  Zimbabwe  1997    11404948    Africa    46.809   792.449960
1702  Zimbabwe  2002    11926563    Africa    39.989   672.038623
1703  Zimbabwe  2007    12311143    Africa    43.487   469.709298
"""

print(df.describe(percentiles=[.20, .40, .60, .80]))
# 	year	population	life_exp	gdp_cap
# count	1704.00000	1.704000e+03	1704.000000	1704.000000
# mean	1979.50000	2.960121e+07	59.474439	7215.327081
# std	17.26533	1.061579e+08	12.917107	9857.454543
# min	1952.00000	6.001100e+04	23.599000	241.165876
# 25%	1965.75000	2.793664e+06	48.198000	1202.060309
# 50%	1979.50000	7.023596e+06	60.712500	3531.846988
# 75%	1993.25000	1.958522e+07	70.845500	9325.462346
# max	2007.00000	1.318683e+09	82.603000	113523.132900

# include objects in describe
print(df.describe(include="object"))
# 	country	continent
# count	1704	1704
# unique	142	5
# top	Afghanistan	Africa
# freq	12	624

# show headers
print(df.columns)
# Index(['country', 'year', 'population', 'continent', 'life_exp', 'gdp_cap'], dtype='object')

# show headers if dictionary
print(df.keys())
# Index(['country', 'year', 'population', 'continent', 'life_exp', 'gdp_cap'], dtype='object')

# access a column
print(df["country"])
# 0       Afghanistan
# 1       Afghanistan
# 2       Afghanistan
# 3       Afghanistan
# 4       Afghanistan
#            ...     
# 1699       Zimbabwe
# 1700       Zimbabwe
# 1701       Zimbabwe
# 1702       Zimbabwe
# 1703       Zimbabwe
# Name: country, Length: 1704, dtype: object

# type of column
print(type(df["country"]))
# pandas.core.series.Series

# get head of certain columns
print(df[["country", "continent"]].head())
# 	country	continent
# 0	Afghanistan	Asia
# 1	Afghanistan	Asia
# 2	Afghanistan	Asia
# 3	Afghanistan	Asia
# 4	Afghanistan	Asia

# get unique values from a column
print(df["country"].unique())
# array(['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
#        'Australia', 'Austria', 'Bahrain', 'Bangladesh', 'Belgium',
#        'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
#        'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon',
#        'Canada', 'Central African Republic', 'Chad', 'Chile', 'China',
#        'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.',
#        'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Czech Republic',
#        'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt',
#        'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Ethiopia',
#        'Finland', 'France', 'Gabon', 'Gambia', 'Germany', 'Ghana',
#        'Greece', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Haiti',
#        'Honduras', 'Hong Kong, China', 'Hungary', 'Iceland', 'India',
#        'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
#        'Jamaica', 'Japan', 'Jordan', 'Kenya', 'Korea, Dem. Rep.',
#        'Korea, Rep.', 'Kuwait', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
#        'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mauritania',
#        'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Morocco',
#        'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands',
#        'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman',
#        'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland',
#        'Portugal', 'Puerto Rico', 'Reunion', 'Romania', 'Rwanda',
#        'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
#        'Sierra Leone', 'Singapore', 'Slovak Republic', 'Slovenia',
#        'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
#        'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
#        'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia',
#        'Turkey', 'Uganda', 'United Kingdom', 'United States', 'Uruguay',
#        'Venezuela', 'Vietnam', 'West Bank and Gaza', 'Yemen, Rep.',
#        'Zambia', 'Zimbabwe'], dtype=object)

# 142
print(len(df["country"].unique()))

# print counts of each distinct value in a column
print(df['country'].value_counts())

# Afghanistan          12
# Pakistan             12
# New Zealand          12
# Nicaragua            12
# Niger                12
#                      ..
# Eritrea              12
# Equatorial Guinea    12
# El Salvador          12
# Egypt                12
# Zimbabwe             12
# Name: country, Length: 142, dtype: int64

# print unique values count from column 
print(df["country"].nunique())
# 142

# Rename a column
# inplace will change the data inside the current object 
# if we dont provide inplace we will get changes in output but actual dataframe df wont change
df.rename({"country":"Country"}, axis=1, inplace=True)

# 	Country	year	population	continent	life_exp	gdp_cap
# 0	Afghanistan	1952	8425333	Asia	28.801	779.445314
# 1	Afghanistan	1957	9240934	Asia	30.332	820.853030
# 2	Afghanistan	1962	10267083	Asia	31.997	853.100710
# 3	Afghanistan	1967	11537966	Asia	34.020	836.197138
# 4	Afghanistan	1972	13079460	Asia	36.088	739.981106
# ...	...	...	...	...	...	...
# 1699	Zimbabwe	1987	9216418	Africa	62.351	706.157306
# 1700	Zimbabwe	1992	10704340	Africa	60.377	693.420786
# 1701	Zimbabwe	1997	11404948	Africa	46.809	792.449960
# 1702	Zimbabwe	2002	11926563	Africa	39.989	672.038623
# 1703	Zimbabwe	2007	12311143	Africa	43.487	469.709298
# 1704 rows × 6 columns

print(df.country) # dont use it

# drop a column
df.drop("continent", axis=1, inplace=True)

# add a new column
df["New"] = df["life_exp"] + df["year"]
print(df)

# create a new column and populate it with a loop 
df['Own'] = [i for i in range(df.shape[0])]

# drop columns
df.drop(["New", "Own"], axis=1, inplace=True)