import pandas as pd

# 读取三个CSV文件
testing_df = pd.read_csv('testing.csv')
training_df = pd.read_csv('training.csv')
val_df = pd.read_csv('val.csv')

# 在这里可以进行数据处理、清洗等操作

# 合并数据框
merged_df = pd.concat([testing_df, training_df, val_df], ignore_index=True)

# 将合并后的数据框保存为新的CSV文件
merged_df.to_csv('merged_data.csv', index=False)