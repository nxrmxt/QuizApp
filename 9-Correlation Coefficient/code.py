def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            value = line.strip().split(',')[0]
            data.append(int(value))
    return data

def calculate_correlation_coefficient(a, b):
    n = len(a)
    a_plus = sum(1 for item in a if item == 1)
    b_plus = sum(1 for item in b if item == 1)
    ab_plus = sum(1 for ai, bi in zip(a, b) if ai == 1 and bi == 1)

    if a_plus == 0 or b_plus == 0:
        return 0.0  # To handle cases where division by zero may occur

    return ab_plus / (a_plus * b_plus)

def write_correlation_coefficient(filename, corr_coeff):
    with open(filename, 'w') as file:
        file.write(f"Pearson Correlation Coefficient,{corr_coeff}\n")

def main():
    input_filename = "correlation_input.csv"
    output_filename = "correlation_output.csv"

    a = read_data(input_filename)
    b = read_data(input_filename)

    corr_coeff = calculate_correlation_coefficient(a, b)

    write_correlation_coefficient(output_filename, corr_coeff)

    print(f"Correlation coefficient calculated and saved in '{output_filename}'.")

if __name__ == "__main__":
    main()
