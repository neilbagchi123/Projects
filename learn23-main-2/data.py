#
# Data - work with spreadsheets
#

# install:
#  pandas
#  openpyxl

import pandas as pd

data = pd.read_excel('doctor schedule-southwest.xlsx')

rows = data[(data.Service=='On Call') & (data.Doctor=='Deshpande')]
print(rows)


