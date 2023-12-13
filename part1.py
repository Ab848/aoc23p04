def get_data(file = "test_data.txt") -> list:

    with open(file) as f:
        return f.read().split('\n')[:-1]

def parse_data(data: list) -> list:
    winners: list = []
    games: list = []

    for i in data:
        w_nums: list = (i[7:].split('|')[0].split(' '))[1:-1]
        p_nums: list = (i[7:].split('|')[1].split(' '))[1:]
        games.append([w_nums, p_nums])
    
    for g in games:
        print(g)
        pnts: int = 0

        for n in g[0]:
            if n in g[1] and n != '':
                pnts = (pnts + 1) if pnts == 0 else (pnts + pnts)
        winners.append(pnts)
    
    return sum(winners)

file: str = input("file: ")

print(parse_data(get_data(file)) if file != '' else parse_data(get_data()))
