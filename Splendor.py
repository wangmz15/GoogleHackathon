import json
import sys
from utils import *
import random


class Splendor(object):
	def __init__(self, status):
		self.status = json.loads(status)
		self.AllOperList = []
		self.moveOption= ['get_different_color_gems',  "get_two_same_color_gems" \
					  "reserve_card" , "purchase_card" ,  "noble",
 					  "purchase_reserved_card" , "nobel"]

	def getNobleCard(self,move):
		pass

	def checkDevCard(self):
		
	def evalAllOper(self):
		operations = self.AllOperList
		def opr_to_key(opr):

			value = random.choice(range(100))
			
			return (value)
		operations.sort(key = lambda opr:opr_to_key(opr), reverse = True)

		return operations[0]


	def findDifferentColorGems(self):
		trueGems = []
		for gem in self.status["table"]["gems"]:
			if(gem["count"]>=1):
				trueGems.append(gem)
		for i in range(0,len(trueGems)):
			for j in range(i,len(trueGems)):
				for k in range(j,len(trueGems)):
					dict_output_temp = {}
					differentColorGems = []
					differentColorGems.append(trueGems[i]["color"])
					differentColorGems.append(trueGems[j]["color"])
					differentColorGems.append(trueGems[k]["color"])
					dict_output_temp["get_different_color_gems"] = differentColorGems
					self.AllOperList.append(dict_output_temp)
		return

	def findSameColorGems(self):
		trueGems = []
		for gem in self.status["table"]["gems"]:
			# print("gem:", gem)
			if(gem["count"]>=4):
				# print("gems:", gem)
				trueGems.append(gem)
		
		for gem in trueGems:
			dict_output_temp = {}
			dict_output_temp["get_two_same_color_gems"] = gem["color"]
			self.AllOperList.append(dict_output_temp)
		# print(self.AllOperList)
		return

	def findReserveCard(self):
		#reserve card on table
		for card in self.status["table"]["cards"]:
			dict_output_temp = {}
			dict_temp = {}
			dict_temp["card"] = card
			dict_output_temp["reserve_card"] = dict_temp
			self.AllOperList.append(dict_output_temp)
		#reserve card from top
		for level in range(1,4):
			dict_output_temp = {}
			dict_temp = {}
			dict_temp["level"] = level
			dict_output_temp["reserve_card"] = dict_temp
			self.AllOperList.append(dict_output_temp)

		for gem in self.status["table"]["gems"]:
			if(gem["color"]=="gold"):
				return True
			else:
				return False

	def findPurchaseCard(self):
		for card in self.status["table"]["cards"]:
			dict_output_temp = {}
			dict_output_temp["purchase_card"] = card
			self.AllOperList.append(dict_output_temp)
		return 

	def findPurchaseReservedCard(self):
		player = self.status['name']
		my_reserved_cards = self.status[player]['reserved_cards']
		for card in my_reserved_cards:
			dic= {}
			dic["purchase_reserved_card"] = card
			self.AllOperList.append(dic)
		return

	def findAllOper(self):
		self.findPurchaseCard()
		self.findReserveCard()
		self.findPurchaseReservedCard()
		self.findDifferentColorGems()
		self.findSameColorGems()

		for oper in self.AllOperList:
			if not checkMoveValid(self.status,oper):
				self.AllOperList.remove(oper)
		
		
		pass



