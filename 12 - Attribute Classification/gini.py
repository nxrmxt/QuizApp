import math
import csv

# Global variables to store data and results
sub_classes = []                   # Subclasses for analysis
main_class = {}                    # Count of main class values (e.g., "Yes" and "No")
dist_val = {                       # Distinct values for each subclass
    "day": set(),
    "outlook": set(),
    "temp": set(),
    "humidity": set(),
    "wind": set(),
}
dist_val_count = {}                # Count of distinct values
val_count = {}                     # Count of values for each subclass

# Variables to keep track of minimum Gini index and selected root
min_gini = float('inf')
root = "null"

# Output file stream
with open("gini_output.csv", "w", newline="") as fw:
    writer = csv.writer(fw)

    # Function to calculate the Gini index and select the root
    def calculate_gini(sub_class, main_c_gini):
        tot_r = main_class["Yes"] + main_class["No"]  # Total count of main class values

        ent = 0  # Initialize Gini entropy

        # Calculate Gini index for the given subclass
        for dv in dist_val[sub_class]:
            t_r = dist_val_count[dv]  # Total count for the distinct value
            p_r = val_count[sub_class].get("Yes", 0)  # Count of "Yes" in the subclass
            n_r = val_count[sub_class].get("No", 0)   # Count of "No" in the subclass

            ent += (t_r / tot_r) * (1 - (p_r / t_r) ** 2 - (n_r / t_r) ** 2)

        gini = ent  # Final Gini index

        # Output the Gini index for the subclass
        print(f"Gini Index ( {sub_class} | playGame ) : {gini}\n")
        writer.writerow([f"Gini Index ( {sub_class} | playGame )", gini])

        # Check if the current Gini index is the minimum
        global min_gini, root
        if gini < min_gini:
            min_gini = gini
            root = sub_class  # Update the root with the minimum Gini index

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

            main_class[play_game] = main_class.get(play_game, 0) + 1  # Update the count for the main class value

            dist_val_count[day] = dist_val_count.get(day, 0) + 1  # Update the count for the distinct values
            dist_val_count[outlook] = dist_val_count.get(outlook, 0) + 1
            dist_val_count[temp] = dist_val_count.get(temp, 0) + 1
            dist_val_count[humidity] = dist_val_count.get(humidity, 0) + 1
            dist_val_count[wind] = dist_val_count.get(wind, 0) + 1

            val_count[day] = val_count.get(day, {})
            val_count[day][play_game] = val_count[day].get(play_game, 0) + 1  # Update the count for values in the subclasses

            val_count[outlook] = val_count.get(outlook, {})
            val_count[outlook][play_game] = val_count[outlook].get(play_game, 0) + 1

            val_count[temp] = val_count.get(temp, {})
            val_count[temp][play_game] = val_count[temp].get(play_game, 0) + 1

            val_count[humidity] = val_count.get(humidity, {})
            val_count[humidity][play_game] = val_count[humidity].get(play_game, 0) + 1

            val_count[wind] = val_count.get(wind, {})
            val_count[wind][play_game] = val_count[wind].get(play_game, 0) + 1

    # Calculate Gini index for the main class
    pos_r = main_class["Yes"]
    neg_r = main_class["No"]
    tot_r = pos_r + neg_r

    main_c_gini = 1 - ((pos_r / tot_r) ** 2 + (neg_r / tot_r) ** 2)

    # Output the Gini index for the main class
    print(f"Main Class Gini Index : {main_c_gini}\n")

    # Calculate and output the Gini index for each subclass
    for sub_class in sub_classes[1:]:
        calculate_gini(sub_class, main_c_gini)

    # Output the selected root with the minimum Gini index
    print(f"The selected root for splitting is: {root} (Minimum Gini Index)\n")
    writer.writerow([f"The selected root for splitting is: {root} (Minimum Gini Index)"])
