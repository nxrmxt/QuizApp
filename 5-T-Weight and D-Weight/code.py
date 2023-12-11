import csv

def calculate_weights(filename):
  """
  Reads data from a CSV file and calculates T-Weight and D-Weight for each cell.

  Args:
    filename: The filename of the CSV file.

  Returns:
    A dictionary mapping (row, column) tuples to dictionaries containing:
      * count: The total count for the cell.
      * t_weight: The T-Weight of the cell.
      * d_weight: The D-Weight of the cell.
  """

  cell_data = {}
  column_total = {}
  row_total = {}

  with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line

    for row in reader:
      row_name, col_name, count = row
      count = int(count)

      cell_data[(row_name, col_name)] = {
          "count": count,
          "t_weight": 0,
          "d_weight": 0,
      }
      column_total[col_name] = column_total.get(col_name, 0) + count
      row_total[row_name] = row_total.get(row_name, 0) + count

  for (row_name, col_name), cell in cell_data.items():
    cell["t_weight"] = cell["count"] / row_total[row_name] * 100
    cell["d_weight"] = cell["count"] / column_total[col_name] * 100

  return cell_data


if __name__ == "__main__":
  input_filename = "5-T-Weight and D-Weight\input.csv"

  cell_data = calculate_weights(input_filename)

  # Access individual cell data
  # print(cell_data[("row1", "col1")])

  # Loop through all cells
  for (row_name, col_name), cell in cell_data.items():
    print(f"Cell ({row_name}, {col_name}): Count: {cell['count']}, T-Weight: {cell['t_weight']:.2f}%, D-Weight: {cell['d_weight']:.2f}%")
