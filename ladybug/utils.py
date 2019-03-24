import numpy as np

def checkMoveValid(input,move):
    #input:
    #   input: original input
    #   move:  output to be test
    #output:
    #   bool

    player = input['playerName']
    my_table = None
    for i in input['players']:
        if i['name'] == player:
            my_table = i
    if my_table == None:
        # print('Error no player')
        return False
    check_gem_init={'red':0,'gold':0,'green':0,'blue':0,'white':0,'black':0}
    if 'get_different_color_gems' in move:
        if len(move['get_different_color_gems'])<=3 and len(np.unique(move['get_different_color_gems']))==len(move['get_different_color_gems']):
            check_gem=check_gem_init
            num=len(move['get_different_color_gems'])
            for gems in input['table']['gems']:
                check_gem[gems['color']]=gems['count']
            for gems in move['get_different_color_gems']:
                if check_gem[gems]==0:
                    return False
            if 'gems' in my_table:
                for gems in my_table['gems']:
                    num+=gems['count']
            if num>10:
                return False
        else:
            return False
    elif 'get_two_same_color_gems' in move:
        if True:
            check_gem=check_gem_init
            num=len(move['get_two_same_color_gems'])
            for gems in input['table']['gems']:
                check_gem[gems['color']]=gems['count']
            if check_gem[move['get_two_same_color_gems']] <4:
                return False
            if 'gems' in my_table:
                for gems in my_table['gems']:
                    num+=gems['count']
            if num>10:
                return False
        else:
            return False
    elif 'reserve_card' in move:
        card=move['reserve_card']['card']
        flag=False
        for cards in input['table']['cards']:
            if card==cards:
                flag=True
        if flag==False:
            return False
        if 'reserved_cards' not in my_table or len(my_table['reserved_cards'])>2:
            return False
    elif 'purchase_card' in move:
        card=move['purchase_card']
        flag=False
        for cards in input['table']['cards']:
            if card==cards:
                flag=True
        if flag==False:
            return False
        check_gem=check_gem_init
        if 'gems' in my_table:
            for gems in my_table['gems']:
                check_gem[gems['color']]=gems['count']
        #hongli
        if 'purchased_cards' in my_table:
            for cards in my_table['purchased_cards']:
                check_gem[cards['color']] += 1
        for gems in card['costs']:
            if gems['count']>check_gem[gems['color']]:
                return False
    elif 'purchase_reserved_card' in move:
        card=move['purchase_reserved_card']
        #check reserve or not
        if 'reserved_cards' not in my_table:
            return False
        flag=False
        for r_cards in my_table['reserved_cards']:
            if r_cards==card:
                flag=True
        if flag==False:
            return False

        flag=False
        for cards in input['table']['cards']:
            if card==cards:
                flag=True
        if flag==False:
            return False
        check_gem=check_gem_init
        if 'gems' in my_table:
            for gems in my_table['gems']:
                check_gem[gems['color']]=gems['count']
        #hongli
        if 'purchased_cards' in my_table:
            for cards in my_table['purchased_cards']:
                check_gem[cards['color']] += 1
        for gems in card['costs']:
            if gems['count']>check_gem[gems['color']]:
                return False
    return True
#2<4
#
if __name__=='__main__':
    import json
    f=open('./input_0.txt')
    a=''
    for i in f.readlines():
        a=a+i.strip('\n')
    test=json.loads(a)
    print(checkMoveValid(test,{}))

    m1={'get_different_color_gems':['red','green','blue']}
    print(checkMoveValid(test,m1))
    m2={'get_two_same_color_gems':'red'}
    print(checkMoveValid(test,m2))
    m3={'reserve_card':{'card':{'color':'blue','costs':[{'color':'blue','count':5}],'level':2,'score':2}}}
    print(checkMoveValid(test, m3))
    m31={'reserve_card':{'card':{
        "score": 5,
        "level": 3,
        "color": "white",
        "costs": [
          {
            "color": "white",
            "count": 3
          },
          {
            "color": "black",
            "count": 7
          }
        ]
      }}}
    print(checkMoveValid(test, m31))
    m4={'purchase_card':{
        "score": 5,
        "level": 3,
        "color": "white",
        "costs": [
          {
            "color": "white",
            "count": 0
          },
          {
            "color": "black",
            "count": 0
          }
        ]
      }}
    print(checkMoveValid(test, m4))