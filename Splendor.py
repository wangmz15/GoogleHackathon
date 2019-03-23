import json
import sys
from utils import *
import random
from collections import defaultdict

class Splendor(object):
	def __init__(self, status):

		#####################################################
		self.benefit_weight = 0.7
		self.epoch_threshold = 3




		######################################################
		self.status = json.loads(status)
		self.AllOperList = []
		self.moveOption= ['get_different_color_gems', "get_two_same_color_gems" , "reserve_card" , "purchase_card" ,  "noble", "purchase_reserved_card"]

	def checkNobleCard(self):
		self.nobel_benefit = {'red': 0, 'gold': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
		for nobel_card in self.status['nobles']:
			for item in nobel_card['requirements']:
				self.nobel_benefit[item['color']] += item['count']
		
		return 


	
    def calDevRound(self,cards):
        player = self.status['playerName']
        my_table = None
        for i in self.status['players']:
            if i['name'] == player:
                my_table = i
        check_gem_init = {'red': 0, 'gold': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
        check_gem=check_gem_init
        if 'purchased_cards' in my_table:
            for cards in my_table['purchased_cards']:
                check_gem[cards['color']] += 1
        ret=[]
        for card in cards:
            costs = []
            steps = 0
            for gems in card['costs']:
                if gems['count'] > 0:
                    costs.append(max(gems['count'] - check_gem[gems['color']], 0))
            costs = np.array(costs)
            while sum(costs > 0) > 1:
                costs = -np.sort(-costs)
                for i in range(min(3,costs.shape[0])):
                    if costs[i] == 0:
                        break
                    costs[i] -= 1
                steps += 1
            costs = -np.sort(-costs)
            steps += (costs[0] + 1) // 2
            ret.append(steps)
        return ret

    def checkDevCard(self,set):
        check_gem_init = {'red': 0, 'gold': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
        check_gem = check_gem_init
        for card in set:
            check_gem[card['color']]+=1
        return check_gem

	def evaluateDevDistance(self, validDevSet, gemState):



		pass


	
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
			# self.AllOperList.append(dict_output_temp)

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
		playerName = self.status['playerName']
		my_reserved_cards = []
		for player in self.status['players']:
			if player['name'] == playerName:
				if 'reserved_cards' in player:
					my_reserved_cards = player['reserved_cards']
				break
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
			# try:
			if not checkMoveValid(self.status,oper):
				self.AllOperList.remove(oper)
			# except:
				# print oper

	def calDevRound(self, cards):
		player = self.status['playerName']
		my_table = None
		for i in self.status['players']:
			if i['name'] == player:
				my_table = i
		check_gem_init = {'red': 0, 'gold': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
		check_gem = check_gem_init
		if 'purchased_cards' in my_table:
			for cards in my_table['purchased_cards']:
				check_gem[cards['color']] += 1
		ret = []
		for card in cards:
			costs = []
			steps = 0
			for gems in card['costs']:
				if gems['count'] > 0:
					costs.append(max(gems['count'] - check_gem[gems['color']], 0))
			costs = np.array(costs)
			while sum(costs > 0) > 1:
				costs = -np.sort(-costs)
				for i in range(min(3, costs.shape[0])):
					if costs[i] == 0:
						break
					costs[i] -= 1
				steps += 1
			costs = -np.sort(-costs)
			steps += (costs[0] + 1) // 2
			ret.append(steps)
		return ret

	def checkDevCard(self, set):
		check_gem_init = {'red': 0, 'gold': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
		check_gem = check_gem_init
		for card in set:
			check_gem[card['color']] += 1
		return check_gem

