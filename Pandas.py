# Pandas
# Series
import pandas as pd
import numpy as np
series = pd.Series([1,2,3,4,5])
print(series)
'''
0    1
1    2
2    3
3    4
4    5
dtype: int64
'''
series = pd.Series([1,2,3,4,5], index=['a','b','c','d','c'])
print(series)
'''
a    1
b    2
c    3
d    4
c    5
dtype: int64
'''
print(series[2]) # 3
print(series.iloc[2]) # 3, 인덱스 기반

print(series['d']) # 4
print(series.loc['d']) # 4

print(series[2:])
'''
c    3
d    4
c    5
dtype: int64
'''
print(series.iloc[2:])
'''
c    3
d    4
c    5
dtype: int64
'''

# date_range
dates1 = pd.date_range('20190525', periods=12)
print(dates1)
'''
DatetimeIndex(['2019-05-25', '2019-05-26', '2019-05-27', '2019-05-28',
               '2019-05-29', '2019-05-30', '2019-05-31', '2019-06-01',
               '2019-06-02', '2019-06-03', '2019-06-04', '2019-06-05'],
              dtype='datetime64[ns]', freq='D')
'''
series = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
series.index = dates1
print(series)
'''
2019-05-25     1
2019-05-26     2
2019-05-27     3
2019-05-28     4
2019-05-29     5
2019-05-30     6
2019-05-31     7
2019-06-01     8
2019-06-02     9
2019-06-03    10
2019-06-04    11
2019-06-05    12
Freq: D, dtype: int64
'''

# DataFrame
df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
df.to_csv('data.csv', index=False)
'''
  A         B         C         D
0  0.350321 -1.703510  1.872366 -1.744185
1  0.697886 -0.134966 -0.081319 -0.571860
2 -0.941900 -0.443987  1.141855 -0.036247
3 -0.354064  0.843784 -0.759549 -0.415161
4  0.053129  0.137098  1.170418 -1.667163
5 -0.252549 -0.969976 -0.188476 -0.080983
6  0.110817 -0.564984 -1.238936  0.188209
7 -0.036543 -1.766170  0.894899 -0.223467
8  1.691206  0.659383  0.125601 -0.031147
9 -0.813395  0.732903  1.274275  1.531366
'''
df = pd.read_csv('data.csv')
days = pd.date_range('20190525', periods=10)
df.index = days
print(df)
'''
                   A         B         C         D
2019-05-25 -0.224821 -1.032161 -0.843770 -1.198716
2019-05-26  0.533863 -0.397688  0.232872  0.080827
2019-05-27  0.929351  0.002959 -0.428448  2.111585
2019-05-28 -0.108018  0.559095 -0.303224  1.830943
2019-05-29  0.651523 -0.501879 -1.436901 -2.484986
2019-05-30  1.414163 -0.763858  2.217013  1.866800
2019-05-31 -0.847404  0.526766 -2.654531  1.191829
2019-06-01  0.667680 -0.268561  0.826031  1.227230
2019-06-02  0.714714 -1.653488 -0.325652 -1.138183
2019-06-03 -0.139156 -0.076099 -0.346663  0.244723
'''
print(df.index)
'''
DatetimeIndex(['2019-05-25', '2019-05-26', '2019-05-27', '2019-05-28',
               '2019-05-29', '2019-05-30', '2019-05-31', '2019-06-01',
               '2019-06-02', '2019-06-03'],
              dtype='datetime64[ns]', freq='D')
'''
print(df.values)
'''
[[-0.22482116 -1.03216076 -0.8437699  -1.19871634]
 [ 0.5338626  -0.39768847  0.23287223  0.08082726]
 [ 0.92935109  0.00295908 -0.42844757  2.11158477]
 [-0.10801805  0.55909514 -0.30322443  1.83094325]
 [ 0.65152321 -0.50187911 -1.43690135 -2.48498645]
 [ 1.41416287 -0.76385812  2.2170135   1.8668001 ]
 [-0.84740447  0.52676585 -2.65453052  1.19182927]
 [ 0.6676799  -0.26856054  0.82603077  1.22723018]
 [ 0.71471413 -1.65348777 -0.32565195 -1.13818297]
 [-0.13915587 -0.0760992  -0.34666331  0.24472321]]
'''

print() # Generating a Crosstab
df = pd.DataFrame(
        {
            "Gender": ['Male', 'Male', 'Female', 'Female', 'Female'],
            "Team": [1,2,3,4,5]
        })
print(df)
'''
   Gender  Team
0    Male     1
1    Male     2
2  Female     3
3  Female     4
4  Female     5
'''
print(pd.crosstab(df.Gender, df.Team)) # 행, 열
'''
Team    1  2  3  4  5
Gender
Female  0  0  1  1  1
Male    1  1  0  0  0
'''
print(pd.crosstab(df.Team, df.Gender))
'''
Gender  Female  Male
Team
1            0     1
2            0     1
3            1     0
4            1     0
5            1     0
'''
