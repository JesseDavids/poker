from treys import Card
from treys import Evaluator
import sys
from treys import Deck

#fall-back to libs


# 'AS, 10C, 10H, 3D, 3S' T = 10
hand = sys.argv[1]
# print(hand)

hand = hand.split(',')
backList = []
frontList = []
finalList = []

for each in hand:
    # print(each)
    card = each.split(' ')[-1]

    front = (card[0])
    back = (card[-1].lower())

    frontList.append(front)
    backList.append(back)

#replace any 1's with a T for the lib to work
l = list(map(lambda x: x.replace('1', 'T'), frontList))


for front in l:
    for back in backList:
        finalList.append(front+back)


finalList2 = []
#skip every 6th element in the list
for x in finalList[::6]:
    finalList2.append(x)



evaluator = Evaluator()
deck = Deck()
board = deck.draw(5) #5 cards
board = []

#create the board based on the string input requested
for x in finalList2:
    # print(x)
    board.append(Card.new(x))

#lib needs a hand to work 
hand = [
    Card.new('Qs'),
    Card.new('5h')
]


p1_score = evaluator.evaluate(hand, board)
p1_class = evaluator.get_rank_class(p1_score)

print ("Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))