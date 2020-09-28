#Q1)Blood glucose levels for obese patients have a mean of 100 with a standard deviation of15. A researcher thinks that a diet high in raw cornstarch will have a positive effect onblood glucose levels. A sample of 36 patients who have tried the raw cornstarch diethave a mean glucose level of 108. Test the hypothesis

import math
Sample_count = 36
Sample_Mean = 108
Population_Mean = 100
Population_sigma = 15 #(Standard deviation)
# The population mean is 100 so we have define our hypotheses based on that.
#Null Hypothesis is H0:Mean=100
#Alternative Hypothesis is H1:≠100
#There is no information provided about the significance level or confidence interval, so lets assume it to be 0.05 or 95%
#which is commonly used.
#Lets calculate Z score
z=(Sample_Mean - Population_Mean)/(Population_sigma/math.sqrt(Sample_count))
print('The z score is' ,z)
print('By looking this value up in z table, we get a value of 0.9993')
print('Which implies the probability of having value less than 108 is 99.93% and more than or equals to 108 is 0.007')
print('It is less than 0.05 so we will reject the Null hypothesis i.e. there is raw cornstarch effect')


#The z score is 3.2
#By looking this value up in z table, we get a value of 0.9993
#Which implies the probability of having value less than 108 is 99.93% and more than or equals to 108 is 0.007
#It is less than 0.05 so we will reject the Null hypothesis i.e. there is raw cornstarch effect

#Q2)In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample of 100 voters are surveyed from each state.
#What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?

#let :-
#P1 = Proportion of Republican voters in the first state
#P2 = Proportion of Republican voters in the second state
#P_1 = Proportion of Republican voters in the sample from the first state
#P_2 = Proportion of Republican voters in the sample from the second state.
#N1 = The number of voters sampled from the first state
N1 = 100
#N2=The number of voters sampled from the second state
N2 = 100
P1 = 0.52
#Q1=(1 - P1), the proportion on non republican voters in first state
Q1 = 0.48
P2 = 0.47
#Q2=(1 - P2), the proportion on non republican voters in second state
Q2 = 0.53
#The mean of the difference in sample proportions or the expected value E[P_1-P_2]
mu =P1 - P2
#The standard deviation of the difference (Std)
std = math.sqrt(((P1 * Q1 ) / N1) + ((P2 * Q2) /N2))
print("Mu : ",mu,"Std : ",std)
#This problem requires us to find the probability that P_1 is less than P_2
#This is equivalent to finding the probability that P_1 - P_2 < 0
x = 0
#To find this probability, we need to transform the random variable (P_1 - P_2) into a z-score.
#Z= Z_score(P_1,P_2)
#That transformation appears below.
Z = (x - mu)/std
print("Z_score(P_1,P_2):",Z)
#From Z table we find that the probability of a z-score being -0.7082 or less is 0.24.
print('The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is 0.24.')

#Mu : 0.050000000000000044 Std : 0.07061869440877536
#Z_score(P_1,P_2): -0.7080278164104213
#The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is 0.24.

#Q3)You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. How well did you score on the test compared to the average test taker?

#The z score tells you how many standard deviations from the mean your score is
#My score =x
x = 1100
#Population Mean =mu
mu = 1026
#population standard deviation =sd
sd = 209
z = ( x - mu)/sd
print("Z Score : ",z)
print('The above calculation shows that my score is 0.35 standard deviations above the mean')

#Z Score : 0.35406698564593303
#The above calculation shows that my score is 0.35 standard deviations above the mean















