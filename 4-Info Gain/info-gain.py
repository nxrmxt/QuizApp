#Reference -https://gist.github.com/SoumenAtta/a5c803685ef8280497b34dd27cdea3e7

import pandas as pd
import math

target_column_name = 'Routine'
def entropy(data):
  class_counts = data[target_column_name].value_counts()
  entropy_value = 0

  for count in class_counts:
    probability = count / len(data)
    entropy_value -= probability * math.log(probability, 2)

  return entropy_value


def info_gain(data, feature):
  total_entropy = entropy(data)
  unique_values = data[feature].unique()
  weighted_entropy = 0

  for value in unique_values:
    subset = data[data[feature] == value]
    subset_entropy = entropy(subset)
    weighted_entropy += (len(subset) / len(data)) * subset_entropy

  return total_entropy - weighted_entropy


titanic_data = pd.read_csv('info-gain.csv')

for column in titanic_data.columns[:-1]:
  # Exclude the target column ('Survived')
  i_gain = info_gain(titanic_data, column)
  print(f"Information gain for {column}: {i_gain}")
