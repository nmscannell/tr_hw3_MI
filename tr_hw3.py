import pandas as pd
import math
import csv

# for each term, the num docs for each class []
term_class_totals = {}
# H, N, R, E, I, D, O
class_totals = {
    'H': 0,
    'N': 0,
    'R': 0,
    'E': 0,
    'I': 0,
    'D': 0,
    'O': 0
}
#class_docs = {
#    'H': [],
#    'N': [],
#    'R': [],
#    'E': [],
#    'I': [],
#    'D': [],
#    'O': []
#}
class_top300 = {
    'H': [],
    'N': [],
    'R': [],
    'E': [],
    'I': [],
    'D': [],
    'O': []
}
class_map = {
    'H': 0,
    'N': 1,
    'R': 2,
    'E': 3,
    'I': 4,
    'D': 5,
    'O': 6
}
docs = {}
doc_labels = {}

sheet1 = pd.ExcelFile('Annotated_for_health.xlsx').parse(0).values
sheet2 = pd.ExcelFile('Annotated_for_topic.xlsx').parse(0).values


def parse_doc(doc):
    doc = doc.split()
    tokens = []
    for i in range(len(doc)):
        doc[i] = doc[i].strip().strip('\u201C').strip('\u201D').lower()
        doc[i] = doc[i].strip('.!?,/\\*()-_&;~:[]{}')
        if doc[i].count('/') > 0 and doc[i].count('.com') == 0:
            words = doc[i].split('/')
            for j in range(len(words)):
                tokens.append(words[j])
        else:
            tokens.append(doc[i])
    return tokens


def process_data():
    for d in range(359):
        # update the total num docs for each class
        c1 = sheet1[d][1]
        n = class_totals[c1]
        class_totals[c1] = n+1
        c2 = sheet2[d][1]
        n = class_totals[c2]
        class_totals[c2] = n + 1

        # parse the document and get a list without duplicates: we only care about if the term exists, not how many times
        tokens = parse_doc(sheet1[d][0])
        no_dup = list(dict.fromkeys(tokens))

        # update the number of documents that the term belongs in for each class
        for term in no_dup:
            if term in term_class_totals:
                totals = term_class_totals[term]
                totals[class_map[c1]] += 1
                totals[class_map[c2]] += 1
                term_class_totals[term] = totals
            else:
                totals = [0 for i in range(7)]
                totals[class_map[c1]] = 1
                totals[class_map[c2]] = 1
                term_class_totals[term] = totals

        # store the full tokens in a dict with its doc id
        docs[d] = tokens

        # store labels for each doc
        doc_labels[d] = (c1, c2)


def mi_features(c):
    mi_scores = []

    # for each term, calc mi score
    for i in term_class_totals:
        mi_scores.append([i, calc_mi(c, term_class_totals[i])])

    # sort the scores in descending order
    mi_scores.sort(reverse=True, key=lambda e: e[1])

    # save the top 300 terms for the class
    for i in range(300):
        class_top300[c].append(mi_scores[i][0])

    # create a doc with each term and its mi score
    filename = c + '.scores'
    with open(filename, 'w') as f:
        for i in range(len(mi_scores)):
            s = str(mi_scores[i][0]) + "  " + "{:.5f}".format(mi_scores[i][1]) + '\n'
            f.write(s)


def calc_mi(c, totals):
    print(totals)
    # n11: number of docs with the term in the class
    n11 = totals[class_map[c]]

    # n10: number of docs with the term not in the class: sum of count for other classes
    if c == 'H':
        n10 = totals[1]
    elif c == 'N':
        n10 = totals[0]
    else:
        n10 = 0
        for i in range(2, len(totals)):
            if i != class_map[c]:
                n10 += totals[i]

    # n01: number of docs without the term in the class: total docs for class - n11
    n01 = class_totals[c] - n11

    # n00: number of docs without the term not in the class: total docs for other classes - n10
    if c == 'H':
        n00 = class_totals['N']
    elif c == 'N':
        n00 = class_totals['H']
    else:
        n00 = 0
        for x, y in class_totals.items():
            if x != c and x != 'H' and x != 'N':
                n00 += y
    n00 -= n10

    n = n11 + n10 + n01 + n00
#    print(n, n11, n10, n01, n00)

    result = 0
    if n11 != 0:
        result += (n11/n)*math.log2((n*n11)/((n11+n10)*(n11+n01)))
    if n01 != 0:
        result += (n01/n)*math.log2((n*n01)/((n00+n01)*(n11+n01)))
    if n10 != 0:
        result += (n10/n)*math.log2((n*n10)/((n11+n10)*(n00+n10)))
    if n00 != 0:
        result += (n00/n)*math.log2((n*n00)/((n00+n01)*(n10+n00)))
    return result


def build_binary_datasets(c):
    file1 = c + '50.data'
    file2 = c + '300.data'
    words1 = class_top300[c][:50]
    words2 = class_top300[c]

    with open(file1, 'w') as csvf:
        writer = csv.writer(csvf)
        with open(file2, 'w') as csvf2:
            writer2 = csv.writer(csvf2)
            for i in range(len(docs)):
                classes = doc_labels[i]
                tokens = docs[i]
                s = ''
                s2 = ''
                if c == 'H' or c == 'N':
                    label = classes[0]
                else:
                    label = classes[1]
                for t in tokens:
                    if t in words1:
                        s += t + ' '
                    if t in words2:
                        s2 += t + ' '
                s = s[:len(s)-1]
                s2 = s2[:len(s2)-1]
                if label == c:
                    label = 1
                else:
                    label = 0
                writer.writerow([s] + [label])
                writer2.writerow([s2] + [label])


def create_arff_data_a(c):
    pass


def create_arff_data_b(c):
    pass

print(term_class_totals)
process_data()
print(term_class_totals)
print(class_totals)
mi_features('H')
mi_features('N')
mi_features('D')
mi_features('I')
mi_features('R')
mi_features('E')
mi_features('O')
#print(term_class_totals)
build_binary_datasets('H')
#print(type('strength'))
build_binary_datasets('N')
build_binary_datasets('D')
build_binary_datasets('I')
build_binary_datasets('R')
build_binary_datasets('E')
build_binary_datasets('O')
