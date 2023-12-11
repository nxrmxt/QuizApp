import csv
import re

def get_transactions():
    # Replace this with your actual transaction data
    transactions = [
        ['bread', 'milk'],
        ['bread', 'diapers', 'beer', 'eggs'],
        ['milk', 'diapers', 'beer', 'cola'],
        ['bread', 'milk', 'diapers', 'beer'],
        ['bread', 'milk', 'diapers', 'cola']
    ]
    return transactions

def get_unique_items(transactions):
    unique_items = []
    for transaction in transactions:
        for item in transaction:
            if item not in unique_items:
                unique_items.append(item)
    return unique_items

def generate_candidates(prev_itemsets, k):
    candidates = []
    for i in range(len(prev_itemsets)):
        for j in range(i + 1, len(prev_itemsets)):
            union_set = list(set(prev_itemsets[i] + prev_itemsets[j]))
            if len(union_set) == k and union_set not in candidates:
                candidates.append(union_set)
    return candidates

def get_frequent_itemsets(transactions, min_support):
    unique_items = get_unique_items(transactions)
    itemsets = [[item] for item in unique_items]
    k = 2
    frequent_itemsets = []

    while itemsets:
        counts = {}
        for transaction in transactions:
            for itemset in itemsets:
                if all(item in transaction for item in itemset):
                    counts[tuple(itemset)] = counts.get(tuple(itemset), 0) + 1

        frequent_itemsets.extend([(list(itemset), support) for itemset, support in counts.items() if support >= min_support])

        itemsets = generate_candidates(itemsets, k)
        k += 1

    return frequent_itemsets

def print_frequent_itemsets(frequent_itemsets):
    for itemset, support in frequent_itemsets:
        print(f"{itemset}: {support}")

def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            generate_rules_from_itemset([], itemset, support, rules, min_confidence)
    return rules

def generate_rules_from_itemset(antecedent, consequent, support, rules, min_confidence):
    if antecedent and consequent:
        confidence = support / get_support(antecedent)
        if confidence >= min_confidence:
            rules.append((antecedent, consequent, support, confidence))

    if len(antecedent) < len(consequent) - 1:
        for item in consequent:
            if item not in antecedent:
                generate_rules_from_itemset(antecedent + [item], consequent, support, rules, min_confidence)

def get_support(itemset):
    for item, support in frequent_itemsets:
        if set(item) == set(itemset):
            return support
    return 0

if __name__ == "__main__":
    transactions = get_transactions()
    min_support = 2  # Set your minimum support threshold here
    min_confidence = 0.7  # Set your minimum confidence threshold here

    frequent_itemsets = get_frequent_itemsets(transactions, min_support)
    print("Frequent Itemsets:")
    print_frequent_itemsets(frequent_itemsets)
    print("\nAssociation Rules:")
    association_rules = generate_association_rules(frequent_itemsets, min_confidence)
    for rule in association_rules:
        antecedent, consequent, support, confidence = rule
        print(f"{antecedent} => {consequent} (Support: {support}, Confidence: {confidence})")
