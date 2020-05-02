import numpy as np
def pick_word() :
    x = np.random.randint(1, 4)
    chaine = ""
    with open('wor.txt', 'r') as f:
        for i, line in enumerate(f):
            if i == x:
                chaine += line
    return chaine


def replace_space(ch, c):
    x= ch.index(c)
    ch=ch[:x] + ' ' + ch[x+1:]
    return ch

def main () :
    play = 1
    while play :
        ch = pick_word()
        print(ch)
        long = len(ch)
        n = 6
        disp = ["-"] * (long - 1)
        print("the string length is : ", long - 1, ' ', ''.join(disp))
        cont = True
        m = 0
        chaine = ch
        while cont:
            x = input("guess a caracter ! ")
            if x in ch:
                disp[ch.index(x)] = x
                ch = replace_space(ch, x)
                print(''.join(disp))
                m += 1
                if m == long - 1:
                    cont = False
            else:
                print('wrong choise ')
                n -= 1
                if n == 0:
                    cont = False
        play = int(input("if you want to play again press 1 \n else press 0 "))

main()