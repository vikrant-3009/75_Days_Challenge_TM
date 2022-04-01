class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        for i in range(n):
            transactions[i] = transactions[i].split(',')
            transactions[i][1] = int(transactions[i][1])
        transactions.sort(key=lambda x:x[1])
        # print(transactions)
        
        ans = set()
        for i in range(n):
            j = i+1
            while j < n and (int(transactions[j][1]) - int(transactions[i][1])) <= 60:
                # print('i', 'j', i, j)
                if (transactions[i][0] == transactions[j][0]) and (transactions[i][3] != transactions[j][3]):
                    # adding the indexes of the invalid transactions to the set
                    ans.add(j)
                    ans.add(i)
                # print(ans)
                j += 1
                
        for i in range(n):
            if int(transactions[i][2]) > 1000:
                ans.add(i)
        
        res = []
        for i in ans:
            transactions[i][1] = str(transactions[i][1])
            res.append(",".join(transactions[i]))
        
        return res