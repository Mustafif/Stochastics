import pandas as pd
from scipy.stats import poisson
import numpy as np

# A class to represent each of the Poisson Data in the files 
class PoissonData:
    def __init__(self, filename):
        self.arrivals = pd.read_excel(filename,usecols=[1])
        self.lambdaHat = self.arrivals.mean().values[0]
        self.mu = 30
    # Q5 ii) 
    def no_arrivals_5_hours_prob(self):
        lambda_5_hours = self.lambdaHat * (5 / 24)
        return poisson.pmf(0, lambda_5_hours)
    # Q5 iii)
    def at_least_one_arrival_prob(self):
        prob = 1 - poisson.pmf(0, self.lambdaHat)
        return prob
    # Q5 iv) 
    def mean_arrivals(self):
        return self.lambdaHat
    # Q5 iv)
    def variance_arrivals(self):
        return self.lambdaHat
    # Q5 v)
    def average_total_time(self):
        return self.arrivals.mean() * self.mu
    # Q5 v)
    def std_dev_total_time(self):
        return np.sqrt(self.arrivals.var()) * self.mu
    def to_string(self): 
        return f"""
File: {filename}
Estimated lambda: {self.lambdaHat:.4f}
Probability no arrivals in 5 hours: 
{self.no_arrivals_5_hours_prob():.4f}
Probability at least one arrival in a day: 
{self.at_least_one_arrival_prob():.4f}
Mean arrivals per day: {self.mean_arrivals():.4f}
Variance of arrivals per day: {self.variance_arrivals():.4f}
Average total time patients assisted per day: 
{self.average_total_time().values[0]:.4f} minutes
Standard deviation of total time patients assisted per day: 
{self.std_dev_total_time().values[0]:.4f} minutes
"""
# will store all the results 
result_file = open('results.txt', 'a')
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