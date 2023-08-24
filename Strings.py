name = "prime king"

print(name.upper())
print(name)

################

print(name.find('k'))   ## will return index if it find otherwise it will return -1

#################3

print(name.replace("prime king", "Ironman"))
print(name)

#################3

print("e" in name)
print("z" in name)

################   Operators

print(5-2)
print(5*2)
print(5/2)
print(5//2)  ## it will remove the after part of decimal 
print(5%2)
print(5**2)  ## power

#####################
i = 5
i = i+2
i += 5

#############
print(3>2)   ## true
print(3<2)    ## false
print(3 == 2)
print(3!=2)

## Logical operator
print(3 >2 and 2> 6)
print(2==2 or 3<2)
print(not 3>2)