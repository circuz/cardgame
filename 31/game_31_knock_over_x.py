# Knock over x or toss worst card in worst suit :)
from cardgame_setup import SUITS

def strategy(self, discard, target):

    # bestranks is the highest total suit value
    bestranks = max(self.tally())
    if bestranks > target:
        self.knock()
    else:
        disccard = discard.peek()
        # Would it be of benefit at all to pick up this card? But is it good enough? 
        if bestranks < max(self.tally([disccard])) and (disccard.rank > (1/3 * target)):
            self.pull(discard=True)
        else:
            self.pull(discard=False)

        tally = self.tally()
        worsttall = 40
        worstsuit = 0
        for suit, tall in enumerate(tally):
            if tall < worsttall:
                if tall > 0:
                    worsttall = tall
                    worstsuit = suit

        worstcard = -1
        worstrank = 15
        for i, card in enumerate(self.hand):
            if card.suit == worstsuit:
                if card.rank == 1:
                    if worstrank == 15:
                        worstcard = i
                elif card.rank < worstrank:
                    worstcard = i
                    worstrank = card.rank

        #self.show()
        self.drop(self.hand[worstcard]) 
        #self.show()
    return

