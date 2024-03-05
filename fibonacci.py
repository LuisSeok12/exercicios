def fibonacci(numero):
    fib1, fib2 = 0, 1
    while fib2 < numero:
        fib1, fib2 = fib2, fib1 + fib2
    if fib2 == numero:
        return True
    else:
        return False

numero = int(input("Digite um numero para ver se está na sequencia de Fibonacci:"))
if fibonacci(numero):
    print(numero, "pertence a Fibonacci")
else:
    print(numero, "não pertence a Fibonacci.")
