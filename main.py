from Splendor import Splendor
import sys, json
from utils import checkMoveValid
import random
def main(status):
	# my code here
	
	# open("before_output.txt"+str(index), "w").write("before")
	splendor = Splendor(status)
	# open("initial.txt"+str(index), "w").write("initial")
	splendor.findAllOper()
	# open("findall.txt"+str(index), "w").write("findall")
	best_oper = splendor.evalAllOper()
	# open("best.txt"+str(index), "w").write("best")
	# index = random.choice(range(100))
	# index = json.loads(status)['round']
	# open("output.txt"+str(index), "w").write(json.dumps(best_oper))
	print(json.dumps(best_oper))
	# print(json.dumps({"get_two_same_color_gems": "blue"}))

if __name__ == "__main__":
    status = ''.join(sys.stdin.readlines())
	# status=sys.argv[1]

	# open("indput111.txt", "w").write(status)
    main(status)
