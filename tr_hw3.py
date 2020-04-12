import pandas as pd
import math
import csv
import numpy as np
import nltk
#nltk.download()


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
class_docs = {
    'H': [],
    'N': [],
    'R': [],
    'E': [],
    'I': [],
    'D': [],
    'O': []
}
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


def process_data():
    sheet1 = pd.ExcelFile('Annotated_for_health.xlsx').parse(0).values
    sheet2 = pd.ExcelFile('Annotated_for_topic.xlsx').parse(0).values
    punct = ['.', '?', '"', ',', "'"]
    for d in range(359):
        # update the total doc num for the class
        c = sheet1[d][1]
        n = class_totals[c]
        class_totals[c] = n+1
        l = nltk.word_tokenize(sheet1[d][0])
        l = list(filter(lambda i: i not in punct, l))

        for i in range(len(l)):
            if l[i] == "n't":
                l[i] = 'not'
            l[i] = l[i].strip('.!?",/\\*()-_&;~:[]{}').lower()
            if l[i].count('/') > 0 and l[i].count('.com') == 0:
                words = l[i].split('/')
                l[i] = words[0]
                for j in range(1, len(words)):
                    l.append(words[j])

        class_docs[c].append(l)
        l = list(dict.fromkeys(l))
        if '' in l:
            l.remove('')

        # update the num docs for the class for each term
        for t in l:
            if t in term_class_totals:
                li = term_class_totals[t]
                li[class_map[c]] += 1
                term_class_totals[t] = li
            else:
                li = [0 for n in range(7)]
                li[class_map[c]] = 1
                term_class_totals[t] = li

        # update the total doc num for the class
        c = sheet2[d][1]
        n = class_totals[c]
        class_totals[c] = n + 1
        l = nltk.word_tokenize(sheet2[d][0])
        l = list(filter(lambda i: i not in punct, l))

        for i in range(len(l)):
            if l[i] == "n't":
                l[i] = 'not'
            l[i] = l[i].strip('.!?",/\\*()-_&;~:[]{}').lower()
            if l[i].count('/') > 0 and l[i].count('.com') == 0:
                words = l[i].split('/')
                l[i] = words[0]
                for j in range(1, len(words)):
                   l.append(words[j])

        class_docs[c].append(l)
        l = list(dict.fromkeys(l))
        if '' in l:
            l.remove('')

        # update the num docs for the class for each term
        for t in l:
            if t in term_class_totals:
                li = term_class_totals[t]
                li[class_map[c]] += 1
                term_class_totals[t] = li
            else:
                li = [0 for n in range(7)]
                li[class_map[c]] = 1
                term_class_totals[t] = li


def mi_features(c):
    mi_scores = []

    for i in term_class_totals:
        print(i)
        print(term_class_totals[i])
        mi_scores.append([i, calc_mi(c, term_class_totals[i])])

    mi_scores.sort(reverse=True, key=lambda e: e[1])

    for i in range(300):
        class_top300[c].append(mi_scores[i][0])

    filename = c + '.scores'
    with open(filename, 'w') as f:
        for i in range(len(mi_scores)):
            s = mi_scores[i][0] + "  " + "{:.5f}".format(mi_scores[i][1]) + '\n'
            f.write(s)


def calc_mi(c, totals):
    print(totals)
    n11 = totals[class_map[c]]
    n10 = 0
    for i in range(len(totals)):
        if i != class_map[c]:
            n10 += totals[i]
    n01 = class_totals[c] - n11
    n00 = 0
    for x, y in class_totals.items():
        if x != c:
            n00 += y
    n00 -= n10
    n = n11 + n10 + n01 + n00
    print(n, n11, n10, n01, n00)

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
        for doc in class_docs[c]:
            s = ''
            for t in doc:
                if t in words1:
                    s += t + ' '
            s = s[:len(s)-1]
            if len(s) == 0:
                continue
            writer.writerow([s] + [c])
    with open(file2, 'w') as csvf:
        writer = csv.writer(csvf)
        for doc in class_docs[c]:
            s = ''
            for t in doc:
                if t in words2:
                    s += t + ' '
            s = s[:len(s)-1]
            if len(s) == 0:
                continue
            writer.writerow([s] + [c])


def create_ARFF_dataA():
    pass


def create_ARFF_dataB():
    pass

print(term_class_totals)
process_data()
print(term_class_totals)
print(class_totals)
mi_features('H')
print(term_class_totals)
print(class_docs['H'])
build_binary_datasets('H')
print(type('strength'))