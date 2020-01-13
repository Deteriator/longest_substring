'''
A:
    1.Define variable to hold running substring
    2.Define variable to hold potential longer substring
    3.Loop over string 
        a. put first instance of non repeating string in finalstr variable
        b. build new string and compare with finalstr   
           if len of substr > finalstr  set finalstr to newstr
    4.return the length of finalstr.

C:
'''
def longest_substring(string):
    substr = string[0]
    finalstr = ''
    start = 0
    check = {}
    for i in range(start,len(string)):
        if string[i] not in check:
            finalstr += string[i]
            check[string[i]] = string[i]
    print(check)
    return (len(finalstr))
    
    
print(longest_substring("abcabcbb") == 3)
print(longest_substring("bbbbb") == 1)
print(longest_substring("pwwkew") == 3)