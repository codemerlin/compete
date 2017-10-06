n, r = map(int,raw_input().split())
fact_n = 1; 
fact_r = 1;
fact_n_r= 1;
for i in range(1,n+1):
    fact_n *= i;
    if(i==r) :
        fact_r = fact_n
    if(i==n-r) :
        fact_n_r = fact_n

print (fact_n/(fact_r*fact_n_r))%1000000007
