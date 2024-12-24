numberlargest = int(input("Enter the largest number: "))
numbersmallest = int(input("Enter the smallest number: "))
while numbersmallest:
    numberStore = numbersmallest
    numbersmallest = numberlargest %  numbersmallest
    numberlargest = numberStore

print("HCF is:", numberlargest)
