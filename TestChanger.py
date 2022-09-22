import changeGiver,unittest

class Testing(unittest.TestCase):
    known_val=((5,4),(1,1))

    def test_check(self):
        for inp,out in self.known_val:
            res = changeGiver.giveChange(inp)
            res = len(res)
            self.assertEqual(out,res)
    def test_negative(self):
        '''"Enter valide amount if you change for negative values keep the money on the machine and ran away"'''
        self.assertRaises(changeGiver.NotIntegerError, changeGiver.invalideInput, -1)

if __name__=='__main__':
    unittest.main()
