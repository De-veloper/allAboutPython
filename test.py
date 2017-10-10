import argparse
 
parser = argparse.ArgumentParser(description='This does almost nothing')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
#parser.add_argument('-r', '--run', action='run', version='loading ...')
args = parser.parse_args()

print 'please add -h to see all the commands'