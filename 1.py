import random
import string

def generate(N, K):
    chara = string.ascii_letters + string.digits 
    pars = set()  

    while len(pars) < N:
        par = ''.join(random.choice(chara) for _ in range(K))
        pars.add(par)
    
    return list(pars)

if __name__ == "__main__":
    N = int(input("кол-во паролей (N): "))
    K = int(input("длины паролей (K): "))
    
    pars = generate(N, K)
    for i, par in enumerate(pars, 1):
        print(f"пароль {i}: {par}")
