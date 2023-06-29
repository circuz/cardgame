# Knock over 20 or toss worst card in worst suit :)
def strategy(self, pile):

    if max(self.tally()) < max(self.tally([pile.peek()])):
        self.pull(pile=True)
    else:
        self.pull(pile=False)

    tally = self.tally()
    worsttall = 40
    worstsuit = 0
    for suit, tall in enumerate(tally):
        if tall < worsttall:
            if tall > 0:
                worsttall = 40
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
    if max(self.tally()) > 20:
        self.knock()
    return
