import numpy as np

def checkMoveValid(input,move):
    #input:
    #   input: original input
    #   move:  output to be test
    #output:
    #   bool
    if 'get_different_color_gems' in move:
        if len(move['get_different_color_gems'])<=3 and np.unique(move['get_different_color_gems'].shape[0]==3):
            check_gem={}
            for gems in input['table']['gems']:
                check_gem[gems['color']]=gems[count]
            for gems in move['get_different_color_gems']:
                if gems not in check_gem or check_gem[gems]==0:
                    return False
        else:
            return False
    elif 'get_two_same_color_gems' in move:
        if len(move['get_two_same_color_gems'])==2 and np.unique(move['get_two_same_color_gems'].shape[0]==1):
            check_gem={}
            for gems in input['table']['gems']:
                check_gem[gems['color']]=gems[count]
            if move['get_two_same_color_gems'] not in check_gem or check_gem[move['get_two_same_color_gems']] <4:
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
    elif 'purchase_card' in move:
        card=move['purchase_card']
        player=input['playerName']
        my_table=None
        for i in input['players']:
            if i['name']==player:
                my_table=i
        if my_table==None:
            #print('Error no player')
            return False
        flag=False
        for cards in input['table']['cards']:
            if card==cards:
                flag=True
        if flag==False:
            return False
        check_gem={}
        for gems in my_table['gems']:
            check_gem[gems['color']]=gems['count']
        #hongli
        for cards in my_table['purchased_cards']:
            check_gem[cards['color']]+=1
        for gems in card['costs']:
            if gems['color'] not in check_gem or gems['count']>check_gem[gems['color']]:
                return False
    elif 'purchase_reserved_card' in move:
        card=move['purchase_reserved_card']
        player=input['playerName']
        my_table=None
        for i in input['players']:
            if i['name']==player:
                my_table=i
        if my_table==None:
            #print('Error no player')
            return False
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
        check_gem={}
        for gems in my_table['gems']:
            check_gem[gems['color']]=gems['count']
        #hongli
        for cards in my_table['purchased_cards']:
            check_gem[cards['color']]+=1
        for gems in card['costs']:
            if gems['color'] not in check_gem or gems['count']>check_gem[gems['color']]:
                return False
    return True
#2<4
#
if __name__=='__main__':
    import json
    f=open('./input_0.txt')
    test=json.loads(f.readlines())
    print(test)
    print(checkMoveValid(test),{})
