#Q1)

#Chi-Square test of independence
#H0 :Null Hypothesis: The two categorical variables are independent.
#H1:Alternative Hypothesis: The two categorical variables are dependent.
import numpy as np
import pandas as pd
import scipy.stats as stats
male = [40,44,53,57]
female = [60,54,46,41]
High_school=[60,40]
Bachelors = [54,44]
Masters = [46,53]
Phd = [41,57]
marks = male+female
print(marks)
sex=['M','M','M','M','F','F','F','F']
education =['High_school','Bachelors','Masters','Ph.d','High_school','Bachelors','Masters','Ph.d']
DF=pd.DataFrame({"Education":education,"Marks":marks,"Sex":sex})
DF
print(DF)

cross_tab = pd.crosstab([DF.Sex,DF.Marks],DF.Education,margins=True)
cross_tab

DF1 = pd.crosstab(DF.Sex, DF.Education,DF.Marks, aggfunc="sum",margins=True)
DF1

DF1.columns = ["Bachelors","High_School","Masters","Ph.d.","Genderwise_total"]
DF1.index = ["Female","Male","Combined"]
DF1

# Creating a table exlcuding the total for later use
DF2 = DF1.iloc[0:2,0:4]
DF2

# For a test of independence, we use the same chi-squared formula that we usedfor the goodness-of-fit test.
# The main difference is we have to calculate the expected counts of each cellin a 2-dimensional table instead of
# a 1-dimensional table. To get the expected count for a cell, multiply the row total for that cell by the column
# total for that cell and then divide by the total number of observations. Wecan quickly get the expected counts
# for all cells in the table by taking the row totals and column totals of thetable, performing an outer product
# on them with the np.outer() function and dividing by the number of observations:
DF3=np.outer(DF1["Genderwise_total"][0:2],DF1.loc["Combined"][0:4]) / 395.0
DF3 = pd.DataFrame(DF3)
DF3.columns = ["Bachelors","High_School","Masters","Ph.d."]
DF3.index = ["Female","Male"]
DF3

# Now we will calculate the chisquare statistic, critical value and p value.
# We called the .sum() twice, once to get the column sum and second time to add the sum, returning the sum of entire
# 2D table
chi_squared_stat = (((DF3-DF2)**2)/DF3).sum().sum()
print(chi_squared_stat)

#Find the critical value for 95% confidence and degree of freedom (df) is 3
cvalue = stats.chi2.ppf(q = 0.95,df= 3)
print("Critical value")
print(cvalue)

# Find the p-value
p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,df=3)
print("P value")
print(p_value)


# Use stats.chi2_contingency() function to conduct a test of independence automatically given a frequency table
# of observed counts:
result = stats.chi2_contingency(observed= DF2)
print(result)
print('-'*115)
print('The output shows the chi-square statistic = 8, the p-value as 0.045 and the degrees of freedom as 3')
print('The critical value with 3 degree of freedom is 7.815. Since 8.006 > 7.815, therefore we reject the null hypothesis and conclude that the education level depends on gender at a 5% level of significance.')


#The output shows the chi-square statistic = 8, the p-value as 0.045 and the degrees of freedom as 3
#The critical value with 3 degree of freedom is 7.815. Since 8.006 > 7.815, therefore we reject the null hypothesis and conclude that the education level depends on gender at a 5% level of significance.

#Q2)Using the following data, perform a oneway analysis of variance using α=.05. Writeup the results in APA format.
#[Group1: 51, 45, 33, 45, 67]
#[Group2: 23, 43, 23, 43, 45]
#[Group3: 56, 76, 74, 87, 56]


#The analysis of variance or ANOVA is a statistical inference test that lets you compare multiple groups at the same time. The one-way ANOVA tests whether the mean of some numeric variable diff
# variable.It essentially answers the question: do any of the group means differ from one another?
#The scipy library has a function for carrying out one-way ANOVA tests calledscipy.stats.f_oneway()
import scipy.stats as stats
Group1 = [51, 45, 33, 45, 67]
Group2 = [23, 43, 23, 43, 45]
Group3 = [56, 76, 74, 87, 56]
# Perform the ANOVA
statistic, pvalue = stats.f_oneway(Group1,Group2,Group3)
print("F Statistic value {} , p-value {}".format(statistic,pvalue))
if pvalue < 0.05: print('True')
else: 
    print('False')
print("-"*115)
print("The test result suggests the groups have different same sample means in this example, since the p-value is significant at a 99% confidence level. Here the p-value returned is 0.00305 which is < 0.05")

#The test result suggests the groups have different same sample means in this example, since the p-value is significant at a 99% confidence level. Here the p-value returned is 0.00305 which is < 0.05

#Q3)Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25. For 10, 20, 30, 40, 50

stats.f_oneway([10, 20, 30, 40, 50],[5,10,15, 20, 25])
Group1 = [10, 20, 30, 40, 50]
Group2 = [5,10,15, 20, 25]
mean_1 = np.mean(Group1)
mean_2 = np.mean(Group2)
grp1_sub_mean1 = []
grp2_sub_mean2 = []
add1 = 0
add2 = 0
for items in Group1: add1 += (items - mean_1)**2
for items in Group2: add2 += (items - mean_2)**2
var1 = add1/(len(Group1)-1)
var2 = add2/(len(Group2)-1)
F_Test = var1/var2
print("F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25 is : ",F_Test)


