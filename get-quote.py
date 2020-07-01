import random


def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd].rstrip('\n'))
    rnd = random.randint(0, last)
    print(quotes[rnd].rstrip('\n'))
    rnd = random.randint(0, last)
    print(quotes[rnd].rstrip('\n'))


with open('quotes.txt', 'a') as ouf:
    ouf.write(input('Insert your quote:') + '\n')

if __name__ == "__main__":
    primary()