import itertools
      
class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = bid
        if "J" in hand:
            self.score = self._jinhand(hand)
        else:
            self.score = self._getscore(hand)

    
    def __eq__(self, other):
        return self.hand == other.hand
    
    def __lt__(self, other):
        every = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
        every.reverse()
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False
        ind = 0
        while ind < 5:
            myhand = self.hand[ind]
            otherhand = other.hand[ind]
            myind = every.index(myhand)
            otherind = every.index(otherhand)
            if myind < otherind:
                return True
            if myind > otherind:
                return False
            ind+= 1
        return False

    
    def _getscore(self, hand):
        d = {i:0 for i in hand}
        for i in hand:
            d[i] += 1
        if len(d) == 5:
            return 1
        if len(d) == 4:
            return 2
        if len(d) == 3:
            for val in d.values():
                if val == 2:
                    return 3
            return 4
        if len(d) == 2:
            for val in d.values():
                if val == 2:
                    return 5
            return 6
        return 7

    def _jinhand(self, hand):
        bestscore = self._getscore(hand)
        newhand = [i for i in hand]
        bestletter = "J"
        jindeces = []
        for i,letter in enumerate(hand):
            if letter == "J":
                jindeces.append(i)
        perms = [''.join(seq) for seq in itertools.product("01", repeat=len(jindeces))]
        #print(perms)
      
        every = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

        for perm in perms:
            changes = []
            for i,num in enumerate(perm):
                if num == "1":
                    changes.append(jindeces[i])
            for letter in every:
                for change in changes:
                    newhand[change] = letter
                newscore = self._getscore(newhand)

                if newscore > bestscore:
                    bestletter = letter
                    bestscore = newscore
                newhand = [e for e in hand]

        return bestscore




def dotask(s):

    hp = []
    for line in s:
        hand, bid = map(str, line.split())
        hp.append(Hand(hand, int(bid)))



    srt = sorted(hp)



    su = 0
    for ind, elem in enumerate(srt, 1):
        su += elem.bid*ind

    print(su)





if __name__ == "__main__":
    s = open('input7.txt', 'r').read().split('\n')
    dotask(s)


#255086951
