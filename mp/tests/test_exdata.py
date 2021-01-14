import unittest
from lab.exdata import ExData


class TestExData(unittest.TestCase):
    def setUp(self):
        self.exd = ExData("tests/test.json")

    def test_get_key_list(self):
        kl = self.exd.get_key_list()
        self.assertEqual("key1", kl[0])
        self.assertEqual("key2", kl[1])
        self.assertEqual("key3", kl[2])

    def test_get_data(self):
        # 正常系
        d1 = self.exd.get_data("key1")
        d2 = self.exd.get_data("key2")
        self.assertEqual(0.00, d1["v"][0])
        self.assertEqual(0.001, d1["i"][0])
        self.assertEqual(0.00, d2["v"][0])
        self.assertEqual(0.006, d2["i"][0])
        # 異常系
        d3 = self.exd.get_data("notexist")
        self.assertIsNone(d3)

    def test_get_voltage_list(self):
        # 正常系
        expected = [0.00, 0.50, 1.00, 1.50, 2.00]
        vl = self.exd.get_voltage_list("key1")
        for idx, v in enumerate(vl):
            self.assertEqual(expected[idx], v)
        # 異常系
        vle = self.exd.get_voltage_list("notexist")
        self.assertIsNone(vle)

    def test_get_current_list(self):
        # 正常系
        expected = [0.001, 0.002, 0.003, 0.004, 0.005]
        il = self.exd.get_current_list("key1")
        for idx, i in enumerate(il):
            self.assertEqual(expected[idx], i)
        # 異常系
        ile = self.exd.get_current_list("notexist")
        self.assertIsNone(ile)

    def test_get_data_body(self):
        # 正常系
        d1 = self.exd.get_data_body("key1", 0)
        d2 = self.exd.get_data_body("key1", 1)
        self.assertEqual(0.00, d1[0])
        self.assertEqual(0.001, d1[1])
        self.assertEqual(0.50, d2[0])
        self.assertEqual(0.002, d2[1])
        # 異常系
        d3 = self.exd.get_data_body("notexist", 0)
        d4 = self.exd.get_data_body("key1", 5)
        d5 = self.exd.get_data_body("key1", -1)
        self.assertIsNone(d3)
        self.assertIsNone(d4)
        self.assertIsNone(d5)

    def test_find_currents_by_voltage(self):
        # 正常系
        cl = self.exd.find_currents_by_voltage("key3", 0.50)
        self.assertEqual(0.011, cl[0])
        self.assertEqual(0.013, cl[1])
        cl2 = self.exd.find_currents_by_voltage("key3", 2.00)
        self.assertEqual(0, len(cl2))
        # 異常系
        cl3 = self.exd.find_currents_by_voltage("noexist", 0.00)
        self.assertIsNone(cl3)


if __name__ == "__main__":
    unittest.main()
