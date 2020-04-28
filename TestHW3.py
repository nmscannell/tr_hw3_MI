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
        result = tr_hw3.parse_doc(s, True)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result)
        print('Finished test_parse_simple_sentence')

    def test_parse_med_sentence(self):
        s = "This, is a, med/intermediate 'level-difficulty' sentence."
        tok = ['this', 'is', 'a', 'med', 'intermediate', 'level', 'difficulty', 'sentence']
        print('Running test_parse_med_sentence')
        print('sentence: ', s)
        result = tr_hw3.parse_doc(s)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result)
        print('Finished test_parse_med_sentence')

    def test_parse_complex_sentence(self):
        s = "This, is a, far](more 'difficult' doc. # it contains% odd google.com term& can't"
        tok = ['this', 'is', 'a', 'far', 'more', 'difficult', 'doc', 'it', 'contains%', 'odd', 'google.com', 'term', "can't"]
        print('Running test_parse_complex_sentence')
        print('sentence: ', s)
        result = tr_hw3.parse_doc(s)
        print('result: ', end='')
        print(result)
        self.assertEqual(tok, result)
        print('Finished test_parse_complex_sentence')

    def test_process_data(self):
        print('Running test_process_data')
        tr_hw3.process_data(True)
        print('Finished test_process_data')

    def test_mi_features_H(self):
        print('Running test_mi_features_H')
        self.assertFalse(os.path.exists('scores/H.scores'))
        print('H.scores does not already exist')
        tr_hw3.mi_features('H', True)
        self.assertTrue(os.path.exists('scores/H.scores'))
        print('H.scores exists')
        with open('scores/H.scores') as f1:
            with open('test_files/H.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_H')

    def test_mi_features_N(self):
        print('Running test_mi_features_N')
        self.assertFalse(os.path.exists('scores/N.scores'))
        print('N.scores does not already exist')
        tr_hw3.mi_features('N', True)
        self.assertTrue(os.path.exists('scores/N.scores'))
        print('N.scores exists')
        with open('scores/N.scores') as f1:
            with open('test_files/N.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_N')

    def test_mi_features_D(self):
        print('Running test_mi_features_D')
        self.assertFalse(os.path.exists('scores/D.scores'))
        print('D.scores does not already exist')
        tr_hw3.mi_features('D', True)
        self.assertTrue(os.path.exists('scores/D.scores'))
        print('D.scores exists')
        with open('scores/D.scores') as f1:
            with open('test_files/D.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_D')

    def test_mi_features_E(self):
        print('Running test_mi_features_E')
        self.assertFalse(os.path.exists('scores/E.scores'))
        print('E.scores does not already exist')
        tr_hw3.mi_features('E', True)
        self.assertTrue(os.path.exists('scores/E.scores'))
        print('E.scores exists')
        with open('scores/E.scores') as f1:
            with open('test_files/E.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_E')

    def test_mi_features_I(self):
        print('Running test_mi_features_I')
        self.assertFalse(os.path.exists('scores/I.scores'))
        print('I.scores does not already exist')
        tr_hw3.mi_features('I', True)
        self.assertTrue(os.path.exists('scores/I.scores'))
        print('I.scores exists')
        with open('scores/I.scores') as f1:
            with open('test_files/I.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_I')

    def test_mi_features_O(self):
        print('Running test_mi_features_O')
        self.assertFalse(os.path.exists('scores/O.scores'))
        print('O.scores does not already exist')
        tr_hw3.mi_features('O', True)
        self.assertTrue(os.path.exists('scores/O.scores'))
        print('O.scores exists')
        with open('scores/O.scores') as f1:
            with open('test_files/O.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_O')

    def test_mi_features_R(self):
        print('Running test_mi_features_R')
        self.assertFalse(os.path.exists('scores/R.scores'))
        print('R.scores does not already exist')
        tr_hw3.mi_features('R', True)
        self.assertTrue(os.path.exists('scores/R.scores'))
        print('R.scores exists')
        with open('scores/R.scores') as f1:
            with open('test_files/R.scores') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_mi_features_R')

    def test_calc_mi(self):
        pass

    def test_build_binary_dataset_H(self):
        print('Running test_build_binary_dataset_H')
        self.assertFalse(os.path.exists('data/H50.data'))
        print('H50.data does not already exist')
        self.assertFalse(os.path.exists('data/H300.data'))
        print('H300.data does not already exist')
        tr_hw3.build_binary_datasets('H', True)
        self.assertTrue(os.path.exists('data/H50.data'))
        print('H50.data exists')
        self.assertTrue(os.path.exists('data/H300.data'))
        print('H300.data exists')
        with open('data/H50.data') as f1:
            with open('test_files/H50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/H300.data') as f1:
            with open('test_files/H300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_H')

    def test_build_binary_dataset_N(self):
        print('Running test_build_binary_dataset_N')
        self.assertFalse(os.path.exists('data/N50.data'))
        print('N50.data does not already exist')
        self.assertFalse(os.path.exists('data/N300.data'))
        print('N300.data does not already exist')
        tr_hw3.build_binary_datasets('N', True)
        self.assertTrue(os.path.exists('data/N50.data'))
        print('N50.data exists')
        self.assertTrue(os.path.exists('data/N300.data'))
        print('N300.data exists')
        with open('data/N50.data') as f1:
            with open('test_files/N50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/N300.data') as f1:
            with open('test_files/N300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_N')

    def test_build_binary_dataset_D(self):
        print('Running test_build_binary_dataset_D')
        self.assertFalse(os.path.exists('data/D50.data'))
        print('D50.data does not already exist')
        self.assertFalse(os.path.exists('data/D300.data'))
        print('D300.data does not already exist')
        tr_hw3.build_binary_datasets('D', True)
        self.assertTrue(os.path.exists('data/D50.data'))
        print('D50.data exists')
        self.assertTrue(os.path.exists('data/D300.data'))
        print('D300.data exists')
        with open('data/D50.data') as f1:
            with open('test_files/D50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/D300.data') as f1:
            with open('test_files/D300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_D')

    def test_build_binary_dataset_E(self):
        print('Running test_build_binary_dataset_E')
        self.assertFalse(os.path.exists('data/E50.data'))
        print('E50.data does not already exist')
        self.assertFalse(os.path.exists('data/E300.data'))
        print('E300.data does not already exist')
        tr_hw3.build_binary_datasets('E', True)
        self.assertTrue(os.path.exists('data/E50.data'))
        print('E50.data exists')
        self.assertTrue(os.path.exists('data/E300.data'))
        print('E300.data exists')
        with open('data/E50.data') as f1:
            with open('test_files/E50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/E300.data') as f1:
            with open('test_files/E300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_E')

    def test_build_binary_dataset_I(self):
        print('Running test_build_binary_dataset_I')
        self.assertFalse(os.path.exists('data/I50.data'))
        print('I50.data does not already exist')
        self.assertFalse(os.path.exists('data/I300.data'))
        print('I300.data does not already exist')
        tr_hw3.build_binary_datasets('I', True)
        self.assertTrue(os.path.exists('data/I50.data'))
        print('I50.data exists')
        self.assertTrue(os.path.exists('data/I300.data'))
        print('I300.data exists')
        with open('data/I50.data') as f1:
            with open('test_files/I50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/I300.data') as f1:
            with open('test_files/I300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_I')

    def test_build_binary_dataset_O(self):
        print('Running test_build_binary_dataset_O')
        self.assertFalse(os.path.exists('data/O50.data'))
        print('O50.data does not already exist')
        self.assertFalse(os.path.exists('data/O300.data'))
        print('O300.data does not already exist')
        tr_hw3.build_binary_datasets('O', True)
        self.assertTrue(os.path.exists('data/O50.data'))
        print('O50.data exists')
        self.assertTrue(os.path.exists('data/O300.data'))
        print('O300.data exists')
        with open('data/O50.data') as f1:
            with open('test_files/O50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/O300.data') as f1:
            with open('test_files/O300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_O')

    def test_build_binary_dataset_R(self):
        print('Running test_build_binary_dataset_R')
        self.assertFalse(os.path.exists('data/R50.data'))
        print('R50.data does not already exist')
        self.assertFalse(os.path.exists('data/R300.data'))
        print('R300.data does not already exist')
        tr_hw3.build_binary_datasets('R', True)
        self.assertTrue(os.path.exists('data/R50.data'))
        print('R50.data exists')
        self.assertTrue(os.path.exists('data/R300.data'))
        print('R300.data exists')
        with open('data/R50.data') as f1:
            with open('test_files/R50.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('data/R300.data') as f1:
            with open('test_files/R300.data') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_build_binary_dataset_R')

    def test_create_arff_a_H(self):
        print('Running test_create_arff_a_H')
        self.assertFalse(os.path.exists('arff/multi_H.arff'))
        print('multi_H.arff does not already exist')
        tr_hw3.create_arff_data_a('H', True)
        self.assertTrue(os.path.exists('arff/multi_H.arff'))
        print('multi_H.arff exists')
        with open('arff/multi_H.arff') as f1:
            with open('test_files/multi_H.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_H')

    def test_create_arff_a_N(self):
        print('Running test_create_arff_a_N')
        self.assertFalse(os.path.exists('arff/multi_N.arff'))
        print('multi_N.arff does not already exist')
        tr_hw3.create_arff_data_a('N', True)
        self.assertTrue(os.path.exists('arff/multi_N.arff'))
        print('multi_N.arff exists')
        with open('arff/multi_N.arff') as f1:
            with open('test_files/multi_N.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_N')

    def test_create_arff_a_D(self):
        print('Running test_create_arff_a_D')
        self.assertFalse(os.path.exists('arff/multi_D.arff'))
        print('multi_D.arff does not already exist')
        tr_hw3.create_arff_data_a('D', True)
        self.assertTrue(os.path.exists('arff/multi_D.arff'))
        print('multi_D.arff exists')
        with open('arff/multi_D.arff') as f1:
            with open('test_files/multi_D.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_D')

    def test_create_arff_a_E(self):
        print('Running test_create_arff_a_E')
        self.assertFalse(os.path.exists('arff/multi_E.arff'))
        print('multi_E.arff does not already exist')
        tr_hw3.create_arff_data_a('E', True)
        self.assertTrue(os.path.exists('arff/multi_E.arff'))
        print('multi_E.arff exists')
        with open('arff/multi_E.arff') as f1:
            with open('test_files/multi_E.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_E')

    def test_create_arff_a_I(self):
        print('Running test_create_arff_a_I')
        self.assertFalse(os.path.exists('arff/multi_I.arff'))
        print('multi_I.arff does not already exist')
        tr_hw3.create_arff_data_a('I', True)
        self.assertTrue(os.path.exists('arff/multi_I.arff'))
        print('multi_I.arff exists')
        with open('arff/multi_I.arff') as f1:
            with open('test_files/multi_I.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_I')

    def test_create_arff_a_O(self):
        print('Running test_create_arff_a_O')
        self.assertFalse(os.path.exists('arff/multi_O.arff'))
        print('multi_O.arff does not already exist')
        tr_hw3.create_arff_data_a('O', True)
        self.assertTrue(os.path.exists('arff/multi_O.arff'))
        print('multi_O.arff exists')
        with open('arff/multi_O.arff') as f1:
            with open('test_files/multi_O.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_O')

    def test_create_arff_a_R(self):
        print('Running test_create_arff_a_R')
        self.assertFalse(os.path.exists('arff/multi_R.arff'))
        print('multi_R.arff does not already exist')
        tr_hw3.create_arff_data_a('R', True)
        self.assertTrue(os.path.exists('arff/multi_R.arff'))
        print('multi_R.arff exists')
        with open('arff/multi_R.arff') as f1:
            with open('test_files/multi_R.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created file is correct')
        print('Finished test_create_arff_a_R')

    def test_create_arff_b_H(self):
        print('Running test_create_arff_b_H')
        self.assertFalse(os.path.exists('arff/binary_H50.arff'))
        print('binary_H50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_H300.arff'))
        print('binary_H300.arff does not already exist')
        tr_hw3.create_arff_data_b('H', True)
        self.assertTrue(os.path.exists('arff/binary_H50.arff'))
        print('binary_H50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_H300.arff'))
        print('binary_H300.arff exists')
        with open('arff/binary_H50.arff') as f1:
            with open('test_files/binary_H50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_H300.arff') as f1:
            with open('test_files/binary_H300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_H')

    def test_create_arff_b_N(self):
        print('Running test_create_arff_b_N')
        self.assertFalse(os.path.exists('arff/binary_N50.arff'))
        print('binary_N50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_N300.arff'))
        print('binary_N300.arff does not already exist')
        tr_hw3.create_arff_data_b('N', True)
        self.assertTrue(os.path.exists('arff/binary_N50.arff'))
        print('binary_N50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_N300.arff'))
        print('binary_N300.arff exists')
        with open('arff/binary_N50.arff') as f1:
            with open('test_files/binary_N50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_N300.arff') as f1:
            with open('test_files/binary_N300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_N')

    def test_create_arff_b_D(self):
        print('Running test_create_arff_b_D')
        self.assertFalse(os.path.exists('arff/binary_D50.arff'))
        print('binary_D50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_D300.arff'))
        print('binary_D300.arff does not already exist')
        tr_hw3.create_arff_data_b('D', True)
        self.assertTrue(os.path.exists('arff/binary_D50.arff'))
        print('binary_D50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_D300.arff'))
        print('binary_D300.arff exists')
        with open('arff/binary_D50.arff') as f1:
            with open('test_files/binary_D50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_D300.arff') as f1:
            with open('test_files/binary_D300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_D')

    def test_create_arff_b_E(self):
        print('Running test_create_arff_b_E')
        self.assertFalse(os.path.exists('arff/binary_E50.arff'))
        print('binary_E50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_E300.arff'))
        print('binary_E300.arff does not already exist')
        tr_hw3.create_arff_data_b('E', True)
        self.assertTrue(os.path.exists('arff/binary_E50.arff'))
        print('binary_E50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_E300.arff'))
        print('binary_E300.arff exists')
        with open('arff/binary_E50.arff') as f1:
            with open('test_files/binary_E50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_E300.arff') as f1:
            with open('test_files/binary_E300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_E')

    def test_create_arff_b_I(self):
        print('Running test_create_arff_b_I')
        self.assertFalse(os.path.exists('arff/binary_I50.arff'))
        print('binary_I50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_I300.arff'))
        print('binary_I300.arff does not already exist')
        tr_hw3.create_arff_data_b('I', True)
        self.assertTrue(os.path.exists('arff/binary_I50.arff'))
        print('binary_I50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_I300.arff'))
        print('binary_I300.arff exists')
        with open('arff/binary_I50.arff') as f1:
            with open('test_files/binary_I50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_I300.arff') as f1:
            with open('test_files/binary_I300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_I')

    def test_create_arff_b_O(self):
        print('Running test_create_arff_b_O')
        self.assertFalse(os.path.exists('arff/binary_O50.arff'))
        print('binary_O50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_O300.arff'))
        print('binary_O300.arff does not already exist')
        tr_hw3.create_arff_data_b('O', True)
        self.assertTrue(os.path.exists('arff/binary_O50.arff'))
        print('binary_O50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_O300.arff'))
        print('binary_O300.arff exists')
        with open('arff/binary_O50.arff') as f1:
            with open('test_files/binary_O50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_O300.arff') as f1:
            with open('test_files/binary_O300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_O')

    def test_create_arff_b_R(self):
        print('Running test_create_arff_b_R')
        self.assertFalse(os.path.exists('arff/binary_R50.arff'))
        print('binary_R50.arff does not already exist')
        self.assertFalse(os.path.exists('arff/binary_R300.arff'))
        print('binary_R300.arff does not already exist')
        tr_hw3.create_arff_data_b('R', True)
        self.assertTrue(os.path.exists('arff/binary_R50.arff'))
        print('binary_R50.arff exists')
        self.assertTrue(os.path.exists('arff/binary_R300.arff'))
        print('binary_R300.arff exists')
        with open('arff/binary_R50.arff') as f1:
            with open('test_files/binary_R50.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        with open('arff/binary_R300.arff') as f1:
            with open('test_files/binary_R300.arff') as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                self.assertEqual(lines1, lines2)
        print('Created files are correct')
        print('Finished test_create_arff_b_R')


if __name__ == '__main__':
    sys.stdout = open('tests.log', 'w')
    test = unittest.TestLoader().loadTestsFromTestCase(TestHW3)
    unittest.TextTestRunner(stream=sys.stdout).run(test)
