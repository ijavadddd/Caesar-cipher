##Import alphabet for check our character and shift it in alphabet list
from string import ascii_lowercase , ascii_uppercase

##This function will encryot your string
def Encrypt(string,key):
    ##Here i seprate lower and upper because i dont want change my string format
    alphaU = ascii_uppercase
    alphaL = ascii_lowercase
    ##new string will add to this variable
    temp=''

    for ch in string:
        ##Check the character is in upper list pr not
        if ch in alphaU:
            new_ch = (alphaU.index(ch) + key) % len(alphaU)
            temp+=alphaU[new_ch]

        ##Check the character is in lower list pr not
        elif ch in alphaL:
            new_ch = (alphaL.index(ch) + key) % len(alphaL)
            temp+=alphaL[new_ch]

        ##Don't change special characters  
        else:
            temp+=ch
    print(temp)

##This function ill decrypt
def Decrypt(string,key):
    key*=-1
    return Encrypt(string,key)

##Brute force is for when u don't know key value and it will try every possible key 
def BruteForce(string):
    alphaU = ascii_uppercase
    key=1
    while key<= len(alphaU):
        Decrypt(string,key)
        key+=1

