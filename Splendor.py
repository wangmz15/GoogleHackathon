import json



class Splendor:
	def __init__(self, status):
		self.status = json.loads(status)

		self.moveOption= ['get_different_color_gems',  "get_two_same_color_gems" \
					  "reserve_card" , "purchase_card" ,  "noble", "purchase_reserved_card"]


	def findAllOper(self):

		
		pass


