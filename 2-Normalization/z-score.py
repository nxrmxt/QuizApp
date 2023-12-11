def z_score(data):
  data_mean = sum(data)/len(data)
  squared_diff_sum = 0
  for x in data:
    squared_diff_sum += (x - data_mean)**2

  variance = squared_diff_sum/len(data)
  data_std = variance**0.5

  normalized_data = []
  for x in data:
    normalized_value = (x-data_mean)/data_std
    normalized_data.append(normalized_value)

  return normalized_data

input_list = [2, 5, 7, 10, 3.0] 
normalized_data = z_score(input_list)
print(input_list)
print(normalized_data)
