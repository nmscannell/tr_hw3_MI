import tr_hw3
import unittest
import logging as log
import sys
import glob
import os


class TestHW3(unittest.TestCase):

    def tearDown(self):
        print('Tear Down: removing any created files')
        for f in glob.glob('arff/*'):
            os.remove(f)
        for f in glob.glob('scores/*'):
            os.remove(f)
        for f in glob.glob('data/*.data'):
            os.remove(f)

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
        pass
'''
    def test_calc_mi(self):
        pass

    def test_mi_features_H(self):
        pass

    def test_mi_features_N(self):
        pass

    def test_mi_features_D(self):
        pass

    def test_mi_features_E(self):
        pass

    def test_mi_features_I(self):
        pass

    def test_mi_features_O(self):
        pass

    def test_mi_features_R(self):
        pass

    def test_build_binary_dataset_H(self):
        pass

    def test_build_binary_dataset_N(self):
        pass

    def test_build_binary_dataset_D(self):
        pass

    def test_build_binary_dataset_E(self):
        pass

    def test_build_binary_dataset_I(self):
        pass

    def test_build_binary_dataset_O(self):
        pass

    def test_build_binary_dataset_R(self):
        pass

    def test_create_arff_a_H(self):
        pass

    def test_create_arff_a_N(self):
        pass

    def test_create_arff_a_D(self):
        pass

    def test_create_arff_a_E(self):
        pass

    def test_create_arff_a_I(self):
        pass

    def test_create_arff_a_O(self):
        pass

    def test_create_arff_a_R(self):
        pass

    def test_create_arff_b_H(self):
        pass

    def test_create_arff_b_N(self):
        pass

    def test_create_arff_b_D(self):
        pass

    def test_create_arff_b_E(self):
        pass

    def test_create_arff_b_I(self):
        pass

    def test_create_arff_b_O(self):
        pass

    def test_create_arff_b_R(self):
        pass

    def test_mi_features_H_no_setup(self):
        pass

    def test_build_binary_dataset_H_no_setup(self):
        pass

    def test_create_arff_a_H_no_setup(self):
        pass

    def test_create_arff_b_H_no_setup(self):
        pass
'''

if __name__ == '__main__':
    sys.stdout = open('tests.log', 'w')
    test = unittest.TestLoader().loadTestsFromTestCase(TestHW3)
    unittest.TextTestRunner(stream=sys.stdout).run(test)
