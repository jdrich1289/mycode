from typing import Counter


beginning = int(input("Enter a start point: "))
ending = int(input("Enter an end point: "))
arigato = beginning

while ending >= arigato:
    print(arigato, end=" ")
    arigato += 1

if beginning > ending:
    print("Beginning value is greater than ending value.")