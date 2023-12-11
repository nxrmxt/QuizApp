import csv

# Open the file
with open("13 - Bayes Classfication/bayes.csv") as f:
    reader = csv.reader(f)

    # Extract column headers
    title = next(reader)

    # Initialize data structures
    parent = {}
    child = {}
    count = 0

    for row in reader:
        # Extract values from the row
        columns = row

        # Count occurrences of the result class
        result_class = columns[-1]
        parent[result_class] = parent.get(result_class, 0) + 1

        # Count occurrences of attributes given the result class
        for i in range(1, len(columns) - 1):
            attribute = title[i]
            value = columns[i]
            child.setdefault(attribute, {})
            child[attribute].setdefault(value, {})
            child[attribute][value].setdefault(result_class, 0)
            child[attribute][value][result_class] += 1

        count += 1

    # Convert maps to lists
    result_classes = list(parent.keys())
    output = [1] * len(result_classes)

    # Get user input for attribute conditions
    for attribute, values in child.items():
        while True:
            condition = input(f"Enter {attribute} condition: ")
            if condition not in values:
                print("No match. Please enter a valid condition.")
            else:
                break

            for i, result_class in enumerate(result_classes):
                # Calculate conditional probabilities
                probability = child[attribute][condition][result_class] / parent[result_class]
                output[i] *= probability

                print(f"{probability} / {parent[result_class]}")
                print(f"Updated output: {output[i]}")

    # Multiply by prior probabilities
    for i, result_class in enumerate(result_classes):
        output[i] *= parent[result_class] / count

    # Calculate sum and normalize probabilities
    sum_of_probabilities = sum(output)
    for i, result_class in enumerate(result_classes):
        output[i] = output[i] / sum_of_probabilities

    # Print results
    print(f"Sum of probabilities: {sum_of_probabilities}")
    print("Output probabilities:")
    for i, result_class in enumerate(result_classes):
        percentage = output[i] * 100
        print(f"{result_class}: {output[i]}")
        print(f"Percentage: {percentage:.2f}%")

