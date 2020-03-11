import math
def main():
    MAX = 1000000
    amt = 0
    for i in range(2, MAX):
        if i > 10 and any([int(x) % 2 == 0 for x in str(i)]):
            continue

        if all([test_primes(x) for x in circleNum(i)]):
            amt += 1
    print(amt)

def test_primes(num):
    root = int(math.sqrt(num))
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True

def circleNum(num):
    numStr = str(num)
    numbers = []
    for i in range(0, len(numStr)):
        currNbr = ""
        for j in range(0, len(numStr)):
            currNbr += numStr[(i + j) % len(numStr)]
        numbers.append(int("".join(currNbr)))
    return numbers



if __name__ == "__main__":
    main()
