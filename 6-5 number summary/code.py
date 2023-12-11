import csv
import statistics

# Function to calculate the first quartile (Q1)
def calculate_quartile1(v):
    n = len(v)
    first = v[:n//2]
    return statistics.median(first)

# Function to calculate the third quartile (Q3)
def calculate_quartile3(v):
    n = len(v)
    last = v[n//2 + n%2:]
    return statistics.median(last)

# Read data from the input file
with open('five_number_input.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row
    arr = [int(row[0]) for row in reader]

arr.sort()

# Write results to the output file and console
with open('five_number_output.csv', 'w') as outfile:
    outfile.write(f"Minimum value:, {arr[0]}\n")
    outfile.write(f"First Quartile (Q1) value:, {calculate_quartile1(arr)}\n")
    outfile.write(f"Median value:, {statistics.median(arr)}\n")
    outfile.write(f"Third Quartile (Q3) value:, {calculate_quartile3(arr)}\n")
    outfile.write(f"Maximum value:, {arr[-1]}\n")

print(f"The minimum value is {arr[0]}")
print(f"The First Quartile (Q1) is {calculate_quartile1(arr)}")
print(f"The median is {statistics.median(arr)}")
print(f"The Third Quartile (Q3) is {calculate_quartile3(arr)}")
print(f"The maximum value is {arr[-1]}")
