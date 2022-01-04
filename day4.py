from pathlib import Path

class Card:
    numbers: list[list[int]]
    hits: list[list[bool]]
    iswinner: bool

    def __init__(self, cardstring: str):
        '''Create a Card from input like the following:
              22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19'''
        self.numbers = [list(map(int,line.split())) for line in cardstring.split('\n')]
        self.hits = [[ False for _ in range(5)] for _ in range(5)]
        self.iswinner = False

    def update(self, pick:int) -> bool:
        def is_winner() -> bool:
            def colchoosen(col: int) -> bool:
                return sum(self.hits[row][col] for row in range(5)) == 5

            return (
                any(sum(self.hits[row]) == 5 for row in range(5)) or
                any(colchoosen(col) for col in range(5))
            )

        for row in range(5):
            for col in range(5):
                if self.numbers[row][col] == pick:
                    self.hits[row][col] = True
                    self.iswinner = is_winner()
                    return self.iswinner
        return False

    def sum_of_unmarked_numbers(self) -> int:
        return sum([self.numbers[row][col] for row in range(5) for col in range(5) if not self.hits[row][col]])

def solve():

    data: list[str] = Path("day4_input.txt").read_text().rstrip().split('\n\n')

    picks: list[int] = list(map(int, data[0].split(',')))
    carddatasets: list[str] = data[1:]
    cards: list[Card] = [Card(carddata) for carddata in carddatasets ]

    for pick in picks:
        for card in cards:
            if not card.iswinner:
                card_wins = card.update(pick)
                if card_wins:
                    unmarked_sum = card.sum_of_unmarked_numbers()
                    print(f'Winner: {unmarked_sum=}, {pick=}, {unmarked_sum * pick = }')

solve()