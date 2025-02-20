import sys
import pprint
from pollen import pollendata


if sys.argv[1] == 'tree':
    globals()['pollendata']().tree()
if sys.argv[1] == 'weed':
    globals()['pollendata']().weed()
if sys.argv[1] == 'grass':
    globals()['pollendata']().grass()
if sys.argv[1] == 'spores':
    globals()['pollendata']().spores()
    """print(globals())
    
    print(sys.argv[1])"""
   

#print(pollendata().tree())

print("JEREMY WAS HERE!")
