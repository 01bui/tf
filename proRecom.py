

data_path = './santander/'

#Once the CSV files are downloaded, let's read them into Pandas dataframes.
import pandas as pd

COLUMNS = ["fecha_dato"]

df_train = pd.read_csv(data_path+"train_ver2.csv", usecols=['ncodpers'])
df_test = pd.read_csv(data_path+"test_ver2.csv", usecols=['ncodpers'])
print("Number of rows in train : ", df_train.shape[0])
print("Number of rows in test : ", df_test.shape[0])
