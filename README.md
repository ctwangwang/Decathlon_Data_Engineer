# Decathlon_Data_Engineer

Task 1: Data extraction - Python (Decathlon_task1.ipynb)

For the first task, 
- I used the Decathlon API in https://developers.decathlon.com/sport-places/#code-samples to extract the sport places of every store in the neighbourhood of 2km radius, and save the result to different files in JSON format.

Task 2A: Data processing (Decathlon_task2A.ipynb)

For the second task, 
- I used store_dim.csv to extract the mapping of store and location, and declare a dictionary "store_mapping" to save the mapping
- I used the Decathlon API in https://developers.decathlon.com/products/sports/docs to extract the mapping of sport ID and sport Name, and declare a dictionary "sport_id_name_mapping" to save the mapping
- Declare a Pyspark DataFrame, "df_res" to store the result 
- Load the data from task 1 as Pyspark DataFrame, and calculate features below, and the accessibility may has same amount of times, if the sports have same amount of times, then the sports will be ranked the same rank, for example, if Sport A has 5 times of appearance, and Sport B, Sport C have 3 times of appearance, and Sport D has 1 times of appearance, then the Sport A will be ranked 1st most accessible sport, Sport B and Sport C will be ranked 2nd most accessible sport, and the 3rd most accessible sport will be None.
- Average distance of sport place to store: calculate the average of proximity of the sport places
- Number unique sports accessible per store: calculate the unique number of sport of sport places
- Top1 most accessible sport per store: find the sport which appears the most times
- Top2 most accessible sport per store: find the sport which appears the second most times
- Top3 most accessible sport per store: find the sport which appears the third most times
- Loop over the stores to calculate the features separately and save it to the Pyspark DataFrame, "df_res"


Task 2B: Redshift pipeline - SQL (Decathlon_task2B.sql)

- I created a Redshift cluster, and upload "transaction_detail.csv" to S3 bucket, after setting up the security group, I used SQLWorkbenchJ to connect to the Redshift cluster and do the SQL operations
- From the "transaction_detail.csv", I found that there are sale/return records for each store and sgtin_hash, and the number of sale/return records for each store and sgtin_hash are from 1 to 14 times, and the question is to ask the average days between sale and return of all items per store, so I think it is to calculate the date difference of the earliest day and the latest date, and divide the number of cases, which is the average days per transaction record, and I call it fluidity, as I think if fluidity is bigger, then it means the products of the store make more transactions over a certain of time. And I calculate the average fluidity of each store as result.
