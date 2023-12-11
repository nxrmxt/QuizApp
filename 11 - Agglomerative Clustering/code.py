import csv
from typing import Dict

op = 1

fwtr = open("linkage_output.csv", "w")

# Function to perform agglomerative clustering and return the name of the resulting cluster
def agglomerative(input_file: str) -> str:
    dm: Dict[str, Dict[str, int]] = {}

    with open(input_file, "r") as file:
        reader = csv.reader(file)
        points = next(reader)[1:]

        for line in reader:
            point = line[0]
            dist_values = [int(dist) if dist else 0 for dist in line[1:]]
            dm[point] = dict(zip(points, dist_values))

    pt1, pt2 = "", ""
    min_dist = float("inf")

    # Find the two points with the minimum distance
    for p, dist_dict in dm.items():
        for pp, dist in dist_dict.items():
            if p != pp and dist < min_dist:
                pt1, pt2 = p, pp
                min_dist = dist

    print(f"Clusters Chosen: {pt1} & {pt2}")

    up, down = sorted([pt1, pt2])

    new_pt = down + up

    # Create 'new_pt' in dm if it's not present
    dm[new_pt] = {}

    for point, dist_dict in dm.items():
        if point > new_pt:
            dm[point][new_pt] = min(dm[point][up], dm[point][down])

    for point, d1 in dm[down].items():
        if point < up:
            d1 = min(d1, dm[up][point])
        else:
            d1 = min(d1, dm[point][up])

        dm[new_pt][point] = d1

    for point, dist_dict in dm.items():
        if point >= up:
            d1 = dm[point][up]

            if down > point:
                d1 = min(d1, dm[down][point])
            else:
                d1 = min(d1, dm[point][down])

            dm[point][new_pt] = d1
            dm[point].pop(up, None)

            if point >= down:
                dm[point].pop(down, None)

    dm.pop(up, None)
    dm.pop(down, None)

    # Create an output file with updated cluster data
    output = f"output{op}.csv"
    with open(output, "w", newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow([""] + list(dm.keys()))
        for point, dist_dict in dm.items():
            writer.writerow([point] + list(dist_dict.values()))

    fwtr.write(f"{down} & {up}\n")
    return output

def main():
    input_file = "linkage_input.csv"

    with open(input_file, "r") as file1:
        reader1 = csv.reader(file1)
        next(reader1)
        points = next(reader1)[1:]
        len_points = len(points)

        for _ in range(1, len_points - 1):
            output_file = agglomerative(input_file)
            input_file = output_file

if __name__ == "__main__":
    main()
