# Hypothesis Testing with SciPy

In this project, various SciPy statistical tests were carried out to determine whether or not samples were significantly different from the mean population or from each other. The p-value is the percentage likelihood that the difference is due to random chance. A p-value of less than 0.05 is generally considered proof of statistical difference, therefore the p-value was used each time to make claims. 

The key concepts explored in this project include:
- P-values
- 1 Sample T-Test
- 2 Sample T-Test
- ANOVA (Analysis of Variance)
- Tukey’s Range Test
- Binomial Test
- Chi Square test
- A/B Testing
- NumPy basics
- Pandas basics

This project uses hypothetical data provided by Codecademy developers. 

The first set of data (familiar.py) is from Familiar, a startup in the new market of blood transfusion. The aim is to statistically understand the impact of the company's product packages on their subscriber's life expectancy and iron levels using simple T-Tests. 
  
The second set of data (dog_data.csv) is from FetchMaker, a tech startup that matches up prospective dog owners with their perfect pet. The aim is to use several types of statistical analysis tests, such as Tukey and Chi Square tests, to compare various attributes of several dog breeds. The attributes that FetchMaker keeps track of are:
- `weight`, an integer representing how heavy a dog is in pounds
- `tail_length`, a float representing tail length in inches
- `age`, in years
- `color`, a String such as "brown" or "grey"
- `is_rescue`, a boolean 0 or 1

The third set of data (noshmishmosh.py) is from Nosh Mish Mosh, a recipe and ingredient meal delivery service which is running an A/B test to see if they can convince more people to purchase meal plans with a more artisanal-looking vegetable selection. The aim is to calculate the baseline and minimum detectable effect for an A/B test from a provided dataset, in order to evaluate how many people need to be shown the new assets before checking if the results are a significant improvement. 

The fourth set of data (clicks.csv) is from FarmBurg, a company that makes a farming simulation social network game and is carrying out an A/B test with three different upgrade packages: A, B, and C. The aim is to see which option in the A/B test is the best option to reach their target goal. The CSV file has the following columns:
- `user_id`: a unique id for each visitor to the FarmBurg site
- `ab_test_group`: either A, B, or C depending on which group the visitor was assigned to
- `click_day`: only filled in if the user clicked on a link to purchase