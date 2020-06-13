# Hypothesis Testing with SciPy

In this project, various SciPy statistical tests were carried out  to determine whether or not samples were
 significantly different form the mean population or from each other. The p-value is the percentage likelihood that
  the difference is due to random chance. A p-value of less than 0.05 is generally considered proof of statistical
   difference, therefore the p-value was used each time to make claims. 

The key concepts explored in this project include:
- P-values
- 1 Sample T-Test
- 2 Sample T-Test
- ANOVA (Analysis of Variance)
- Tukey’s Range Test
- Binomial Test
- Chi Square test
- NumPy basics

This project uses hypothetical data provided by Codecademy developers. The first set of data (familiar.py) is from
 Familiar, a startup in the new market of blood transfusion. The aim is to statistically understand the impact of the
  company's product packages on their subscriber's life expectancy and iron levels. 
  
The second set of data (fetchmaker.py) is from FetchMaker, a tech startup that matches up prospective dog
owners with their perfect pet. It consists of data on thousands of adoptable dogs. 
The attributes that FetchMaker keeps track of are:
- `weight`, an integer representing how heavy a dog is in pounds
- `tail_length`, a float representing tail length in inches
- `age`, in years
- `color`, a String such as "brown" or "grey"
- `is_rescue`, a boolean 0 or 1

Several types of statistical analysis tests were used to compare various attributes of several dog breeds. 