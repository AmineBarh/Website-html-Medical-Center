import pandas as pd

# Your dataset
data = """Name,Age,Salary,Education
John,28,50000,Bachelor's
Alice,25,60000,Master's
Bob,35,NaN,High School
Eva,40,55000,NaN
Chris,32,48000,Bachelor's
Sophia,27,NaN,Ph.D.
Mike,45,-60000,High School
Emily,33,42000,Master's
David,29,55000,Ph.D.
Linda,38,NaN,Bachelor's
Alex,42,48000,NaN
Sarah,25,52000,High School
Jake,30,-45000,Master's
Olivia,35,49000,Bachelor's
Daniel,41,NaN,Ph.D.
Grace,36,51000,High School
Brandon,31,46000,Bachelor's
Emma,29,-48000,Master's
"""

# Create a DataFrame from the CSV-style data
df = pd.read_csv(pd.compat.StringIO(data))

# Handling missing values
df['Salary'].fillna(df['Salary'].median(), inplace=True)
df['Education'].fillna(df['Education'].mode()[0], inplace=True)

# Dealing with negative salary
df.loc[df['Salary'] < 0, 'Salary'] = df['Salary'].median()

# Removing duplicates
df.drop_duplicates(inplace=True)

# Display the cleaned data
print(df)
