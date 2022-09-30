#take in 5 cards, evaluate best hand from those cards. Will accept a string of '3A, 5S, KH, JS, 2D'

ogRank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

#diamon,heart,spade,clubs
ogIdentifiers = ['D','H','S','C']


cards = ['5A', '9S', '4H', '4S', '5D']

#we will split the rank and look for duplicates (this will acount for the first 3 and high card)
rankList = []

duplicateList = []
newList = []
identifierList = [] 




def pairs(cards):
    for card in cards:
        rank = card[0:1]
        identifier = card[1:2]
        
        rankList.append(rank)
        identifierList.append(identifier)

        newlist = []
        duplist = []
        for i in rankList:
            if i not in newlist:
                newlist.append(i)
            else:
                duplist.append(i) # this method catches the first duplicate entries, and appends them to the list

    print(duplist)
    if(len(duplist) == 1):
        print('One Pair')

    if (len(duplist) == 2):
        print('Two Pair')

    if(len(duplist) == 2):
        print('Three of a Kind')




def straight(cards, ogRank):
    #sanitty checking..
    for card in cards:
        rank = card[0:1]
        identifier = card[1:2]
        
        rankList.append(rank)
        identifierList.append(identifier)

        res = [x for x in rankList + ogRank if x not in rankList or x not in ogRank]

    # print(res)
    # if(len(res) <= 8):
    #     print('Straight')
    # print(res)


        #this bit of code should identify a straight
        #convert ranklist into int





def flush(cards):
    pass






# straight(cards, ogRank)
pairs(cards)

