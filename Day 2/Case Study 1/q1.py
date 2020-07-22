num = int(input('>'))

counter = 1
factors = []
while counter<num+1:
    #print(counter)
    if num%counter == 0 and counter%2==0:
        print(counter, ": Even Factor")
    elif num%counter == 0 and counter%2!=0:
        print(counter, ": Odd Factor")
            
    counter+=1
