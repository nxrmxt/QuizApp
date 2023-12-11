def min_max_norm(data):
  data_min = min(data)
  data_max = max(data)

  normalized_data = []

  for x in data:
    normalized_value = (x - data_min)/(data_max-data_min)
    normalized_data.append(normalized_value)

  return normalized_data

data = [1,2,3,4,5,6,7,8,9,10]
print(data)
print(min_max_norm(data))
  
  