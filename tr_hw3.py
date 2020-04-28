import pandas as pd
import math
import csv
import os

# a dictionary that stores the total number of documents for each class as a list for each term
# for example term_class_totals['weight'] = [total # docs in H containing 'weight', total in N containing 'weight', etc]
term_class_totals = {}
# a dictionary that stores the total number of documents for each class
class_totals = {
    'H': 0,
    'N': 0,
    'R': 0,
    'E': 0,
    'I': 0,
    'D': 0,
    'O': 0
}
# a dictionary to store the top 300 features for each class for build_binary_datasets
class_top300 = {
    'H': [],
    'N': [],
    'R': [],
    'E': [],
    'I': [],
    'D': [],
    'O': []
}
# a dictionary to map classes to indices for use with term_class_totals to calc MI scores
class_map = {
    'H': 0,
    'N': 1,
    'R': 2,
    'E': 3,
    'I': 4,
    'D': 5,
    'O': 6
}
# dictionary to store tokenized documents by doc ID
docs = {}
# dictionary to store labels for each document by doc ID as tuples (health, topic)
doc_labels = {}


def parse_doc(doc, test=False):
    """ A helper function to parse and tokenize a document. All white space is removed.
    All punctuation at the end of terms are removed and all words are lowercased. If a token
    is a conjunction of terms separated by / and is not a website, the token is split up into
    its individual terms (per suggestion from Dr McRoy via email).

    :param doc: the document to parse
    :param test: True if testing--used for logging
    :return: a list containing the tokenized document
    """
    if test: print('in parse_doc for: ' + doc)
    doc = doc.split()
    tokens = []
    for i in range(len(doc)):
        doc[i] = doc[i].strip().strip('\u201C').strip('\u201D').lower()
        doc[i] = doc[i].strip('.\"\'!?,/\\*()-_&;~:[]{}').replace('"',"'").replace(',', '.')
        if len(doc[i]) == 0 or doc[i] == '#' or doc[i] == '+' or doc[i] == '++' or doc[i] == '%' or doc[i] == '@':
            continue
        if doc[i].count('/') > 0 and doc[i].count('.com') == 0:
            words = doc[i].split('/')
            for j in range(len(words)):
                tokens.append(words[j].strip('\u201C').strip('\u201D').strip('.\"\'!?,/\\*()-_&;~:[]{}'))
        elif doc[i].count('-') > 0 and doc[i].count('.com') == 0:
            words = doc[i].split('-')
            for j in range(len(words)):
                tokens.append(words[j].strip('\u201C').strip('\u201D').strip('.\"\'!?,/\\*()-_&;~:[]{}'))
        elif doc[i].count('...') > 0:
            words = doc[i].split('...')
            for j in range(len(words)):
                tokens.append(words[j].strip('\u201C').strip('\u201D').strip('.\"\'!?,/\\*()-_&;~:[]{}'))
        elif doc[i].count(']') > 0:
            words = doc[i].split(']')
            for j in range(len(words)):
                tokens.append(words[j].strip('\u201C').strip('\u201D').strip('.\"\'!?,/\\*()-_&;~:[]{}'))
        elif doc[i].count('[') > 0:
            words = doc[i].split('[')
            for j in range(len(words)):
                if words[j] == '#':
                    continue
                tokens.append(words[j].strip('\u201C').strip('\u201D').strip('.\"\'!?,/\\*()-_&;~:[]{}'))
        else:
            tokens.append(doc[i])
    if test: print('Finished parsing')
    return tokens


def process_data(test=False):
    """ A function to parse the two xlsx files and store information for later use.
    The total number of documents are stored for each class in class_totals. The tokenized
    documents are stored in the docs dictionary by doc ID. The labels for each doc are stored
    in tuples (first index for health annotation, second index for topic annotation) in the
    doc_labels dictionary by doc ID. Term_class_totals stores the number of documents in each
    class that each term appears in (document frequency, not term frequency, for MI scores).

    :param test: True if testing--used for logging
    """
    if test:
        print('in process_data')
        print('class_totals: ', end='')
        print(class_totals)
        print('length of term_class_totals: ', end='')
        print(len(term_class_totals))
        print('length of docs: ', end='')
        print(len(docs))
        print('length of doc_labels: ', end='')
        print(len(doc_labels))

    # open the excel files as pandas data frames for easy parsing
    sheet1 = pd.ExcelFile('data/Annotated_for_health.xlsx').parse(0).values
    sheet2 = pd.ExcelFile('data/Annotated_for_topic.xlsx').parse(0).values

    # they are already sorted by the sentences, but if a new, unsorted, copy is used to
    # test my code, they will need to be sorted by column 0 by uncommenting the below lines.
    # sheet1[sheet1[:, 0].argsort()]
    # sheet2[sheet2[:, 0].argsort()]

    if test: print('opened xlsx files')

    for d in range(359):
        if test:
            try:
                assert sheet1[d][0] == sheet2[d][0]
            except AssertionError:
                print('First and second docs not equal!')
                return

        # update the total num docs for each class
        c1 = sheet1[d][1]
        n = class_totals[c1]
        class_totals[c1] = n+1
        c2 = sheet2[d][1]
        n = class_totals[c2]
        class_totals[c2] = n + 1

        # parse the document and store for ease of use in other functions
        tokens = parse_doc(sheet1[d][0])
        # get a list of terms without duplicates: we only care about if the term exists,
        # not how many times, to calculate MI scores
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

        # store labels for each doc (first index: by health; second: by topic)
        doc_labels[d] = (c1, c2)

    if test:
        print('finished process_data')
        print('class_totals: ', end='')
        print(class_totals)
        print('length of term_class_totals: ', end='')
        print(len(term_class_totals))
        print('length of docs: ', end='')
        print(len(docs))
        print('length of doc_labels: ', end='')
        print(len(doc_labels))


def mi_features(c, test=False):
    """ Given a class, c, calculate the mutual information scores for all
    terms in the training set for that class. After the scores are calculated,
    the top 300 terms are stored in descending order for build_binary_datasets.
    A document is created, C.scores, that lists all of the terms and their MI
    scores in descending order. The scores are calculated in the helper function,
    calc_mi.

    :param c: a class/topic
    :param test: True if testing--used for logging
    """
    if test: print('in mi_features for ' + c)

    if len(docs) == 0: process_data()
    mi_scores = []

    # for each term, calc mi score
    for i in term_class_totals:
        mi_scores.append([i, calc_mi(c, term_class_totals[i])])

    # sort the scores in descending order
    mi_scores.sort(reverse=True, key=lambda e: e[1])

    if test:
        print('scored and sorted all terms; length mi_scores: ', end='')
        print(len(mi_scores))
        print('saving top 300 terms for ' + c)

    # save the top 300 terms for the class for build_binary_datasets
    for i in range(300):
        class_top300[c].append(mi_scores[i][0])

    if test: print('creating scores/' + c + '.scores')

    # create a doc with each term and its mi score
    filename = 'scores/' + c + '.scores'
    with open(filename, 'w') as f:
        for i in range(len(mi_scores)):
            s = str(mi_scores[i][0]) + "  " + "{:.5f}".format(mi_scores[i][1]) + '\n'
            f.write(s)

    if test: print('finished mi_features')


def calc_mi(c, totals, test=False):
    """ A helper function to calculate the mutual information score for a term for
    a given class. It finds the values of N11, N10, N01, and N00, then uses the
    equation from the textbook to calculate MI.

    :param c: a class/topic
    :param totals: a list containing the total number of documents for each class
    that the term is in; for example, totals[0] contains the number of documents in
    class H that the term is in
    :param test: True if testing--used for logging
    :return: the calculated MI score for the term in the class
    """
    if test: print('calculating score')

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
    if test:
        print('n11: ' + str(n11))
        print('n10: ' + str(n10))
        print('n01: ' + str(n01))
        print('n00: ' + str(n00))
        print('n: ' + str(n))
    # calculate the MI score based on the equation in the textbook
    result = 0
    if n11 != 0: result += (n11/n)*math.log2((n*n11)/((n11+n10)*(n11+n01)))
    if n01 != 0: result += (n01/n)*math.log2((n*n01)/((n00+n01)*(n11+n01)))
    if n10 != 0: result += (n10/n)*math.log2((n*n10)/((n11+n10)*(n00+n10)))
    if n00 != 0: result += (n00/n)*math.log2((n*n00)/((n00+n01)*(n10+n00)))
    if test: print('mi score: ' + result)
    return result


def build_binary_datasets(c, test=False):
    """ Given a topic, c, create two binary datasets, C50.data and C300.data.
    Each dataset contains the documents in the training set, reduced to only
    contain the top 50 or top 300 features of the given class. Documents are
    labeled 1, if they are in the given class, or 0 otherwise.

    :param c: a topic/class
    :param test: True if testing--used for logging
    """
    if test: print('in build_binary_datasets for ' + c)
    if len(class_top300[c]) == 0: mi_features(c)

    file1 = 'data/' + c + '50.data'
    file2 = 'data/' + c + '300.data'
    words1 = class_top300[c][:50]
    words2 = class_top300[c]

    with open(file1, 'w') as csvf:
        writer = csv.writer(csvf)
        with open(file2, 'w') as csvf2:
            writer2 = csv.writer(csvf2)
            if test: print('Files are open and being written')
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
    if test: print('finished in build_binary_datasets')


def create_arff_data_a(c, test=False):
    """ Given a topic, c, create an arff file, multi_C.arff, using all of the
    features of the training set. Documents are labeled by their class.
    These are usable by Weka tools.

    :param c: a class/topic
    :param test: True if testing--used for logging
    """
    if test: print('in create_arff_data_a for ' + c)
    if len(docs) == 0: process_data()

    file_name = 'arff/multi_' + c + '.arff'
    with open(file_name, 'w') as f:
        if test: print('file is open and being written')
        f.write('@relation multiclass\n\n')
        keys = list(term_class_totals.keys())
        keys.sort()
        for term in keys:
            # weka was having trouble reading files without quotes for some of the words--not consistent
            f.write('@attribute "' + term + '" numeric\n')
        if c == 'H' or c == 'N':
            f.write('@attribute CLASS {H,N}\n')
        else:
            f.write('@attribute CLASS {D,E,I,O,R}\n')
        f.write('\n@data')
        for doc, tokens in docs.items():
            f.write('\n')
            s = ''
            for term in keys:
                if term in tokens:
                    s += '1,'
                else:
                    s += '0,'
            if c == 'H' or c == 'N':
                s += doc_labels[doc][0]
            else:
                s += doc_labels[doc][1]
            f.write(s)
    if test: print('finished creating arff file')


def create_arff_data_b(c, test=False):
    """" Given a topic, c, create two arff files. The first, binary_C50.arff, uses
    the top 50 features of the class in the dataset. The second, binary_C300.arff,
    uses the top 300 features of the class. The labels are 1, if the document is
    in the class, or 0 otherwise. These are usable by Weka tools.

    :param c: a class/topic
    :param test: True if testing--used for logging
    """
    if test: print('in create_arff_data_b for ' + c)
    if not os.path.isfile('data/'+c+'50.data'): build_binary_datasets(c)

    file_name = 'arff/binary_' + c + '50.arff'
    with open(file_name, 'w') as f:
        if test: print('binary 50 arff file being written')
        f.write('@relation binary\n\n')
        terms = class_top300[c][:50]
        terms.sort()
        for term in terms:
            # weka was having trouble reading files without quotes for some of the words--not consistent
            f.write('@attribute "' + term + '" numeric\n')
        f.write('@attribute CLASS {1,0}\n')
        f.write('\n@data')

        # Need to read shortened sentences in the binary datasets created by build_binary_dataset
        with open('data/' + c + '50.data') as csvf:
            read = csv.reader(csvf)
            for row in read:
                f.write('\n')
                tokens = row[0].split()
                s = ''
                for term in terms:
                    if term in tokens:
                        s += '1,'
                    else:
                        s += '0,'
                s += row[1]
                f.write(s)

    file_name = 'arff/binary_' + c + '300.arff'
    with open(file_name, 'w') as f:
        if test: print('binary 300 arff file being written')
        f.write('@relation binary\n\n')
        terms = class_top300[c]
        terms.sort()
        for term in terms:
            # weka was having trouble reading files without quotes for some of the words--not consistent
            f.write('@attribute "' + term + '" numeric\n')
        f.write('@attribute CLASS {1,0}\n')
        f.write('\n@data')

        # Need to read shortened sentences in the binary datasets created by build_binary_dataset
        with open('data/' + c + '300.data') as csvf:
            read = csv.reader(csvf)
            for row in read:
                f.write('\n')
                tokens = row[0].split()
                s = ''
                for term in terms:
                    if term in tokens:
                        s += '1,'
                    else:
                        s += '0,'
                s += row[1]
                f.write(s)
    if test: print('finished creating binary arff files')

'''
process_data()

mi_features('H')
mi_features('N')
mi_features('D')
mi_features('I')
mi_features('R')
mi_features('E')
mi_features('O')

build_binary_datasets('H')
build_binary_datasets('N')
build_binary_datasets('D')
build_binary_datasets('I')
build_binary_datasets('R')
build_binary_datasets('E')
build_binary_datasets('O')

create_arff_data_a('H')
create_arff_data_a('N')
create_arff_data_a('D')
create_arff_data_a('I')
create_arff_data_a('E')
create_arff_data_a('R')
create_arff_data_a('O')

create_arff_data_b('H')
create_arff_data_b('N')
create_arff_data_b('D')
create_arff_data_b('I')
create_arff_data_b('E')
create_arff_data_b('R')
create_arff_data_b('O')
'''
