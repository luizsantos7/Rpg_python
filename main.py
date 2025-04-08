import random

print("Bem vindo caçador, este é o mágico mundo de ViLunaris")
nome_player = input("Digite seu Nome:")

hp = 100
dano = 10
level = 1
exp = 0

player = {
    'nome': nome_player,       
    'hp': hp*level,
    'ataque':25*level,
    
}


def criar_monstro():
    nomes_monstros = ["Orc", "Goblin", "Slime", "Titan", "Rei Demonio"]
    tipos_monstros = ['Terra', 'Agua', 'Fogo', 'Grama'] 
    level_monstro = random.randint(1,10)
    nome = random.choice(nomes_monstros)
    tipo = random.choice(tipos_monstros)
    
    monstro = {
        'nome':nome,
        'tipo':tipo,
        'hp': hp*level_monstro,
        'dano':15*level_monstro,
        'level':level_monstro,
    }

    return monstro

monstro_gerado = criar_monstro()

def criar_equipamento():
    tipo_equip=['capacete','armadura','espada','clava']
    raridades=['comum','raro','epico','lendario']
    buff_equip = ['vida', 'dano']

    tipo = random.choice(tipo_equip)
    raridade=random.choice(raridades)
    buff = random.choice(buff_equip)

    if raridade == 'comum':
        valor_buff = random.randint(15,25)

        if buff== 'vida':
            player['hp'] =+ valor_buff
        else:
            player[dano] =+ valor_buff


    elif raridade == 'raro':
        valor_buff = random.randint(26,50)

        if buff== 'vida':
            player['hp'] =+ valor_buff
        else:
            player[dano] =+ valor_buff


    elif raridade == 'epico':
        valor_buff = random.randint(51,75)

        if buff== 'vida':
            player['hp'] =+ valor_buff
        else:
            player[dano] =+ valor_buff


    elif raridade == 'lendario':
        valor_buff = random.randint(75,125)

        if buff== 'vida':
            player['hp'] =+ valor_buff
        else:
            player[dano] =+ valor_buff

    item = {
        'tipo': tipo,
        'raridade': raridade,
        'buff': f'+ {valor_buff} pontos de atributo.',
    }

    return item

item_gerado = criar_equipamento()

print(f"NOME:{monstro_gerado['nome']} // TIPO:{monstro_gerado['tipo']} // LEVEL:{monstro_gerado['level']} // HP:{monstro_gerado['hp']} //")
print(f"ITEM:{item_gerado['tipo']} // RARIDADE: {item_gerado['raridade']} // BUFF: {item_gerado['buff']}")

