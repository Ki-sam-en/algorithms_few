class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True # сразу обрабатывается, если число верное
        if n < 0: return False # если отрицательное или 0
        
        n = list(str(n)) # список для последующих итераций 

        count = [] 
        t = []
        while True:
            for i in n: # i = 1, 9
                count.append(int(i)**2) # 1, 81
            n = sum(count) # 82
            t.append(n)

            if n == 1:
                return True
            if len(t) != len(set(t)):
                return False
            else:
                n = list(str(n))
                count = []
                continue