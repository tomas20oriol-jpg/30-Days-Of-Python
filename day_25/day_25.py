# Exercises Day 25
import pandas as pd

# 1. Read the hacker_news.csv from data directory
data = pd.read_csv('./data/hacker_news.csv')

# 2. Get the first five rows
print(data.head(5))

# 3. Get the last five rows
print(data.tail(5))

# 4. Get the title column as pandas series
titles = data['title']

# 5. Count the number of rows and columns
df = pd.DataFrame(data)
# Filter the titles which contain python
# Rows and columns
df.shape            # (n_rows, n_columns)
n_rows, n_cols = df.shape

# Titles containing "python" (case-insensitive)
python_titles = df[df["title"].str.contains("python", case=False, na=False)]

# Titles containing "JavaScript"
js_titles = df[df["title"].str.contains("javascript", case=False, na=False)]

df.head()               # first rows, see what a record looks like
df.shape                # size
df.info()               # columns, dtypes, non-null counts
df.describe()           # stats for numeric columns
df.describe(include="object")   # unique/top for text columns
df.isna().sum()         # missing values per column
df.duplicated().sum()   # duplicate rows
df["author"].value_counts()   # distribution of a categorical column