'''
1/16/2020
OneAway

Check if two strings are 1 or 0 edits away
Add, Remove, Edit

1. If len(str2) == len(str1) + 1
    * Compare Chars 
2. If len(str2) == len(str1) - 1
    * Compare Chars 
3. If len(str2) == len(str1)
    * Compare Chars 

'''


def oneAway(str1: str, str2: str):
    # Check if they are the same string
    if (str1 == str2):
        return True
    
    len1 = len(str1)
    len2 = len(str2)
    i = 0
    j = 0 
    count = 0 

    while (i < len1 and j < len2): 
        if (str1[i] != str2[j]): #If current chars dont match
            if (count == 1): # If there is already one error 
                return False
            # If length of one string is more, then only possible edit is to remove char
            if (len1 > len2): 
                i += 1
            elif (len2 > len1): 
                j += 1
            else: # If lengths of both strings are the same
                i += 1
                j += 1
            #Increment count of edit
            count += 1
        else: # If the current characters match
            i += 1
            j += 1 

    # If there is an extra char at the end of one string 
    if (i < len1 or j < len2):
        count += 1

    return count == 1

 
    

    




tester = "pale"
t1 = "ple" # T
t2 = "bale" # T
t3 = "pales" # T
t4 = "pale" #t
t5 = "ble" #f

print(oneAway(tester, t4))
print(oneAway(tester, t1))
print(oneAway(tester, t2))
print(oneAway(tester, t3))
print(oneAway(tester, t5))