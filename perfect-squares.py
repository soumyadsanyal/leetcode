class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        method:
        firstly, any integer n is the sum of <=n many perfect squares (can just do 1+1+1+...+1=n)
        a min search should try to do some dynamic programming and cacheing actually

        1 -> 1, 1
        2 -> 1+1, 2
        3-> 1+1+1, 3
        4-> 4, 1
        5-> 4+1, 2
        6-> 4+1+1, 3
        7-> 4+1+1+1, 4
        8-> 4+4, 2
        9-> 9, 1
        10-> 9+1, 2
        11-> 9+1+1, 3
        12-> 9+1+1+1, 4
        13-> 9+4, 2
        14-> 9+4+1, 3
        15-> 9+4+2, 3
        16-> 16, 1
        17 -> 16+1, 2
        
        N -> n_1 = largest perfect square <=N, d = N-n_1
        f(N) = f(n_1) + f(N-n_1) ?
        f(n_1) + f(N-n_1) : f(n_2) + f(N-n_2)
        n_1 >= n_2
        
        there might be a way that n_1 > n_2, but n_2 is optimal
        
        for each x in ps, x<=N, need to compute f(x) + f(N-x), and then take the minimum over these
        
        do this using cacheing
        
        f(1) = 1
        f(2) = 2
        f(3) = 3
        f(4) = 1
        f(5) = min{f(4)+f(1), f(1)+f(4)} = 2
        f(6) = min{f(4) + f(2), f(1) + f(5)} = min{2, 3} = 2
        f(7) = min{f(4) + f(3), f(1) + f(6)} = min{4, 3} = 3
        
        
        for n, do:
        search for the largest 
        
        """
        squares = []
        term=1
        while term*term<=n:
            squares.append(term*term)
            term+=1
        #now we have all the perfect squares <=N. next, need to build the result array
        if n in squares:
            return 1
        f={}
        f[1]=1
        f[2]=2
        f[3]=3
        f[4]=1
        for term in range(5, n+1):
            if term in squares:
                f[term]=1
            else:
                f[term] = min([f[square]+f[term-square] for square in squares if square<term])
                #print(term, f[term], f, squares)
        return f[n]
            
            
            
        
