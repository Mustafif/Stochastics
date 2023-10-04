import pandas as pd
from scipy.stats import poisson
import numpy as np

# A class to represent each of the Poisson Data in the files 
class PoissonData:
    def __init__(self, filename):
        self.data = pd.read_excel(filename,usecols=[1])
        self.arrivals = self.data
        self.lambda_hat = self.arrivals.mean().values[0]
        self.mu = 30
    # Q5 ii) 
    def no_arrivals_5_hours_prob(self):
        lambda_5_hours = self.lambda_hat * 5 / 24
        return poisson.pmf(0, lambda_5_hours)
    # Q5 iii)
    def at_least_one_arrival_prob(self):
        return 1 - poisson.pmf(0, self.lambda_hat)
    # Q5 iv) 
    def mean_arrivals(self):
        return self.lambda_hat
    # Q5 iv)
    def variance_arrivals(self):
        return self.lambda_hat
    # Q5 v)
    def average_total_time(self):
        return self.arrivals.mean() * self.mu
    # Q5 v)
    def std_dev_total_time(self):
        return np.sqrt(self.arrivals.var()) * self.mu
    
    def to_string(self): 
        return f"""
File: {filename}
Estimated λ: {pdata.lambda_hat}
Probability no arrivals in 5 hours: {pdata.no_arrivals_5_hours_prob()}
Probability at least one arrival in a day: {pdata.at_least_one_arrival_prob()}
Mean arrivals per day: {pdata.mean_arrivals()}
Variance of arrivals per day: {pdata.variance_arrivals()}
Average total time patients assisted per day: {pdata.average_total_time().values[0]} minutes
Standard deviation of total time patients assisted per day: {pdata.std_dev_total_time().values[0]} minutes
"""

# will store all the results 
result_file = open('results.txt', 'a')
# Usage:
# Each poisson data will be read from the directory `poissn`
# and get the data from the `poissn.xlsx` file 
for i in range(10):
    result_file.write('---------------------------')
    filename = f'poissn/poissn{i}.xlsx'
    pdata = PoissonData(filename)
    string = pdata.to_string()
    result_file.write(string)
    result_file.write('---------------------------')


result_file.close()