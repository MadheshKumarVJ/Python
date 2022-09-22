import subtraction,unittest

class Testing(unittest.TestCase):
    known_val=(((2,2),0),((2,1),1))

    def test_check(self):
        for inp,out in self.known_val:
            res = subtraction.sub(inp[0],inp[1])
            self.assertEqual(out,res)
if __name__=='__main__':
    unittest.main()