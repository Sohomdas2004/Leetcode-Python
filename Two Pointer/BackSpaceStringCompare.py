#Leetcode - 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res=""
        i=len(s)-1
        skip=0
        while(i>-1):
            if(s[i]=="#"):
                skip+=1
            elif skip>0:
                skip-=1
            else:
                s_res+=s[i]
            i-=1

        t_res=""
        i=len(t)-1
        skip=0
        while(i>-1):
            if(t[i]=="#"):
                skip+=1
            elif skip>0:
                skip-=1
            else:
                t_res+=t[i]
            i-=1

        return s_res[::-1]==t_res[::-1]