def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x): # chamamos a função "epar" dentro da função "par_ou_impar" e usamos seu retorno com if. Se a função retorna True           
        return "par"
    else: 
        return "impar"
    
print(par_ou_impar(4))
print(par_ou_impar(5))
print(par_ou_impar(10))