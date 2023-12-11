import csv
from collections import Counter
from itertools import combinations

min_freq_percent = float(input("Frequency %: "))
min_freq = 0
datatable = []
products = set()
freq = Counter()

def wordsof(s):
    return [token.strip() for token in s.split() if token.isalnum()]

def combine(arr, miss):
    return ' '.join([arr[i] for i in range(len(arr)) if i != miss])

def cloneit(arr):
    return set(arr)

def apriori_gen(sets, k):
    set2 = set()
    for item1 in sets:
        for item2 in sets:
            if len(set(item1.split())) == len(set(item2.split())) and item1 != item2:
                v1 = wordsof(item1)
                v2 = wordsof(item2)

                alleq = all(v1[i] == v2[i] for i in range(k - 1))

                v1.append(v2[k - 1])
                if v1[-1] < v1[-2]:
                    v1[-1], v1[-2] = v1[-2], v1[-1]

                for i in range(len(v1)):
                    tmp = combine(v1, i)
                    if tmp not in sets:
                        alleq = False

                if alleq:
                    set2.add(combine(v1, -1))

    return set2

with open("item_set_input.csv", 'r') as fin:
    csv_reader = csv.reader(fin)
    for line in csv_reader:
        arr = wordsof(line[0])
        tmpset = set(arr)
        datatable.append(tmpset)

        for item in tmpset:
            products.add(item)
            freq[item] += 1

print(f"No of transactions: {len(datatable)}")
min_freq = min_freq_percent * len(datatable) / 100
print(f"Min frequency: {min_freq}")

q = [item for item in products if freq[item] < min_freq]

for item in q:
    products.remove(item)

pass_number = 1
print(f"\nFrequent {pass_number}-item set:")
for item in products:
    print(f"{{{item}}}: {freq[item]}")

i = 2
prev = cloneit(products)

while i:
    cur = apriori_gen(prev, i - 1)

    if not cur:
        break

    for item in cur:
        arr = wordsof(item)
        tot = sum(1 for transaction in datatable if all(prod in transaction for prod in arr))

        if tot >= min_freq:
            freq[item] += tot
        else:
            q.append(item)

    while q:
        cur.remove(q.pop(0))

    flag = all(freq[item] >= min_freq for item in cur)

    if not cur:
        break

    print(f"\n\nFrequent {pass_number}-item set:")
    for item in cur:
        print(f"{{{item}}}: {freq[item]}")

    prev = cloneit(cur)
    i += 1

with open("item_set_output.csv", 'w') as fw:
    for item in prev:
        fw.write(f"{{{item}}}\n")
