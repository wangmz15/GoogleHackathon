# API FOR SPLENDER



## 找出所有可能的合理操作

### findAllOper

找到所有的决策

#### input

null

#### return

list（所有决策）

```
{
	"get_two_same_color_gems":[
		{"get_two_same_color_gems" : "red"},
		{"get_two_same_color_gems" : "blue"}
	],

	
	"reserve_card" :[
		{"reserve_card" : {
	​		"card" : { "color" : "blue", 
	​		"costs" : [ { "color" : "blue", "count" : 5 } ], 
	​		"level" : 2, "score" : 2}
	​		},
		{"reserve_card" : { "level" : 1 }},
	]
​	,
				

	"get_different_color_gems":[
		{"get_different_color_gems" : [ "red", "green", "blue" ]},

	]
	,


	"purchase_card" :[
		{"purchase_card" : {
​		"color" : "black", 
​		"costs" : [ { "color" : "green", "count" : 5 }, { "color" : "red", "count" : 3 }], 
​		"level" : 2, 
​		"score" : 2}
​		}
	]
	
​	
​		
​	
}
```



## 对所有操作估值，判断操作

### evalAllOper

总估价函数

##### 策略

- 购买场上发展卡 (chooseBuyDevOper)
- 购买保留卡
- 购买宝石
- 选择保留卡：（调用距离函数，选择最近的卡作为保留卡）
- 不操作（空json）

#### input

list ：操作列表

```
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
​		"costs" : [ { "color" : "green", "count" : 5 }, 
					{ "color" : "red", "count" : 3 }], 
​		"level" : 2, 
​		"score" : 2
		}
​	}
]
```

#### return:

返回最优步骤

```
{"reserve_card" : {
​	"card" : { 
​		"color" : "blue", 
​		"costs" : [ { "color" : "blue", "count" : 5 } ], 
​		"level" : 2, "score" : 2}
​	}
}
```



### chooseBuyDevOper

从所有买发展卡操作中，选择

1、3type中点数最高者 

2、否则选择点数最高者

#### input

list：3种红利集合，

dic：所有购买发展卡的操作

```
{
	'benefit_types': ['red','blue','white'],
	'purchase_dev_operation':[
        {
			"purchase_card" : {
				"color" : "black", 
				"costs" : [ { "color" : "green", "count" : 5 }, 
							{ "color" : "red", "count" : 3 }], 
				"level" : 2, 
				"score" : 2
			}
		},
		{
			"purchase_card" : {
				"color" : "white", 
				"costs" : [ { "color" : "green", "count" : 5 }, 
							{ "color" : "red", "count" : 3 }], 
				"level" : 2, 
				"score" : 2
			}
		}
	]
}
```

#### return

dic：最终选出的购买发展卡的操作

```
{
	"purchase_card" : {
        "color" : "white", 
        "costs" : [ { "color" : "green", "count" : 5 }, 
                { "color" : "red", "count" : 3 }], 
        "level" : 2, 
        "score" : 2
	}
}
```



### chooseBuyReservedOper

从所有买保留卡操作中，选择

1、3type中点数最高者 

2、否则选择点数最高者

#### input

list：3种红利集合，

dic：所有购买保留卡的操作

```
{
	'benefit_types': ['red','blue','white'],
	'purchase_reseved_operation':
	[
        {
            "purchase_reserved_card" : { 
                "color" : "black", 
                "costs" : [ { "color" : "green", "count" : 5}, 
                			{"color" : "red", "count" : 3}], 
                "level" : 2, 
                "score" : 2}}]
        },
        {
            "purchase_reserved_card" : { 
                "color" : "black", 
                "costs" : [ { "color" : "green", "count" : 5}, 
                			{"color" : "red", "count" : 3}], 
                "level" : 2, 
                "score" : 2}}]
        }
	]
}
```

#### return

dic：最终选出的购买保留卡的操作

```
{
    "purchase_reserved_card" : { 
    "color" : "black", 
    "costs" : [ { "color" : "green", "count" : 5}, 
    			{"color" : "red", "count" : 3}], 
    "level" : 2, 
    "score" : 2}}]
}
```



### chooseBuyGemsOper

对于【发展卡和保留卡】都调用countDevRound 筛掉round>4的【发展卡保留卡】= 剩下的卡 

min_distance

min_oper

for oper in 剩下的操作：

​	distance = evalGemDistance( 剩下的卡,  oper之后的【红利+宝石】）

​	if distance < min_distance:

​		min_distance = distance

​		min_oper = oper

#### input

list：3种红利集合，

dic：所有获取宝石的操作

```
{
	'benefit_types': ['red','blue','white'],
	'get_gems_operation':[
        {"get_different_color_gems" : [ "red", "green", "blue" ]},
		{"get_two_same_color_gems" : "red"}
	]
}
```

#### return

dic：最终选出的选择宝石的操作

```
{"get_two_same_color_gems" : "red"}
```



### evalGemDistance

for 卡 in 卡的集合：	

​	distance_tmp = 卡 - （已有的宝石+红利）

​	distance +=（distance_tmp\*权重）+ distance_tmp*（1-权重）

#### input

list：卡的集合

dic: 宝石数目

```
{
    'cards':[{
          "level": 3,
          "score": 3,
          "color": "green",
          "costs": [{
            "color": "white",
            "count": 5
          }, {
            "color": "black",
            "count": 3
          }]
        }, 
        {
          "level": 1,
          "score": 1,
          "color": "white",
          "costs": [{
            "color": "green",
            "count": 4
          }]
        }
    ],
    'gems':{
        'red':4,
        'blue':6
    }
}
```

#### return

float: distance

```
3.5
```





### chooseReservedCardOper

min_distance = inf

min_card

for card in 保留卡动作集合的卡：	

​	distance = card - （已有的宝石+红利）

​	if  distance < min_distance:

​		min_distance = distance

​		min_card = card

#### input

list： 保留卡动作的集合

```
[
    {
    	"reserve_card" : {
    			"card" : { 
                    "color" : "blue", 
                    "costs" : [ { "color" : "blue", "count" : 5 } ], 
                    "level" : 2, 
                    "score" : 2
    			}
    		}
    },
    {
    	"reserve_card" : {
    			"card" : { 
                    "color" : "red", 
                    "costs" : [ { "color" : "blue", "count" : 5 } ], 
                    "level" : 3, 
                    "score" : 5
    			}
    		}
    }
]
```

#### return

dic：某保留卡操作

```
    {
    	"reserve_card" : {
    			"card" : { 
                    "color" : "red", 
                    "costs" : [ { "color" : "blue", "count" : 5 } ], 
                    "level" : 3, 
                    "score" : 5
    			}
    		}
    }
```



### checkNobleCardBenefit

noble卡上红利的分布

#### input:
None

<!-- list： 贵族卡集合

```
[{
    "level": 3,
    "score": 3,
    "color": "green",
    "costs": [
          {"color": "white","count": 5},
          {"color": "blue","count": 3},
          {"color": "red","count": 3},
          {"color": "black","count": 3}
        ]
},
{
    "level": 3,
    "score": 3,
    "color": "green",
    "costs": [
          {"color": "white","count": 5},
          {"color": "blue","count": 3},
          {"color": "red","count": 3},
          {"color": "black","count": 3}
        ]
}
]
``` -->

#### return:

dic, 每种颜色的红利有多少个

```
{	
	'red':3, 
	'blue':5,
	'white': 6,
	'green':10
}
```

### 

### checkDevCardBenefit

dev卡上红利的分布

#### input:
None
<!-- 
list: 发展卡集合

```
[{
	"score": 3,
	"requirements": [
    	{
        "color": "red",
        "count": 4
        },
        {
        "color": "green",
        "count": 4
        }
	]
},
{
    "score": 3,
    "requirements": [
        {
        "color": "black",
        "count": 3
        },
        {
        "color": "blue",
        "count": 3
}
]
``` -->

#### return

dic, 每种颜色的红利有多少个

```
{	
	'red':3, 
	'blue':5
}
```





### countDevRound

#### input:

dic 某张发展卡

```
{
    
}
```

#### return:

int ：需要多少轮可以买到某张卡

##### example

```
4
```



### calc3BenefitType

#### input:

2*dic = 发展卡和贵族卡的红利分布

```
{
    {	
	'red':3, 
	'blue':5
    },
    {	
	'red':3, 
	'blue':5
	}
}
```

#### return:

3种红利的类型

```
['red', 'blue', 'green']
```







## 检查move的合法性

### checkMoveValid

检查步骤合法性

#### input: 

input（原来的输入），move（某一个决策）

```
{

	input: 略

	move: {"get_two_same_color_gems" : "red"}

}
```

#### return: 

bool（当前决策是否合法）