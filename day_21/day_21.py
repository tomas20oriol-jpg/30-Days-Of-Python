# Exercises: Level 1
# Python has the module called statistics and we can use this module to do 
# all the statistical calculations. However, to learn how to make function 
# and reuse function let us try to develop a program, which calculates the 
# measure of central tendency of a sample (mean, median, mode) and measure 
# of variability (range, variance, standard deviation). In addition to 
# those measures, find the min, max, count, percentile, and frequency 
# distribution of the sample. You can create a class called Statistics and 
# create all the functions that do statistical calculations as methods for 
# the Statistics class. Check the output below.
from collections import Counter
class stats:
    def __init__(self, data):
        if not data:
            raise ValueError("There is no data in the list, it cannot be empty.")
        self.data = sorted(data)
        self.n = len(data)

    def count(self):
        """Calculate the number of values we have"""
        return self.n

    def sum(self):
        """Calculates the sum of all the values we have"""
        total = 0
        for x in self.data:
            total += x
        return total

    def min(self):
        """Calculates the minimum of the values we have"""
        return self.data[0]

    def max(self):
        """Calculates the maximum of the values we have"""
        return self.data[-1]

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.n

    def median(self):
        median_index = self.n // 2
        if self.n % 2 == 0:
            #Even number length goes like this
            return (self.data[median_index - 1] + self.data[median_index]) / 2
        else:
            return self.data[median_index]

    def mode(self):
        frequencies = {}
        for value in self.data:
            frequencies[value] = frequencies.get(value, 0) + 1

        max_freq = max(frequencies.values())

        modes = [k for k, v in frequencies.items() if v == max_freq]

        if len(modes) == len(frequencies):
            return 'There is no mode'
        else:
            return modes[0]

    def std(self):
        sum_of_diff = 0
        for x in self.data:
            sum_of_diff += (x - self.mean())**2

        return_value = (sum_of_diff / self.n)**0.5
        return f'{return_value :.2g}'

    def var(self):
        sum_of_diff = 0
        for x in self.data:
            sum_of_diff += (x - self.mean())**2

        return_value = (sum_of_diff / self.n)
        return f'{return_value :.3g}'

    def freq_dist(self):
        return Counter(self.data)

    def describe(self):
        return (f'Count: {self.count()} \n'
                    f'Sum: {self.sum()} \n'
                    f'Min: {self.min()} \n'
                    f'Max: {self.max()} \n'
                    f'Range: {self.range()} \n'
                    f'Mean: {self.mean()} \n'
                    f'Median: {self.median()} \n'
                    f'Mode: {self.mode()} \n'
                    f'Variance: {self.var()} \n'
                    f'Standard Deviation: {self.std()} \n'
                    f'Frequency Distribution: {self.freq_dist()}')
    

    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26] 
data = stats(ages)

print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Standard Deviation:', data.std())
print('Variance:', data.var())
print('Frequency Distribution:', data.freq_dist())
print(data.describe())


# Exercises: Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes,
# expenses properties and it has total_income, total_expense, account_info,
# add_income, add_expense and account_balance methods. Incomes is a set of
# incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (f'Account of {self.firstname} {self.lastname}\n'
                f'Total income: {self.total_income()}\n'
                f'Total expense: {self.total_expense()}\n'
                f'Balance: {self.account_balance()}')


account = PersonAccount('Asabeneh', 'Yetayeh')
account.add_income('Salary', 5000)
account.add_income('Freelance', 200)
account.add_expense('Rent', 1500)
account.add_expense('Food', 300)
print(account.account_info())
