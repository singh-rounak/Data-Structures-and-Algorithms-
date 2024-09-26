def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    
    #To store characters and their frequencies
    map1 = {}
    map2 = {}
    
    #Check whether they have same char and corresponding freq
    for i in range(len(s)):
        map1[s[i]] = 1 + map1.get(s[i], 0)
        map2[t[i]] = 1 + map2.get(t[i], 0)
        
    for key in map1:
        if map1[key] != map2[key]:
            return False
    return True
    
isAnagram(s, t)