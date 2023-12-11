import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    input_filename = "cluster_input.csv"
    output_filename = "cluster_output.csv"

    v = []
    
    # Read data from the CSV file
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines[1:]:  # Skip the header line
            _, x, y = line.strip().split(',')
            v.append((int(x), int(y)))

    n = len(v)
    
    # Calculate the coordinates of the midpoint (average)
    mid_x = sum(x for x, y in v) / n
    mid_y = sum(y for x, y in v) / n
    print(f"Midpoint of the data: ({mid_x},{mid_y})")

    # Write the header for the output CSV file
    with open(output_filename, 'w') as outfile:
        outfile.write(" , p1 ,p2 ,p3 ,p4,C\n")

        # Calculate the distances between all pairs of points
        for i in range(n):
            outfile.write(f"p{i + 1},")
            for j in range(i + 1):
                f_x1, s_y1 = v[i]
                f_x2, s_y2 = v[j]

                if f_x1 == f_x2 and s_y1 == s_y2:
                    outfile.write("0,")
                    break

                dis = distance(f_x1, s_y1, f_x2, s_y2)
                outfile.write(f"{dis},")

            outfile.write("\n")

        outfile.write("C,")

        # Variables for finding the nearest point to the center
        nearest_point = 0
        nearest_distance = float('inf')
        x_new, y_new = 0, 0

        # Calculate the distances of each point from the calculated midpoint
        for i in range(n):
            first, second = v[i]
            d = distance(mid_x, mid_y, first, second)
            print(f"Distance of p{i + 1} from the center: {d} units.")

            if nearest_distance > d:
                nearest_distance = d
                nearest_point = i + 1
                x_new, y_new = first, second

            outfile.write(f"{d},")
            if i == n - 1:
                outfile.write("0,")

        print(f"The nearest distance from the center is: {nearest_distance} units.")
        print(f"The nearest point from the center is: p{nearest_point}")
        outfile.write(",\n")

        # New Center Calculation
        outfile.write(" , p1 ,p2 ,p3 ,p4\n")

        for i in range(n):
            outfile.write(f"p{i + 1},")
            for j in range(i + 1):
                f_x1, s_y1 = v[i]
                f_x2, s_y2 = v[j]

                if f_x1 == f_x2 and s_y1 == s_y2:
                    outfile.write("0,")
                    break

                dis = distance(f_x1, s_y1, f_x2, s_y2)
                outfile.write(f"{dis},")

            outfile.write("\n")

        outfile.write(f"p{nearest_point} (New Center),")

        # Calculate the distances of each point from the new center
        for i in range(n):
            first, second = v[i]
            d = distance(x_new, y_new, first, second)
            print(f"Distance of p{i + 1} from the new center (p{nearest_point}): {d} units.")
            outfile.write(f"{d},")

            if i == n - 1:
                outfile.write("0,")

    print(f"Results have been written to '{output_filename}'.")

if __name__ == "__main__":
    main()
