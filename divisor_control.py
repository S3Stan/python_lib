# divisor control code


def Solve (N):
    # Write your code here
    divisor_sum_total = 0;

    if 1 <= N <= 10**9: # manage N constraint
        for number in range(1, N):
            if N % number == 0:
                divisor_sum_total += number 
        
        if divisor_sum_total == N:
            return('YES')
        else:
            return('NO')
    else:
        return('NO')

    

T = int(input())
if 1 <= T <= 100: # manange t constraints
    for _ in range(T):
        N = int(input())
        out_ = Solve(N)
        print (out_)
else:
    print('NO')
