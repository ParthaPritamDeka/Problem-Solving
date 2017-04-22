def good_fib(n):
   if n <= 1:
       return(n,0)
   else:
       (a,b) = good_fib(n-1)
       return (a+b,a)

print good_fib(4)
