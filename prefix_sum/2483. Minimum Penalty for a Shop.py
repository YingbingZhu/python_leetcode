class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        yes = [0] * (n+1)
        no = [0] * (n+1)
        
        # update list for penaltys for 'N'
        p = 0
        for i in range(n):
            no[i] = p
            p += (customers[i] == 'N')
        no[n] = p

        # update list for penaltys for 'Y'
        p = 0
        for i in reversed(range(n)):
            p += (customers[i] == 'Y')
            yes[i] = p
        
        p = inf
        hour = 0
        for i in range(n+1):
            if yes[i] + no[i] < p:
                p = yes[i] + no[i]
                hour = i
        return hour


            
                