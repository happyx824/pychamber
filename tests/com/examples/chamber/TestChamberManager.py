'''
Created on 31 Mar 2020

@author:     Simon M.C.Yuen
@contact:    simoncpeg@gmail.com
'''
import unittest
from com.examples.chamber.components.ChamberManager import ChamberManager


class TestChamberManager(unittest.TestCase):

    def testMove1(self):
        chamberManager = ChamberManager(1, 'L.R')
    
        self.assertEqual([True, False, False], chamberManager.leftwardParticles)
        self.assertEqual([False, False, True], chamberManager.rightwardParticles)
       
        chamberManager.move()
        self.assertEqual([False, False, False], chamberManager.leftwardParticles)
        self.assertEqual([False, False, False], chamberManager.rightwardParticles)

    def testMove2(self):
        chamberManager = ChamberManager(2, 'R....L')
    
        self.assertEqual([False, False, False, False, False, True], chamberManager.leftwardParticles)
        self.assertEqual([True, False, False, False, False, False], chamberManager.rightwardParticles)
       
        chamberManager.move()
        self.assertEqual([False, False, False, True, False, False], chamberManager.leftwardParticles)
        self.assertEqual([False, False, True, False, False, False], chamberManager.rightwardParticles)

        chamberManager.move()
        self.assertEqual([False, True, False, False, False, False], chamberManager.leftwardParticles)
        self.assertEqual([False, False, False, False, True, False], chamberManager.rightwardParticles)

        chamberManager.move()
        self.assertEqual([False, False, False, False, False, False], chamberManager.leftwardParticles)
        self.assertEqual([False, False, False, False, False, False], chamberManager.rightwardParticles)

    def testIsEmptyChamber(self):
        chamberManager = ChamberManager(1, '...')
        self.assertEqual(True, chamberManager.isEmptyChamber())
        
        chamberManager = ChamberManager(3, 'R.L')
        self.assertEqual(False, chamberManager.isEmptyChamber())
        
        chamberManager.move()
        self.assertEqual(True, chamberManager.isEmptyChamber())
    
    def testGetParticleLocation(self):
        chamberManager = ChamberManager(1, '...')
        self.assertEqual('...', chamberManager.getParticleLocation())
        
        chamberManager = ChamberManager(1, 'R.L')
        self.assertEqual('X.X', chamberManager.getParticleLocation())
        
        chamberManager.move()
        self.assertEqual('.X.', chamberManager.getParticleLocation())
    
    def testAnimate0(self):
        chamberManager = ChamberManager(2, '..R....')
        actual = chamberManager.animate()
        expected = ["..X....",
                    "....X..",
                    "......X",
                    "......."]
        self.assertListEqual(expected, actual, 'animate particle location check')

    def testAnimate1(self):
        chamberManager = ChamberManager(3, 'RR..LRL')
        actual = chamberManager.animate()
        expected = ["XX..XXX",
                     ".X.XX..",
                     "X.....X",
                     "......."]
        self.assertListEqual(expected, actual, 'animate particle location check')

    def testAnimate2(self):
        chamberManager = ChamberManager(2, 'LRLR.LRLR')
        actual = chamberManager.animate()
        expected = ["XXXX.XXXX",
                     "X..X.X..X",
                     ".X.X.X.X.",
                     ".X.....X.",
                     "........."]
        self.assertListEqual(expected, actual, 'animate particle location check')

    def testAnimate3(self):
        chamberManager = ChamberManager(10, 'RLRLRLRLRL')
        actual = chamberManager.animate()
        expected = ["XXXXXXXXXX",
                    ".........."]
        self.assertListEqual(expected, actual, 'animate particle location check')

    def testAnimate4(self):
        chamberManager = ChamberManager(1, '...')
        actual = chamberManager.animate()
        expected = ["..."]
        self.assertListEqual(expected, actual, 'animate particle location check')

    def testAnimate5(self):
        chamberManager = ChamberManager(1, 'LRRL.LR.LRR.R.LRRL.')
        actual = chamberManager.animate()
        expected = ["XXXX.XX.XXX.X.XXXX.",
                     "..XXX..X..XX.X..XX.",
                     ".X.XX.X.X..XX.XX.XX",
                     "X.X.XX...X.XXXXX..X",
                     ".X..XXX...X..XX.X..",
                     "X..X..XX.X.XX.XX.X.",
                     "..X....XX..XX..XX.X",
                     ".X.....XXXX..X..XX.",
                     "X.....X..XX...X..XX",
                     ".....X..X.XX...X..X",
                     "....X..X...XX...X..",
                     "...X..X.....XX...X.",
                     "..X..X.......XX...X",
                     ".X..X.........XX...",
                     "X..X...........XX..",
                     "..X.............XX.",
                     ".X...............XX",
                     "X.................X",
                     "..................."]
        self.assertListEqual(expected, actual, 'animate particle location check')
        
if __name__ == "__main__":
    unittest.main()
