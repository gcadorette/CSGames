import functools

def main():
    tab = []
    SIZE = 20
    SIZE_OF_LINE = 4
    with open("20x20.txt") as f:
        for line in f:
            tab.append([int(x) for x in line.split(" ")])
    results = []
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            # We just check half of the directions
            # i.e. top-left, top, top-right, right

            #top
            if y >= SIZE_OF_LINE - 1:
                results.append(functools.reduce(lambda x, y : x * y, [tab[y - i][x] for i in range(0, SIZE_OF_LINE)]))
                #top-left
                if x >= SIZE_OF_LINE - 1:
                    results.append(functools.reduce(lambda x, y : x * y, [tab[y - i][x - i] for i in range(0, SIZE_OF_LINE)]))
                #top-right
                if x <= SIZE - SIZE_OF_LINE:
                    results.append(functools.reduce(lambda x, y : x * y, [tab[y - i][x + i] for i in range(0, SIZE_OF_LINE)]))
            #right
            if x <= SIZE - SIZE_OF_LINE:
                results.append(functools.reduce(lambda x, y: x * y, [tab[y][x + i] for i in range(0, SIZE_OF_LINE)]))
    print(max(results))



if __name__ == "__main__":
    main()