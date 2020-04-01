'''
AnimateApplication -- Animation of Particle Movement in a Chamber

@author:     Simon M.C.Yuen
@contact:    simoncpeg@gmail.com

'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from com.examples.chamber.components.ChamberManager import ChamberManager

__all__ = []
__version__ = 0.1
__date__ = '2020-03-31'
__updated__ = '2020-03-31'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class AnimationApplication(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(AnimationApplication).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_desc = '''%s

  Created by user_name on %s.
  A collection of particles is contained in a linear chamber. 
  They all have the same speed, but some are headed toward the right 
  and others are headed toward the left. These particles can pass 
  through each other without disturbing the motion of the particles, 
  so all the particles will leave the chamber relatively quickly.  
  
USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_desc, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-s", "--speed", dest="speed", type=int, required=True, help="set the speed of particles in chamber")
        parser.add_argument("-i", "--init",  dest="initialCondition", required=True, help="set the initial conditions of particles in chamber, like 'LR..RL'")
        
        args = parser.parse_args()
        speed = args.speed
        initialCondition = args.initialCondition
                
        print('Start Animation..')
        chamberManager = ChamberManager(speed, initialCondition)
        print (chamberManager.animate())

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
 
