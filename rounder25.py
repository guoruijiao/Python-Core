
def rounder25(amount):
    '''
    Return amount rounded UP to nearest
    quarter dollar.
        ...$1.89 becomes $2.00
        ...but $1.00/$1.25/$1.75/etc.
           remain unchanged
    '''
    dollars = int(amount)
    cents = round((amount - dollars) * 100)
    quarters = cents // 25
    if cents % 25:
        quarters += 1
    amount = dollars + 0.25 * quarters

    return amount

import unittest

class TestRounder25(unittest.TestCase):

  def setUp(self):
      print("\nSetting up a test.")

  def tearDown(self):
      print("Tearing down a test.")

  def test_roundup(self):
      self.assertEqual(rounder25(1.03), 1.25)
      self.assertEqual(rounder25(1.89), 2.00)

  def test_noround(self):
      self.assertEqual(rounder25(1.00), 1.00)
      self.assertEqual(rounder25(1.25), 1.25)
      self.assertEqual(rounder25(1.50), 1.50)
      self.assertEqual(rounder25(1.75), 1.75)

if __name__ == '__main__':
    unittest.main()
