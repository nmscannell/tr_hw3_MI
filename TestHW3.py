import tr_hw3
import unittest
import sys
import glob
import os


class TestHW3(unittest.TestCase):

    @classmethod
    def setUpClass(TestHW3):
        print('Set Up: removing created files and emptying dictionaries\n')
        for f in glob.glob('arff/*'):
            os.remove(f)
        for f in glob.glob('scores/*'):
            os.remove(f)
        for f in glob.glob('data/*.data'):
            os.remove(f)
        tr_hw3.doc_labels = {}
        tr_hw3.docs = {}
        tr_hw3.term_class_totals = {}
        tr_hw3.class_totals = {'H': 0, 'N': 0, 'R': 0, 'E': 0, 'I': 0, 'D': 0, 'O': 0}
        tr_hw3.class_top300 = {'H': [], 'N': [], 'R': [], 'E': [], 'I': [], 'D': [], 'O': []}

    def tearDown(self):
        print('Tear Down: removing any created files and emptying dictionaries\n')
        for f in glob.glob('arff/*'):
            os.remove(f)
        for f in glob.glob('scores/*'):
            os.remove(f)
        for f in glob.glob('data/*.data'):
            os.remove(f)
        tr_hw3.doc_labels = {}
        tr_hw3.docs = {}
        tr_hw3.term_class_totals = {}
        tr_hw3.class_totals = {'H': 0, 'N': 0, 'R': 0, 'E': 0, 'I': 0, 'D': 0, 'O': 0}
        tr_hw3.class_top300 = {'H': [], 'N': [], 'R': [], 'E': [], 'I': [], 'D': [], 'O': []}

    def test_parse_simple_sentence(self):
        s = "This is a simple sentence."
        tok = ['this', 'is', 'a', 'simple', 'sentence']
        print('Running test_parse_simple_sentence')
        print('sentence: ', s)
        result = tr_hw3.parse_doc(s)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result, 'parse_docs did not produce the correct token list')
        print('Finished test_parse_simple_sentence')

    def test_parse_med_sentence(self):
        s = "This, is a, med/intermediate 'level-difficulty' sentence."
        tok = ['this', 'is', 'a', 'med', 'intermediate', 'level', 'difficulty', 'sentence']
        print('Running test_parse_med_sentence')
        print('sentence: ', s)
        result = tr_hw3.parse_doc(s)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result, 'parse_docs did not produce the correct token list')
        print('Finished test_parse_med_sentence')

    def test_parse_complex_sentence(self):
        s = "This, is a, far](more 'difficult' doc. # it contains% odd google.com term& can't"
        tok = ['this', 'is', 'a', 'far', 'more', 'difficult', 'doc', 'it', 'contains%', 'odd', 'google.com', 'term', "can't"]
        print('Running test_parse_complex_sentence')
        print('sentence: ', s)
        result = tr_hw3.parse_doc(s)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result, 'parse_docs did not produce the correct token list')
        print('Finished test_parse_complex_sentence')

    def test_process_data(self):
        print('Running test_process_data')
        tr_hw3.process_data()
        print('Finished test_process_data')

    def test_mi_features_H(self):
        print('Running test_mi_features_H')
        self.assertFalse(os.path.exists('scores/H.scores'), 'H.scores already exists')
        print('H.scores does not already exist')
        tr_hw3.mi_features('H')
        self.assertTrue(os.path.exists('scores/H.scores'), 'H.scores was not created')
        print('H.scores exists')
        with open('scores/H.scores') as f1:
            with open('test_files/H.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_H')

    def test_mi_features_N(self):
        print('Running test_mi_features_N')
        self.assertFalse(os.path.exists('scores/N.scores'), 'N.scores already exists')
        print('N.scores does not already exist')
        tr_hw3.mi_features('N')
        self.assertTrue(os.path.exists('scores/N.scores'), 'N.scores was not created')
        print('N.scores exists')
        with open('scores/N.scores') as f1:
            with open('test_files/N.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_N')

    def test_mi_features_D(self):
        print('Running test_mi_features_D')
        self.assertFalse(os.path.exists('scores/D.scores'), 'D.scores already exists')
        print('D.scores does not already exist')
        tr_hw3.mi_features('D')
        self.assertTrue(os.path.exists('scores/D.scores'), 'D.scores was not created')
        print('D.scores exists')
        with open('scores/D.scores') as f1:
            with open('test_files/D.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_D')

    def test_mi_features_E(self):
        print('Running test_mi_features_E')
        self.assertFalse(os.path.exists('scores/E.scores'), 'E.scores already exists')
        print('E.scores does not already exist')
        tr_hw3.mi_features('E')
        self.assertTrue(os.path.exists('scores/E.scores'), 'E.scores was not created')
        print('E.scores exists')
        with open('scores/E.scores') as f1:
            with open('test_files/E.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_E')

    def test_mi_features_I(self):
        print('Running test_mi_features_I')
        self.assertFalse(os.path.exists('scores/I.scores'), 'I.scores already exists')
        print('I.scores does not already exist')
        tr_hw3.mi_features('I')
        self.assertTrue(os.path.exists('scores/I.scores'), 'I.scores was not created')
        print('I.scores exists')
        with open('scores/I.scores') as f1:
            with open('test_files/I.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_I')

    def test_mi_features_O(self):
        print('Running test_mi_features_O')
        self.assertFalse(os.path.exists('scores/O.scores'), 'O.scores already exists')
        print('O.scores does not already exist')
        tr_hw3.mi_features('O')
        self.assertTrue(os.path.exists('scores/O.scores'), 'O.scores was not created')
        print('O.scores exists')
        with open('scores/O.scores') as f1:
            with open('test_files/O.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_O')

    def test_mi_features_R(self):
        print('Running test_mi_features_R')
        self.assertFalse(os.path.exists('scores/R.scores'), 'R.scores already exists')
        print('R.scores does not already exist')
        tr_hw3.mi_features('R')
        self.assertTrue(os.path.exists('scores/R.scores'), 'R.scores was not created')
        print('R.scores exists')
        with open('scores/R.scores') as f1:
            with open('test_files/R.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R.scores does not have the correct info')
        print('Created file is correct')
        print('Finished test_mi_features_R')

    def test_calc_mi(self):
        print('Running test_calc_mi for class H and term "workout"')
        result = tr_hw3.calc_mi('H', [23, 30, 11, 5, 14, 16, 7])
        self.assertEqual(result, 0.009100701011345146, 'MI score not correctly calculated')
        print('testing for class H and term "diet"')
        result = tr_hw3.calc_mi('H', [14, 15, 2, 2, 5, 18, 2])
        self.assertEqual(result, 0.008648510597977208, 'MI score not correctly calculated')
        print('Finished test_calc_mi')

    def test_build_binary_dataset_H(self):
        print('Running test_build_binary_dataset_H')
        self.assertFalse(os.path.exists('data/H50.data'), 'H50.data already exists')
        print('H50.data does not already exist')
        self.assertFalse(os.path.exists('data/H300.data'), 'H300.data already exists')
        print('H300.data does not already exist')
        tr_hw3.build_binary_datasets('H')
        self.assertTrue(os.path.exists('data/H50.data'), 'H50.data was not created')
        print('H50.data exists')
        self.assertTrue(os.path.exists('data/H300.data'), 'H300.data was not created')
        print('H300.data exists')
        with open('data/H50.data') as f1:
            with open('test_files/H50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H50.data does not have the correct info')
        with open('data/H300.data') as f1:
            with open('test_files/H300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_H')

    def test_build_binary_dataset_N(self):
        print('Running test_build_binary_dataset_N')
        self.assertFalse(os.path.exists('data/N50.data'), 'N50.data already exists')
        print('N50.data does not already exist')
        self.assertFalse(os.path.exists('data/N300.data'), 'N300.data already exists')
        print('N300.data does not already exist')
        tr_hw3.build_binary_datasets('N')
        self.assertTrue(os.path.exists('data/N50.data'), 'N50.data was not created')
        print('N50.data exists')
        self.assertTrue(os.path.exists('data/N300.data'), 'N300.data was not created')
        print('N300.data exists')
        with open('data/N50.data') as f1:
            with open('test_files/N50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N50.data does not have the correct info')
        with open('data/N300.data') as f1:
            with open('test_files/N300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_N')

    def test_build_binary_dataset_D(self):
        print('Running test_build_binary_dataset_D')
        self.assertFalse(os.path.exists('data/D50.data'), 'D50.data already exists')
        print('D50.data does not already exist')
        self.assertFalse(os.path.exists('data/D300.data'), 'D300.data already exists')
        print('D300.data does not already exist')
        tr_hw3.build_binary_datasets('D')
        self.assertTrue(os.path.exists('data/D50.data'), 'D50.data was not created')
        print('D50.data exists')
        self.assertTrue(os.path.exists('data/D300.data'), 'D300.data was not created')
        print('D300.data exists')
        with open('data/D50.data') as f1:
            with open('test_files/D50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D50.data does not have the correct info')
        with open('data/D300.data') as f1:
            with open('test_files/D300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_D')

    def test_build_binary_dataset_E(self):
        print('Running test_build_binary_dataset_E')
        self.assertFalse(os.path.exists('data/E50.data'), 'E50.data already exists')
        print('E50.data does not already exist')
        self.assertFalse(os.path.exists('data/E300.data'), 'E300.data already exists')
        print('E300.data does not already exist')
        tr_hw3.build_binary_datasets('E')
        self.assertTrue(os.path.exists('data/E50.data'), 'E50.data was not created')
        print('E50.data exists')
        self.assertTrue(os.path.exists('data/E300.data'), 'E300.data was not created')
        print('E300.data exists')
        with open('data/E50.data') as f1:
            with open('test_files/E50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E50.data does not have the correct info')
        with open('data/E300.data') as f1:
            with open('test_files/E300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_E')

    def test_build_binary_dataset_I(self):
        print('Running test_build_binary_dataset_I')
        self.assertFalse(os.path.exists('data/I50.data'), 'I50.data already exists')
        print('I50.data does not already exist')
        self.assertFalse(os.path.exists('data/I300.data'), 'I300.data already exists')
        print('I300.data does not already exist')
        tr_hw3.build_binary_datasets('I')
        self.assertTrue(os.path.exists('data/I50.data'), 'I50.data was not created')
        print('I50.data exists')
        self.assertTrue(os.path.exists('data/I300.data'), 'I300.data was not created')
        print('I300.data exists')
        with open('data/I50.data') as f1:
            with open('test_files/I50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I50.data does not have the correct info')
        with open('data/I300.data') as f1:
            with open('test_files/I300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_I')

    def test_build_binary_dataset_O(self):
        print('Running test_build_binary_dataset_O')
        self.assertFalse(os.path.exists('data/O50.data'), 'O50.data already exists')
        print('O50.data does not already exist')
        self.assertFalse(os.path.exists('data/O300.data'), 'O300.data already exists')
        print('O300.data does not already exist')
        tr_hw3.build_binary_datasets('O')
        self.assertTrue(os.path.exists('data/O50.data'), 'O50.data was not created')
        print('O50.data exists')
        self.assertTrue(os.path.exists('data/O300.data'), 'O300.data was not created')
        print('O300.data exists')
        with open('data/O50.data') as f1:
            with open('test_files/O50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O50.data does not have the correct info')
        with open('data/O300.data') as f1:
            with open('test_files/O300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_O')

    def test_build_binary_dataset_R(self):
        print('Running test_build_binary_dataset_R')
        self.assertFalse(os.path.exists('data/R50.data'), 'R50.data already exists')
        print('R50.data does not already exist')
        self.assertFalse(os.path.exists('data/R300.data'), 'R50.data already exists')
        print('R300.data does not already exist')
        tr_hw3.build_binary_datasets('R')
        self.assertTrue(os.path.exists('data/R50.data'), 'R50.data was not created')
        print('R50.data exists')
        self.assertTrue(os.path.exists('data/R300.data'), 'R300.data was not created')
        print('R300.data exists')
        with open('data/R50.data') as f1:
            with open('test_files/R50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R50.data does not have the correct info')
        with open('data/R300.data') as f1:
            with open('test_files/R300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R300.data does not have the correct info')
        print('Created files are correct')
        print('Finished test_build_binary_dataset_R')

    def test_create_arff_a_H(self):
        print('Running test_create_arff_a_H')
        self.assertFalse(os.path.exists('arff/multi_H.arff'), 'H.arff already exists')
        print('multi_H.arff does not already exist')
        tr_hw3.create_arff_data_a('H')
        self.assertTrue(os.path.exists('arff/multi_H.arff'), 'H.arff was not created')
        print('multi_H.arff exists')
        with open('arff/multi_H.arff') as f1:
            with open('test_files/multi_H.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_H')

    def test_create_arff_a_N(self):
        print('Running test_create_arff_a_N')
        self.assertFalse(os.path.exists('arff/multi_N.arff'), 'N.arff already exists')
        print('multi_N.arff does not already exist')
        tr_hw3.create_arff_data_a('N')
        self.assertTrue(os.path.exists('arff/multi_N.arff'), 'N.arff was not created')
        print('multi_N.arff exists')
        with open('arff/multi_N.arff') as f1:
            with open('test_files/multi_N.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_N')

    def test_create_arff_a_D(self):
        print('Running test_create_arff_a_D')
        self.assertFalse(os.path.exists('arff/multi_D.arff'), 'D.arff already exists')
        print('multi_D.arff does not already exist')
        tr_hw3.create_arff_data_a('D')
        self.assertTrue(os.path.exists('arff/multi_D.arff'), 'D.arff was not created')
        print('multi_D.arff exists')
        with open('arff/multi_D.arff') as f1:
            with open('test_files/multi_D.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_D')

    def test_create_arff_a_E(self):
        print('Running test_create_arff_a_E')
        self.assertFalse(os.path.exists('arff/multi_E.arff'), 'E.arff already exists')
        print('multi_E.arff does not already exist')
        tr_hw3.create_arff_data_a('E')
        self.assertTrue(os.path.exists('arff/multi_E.arff'), 'E.arff was not created')
        print('multi_E.arff exists')
        with open('arff/multi_E.arff') as f1:
            with open('test_files/multi_E.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_E')

    def test_create_arff_a_I(self):
        print('Running test_create_arff_a_I')
        self.assertFalse(os.path.exists('arff/multi_I.arff'), 'I.arff already exists')
        print('multi_I.arff does not already exist')
        tr_hw3.create_arff_data_a('I')
        self.assertTrue(os.path.exists('arff/multi_I.arff'), 'I.arff was not created')
        print('multi_I.arff exists')
        with open('arff/multi_I.arff') as f1:
            with open('test_files/multi_I.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_I')

    def test_create_arff_a_O(self):
        print('Running test_create_arff_a_O')
        self.assertFalse(os.path.exists('arff/multi_O.arff'), 'O.arff already exists')
        print('multi_O.arff does not already exist')
        tr_hw3.create_arff_data_a('O')
        self.assertTrue(os.path.exists('arff/multi_O.arff'), 'O.arff was not created')
        print('multi_O.arff exists')
        with open('arff/multi_O.arff') as f1:
            with open('test_files/multi_O.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_O')

    def test_create_arff_a_R(self):
        print('Running test_create_arff_a_R')
        self.assertFalse(os.path.exists('arff/multi_R.arff'), 'R.arff already exists')
        print('multi_R.arff does not already exist')
        tr_hw3.create_arff_data_a('R')
        self.assertTrue(os.path.exists('arff/multi_R.arff'), 'R.arff was not created')
        print('multi_R.arff exists')
        with open('arff/multi_R.arff') as f1:
            with open('test_files/multi_R.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R.arff does not have the correct info')
        print('Created file is correct')
        print('Finished test_create_arff_a_R')

    def test_create_arff_b_H(self):
        print('Running test_create_arff_b_H')
        self.assertFalse(os.path.exists('arff/binary_H50.arff'), 'H50.arff already exists')
        print('binary_H50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_H300.arff'), 'H300.arff already exists')
        print('binary_H300.arff does not already exist')
        tr_hw3.create_arff_data_b('H')
        self.assertTrue(os.path.exists('arff/binary_H50.arff'), 'H50.arff was not created')
        print('binary_H50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_H300.arff'), 'H300.arff was not created')
        print('binary_H300.arff exists')
        with open('arff/binary_H50.arff') as f1:
            with open('test_files/binary_H50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H50.arff does not have the correct info')
        with open('arff/binary_H300.arff') as f1:
            with open('test_files/binary_H300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'H300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_H')

    def test_create_arff_b_N(self):
        print('Running test_create_arff_b_N')
        self.assertFalse(os.path.exists('arff/binary_N50.arff'), 'N50.arff already exists')
        print('binary_N50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_N300.arff'), 'N300.arff already exists')
        print('binary_N300.arff does not already exist')
        tr_hw3.create_arff_data_b('N')
        self.assertTrue(os.path.exists('arff/binary_N50.arff'), 'N50.arff was not created')
        print('binary_N50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_N300.arff'), 'N300.arff was not created')
        print('binary_N300.arff exists')
        with open('arff/binary_N50.arff') as f1:
            with open('test_files/binary_N50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N50.arff does not have the correct info')
        with open('arff/binary_N300.arff') as f1:
            with open('test_files/binary_N300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'N300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_N')

    def test_create_arff_b_D(self):
        print('Running test_create_arff_b_D')
        self.assertFalse(os.path.exists('arff/binary_D50.arff'), 'D50.arff already exists')
        print('binary_D50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_D300.arff'), 'D300.arff already exists')
        print('binary_D300.arff does not already exist')
        tr_hw3.create_arff_data_b('D')
        self.assertTrue(os.path.exists('arff/binary_D50.arff'), 'D50.arff was not created')
        print('binary_D50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_D300.arff'), 'D300.arff was not created')
        print('binary_D300.arff exists')
        with open('arff/binary_D50.arff') as f1:
            with open('test_files/binary_D50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D50.arff does not have the correct info')
        with open('arff/binary_D300.arff') as f1:
            with open('test_files/binary_D300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'D300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_D')

    def test_create_arff_b_E(self):
        print('Running test_create_arff_b_E')
        self.assertFalse(os.path.exists('arff/binary_E50.arff'), 'E50.arff already exists')
        print('binary_E50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_E300.arff'), 'E300.arff already exists')
        print('binary_E300.arff does not already exist')
        tr_hw3.create_arff_data_b('E')
        self.assertTrue(os.path.exists('arff/binary_E50.arff'), 'E50.arff was not created')
        print('binary_E50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_E300.arff'), 'E300.arff was not created')
        print('binary_E300.arff exists')
        with open('arff/binary_E50.arff') as f1:
            with open('test_files/binary_E50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E50.arff does not have the correct info')
        with open('arff/binary_E300.arff') as f1:
            with open('test_files/binary_E300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'E300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_E')

    def test_create_arff_b_I(self):
        print('Running test_create_arff_b_I')
        self.assertFalse(os.path.exists('arff/binary_I50.arff'), 'I50.arff already exists')
        print('binary_I50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_I300.arff'), 'I300.arff already exists')
        print('binary_I300.arff does not already exist')
        tr_hw3.create_arff_data_b('I')
        self.assertTrue(os.path.exists('arff/binary_I50.arff'), 'I50.arff was not created')
        print('binary_I50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_I300.arff'), 'I300.arff was not created')
        print('binary_I300.arff exists')
        with open('arff/binary_I50.arff') as f1:
            with open('test_files/binary_I50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I50.arff does not have the correct info')
        with open('arff/binary_I300.arff') as f1:
            with open('test_files/binary_I300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'I300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_I')

    def test_create_arff_b_O(self):
        print('Running test_create_arff_b_O')
        self.assertFalse(os.path.exists('arff/binary_O50.arff'), 'O50.arff already exists')
        print('binary_O50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_O300.arff'), 'O300.arff already exists')
        print('binary_O300.arff does not already exist')
        tr_hw3.create_arff_data_b('O')
        self.assertTrue(os.path.exists('arff/binary_O50.arff'), 'O50.arff was not created')
        print('binary_O50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_O300.arff'), 'O300.arff was not created')
        print('binary_O300.arff exists')
        with open('arff/binary_O50.arff') as f1:
            with open('test_files/binary_O50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O50.arff does not have the correct info')
        with open('arff/binary_O300.arff') as f1:
            with open('test_files/binary_O300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'O300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_O')

    def test_create_arff_b_R(self):
        print('Running test_create_arff_b_R')
        self.assertFalse(os.path.exists('arff/binary_R50.arff'), 'R50.arff already exists')
        print('binary_R50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_R300.arff'), 'R300.arff already exists')
        print('binary_R300.arff does not already exist')
        tr_hw3.create_arff_data_b('R')
        self.assertTrue(os.path.exists('arff/binary_R50.arff'), 'R50.arff was not created')
        print('binary_R50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_R300.arff'), 'R300.arff was not created')
        print('binary_R300.arff exists')
        with open('arff/binary_R50.arff') as f1:
            with open('test_files/binary_R50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R50.arff does not have the correct info')
        with open('arff/binary_R300.arff') as f1:
            with open('test_files/binary_R300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2, 'R300.arff does not have the correct info')
        print('Created files are correct')
        print('Finished test_create_arff_b_R')


if __name__ == '__main__':
    sys.stdout = open('tests.log', 'w')
    test = unittest.TestLoader().loadTestsFromTestCase(TestHW3)
    unittest.TextTestRunner(stream=sys.stdout).run(test)
