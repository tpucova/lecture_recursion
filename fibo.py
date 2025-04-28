
def recursive_nth_fibo(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       fibo_1 = recursive_nth_fibo(n-1)
       fibo_2 = recursive_nth_fibo(n-2)
       return fibo_1 + fibo_2
def main():
    pass


if __name__ == "__main__":
    my_n = 4
    nth_fibo = recursive_nth_fibo(my_n)
    print(nth_fibo)
