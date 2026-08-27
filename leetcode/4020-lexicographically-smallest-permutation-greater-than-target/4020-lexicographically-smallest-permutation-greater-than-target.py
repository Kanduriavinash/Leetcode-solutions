class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        def f(i,z=Counter(s)):
            if i==len(t): return None
            
            if z[t[i]]:
                z[t[i]] -= 1
                if res:=f(i+1): return res
                z[t[i]] += 1

            for q in range(ord(t[i])+1,ord('z')+1):
                if z[c:=chr(q)]:
                    z[c] -= 1
                    return t[:i]+c+''.join(sorted(z.elements()))

        return f(0) or ''