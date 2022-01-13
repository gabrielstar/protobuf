import csv
import pandas as pd
import random
from shutil import copyfile

file_name = 'football.csv'
file_name_pandas = 'football_pandas.csv'
file_name_org = 'football_org.csv'

# start with a clean file
for _file_name in [file_name_pandas, file_name]:
    copyfile(file_name_org, _file_name)

# with built-in csv lib
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# results generator
def results_generator(results_num: int):
    for _ in range(results_num):
        yield {
            'MatchResult': random.randint(0, 2),
            'Last3MatchesPoints': random.randint(1, 3),
            'TablePosition': random.randint(1, 18),
            'OpponentLast3MatchesPoints': random.randint(0,3),
            'OpponentTablePosition': random.randint(1, 18)
        }


columns = ['MatchResult', 'Last3MatchesPoints', 'TablePosition', 'OpponentLast3MatchesPoints',
           'OpponentTablePosition']
# write to
with open(file_name, 'a', newline='', encoding='utf-8') as file:
    field_names = columns
    results_num = 300
    results = results_generator(results_num)
    writer = csv.DictWriter(file, field_names)
    for _ in range(results_num):
        writer.writerow(next(results))

# pandas
pd.read_csv(file_name_pandas)
# create a data frame [[]]
df = pd.DataFrame([
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2]
], columns=columns)
df.to_csv(file_name_pandas, mode="a", header=False)
print(df.memory_usage())
