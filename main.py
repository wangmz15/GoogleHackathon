from Splendor import Splendor
import sys, json
from utils import checkMoveValid

def main(status):
    # my code here
    splendor = Splendor(status)
    splendor.findAllOper()
    best_oper = splendor.evalAllOper()
    print(json.dumps(best_oper))

if __name__ == "__main__":
    status = ''.join(sys.stdin.readlines())
    main(status)
