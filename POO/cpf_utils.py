
def formatar_cpf(cpf):
    p1 = cpf[:3]
    p2 = cpf[3:6]
    p3 = cpf[6:9]
    p4 = cpf[9:]
    return f'{p1}.{p2}.{p3}-{p4}'
    
    
def verificar_cpf(cpf):
    if len(cpf) == 11:
        try:
            int(cpf)
            return True
        except ValueError:
            return False
    else:
        return False