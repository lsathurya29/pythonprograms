def roman_to_int(s:str):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    for i in range(len(s)):
        if i>0 and roman[s[i]]>roman[s[i-1]]:
            res+=roman[s[i]]-2*roman[s[i-1]]
        else:
            res+=roman[s[i]]
    return res
print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))
