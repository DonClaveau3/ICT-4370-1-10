"""
Author: Don Claveau
Create Date: 6/7/2019
Description: Tests for FormatHelper.py
Updates:

"""

import unittest
import FormatHelper

from datetime import date

class TestFormatHelper(unittest.TestCase):

    def test_DateFromMmddyyyyString_GivenValidString_ReturnsDate(self):
        #Arrange
        expected = date(1987,3,1)
        #Act/Assert
        actual = FormatHelper.DateFromMmddyyyyString("03/01/1987")
        self.assertEqual(expected, actual)
        actual = FormatHelper.DateFromMmddyyyyString("3/01/1987")
        self.assertEqual(expected, actual)
        actual = FormatHelper.DateFromMmddyyyyString("03/1/1987")
        self.assertEqual(expected, actual)

    def test_DateFromMmddyyyyString_GivenInvalidStrings_RaisesValueError(self):
        #Act/Assert
        with self.assertRaises(ValueError):
            FormatHelper.DateFromMmddyyyyString("invalidstring")
        with self.assertRaises(ValueError):
            FormatHelper.DateFromMmddyyyyString("15/03/1987")
        with self.assertRaises(ValueError):
            FormatHelper.DateFromMmddyyyyString("3151987")

    def test_DateFromYyyyMmDdString_GivenValidStrings_ReturnsDate(self):
        #Arrange
        expected = date(1987,3,1)
        #Act/Assert
        actual = FormatHelper.DateFromYyyyMmDdString("1987-03-01")
        self.assertEqual(expected, actual)
        actual = FormatHelper.DateFromYyyyMmDdString("1987-3-01")
        self.assertEqual(expected, actual)
        actual = FormatHelper.DateFromYyyyMmDdString("1987-03-1")
        self.assertEqual(expected, actual)

    def test_DateFromYyyyMmDdString_GivenInvalidStrings_RaisesValueError(self):
        #Act/Assert
        with self.assertRaises(ValueError):
            FormatHelper.DateFromYyyyMmDdString("invalidstring")
        with self.assertRaises(ValueError):
            FormatHelper.DateFromYyyyMmDdString("1987-15-03")
        with self.assertRaises(ValueError):
            FormatHelper.DateFromYyyyMmDdString("3151987")

    def test_AsPercent_GivenInt_ReturnsValueWithTwoDecimalsAsString(self):
        self.assertEqual("5.00%",FormatHelper.as_percent(5))

    def test_AsPercent_GivenFloatWith3Decimals_ReturnsValueRoundedToTwoDecimalsAsString(self):
        self.assertEqual("0.56%",FormatHelper.as_percent(0.555))

    def test_AsCurrency_GivenInt_ReturnsValueWithTwoDecimalsAsString(self):
        self.assertEqual("$5.00",FormatHelper.as_currency(5))

    def test_AsCurrency_GivenFloatWith3Decimals_ReturnsValueRoundedToTwoDecimalsAsString(self):
        self.assertEqual("$0.56",FormatHelper.as_currency(0.555))

    def test_AsCurrency_GivenNegativeValue_ReturnsAsStringWithMinusSignBeforeDollarSign(self):
        self.assertEqual("-$5.32",FormatHelper.as_currency(-5.32))
    

if __name__ == '__main__':
    unittest.main()