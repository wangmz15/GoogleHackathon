import json
import sys
import random


class Splendor(object):
	def __init__(self):
		self.status = json.loads(''.join(sys.stdin.readlines()))

		self.moveOption= ['get_different_color_gems',  "get_two_same_color_gems" \
					  "reserve_card" , "purchase_card" ,  "noble",
 					  "purchase_reserved_card" , "nobel"]


	def findAllOper(self):

		
		pass


	def evalAllOper(self, operations):

		# current_score = self.status.get('playerName','')
		def opr_to_key(opr):

			value = random.choice(range(len(operations)))
            
            return (value)
        operations.sort(key = lambda opr:opr_to_key(opr), reverse = True)

        return operations[0]


