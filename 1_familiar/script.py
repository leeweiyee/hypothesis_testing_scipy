import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# 1) lifespans of Vein Pack subscribers:
vein_pack_lifespans = familiar.lifespans(package='vein')

# 1-Sample T-Test to compare vein_pack_lifespans to the average life expectancy 71
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(format(vein_pack_test.pvalue, '0.10f')) # p-value is less 0.05; can say that there is a significant difference
# between the life expectancy of the package and the life expectancy 71
if vein_pack_test.pvalue < 0.05:
    print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print("The Vein Pack Is Probably Good For You Somehow!")

# 2) lifespans of Artery Pack subscribers:
artery_pack_lifespans = familiar.lifespans(package='artery')

# 2-Sample T-Test to see if there is a significant difference between the two subscriptions
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(format(package_comparison_results.pvalue, '0.10f')) # p-value is greater than 0.05; cannot say that there is a
# significant difference between the life expectancy of the two packages
if package_comparison_results.pvalue < 0.05:
    print("The Artery Package guarantees even stronger results!")
else:
    print("The Artery Package is also a great product!")

# 3) iron level survey data formatted into a contingency table:
iron_contingency_table = familiar.iron_counts_for_package()

# Chi Square Test to see if a higher iron level of Artery Package subscribers is a significant difference from what
# was reported by Vein Package subscribers
chi2, iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
print(format(iron_pvalue, '0.10f')) # p-value is less than 0.05; can say that there is a significant difference
# between the iron level results of the two packages
if iron_pvalue < 0.05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("While We Can’t Say The Artery Package Will Help You, I Bet It’s Nice!")