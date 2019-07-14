import unittest

from doctest import Dict

class DictTest(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertIsInstance(d, Dict)


    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')


    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')


    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']


    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 在命令行通过参数-m unittest直接运行单元测试
# python -m unittest DictTest
if __name__ == '__main__':
    unittest.main()
