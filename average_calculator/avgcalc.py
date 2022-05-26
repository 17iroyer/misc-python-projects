#avgcalc.py
#Calculates the average of a list of numbers

inputlist = []

listlen = int(input("Number of elements: "))

for i in range(listlen):
    nextnum = int(input("List element %d: "%(i + 1)))
    inputlist.append(nextnum)

def listaverage(num):
    sum = 0
    for t in num:
        sum += t
    
    avg = sum / len(num)
    return avg

print("The averge of the numbers is: ", listaverage(inputlist))
