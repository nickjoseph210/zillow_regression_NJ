import pandas as pd

# Exported MySQL db to csv, and usin Pandas to read the whole thing

df = pd.read_csv("properties_2017_view.csv")

# The above came up with 59 columns.  No thanks.  Find the ones I want to use:

explore_df = pd.read_csv("properties_2017_view.csv", usecols=["bathroomcnt", "bedroomcnt", "calculatedfinishedsquarefeet", "fips", "taxvaluedollarcnt", "taxamount"])
explore_df.head()

# Got it down to 6 columns, choosing: 
# bathroomcnt
# bedroomcnt
# calculatedfinishedsquarefeet
# fips
# taxvaluedollarcnt
# taxamount