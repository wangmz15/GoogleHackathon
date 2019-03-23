# API FOR SPLENDER



## 找出所有可能的合理操作

### findAllOper

找到所有的决策

#### input:

null

#### return:

list（所有决策）

##### example:

```
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
```



## 估值，判断操作

### evalAllOper：

总估价函数

#### input: 

list ：操作列表

##### example:

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



### checkNobleCard

noble卡上红利的分布

#### input:

list： 贵族卡集合

```
[{
    "level": 3,
    "score": 3,
    "color": "green",
    "costs": [
          {
            "color": "white",
            "count": 5
          },
          {
            "color": "blue",
            "count": 3
          },
          {
            "color": "red",
            "count": 3
          },
          {
            "color": "black",
            "count": 3
          }
        ]
},
{
    "level": 3,
    "score": 3,
    "color": "green",
    "costs": [
          {
            "color": "white",
            "count": 5
          },
          {
            "color": "blue",
            "count": 3
          },
          {
            "color": "red",
            "count": 3
          },
          {
            "color": "black",
            "count": 3
          }
        ]
	},
]
```

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

### checkDevCard

dev卡上红利的分布

#### input:

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
```

#### return:

dic, 每种颜色的红利有多少个

```
{	
	'red':3, 
	'blue':5
}
```





### countDevDistance

#### input:

某张发展卡

```
{
    
}
```

#### return:

int 需要多少轮可以买到某张卡

##### example

```
4
```





## 检查move的合法性

### checkMoveValid

检查步骤合法性

#### input: 

input（原来的输入），move（某一个决策）

##### example:

```
{

	input: 略

	move: {"get_two_same_color_gems" : "red"}

}
```

#### return: 

bool（当前决策是否合法）