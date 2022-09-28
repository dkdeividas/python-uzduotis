from cmath import pi
import math
a = float(input("iveskite indo auksti:"))
d = float(input("iveskite indo skersmeni:"))
d1 = float(input("iveskite pirmo rutulio skersmeni:"))
d2 = float(input("iveskite antro rutulio skersmeni:"))
print("Pirmo rutulio turis:", 4/3 * pi * (d1/2) ** 3)
print("Antro rutulio turis:", 4/3 * pi * (d2/2) ** 3)
#apskaiciuot likusio vandens turi
#(Ritinio turis) - (pirmo rutulio turis) + (antro rutulio turis)
#kitaip neismastau, turbut blogai
print("Skyscio turis:", (pi * (d/2) ** 2 * a) - (4/3 * pi * (d1/2) ** 3) + (4/3 * pi * (d2/2) ** 3))