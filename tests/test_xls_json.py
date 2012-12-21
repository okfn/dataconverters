import os
from unittest import TestCase
import dataconverters.xls as xls


class TestCase(TestCase):

    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        testdata_path = os.path.dirname(here)
        self.testdata_path = os.path.join(testdata_path, 'testdata', 'xls')

    def test_1_convert_xls(self):
        """Test converting a XLS to JSON"""
        xlsfo = open(os.path.join(self.testdata_path, 'simple.xls'))
        headers, content = xls.xls_to_json(xlsfo)
        self.assertEqual([{"id": u"date"}, {"id": u"temperature"}, {"id":
                         u"place"}], headers)
        assert ({u"date": u"2011-01-03T00:00:00", u"place": u"Berkeley",
                "temperature": 5.0} in content)

    def test_3_header_type(self):
        """Test guessing header type"""
        xlsfo = open(os.path.join(self.testdata_path, 'simple.xls'))
        headers, content = xls.xls_to_json(xlsfo, header_type=1)
        self.assertEqual([{'type': 'String', 'id': u'date'}, {'id':
                         u'temperature', 'type': 'Integer'}, {'id': u'place',
                         'type': 'String'}], headers)
"""
    def test_2_convert_xlsx(self):
        ""Test converting a XLSX to JSON""
        res = self.app.get('/api/convert/json?url='
                           'http://resources.opendatalabs.org/u/nigelb/'
                           'data-converters/xls/simple.xlsx&type=xls&excel_type=xlsx')
        assert ('"headers": [{"id": "date"}, {"id": "temperature"}, {"id": '
                '"place"}]' in res.data)
        assert ('{"date": "2011-01-03T00:00:00", "place": "Berkeley", '
                '"temperature": 5}' in res.data) """
