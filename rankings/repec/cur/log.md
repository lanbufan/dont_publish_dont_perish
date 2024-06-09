
## COLLECTED DATA (20240608)

# 2005 March

https://ideas.repec.org/top/old/0503/top.inst.all.html

Top 5% Economic Institutions, as of March 2005
Average Rank Score
The average rank score is determined by taking a harmonic mean of the ranks in each method, except the first one (number of works). Click on the column heads to find definitions and rankings for each method.
This ranking is based on 2143 institutions with 6698 registered authors.

# May 2024

## Institutions

https://ideas.repec.org/top/top.inst.all.html

## Departments

https://ideas.repec.org/top/top.econdept.html

Top 12.5% Economics Departments, as of May 2024

The rankings
Top 12.5% Economics Departments, all authors, all publication years

# HYPOTHESIS

## association between high status PhD and publication

rank=50
Near Significance: The p-value of 0.056 suggests that there is a near-significant association between attending a high-status school and having publications at graduation. While it doesn't meet the conventional threshold of 0.05, it indicates a trend that might be worth further investigation.
Observed vs Expected: The observed frequencies for high-status schools (e.g., 45 economists with 0 publications, 16 with 1 publication) are somewhat different from the expected frequencies (e.g., 41.63 with 0 publications, 15.61 with 1 publication).

rank=30
Interpretation
Chi-Square Value: The chi-square value of 12.994 indicates a noticeable difference between the observed and expected frequencies.
P-value: The p-value of 0.023 is less than the conventional threshold of 0.05, indicating that the results are statistically significant. This suggests there is a significant association between the status of the PhD school and the likelihood of having publications at graduation.
Degrees of Freedom: This is the number of independent values or quantities which can be assigned to a statistical distribution, which in this case is 5.
Expected Frequencies: These are the frequencies we would expect if there were no association between school status and publication count.
Conclusion
Statistical Significance: The p-value of 0.023 indicates that there is a statistically significant difference in publication counts between economists from high-status and lower-status schools.
Publication Likelihood: The contingency table shows that a larger proportion of economists from high-status schools (43 out of 57) have zero publications by graduation compared to those from lower-status schools (37 out of 66). This suggests that economists from high-status schools are less likely to have publications by the time they graduate compared to those from lower-status schools.
Hypothesis Confirmation
The hypothesis that economists trained in high-status schools are more likely to have at least one publication by graduation year is not supported by the data. Instead, the data suggests that economists from high-status PhD programs are less likely to have publications by the time they graduate.

## association between high status PhD and more than 1 pub

Two-Proportion Z-Test:

Z-statistic: -1.8348539884128174
P-value: 0.06652732670098302
Interpretation:
Z-Statistic:

The Z-statistic is approximately -1.835. This negative value indicates that the proportion of economists with more than one publication in the high-status group is lower than that in the low-status group.
P-Value:

The P-value is approximately 0.067. This value is higher than the conventional significance level of 0.05 but less than 0.10.
A P-value of 0.067 means there is a 6.7% probability that the observed difference in proportions is due to random chance alone.
Significance:

At a significance level of 0.05, the result is not statistically significant because the P-value (0.067) is greater than 0.05.
However, if we consider a significance level of 0.10, the result is marginally significant, suggesting that there might be a weak evidence of difference.

##logistic 1: only high-status 50

Interpretation
Intercept (const):

The intercept of -0.1823 is not significantly different from zero (p-value = 0.426). This term represents the log-odds of having 0 publications for an economist from a low-status school.
High_Status_School:

The coefficient for High_Status_School is 0.7701, which is significantly different from zero (p-value = 0.023). This positive coefficient indicates that attending a high-status school increases the log-odds of having 0 publications by PhD graduation year.
In terms of odds ratio, exp(0.7701) ≈ 2.16, suggesting that economists from high-status schools are about 2.16 times more likely to have 0 publications by graduation compared to those from low-status schools.
Model Significance:

The likelihood ratio test p-value (0.02156) indicates that the model with High_Status_School as a predictor is significantly better than the null model with only an intercept. This suggests that the status of the PhD-granting institution is a significant predictor of having 0 publications by graduation.
Pseudo R-squared:

The pseudo R-squared value of 0.02606 is relatively low, which is typical for logistic regression models. It indicates that the model explains a small portion of the variance in the dependent variable.
Conclusion
The results suggest that economists who graduated from high-status schools are significantly more likely to have 0 publications by the time they graduate compared to those from low-status schools. This finding is statistically significant at the 5% level.
