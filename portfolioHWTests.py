import unittest
import portfolioHW

class portfolioTest(unittest.TestCase):

    def testCashBalance(self):

        portfolio = portfolioHW.Portfolio()
        portfolio.addCash(500)
        portfolio.withdrawCash(200)

        self.assertEqual(300, portfolio.cash)

if __name__ == "__main__":
    unittest.main()
