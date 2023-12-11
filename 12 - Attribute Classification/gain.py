import math
import csv

# Global variables to store data and results
sub_classes = []
main_class = {}
dist_val = {
    "day": set(),
    "outlook": set(),
    "temp": set(),
    "humidity": set(),
    "wind": set(),
}
dist_val_count = {}
val_count = {}

# Variable to keep track of maximum gain and selected root
max_gain = float('-inf')
root = "null"

# Output file stream
with open("gain_output.csv", "w", newline="") as fw:
    writer = csv.writer(fw)

    # Function to calculate the information gain and select the root
    def calculate_gain(sub_class, main_c_gain):
        tot_r = main_class["Yes"] + main_class["No"]
        ent = 0

        for dv in dist_val[sub_class]:
            t_r = dist_val_count[dv]
            p_r, n_r = val_count[dv].get("Yes", 0), val_count[dv].get("No", 0)

            if p_r != 0:
                ent += -(t_r / tot_r) * ((p_r / t_r) * math.log2(p_r / t_r))

            if n_r != 0:
                ent += -(t_r / tot_r) * ((n_r / t_r) * math.log2(n_r / t_r))

        # Calculate information gain
        gain = main_c_gain - ent

        # Output results
        print(f"Information Gain ( {sub_class} | playGame ) : {gain}")
        writer.writerow([f"Information Gain ( {sub_class} | playGame )", gain])

        global max_gain, root
        if gain > max_gain:
            max_gain = gain
            root = sub_class

    # Open and read the input file
    with open("12 - Attribute Classification\gain_input.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for line in reader:
            day, outlook, temp, humidity, wind, play_game = line

            # Store data for calculations
            dist_val["day"].add(day)
            dist_val["outlook"].add(outlook)
            dist_val["temp"].add(temp)
            dist_val["humidity"].add(humidity)
            dist_val["wind"].add(wind)

            main_class[play_game] = main_class.get(play_game, 0) + 1

            dist_val_count[day] = dist_val_count.get(day, 0) + 1
            dist_val_count[outlook] = dist_val_count.get(outlook, 0) + 1
            dist_val_count[temp] = dist_val_count.get(temp, 0) + 1
            dist_val_count[humidity] = dist_val_count.get(humidity, 0) + 1
            dist_val_count[wind] = dist_val_count.get(wind, 0) + 1

            val_count[day] = val_count.get(day, {})
            val_count[day][play_game] = val_count[day].get(play_game, 0) + 1

            val_count[outlook] = val_count.get(outlook, {})
            val_count[outlook][play_game] = val_count[outlook].get(play_game, 0) + 1

            val_count[temp] = val_count.get(temp, {})
            val_count[temp][play_game] = val_count[temp].get(play_game, 0) + 1

            val_count[humidity] = val_count.get(humidity, {})
            val_count[humidity][play_game] = val_count[humidity].get(play_game, 0) + 1

            val_count[wind] = val_count.get(wind, {})
            val_count[wind][play_game] = val_count[wind].get(play_game, 0) + 1

    # Calculate entropy for the main class
    pos_r = main_class["Yes"]
    neg_r = main_class["No"]
    tot_r = pos_r + neg_r

    main_c_gain = -((pos_r / tot_r) * math.log2(pos_r / tot_r) + (neg_r / tot_r) * math.log2(neg_r / tot_r))

    # Output the main class gain
    print(f"Main Class Information Gain : {main_c_gain}")

    # Calculate and output information gain for each subclass
    for sub_class in sub_classes[1:]:
        calculate_gain(sub_class, main_c_gain)

    # Output the selected root with maximum gain
    print(f"The selected root for splitting is: {root} (Maximum Gain)")
    writer.writerow([f"The selected root for splitting is: {root} (Maximum Gain)"])
