# Bem-vindo ao meu primeiro código em Python :)
understand = input("Olá, muito obrigado por acreditar no meu primeiro projeto em Python! Antes de tudo tenho que explicar uma coisinha.\n\nEsse projeto calcula a média de suas notas escolares no boletim do bimestre de acordo com suas notas (óbvio) junto com sua média de atividades que é 10 se você tiver feito todas. Se você não tiver feitos todas suas atividades, sai daqui e vai estudar! (brincadeira).\n\nCaso não tenha determinada matéria que pedir sua nota, apenas informe a mesma como 0.\n\nSe você entendeu tudo digite 'Sim', se não, digite 'Não': ")

if understand == "Não":
    print("Tente ler a explicação novamente e então execute o código de novo.")
elif understand == "Sim":
    # Português
    por = float(input("Informe sua nota de Língua Portuguesa: "))
    calcpor = (por + 10) / 2
    if(por < 1):
        print(0)
    elif(por >= 1):
        print("Sua nota em língua portuguesa foi: ", calcpor)
    # Matemática
    mat = float(input("Informe sua nota de Matemática: "))
    calcmat = (mat + 10) / 2
    if(mat < 1):
        print(0)
    elif(mat >= 1):
        print("Sua nota em matemática foi: ", calcmat)
    # História
    his = float(input("Informe sua nota de História: "))
    calchis = (his + 10) / 2
    if(his < 1):
        print(0)
    elif(his >= 1):
        print("Sua nota em história foi: ", calchis)
    # Biologia
    bio = float(input("Informe sua nota de Biologia: "))
    calcbio = (bio + 10) / 2
    if(bio < 1):
        print(0)
    elif(bio >= 1):
        print("Sua nota em biologia foi: ", calcbio)
    # Química
    qui = float(input("Informe sua nota de Química: "))
    calcqui = (qui + 10) / 2
    if(qui < 1):
        print(0)
    elif(qui >= 1):
        print("Sua nota em química foi: ", calcqui)
    # Geografia
    geo = float(input("Informe sua nota de Geografia: "))
    calcgeo = (geo + 10) / 2
    if(geo < 1):
        print(0)
    elif(geo >= 1):
        print("Sua nota em geografia foi: ", calcgeo)
    # Física
    fis = float(input("Informe sua nota de Física: "))
    calcfis = (fis + 10) / 2
    if(fis < 1):
        print(0)
    elif(fis >= 1):
        print("Sua nota em física foi: ", calcfis)
    # Filosofia
    fil = float(input("Informe sua nota de Filosofia: "))
    calcfil = (fil + 10) / 2
    if(fil < 1):
        print(0)
    elif(fil >= 1):
        print("Sua nota em filosofia foi: ", calcfil)
    # Sociologia
    soc = float(input("Informe sua nota de Sociologia: "))
    calcsoc = (soc + 10) / 2
    if(soc < 1):
        print(0)
    elif(soc >= 1):
        print("Sua nota em sociologia: ", calcsoc)
    # Inglês
    ing = float(input("Informe sua nota de Inglês: "))
    calcing = (ing + 10) / 2
    if(ing < 1):
        print(0)
    elif(ing >= 1):
        print("Sua nota em inglês foi: ", calcing)
    # Espanhol
    esp = float(input("Informe sua nota de Espanhol: "))
    calcesp = (esp + 10) / 2
    if(esp < 1):
        print(0)
    elif(esp >= 1):
        print("Sua nota em espanhol foi: ", calcesp)
    #Educação Física
    edu = float(input("Informe sua nota de Educação Física: "))
    calcedu = (edu + 10) / 2
    if(edu < 1):
        print(0)
    elif(edu >= 1):
        print("Sua nota em educação física foi: ", calcedu)
    # Artes
    art = float(input("Informe sua nota de Artes: "))
    calcart = (art + 10) / 2
    if(art < 1):
        print(0)
    elif(art >= 1):
        print("Sua nota em artes foi: ", calcart)