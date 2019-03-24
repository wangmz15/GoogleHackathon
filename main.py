from Splendor import Splendor
import sys, json
from utils import checkMoveValid

def main(status):
    # my code here
    splendor = Splendor(status)
    splendor.findAllOper()
    best_oper = splendor.evalAllOper()
    print(json.dumps(best_oper))
    # print(json.dumps({"get_two_same_color_gems": "blue"}))

if __name__ == "__main__":
	
	status=sys.argv[1]
    #status=''.join(open("input2.txt",'r',encoding='utf-8').readlines())
    main(status)
    # status = ''.join(sys.stdin.readlines())
    # main(status)
    # print('{\"get_two_same_color_gems\": \"blue\"}')
