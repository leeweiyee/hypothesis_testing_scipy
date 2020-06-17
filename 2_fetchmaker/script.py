import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# example: retrieve tail lengths of all of the rottweilers in the system
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(rottweiler_tl)
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

# Q1) It is expected that 8% of dogs in the FetchMaker system are rescues. Are whippets significantly more or less
# likely to be a rescue?
# get rescue data for whippets:
whippet_rescue = fetchmaker.get_is_rescue("whippet")
# get the number of entries in whippet_rescue that are 1:
num_whippet_rescues = np.count_nonzero(whippet_rescue)
# number of samples in the whippet set:
num_whippets = np.size(whippet_rescue)
# binomial test to test the number of whippet rescues:
pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print(format(pval, '0.10f')) # p-value is greater than 0.05; cannot say that there is a significant difference
# between the whippets adoption rate and the mean adoption rate

# Q2) Whippets, terriers, and pitbulls are three of the most popular mid-sized dog breeds. Is there a significant
# difference in the average weights of these three dog breeds?
# get weight data for whippets, terriers and pitbulls:
whippet_weight = fetchmaker.get_weight("whippet")
terrier_weight = fetchmaker.get_weight("terrier")
pitbull_weight = fetchmaker.get_weight("pitbull")
# ANOVA to determine if there is a significant difference:
fstat, pval2 = f_oneway(whippet_weight, terrier_weight, pitbull_weight)
print(format(pval2, '0.10f')) # p-value is less than 0.05; can say that there is a significant difference between the
# weights of these dog breeds
# Tukey’s Range Test to determine which of the pairs of these dog breeds differ from each other:
dog_breeds = np.concatenate([whippet_weight, terrier_weight, pitbull_weight])
labels = ['whippet'] * len(whippet_weight) + ['terrier'] * len(terrier_weight) + ['pitbull'] * len(
    pitbull_weight)
tukey_results = pairwise_tukeyhsd(dog_breeds, labels, 0.05)
print(tukey_results) # returns:
#  Multiple Comparison of Means - Tukey HSD, FWER=0.05
# =====================================================
#  group1  group2 meandiff p-adj   lower  upper  reject
# -----------------------------------------------------
# pitbull terrier   -13.24  0.001 -16.728 -9.752   True
# pitbull whippet    -3.34 0.0639  -6.828  0.148  False
# terrier whippet      9.9  0.001   6.412 13.388   True
# -----------------------------------------------------
# results show that there is no significant difference between the weights of whippets and pitbulls but there are
# significant differences in other combinations

# Q3) Do poodles and shihtzus have significantly different color breakdowns?
# get poodle colors:
poodle_colors = fetchmaker.get_color("poodle")
# get shihtzu colors:
shihtzu_colors = fetchmaker.get_color("shihtzu")
# Chi Square contingency table:
color_table = [[np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")],
               [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")],
               [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")],
               [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")],
               [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]
# Chi Square Test to determine if there is a significant difference:
chi2, color_pvalue, dof, expected = chi2_contingency(color_table)
print(format(color_pvalue, '0.10f')) # p-value is less than 0.05; can say that there is a significant difference
# between poodle colors and shihtzu colors