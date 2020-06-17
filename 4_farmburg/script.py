import pandas as pd
from scipy.stats import chi2_contingency, binom_test

df = pd.read_csv("clicks.csv")

print(df.head()) # returns:
# user_id	                            group	click_day
# 0	8e27bf9a-5b6e-41ed-801a-a59979c0ca98	A	nan
# 1	eb89e6f0-e682-4f79-99b1-161cc1c096f1	A	nan
# 2	7119106a-7a95-417b-8c4c-092c12ee5ef7	A	nan
# 3	e53781ff-ff7a-4fcd-af1a-adba02b2b954	A	nan
# 4	02d48cf1-1ae6-40b3-9d8b-8208884a0904	A	Saturday

# define a column that tells us if each visitor clicked on the Purchase link
df['is_purchase'] = df.click_day.apply(lambda x: "Purchase" if pd.notnull(x) else "No Purchase")

# count the number of users who made a purchase from each group
purchase_counts = df.groupby(['group','is_purchase'])['user_id'].count().reset_index()

print(purchase_counts) # returns:
# group	is_purchase	user_id
# 0	A	No Purchase	1350
# 1	A	Purchase	316
# 2	B	No Purchase	1483
# 3	B	Purchase	183
# 4	C	No Purchase	1583
# 5	C	Purchase	83

# chi-squared test to determine if the differences between Groups A, B, and C are significant
contingency = [[316, 1350],
               [183, 1483],
               [83, 1583]]
_, pvalue, _, _ = chi2_contingency(contingency)
print(pvalue) # returns 2.41262135467e-35; significant

# It is later revealed that the A, B, or C test groups refer to three different price points, $0.99, $1.99,
# and $4.99 respectively, to charge customers for an upgrade package. This indicates that a new statistical test has
# to be carried out to see if each price point can make enough money that can exceed a target goal. A minimum
# of $1000/week needs to be generated to justify this project.

# number of site visitors
num_visits = len(df)
# percent of visitors who need to buy an upgrade package at $0.99 in order to make our target of $1,000
p_clicks_099 = (1000 / 0.99) / num_visits
# percent of visitors who need to buy an upgrade package at $1.99 in order to make our target of $1,000
p_clicks_199 = (1000 / 1.99) / num_visits
# percent of visitors who need to buy an upgrade package at $4.99 in order to make our target of $1,000
p_clicks_499 = (1000 / 4.99) / num_visits

# binomial test on each group to see if the observed purchase rate is significantly greater than what is needed in
# order to generate at least $1,000 per week
pvalueA = binom_test(316, n=(1350+316), p=p_clicks_099)
print(pvalueA) # returns 0.21112872994
pvalueB = binom_test(183, n=(1483+183), p=p_clicks_199)
print(pvalueB) # returns 0.206602092466
pvalueC = binom_test(83, n=(1583+83), p=p_clicks_499)
print(pvalueC) # returns 0.0456236724772

# the final price that should be charged for the upgrade package is 4.99