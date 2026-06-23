# given numbers between 1 to 50 if numbers are devisible 
# from 3 then THREE
# from 5 then FIVE 
# from 3 and 5 then THREE FIVE 
# if not then INDIA 

for i in range(1, 51):
    if i % 5 == 0 and i%3 == 0:
        print("THREE FIVE")
    elif i % 5 == 0:
        print("FIVE")
    elif i % 3 == 0:
        print("THREE")

    else:
        print("INDIA")            