# redash_python_df

When you want to juggle (join, etc.) the query results of Redash, SQL is always cumbersome due to its redandancy.
Although we can use python in Redash by the python data source, it seems no build-in function to smoothly convert redash to python data frame and vice versa.

I made a template based on @arikfr's PR idea here. 
https://discuss.redash.io/t/converting-redash-query-results-to-pandas-dataframe-and-vice-versa/3015

# side note
You need to add at least `pandas` and `datetime` as "Modules to import prior to running the script" on data source setting.
<img width="522" alt="image" src="https://user-images.githubusercontent.com/13245856/111248006-65e3da80-864c-11eb-85a4-53f0a5937aa5.png">

