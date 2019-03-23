# API FOR SPLENDER

### checkMoveValid

检查步骤合法性

#### input: 

input（原来的输入），move（某一个决策）

##### example:

{

​	input: 略

​	move: {"get_two_same_color_gems" : "red"}

}



#### return: 

bool（当前决策是否合法）



### findAllOper

找到所有的决策

#### input:

null

#### return:

list（所有决策）

##### example:

[

​	{"get_two_same_color_gems" : "red"},

​	{"get_two_same_color_gems" : "blue"},

​	{"reserve_card" : {

​		"card" : { "color" : "blue", 

​		"costs" : [ { "color" : "blue", "count" : 5 } ], 

​		"level" : 2, "score" : 2}

​		}

​	},

​	{"get_different_color_gems" : [ "red", "green", "blue" ]},

​	{"reserve_card" : { "level" : 1 }},

​	{"purchase_card" : {

​		"color" : "black", 

​		"costs" : [ { "color" : "green", "count" : 5 }, { "color" : "red", "count" : 3 }], 

​		"level" : 2, 

​		"score" : 2}

​	}

]





### evalAllOper：

估价函数

#### input: 

list ：操作列表

##### example:

[

​	{"reserve_card" : {

​		"card" : { 

​			"color" : "blue", 

​			"costs" : [ { "color" : "blue", "count" : 5 } ], 

​			"level" : 2, "score" : 2}

​		}

​	},

​	{"reserve_card" : {

​		"card" : { 

​			"color" : "blue", 

​			"costs" : [ { "color" : "blue", "count" : 5 } ], 

​			"level" : 2, "score" : 2}

​		}

​	},

​	{"get_two_same_color_gems" : "blue"},

​	{"purchase_card" : {

​		"color" : "black", 

​		"costs" : [ { "color" : "green", "count" : 5 }, { "color" : "red", "count" : 3 }], 

​		"level" : 2, 

​		"score" : 2}

​	}

]

#### return:

返回最优步骤

{"reserve_card" : {

​	"card" : { 

​		"color" : "blue", 

​		"costs" : [ { "color" : "blue", "count" : 5 } ], 

​		"level" : 2, "score" : 2}

​	}

}