
import heapq
from dataclasses import dataclass
      
class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = bid
        self.score = self._getscore(hand)

    def __eq__(self, other) -> bool:
        return self.hand == other.hand
    
    def __lt__(self, other) -> bool:
        every = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
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

    def _getscore(self, hand) -> int:
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
    
def dotask(s) -> None:
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