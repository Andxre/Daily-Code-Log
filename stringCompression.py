'''
1/17/2020
1.6: String Compression

aabbbcccccaaa => a2b3c5a2
'''

def compress(string: str):
    res = ""
    counter = 0

    for i in range(len(string)):
        if (i != 0 and string[i] != string[i-1]):
            res += string[i-1]
            res += str(counter)
            counter = 0
        counter += 1

    res += string[-1]
    res += str(counter)

    val = string if len(res) > len(string) else res
    return val




def main():
    print(compress('aaaabbbbccc'))
    print(compress('abc'))
    print(compress('xxxdddyyyzzzxxx'))    

main()