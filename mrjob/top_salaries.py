import csv
from mrjob.job import MRJob
from mrjob.step import MRStep


cols = 'Name,JobTitle,AgencyID,Agency,HireDate,AnnualSalary,GrossPay'.split(',')

class salarymax(MRJob):
    def mapper(self, _, line):
        # Convert each line into a dictionary
        row = dict(zip(cols, [ a.strip() for a in next(csv.reader([line]))]))
        # Yield the salary
        yield 'salary', float(row['AnnualSalary'][1:])

        # Yield the gross pay
        try:
            yield 'gross', float(row['GrossPay'][1:])
        except ValueError:
            self.increment_counter('warn', 'missing gross', 1)

    def reducer(self, key, values):
        topten = []

        for value in values:
            topten.extend([value])
            topten.sort(reverse=True)
            topten = topten[:10]

        for top in topten:
            yield key, top

    combiner = reducer

if __name__ == '__main__':
    salarymax.run()

# python3 ./mrjob/top_salaries.py ./resources/salaries.csv > t.log