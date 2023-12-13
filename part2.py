def get_data(file = "test_data.txt") -> list:

    with open(file) as f:
        return f.read().split('\n')[:-1]

def parse_winners(data: list) -> list:
    winners: list = []
    games: list = []

    for i in data:
        w_nums: list = (i[7:].split('|')[0].split(' '))[1:-1]
        p_nums: list = (i[7:].split('|')[1].split(' '))[1:]

        games.append([w_nums, p_nums])
    
    for g in games:
        pnts: int = 0

        for n in g[0]:
            if n in g[1] and n != '':
                pnts = (pnts + 1)

        winners.append([games.index(g),pnts])
    
    return winners

def parse_cards(data: list) -> list:
    cards: list = []
    buffer: list = []
    
    for i,y in enumerate(data):
        count = 0

        if i == 0:
            cards.append(1)
            buffer.append(y[1])
            continue

        for j in range(len(buffer)):
            if buffer[j] > 0:
                count += cards[j]
                buffer[j] -= 1

        cards.append(count+1)
        buffer.append(y[1])

    return cards

file: str = input("file: ")

print(sum(parse_cards(parse_winners(get_data(file)) if file != '' else parse_data(get_data()))))
