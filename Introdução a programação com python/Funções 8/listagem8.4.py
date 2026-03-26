def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
   
    if epar(x): # chamamos a função "epar" com o valor de "x"        
        
        # a instrução return são ignoradas de forma similar à instrução break dentro de um while ou for.

        return "par" # ultilizamos o seu retorno caso seja "par" 
    
    else: 
        
        return "impar"  # ultilizamos o seu retorno caso seja "impar" 
    
print(par_ou_impar(4))
print(par_ou_impar(5))
print(par_ou_impar(10))