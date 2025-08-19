import random
import re
import os

#CORES
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

#variaveis
linha = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
escolha_comp = []
escolha_pessoa = []
ganhou = False
placar_comp = 0
placar_pess = 0
jogador_da_vez = 0
x = f"{BLUE}X{RESET}"
o = f"{RED}O{RESET}"

#CRIANDO A MATRIZ 3X3
def matriz():
    print("",f"{RED}*{RESET}" * 17,f"\n {RED}*{RESET}{CYAN} JOGO DA VELHA {RESET}{RED}*{RESET}\n",f"{RED}*{RESET}"*17,"\n")
    print(f"{BOLD}PLACAR: COMPUTADOR = {RED}{placar_comp}{BOLD} | JOGADOR = {BLUE}{placar_pess}{RESET}\n")
    print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
    print("-----------")
    print(f" {linha[3]} | {linha [4]} | {linha[5]} ")
    print("-----------")
    print(f" {linha[6]} | {linha [7]} | {linha[8]} ")
    print(f"\nEscolhas do computador: {escolha_comp}")
    print(f"Escolhas dO JOGADOR: {escolha_pessoa}")
    

#JOGADA DO COMPUTADOR
def jogada_computador():
  while True:
    pos_comp = random.randint(0, 8)
    if linha[pos_comp] != x and linha[pos_comp] != o:
      linha[pos_comp] = o
      escolha_comp.append(pos_comp + 1)
      os.system('clear')
      matriz()
      break
    
#JOGADA DA PESSOA
def jogada_pessoa():
  while True:
    pos = int(input("\nEscolha uma posição: ")) - 1
    if pos == 0 or pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8:
      if linha[pos] != "" and linha[pos] != o and linha[pos] != x:
        linha[pos] = x
        escolha_pessoa.append(pos + 1)
        
        os.system('clear')
        matriz()
        break
      else:
          print("\nPESSOA, Esta jogada já foi escolhina, tente novamente\n")
    else:
      print(f"{RED}\nEscolha uma posição válida.{RESET}")

#VERIFICA SE ALGUÉM GANHOU
def Condicao_Ganhador():
  if linha[0] == linha[1] == linha[2]:
    if linha[0] == linha[1] == linha[2] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[0] == linha[4] == linha[8]:
    if linha[0] == linha[4] == linha[8] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[0] == linha[3] == linha[6]:
    if linha[0] == linha[3] == linha[6] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[6] == linha[7] == linha[8]:
    if linha[6] == linha[7] == linha[8] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[2] == linha[4] == linha[6]:
    if linha[2] == linha[4] == linha[6] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[2] == linha[5] == linha[8]:
    if linha[2] == linha[5] == linha[8] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[1] == linha[4] == linha[7]:
    if linha[1] == linha[4] == linha[7] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  elif linha[3] == linha[4] == linha[5]:
    if linha[3] == linha[4] == linha[5] == x:
      vencedor = "VOCÊ"
    else:
      vencedor = "COMPUTADOR"
    return vencedor
  else:
    empate = True
    for i in linha:
      if i != x and i != o:
        empate = False
        break
    if empate == True:
      vencedor = "EMPATE"
      return vencedor
    else:
      return None
    

def identifica_ganhador(condicao_ganhador, placar_comp, placar_pess, ganhou):
  if condicao_ganhador == "VOCÊ":
    placar_pess = placar_pess + 1
    print("\nPARABÉNS, você ganhou!")
  elif condicao_ganhador == "COMPUTADOR":
    placar_comp = placar_comp + 1
    print("\nVOCÊ PERDEU! Mais sorte na próxima vez.")
  elif condicao_ganhador == "EMPATE":
    print("DEU VELHA! O JOGO EMPATOU.")
  
  return placar_comp, placar_pess

while True:  
  if jogador_da_vez == 0:
    jogada_computador()
    condicao_ganhador = Condicao_Ganhador()
    placar_comp, placar_pess = identifica_ganhador(condicao_ganhador, placar_comp, placar_pess, ganhou)
    os.system('clear')
    matriz()
    jogador_da_vez = 1
  elif jogador_da_vez == 1:  
    jogada_pessoa()
    condicao_ganhador = Condicao_Ganhador()
    placar_comp, placar_pess = identifica_ganhador(condicao_ganhador, placar_comp, placar_pess, ganhou)
    os.system('clear')
    matriz()
    jogador_da_vez = 0
  
  if condicao_ganhador == "VOCÊ" or condicao_ganhador == "COMPUTADOR" or condicao_ganhador == "EMPATE":
    resp = input("\nDeseja jogar novamente? (S/N): ").upper()
    if resp == "S":
      jogador_da_vez = 0
      cont = 0
      for i in linha:          
        linha[cont] = f"{cont + 1}"
        cont = cont + 1

      while len(escolha_comp) > 0:
        escolha_comp.remove(escolha_comp[0])
      while len(escolha_pessoa) > 0:
        escolha_pessoa.remove(escolha_pessoa[0])

    elif resp == "N":
      os.system('clear')
      matriz()
      print(f"\n{RED}FIM DE JOGO!")
      break
