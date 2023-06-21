# Knock over 20 or toss best card in best suit :)
def strategy(self, pile):
    self.pull()

    tally = self.tally()
    bestsuit = tally.index(max(tally))

    bestcard = -1
    bestrank =  0
    for i, card in enumerate(self.hand):
        if card.suit == bestsuit:
            if card.rank == 1:
                worstcard = i
                break
            elif card.rank > bestrank:
                bestcard = i
                bestrank = card.rank

    #self.show()
    self.drop(self.hand[bestcard]) 
    #self.show()
    if max(self.tally()) > 20:
        self.knock()
    return
