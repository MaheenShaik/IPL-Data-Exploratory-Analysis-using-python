#loading the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
#loading the ipl matches dataset
ipl=pd.read_csv("matches.csv")
'''print(ipl)'''
#having a glance at the first five records of the dataset
'''print(ipl.head())'''
#looking at the number of rows and columns of a dataset
'''print(ipl.shape)'''
#getting the frequency of most man of the match awards
mom=ipl['player_of_match'].value_counts()
'''print(mom)'''
#getting top 10 players with most man of the match awards
top10mom=ipl['player_of_match'].value_counts()[0:10]
'''print(top10mom)'''
#getting top 5 players with most man of the match awards
top5=(mom.head())
'''print(top5)'''
#bar plot between top5 players and no.of mom awards
x=top5.keys()
'''print(x)'''
y=top5
'''plt.figure(figsize=(8,5))
plt.bar(x,y,color='g')'''
'''plt.show()'''
#getting the frequency of result column
result=ipl['result'].value_counts()
'''print(result)'''
#finding out the number of toss wins w.r.t. each team
tosswin=ipl['toss_winner'].value_counts()
'''print(tosswin)'''
#extracting the records where the team won batting first
battingfirst=ipl[ipl['win_by_runs']!=0]
'''print(battingfirst)'''
#looking at the head
battingfirsthead=battingfirst.head()
'''print(battingfirsthead)'''
#making a histogram for win_by_runs column//histogram is used to see distribution of a column(numerical)//
#histogram is used to visualize only numerical columns
plt.figure(figsize=(5,8))
plt.hist(battingfirst['win_by_runs'],color='g')
plt.title("Distribution of runs")
plt.xlabel('Runs')
plt.show()
#finding out the no. of wins w.r.t each team after batting first
winsafterbattingfirst=battingfirst['winner'].value_counts()
'''print(winsafterbattingfirst)'''
#making a bar plot for top 3 teams with most wins after batting first
y=winsafterbattingfirst[0:3]
'''print(y)'''
x=y.keys()
'''plt.bar(x,y,color=['blue','yellow','red'])
plt.show()'''
#making a pie chart for top 3 teams with most wins after batting first(in pie chart first value=numerical,second val=categorical)
'''plt.pie(y,labels=x,autopct='%0.1f%%')
plt.show()'''
#making a pie chart for all teams with most wins after batting first(in pie chart first value=numerical,second val=categorical)
'''y1=winsafterbattingfirst
x1=y1.keys()
plt.pie(y1,labels=x1,autopct='%0.1f%%')
plt.show()'''
#extracting the records where the team won batting second
battingsecond=ipl[ipl['win_by_wickets']!=0]
'''print(battingsecond)'''
battingsecondhead=battingsecond.head()
'''print(battingsecondhead)'''
#making a histogram for frequency of wins w.r.t number of wickets
'''plt.hist(battingsecond['win_by_wickets'],bins=30)
plt.show()'''
#finding out the frequency of number of wins w.r.t each team after batting second
winsafterbattingsecond=battingsecond['winner'].value_counts()
'''print(winsafterbattingsecond)'''
#making a bar plot for top 3 teams with most wins after batting second
y2=winsafterbattingsecond[0:3]
x2=y2.keys()
'''plt.bar(x2,y2,color=['purple','blue','red'])
plt.show()'''
#making a pie chart for all teams with most wins after batting second
'''plt.pie(winsafterbattingsecond,labels=winsafterbattingsecond.keys())
plt.show()'''
#looking at the number of matches played each season
season=ipl['season'].value_counts()
'''print(season)'''
#looking at the number of matches played each season
city=ipl['city'].value_counts()
'''print(city)'''
#finding out how many times a team has won the match aftr winning the toss
import numpy as np
z=np.sum(ipl['toss_winner']==ipl['winner'])
print(z)
#deliveries dataset
deliveries=pd.read_csv("deliveries.csv")
delhead=deliveries.head()
'''print(delhead)'''
noofmatches=deliveries['match_id'].unique()
'''print(noofmatches)'''
#extracting records where match id=1
match1=deliveries[deliveries['match_id']==1]
mat1head=match1.head()
'''print(mat1head)
print(mat1head.shape)'''
srh=match1[match1['inning']==1]
'''print(srh)'''
srhbat=srh['batsman_runs'].value_counts()
'''print(srhbat)'''
srhdismissal=srh['dismissal_kind'].value_counts()
'''print(srhdismissal)'''
rcb=match1[match1['inning']==2]
rcbbat=rcb['batsman_runs'].value_counts()
'''print(rcbbat)'''
rcbdismissal=rcb['dismissal_kind'].value_counts()
'''print(rcbdismissal)'''





