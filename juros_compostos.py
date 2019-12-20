import math
"""
importando a biblioteca math para uso das funções pow(potenciação)
e log(logaritmo)
"""

def montante(cap, tax, per):
    return (cap * math.pow(1 + tax/100, per))
"""
função para calcular o montante utilizando o capital, taxa e período
como parâmetros de entrada
"""

def capital(jur, tax, per):
    return (jur/(math.pow(1 + tax/100, per) - 1))
"""
função para calcular o capital utilizando os juros, a taxa e o período
como parâmetros de entrada
"""

def periodo(cap, mont, tax):
    return (math.log(cap/mont)/math.log(1 + tax/100) * (-1))
"""
função para calcular o período utilizando o capital, o montante e a taxa
como parâmetros de entrada
"""

    
def taxa(cap, mont, per):
    return((100*(math.pow(cap/mont, 1/per) - 1)) * (-1))
"""
função para calcular a taxa utilizando o capital, o montante e o período
como parâmetros de entrada
"""
    
def convert_taxa(tax, med_entrada, med_saida):
    """
    tax: taxa a ser convertida
    med_entrada: medida da taxa a ser convertida
    med_saida: medida da taxa convertida
    tax_diaria: recebe a taxa convertida medida em dias
    """
    if med_entrada == 'a':
        tax_diaria = math.pow(1 + tax/100, 1/360)
        """
        se a taxa for medida em anos ela será convertida em taxa diária
        """
        
    if med_entrada == 'm':
        tax_diaria = math.pow(1 + tax/100, 1/30)
        """
        se a taxa for medida em meses ela será convertida para taxa diária
        """
        
    if med_entrada == 'd':
        tax_diaria = math.pow(1 + tax/100, 1/1)
        """
        se a taxa for medida em dias ela será convertida em taxa diária
        """
        
    if med_saida == 'a':
        tax_saida = math.pow(tax_diaria, 360)
        """
        se a taxa convertida for medida em anos a taxa diária será convertida
        em taxa anual
        """
     
    if med_saida == 'm':
        tax_saida = math.pow(tax_diaria, 30)
        """
        se a taxa convertida for medida em meses a taxa diária será convertida
        em taxa mensal
        """
    if med_saida == 'd':
        tax_saida = math.pow(tax_diaria, 1)
        """
        se a taxa convertida for medida em dias a taxa diária será convertida
        em taxa diária
        """
    return ((tax_saida - 1)*100)
    """
    retornando taxa convertida
    """
"""
função para fazer a conversão de taxa em uma medida de tempo para a taxa em
outra medida de tempo. Utilizando a taxa, sua medida de tempo e a medida a qual
essa taxa será convertida
"""

print("1 - Juros e Montante")
print("2 - Capital e Montante")
print("3 - Taxa e Montante")
print("4 - Periodo e Montante")
print("5 - Converter taxa")
opc = int(input("Opcao: "))

    
if opc == 1:
    """
    se a opção digitada for 1 os juros e montante serão calculados
    """
    c = float(input("Capital: "))
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    
    i = convert_taxa(i, med_entrada, med_saida)
    """
    convertendo taxa
    """
    
    m = montante(c, i, t)
    j = m - c
    """
    calculando montante e juros
    """
    
    print("Juros: {}".format(j))
    print("Montante: {}".format(m))
    
if opc == 2:
    """
    se a opção digitada for 2 o capital e montante serão calculados
    """
    j = float(input("Juros: "))
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ao ano\nm - ao mes\nd - ao dia\nOpcao: "))
    
    i = convert_taxa(i, med_entrada, med_saida)
    """
    convertendo taxa
    """
    
    c = capital(j, i, t)
    m = montante(c, i, t)
    """
    calculando capital e montante
    """
    
    print("Capital: {}".format(c))
    print("Montante: {}".format(m))
    
if opc == 3:
    """
    se a opcao for 3 a taxa e o montante serão calculados
    """
    
    j = float(input("Juros: "))
    c = float(input("Capital: "))
    t = float(input("Periodo: "))
    
    m = c + j
    i = taxa(c, m, t)
    """
    calculando montante e taxa
    """
    
    print("Taxa: {}".format(i))
    print("Montante: {}".format(m))
    
if opc == 4:
    """
    se a opção for 4 o período e os juros serão calculados
    """
    
    c = float(input("Capital: "))
    i = float(input("Taxa: "))
    j = float(input("Juros: "))
    
    m = c + j
    t = periodo(c, m, i)
    """
    calculando montante e período
    """
    
    print("Periodo: {}".format(t))
    print("Montante: {}".format(m))

if opc == 5:
    """
    se a opção for 5 a taxa será convertida para outra medida de tempo
    """
    i = float(input("Taxa: "))
    med_entrada = str(input("a - ano\nm - mes\nd - dia\nOpcao: "))
    t = float(input("Periodo: "))
    med_saida = str(input("a - ano\nm - mes\nd - dia\nOpcao: "))

    tax_convert = 100 * (math.pow(1 + convert_taxa(i, med_entrada, med_saida)/100, t) - 1)
    """
    convertendo taxa
    """

    print("{}% a.{} = {}% em {} {}".format(i, med_entrada, tax_convert, t, med_saida))
