import json
import sys



class Splendor(object):
	def __init__(self):
		self.status = json.loads(''.join(sys.stdin.readlines()))

		self.moveOption= ['get_different_color_gems',  "get_two_same_color_gems" \
					  "reserve_card" , "purchase_card" ,  "noble",
 					  "purchase_reserved_card" , "nobel"]


	def findAllOper(self):

		
		pass


