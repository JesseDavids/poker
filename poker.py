from treys import Card
from treys import Evaluator

from treys import Deck

#fall-back to libs


# 'AS, 10C, 10H, 3D, 3S' T = 10

evaluator = Evaluator()
deck = Deck()
board = deck.draw(5) #5 cards


board = [
    Card.new('As'),
    Card.new('Tc'),
    Card.new('Th'),
    Card.new('3d'),
    Card.new('3s')
]

hand = [
    Card.new('Qs'),
    Card.new('5h')
]

p1_score = evaluator.evaluate(hand, board)
p1_class = evaluator.get_rank_class(p1_score)

print ("Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))