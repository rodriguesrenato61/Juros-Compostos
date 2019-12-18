import math

def montante(cap, tax, per):
    return (cap * math.pow(1 + tax/100, per))

def capital(jur, tax, per):
    return (jur/(math.pow(1 + tax/100, per) - 1))

def periodo(cap, mont, tax):
    return (math.log(cap/mont)/math.log(1 + tax/100) * (-1))

    
def taxa(cap, mont, per):
    return((100*(math.pow(cap/mont, 1/per) - 1)) * (-1))
    
def convert_taxa(tax, med_entrada, med_saida):
    
    if med_entrada == 'a':
        tax_diaria = math.pow(1 + tax/100, 1/360)
        
    if med_entrada == 'm':
        tax_diaria = math.pow(1 + tax/100, 1/30)
        
    if med_entrada == 'd':
        tax_diaria = math.pow(1 + tax/100, 1/1)
        
    if med_saida == 'a':
        tax_saida = math.pow(tax_diaria, 360)
     
    if med_saida == 'm':
        tax_saida = math.pow(tax_diaria, 30)
        
    if med_saida == 'd':
        tax_saida = math.pow(tax_diaria, 1)
        
    return ((tax_saida - 1)*100)


print("1 - Juros e Montante")
print("2 - Capital e Montante")
print("3 - Taxa e Montante")
print("4 - Periodo e Montante")
print("5 - Converter taxa")
opc = int(input("Opcao: "))

    
if opc == 1:
    c = float(input("Capital: "))
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    
    i = convert_taxa(i, med_entrada, med_saida)
    
    m = montante(c, i, t)
    j = m - c
    
    print("Juros: {}".format(j))
    print("Montante: {}".format(m))
    
if opc == 2:
    j = float(input("Juros: "))
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    
    i = convert_taxa(i, med_entrada, med_saida)
    
    c = capital(j, i, t)
    m = montante(c, i, t)
    
    print("Capital: {}".format(c))
    print("Montante: {}".format(m))
    
if opc == 3:
    
    j = float(input("Juros: "))
    c = float(input("Capital: "))
    t = float(input("Periodo: "))
    
    m = c + j
    i = taxa(c, m, t)
    
    print("Taxa: {}".format(i))
    print("Montante: {}".format(m))
    
if opc == 4:
    
    c = float(input("Capital: "))
    i = float(input("Taxa: "))
    j = float(input("Juros: "))
    
    m = c + j
    t = periodo(c, m, i)
    
    print("Periodo: {}".format(t))
    print("Montante: {}".format(m))

if opc == 5:
    
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ano\nm - mes\nd - dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ano\nm - mes\nd - dia\nOpcao: "))

    tax_convert = 100 * (math.pow(1 + convert_taxa(i, med_entrada, med_saida)/100, t) - 1)

    print("{}% a.{} = {}% em {} {}".format(i, med_entrada, tax_convert, t, med_saida))
