# Trade Policy Impact Analysis Using Difference-in-Differences

## Project Overview

This project conducts a Difference-in-Differences (DiD) analysis to evaluate the causal impact of a trade policy intervention on export values. The study compares treated industries (those affected by tariff reductions) with control industries (unaffected) across pre- and post-policy periods to isolate the treatment effect.

## Key Findings

The analysis reveals several important insights:

- **No statistically significant policy impact** was detected on export values by the 5th April Tariff announcement(exactly on 5th April), we see huges changes on implication of tariffs, slightly delayed
- The treatment effect coefficient was estimated at -23.23 million, suggesting a potential negative impact
- However, this effect is not statistically significant (p-value = 0.697), possibly due to the need and lack thereof a larger sample size(dataset)
- The 95% confidence interval ranges from -144 million to 97.3 million, which includes zero
- This indicates that we cannot reject the null hypothesis of no policy effect

## Methodology

### Research Design
- **Treatment Group**: Industries directly affected by the tariff reduction policy
- **Control Group**: Industries not subject to the policy changes
- **Time Periods**: Clear separation between pre-implementation and post-implementation periods
- **Data Structure**: Balanced panel data with consistent observations across groups and time

### Statistical Model
The core DiD model specification follows standard econometric practice:
- Dependent variable: Export values
- Key independent variables: Treatment indicator, time period indicator, and their interaction
- The interaction term represents the DiD estimator of policy impact

## Results Interpretation

### Treatment Effect Analysis
- The negative coefficient (-23.23 million) suggests the policy may have reduced exports
- However, the high p-value (0.697) indicates this effect is not statistically distinguishable from zero
- The confidence interval crossing zero confirms the lack of statistical significance

### Pre-existing Differences
- Treatment and control groups showed significant baseline differences (-77.38 million)
- This highlights the importance of the DiD design in controlling for pre-existing disparities
- The parallel trends assumption appears reasonable given the model structure

### Time Trends
- A positive time trend was observed (+41.58 million) for both groups
- This trend was not statistically significant (p = 0.324)
- The trend suggests general economic growth affecting all industries

## Model Performance

### Goodness of Fit
- The model explains 38.1% of variation in export values (R-squared = 0.381)
- Overall model significance is confirmed (F-statistic p = 0.0014)

### Diagnostic Checks
- Residual analysis reveals potential autocorrelation issues
- Non-normal residuals suggest possible model misspecification
- These diagnostics indicate areas for methodological improvement

## Technical Implementation

### Data Processing
- Comprehensive data cleaning and validation procedures
- Proper variable transformation and encoding
- Robust handling of missing values and outliers



## Files Included
- Complete Python analysis script with detailed comments
- Dataset used for the analysis
- Visualization code for parallel trends plots


## Future Work
- Extend analysis with additional control variables
- Implement robust standard errors to address autocorrelation
- Conduct placebo tests to validate DiD assumptions
- Explore alternative model specifications
- Expand dataset for increased statistical power


## Requirements
- Python 3.8+
- Pandas, NumPy, Statsmodels, Matplotlib
- Jupyter Notebook environment recommended
