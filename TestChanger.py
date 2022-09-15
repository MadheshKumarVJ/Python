import changeGiver,unittest

class Testing(unittest.TestCase):
    known_val=((5,3),(1,1))

    def test_check(self):
        for inp,out in self.known_val:
            res = changeGiver.giveChange(inp)
            res = len(res)
            self.assertEqual(out,res)
if __name__=='__main__':
    unittest.main()