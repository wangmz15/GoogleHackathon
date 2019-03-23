from Splendor import Splendor
import sys, json
from utils import checkMoveValid

def main(status):
    # my code here
    splendor = Splendor(status)
    all_valid_oper = splendor.findAllOper()
    best_oper = splendor.evalAllOper(all_valid_oper)
    sys.stdout.write(best_oper)

if __name__ == "__main__":
    status = ''.join(sys.stdin.readlines())
    main(status)
