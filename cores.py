# import colorama
# from colorama import Force, Back, Style
# colorama.init() for windows

print('hello world\n')

# IF SUCCESS, GREEN SHOULD BE USED
print('\033[32m' + 'hello world' + '\033[m'+' end of GREEN color in character\n')

# PROCESSING, YELLOW SHOULD BE USED
print('\033[33m' + 'hello world' + '\033[m'+' end of YELLOW color in character\n')


# IF FAIL, RED COLOR SHOULD BE USED
print('\033[31m' + 'hello world' + '\033[m'+' end of RED color in character\n')


'''
   1 vermelho = '\033[31m'
   2 verde = '\033[32m'
   3 azul = '\033[34m'
   4 
   5 ciano = '\033[36m'
   6 magenta = '\033[35m'
   7 amarelo = '\033[33m'
   8 preto = '\033[30m'
   9 
  10 branco = '\033[37m'
  11 
  12 restaura cor original = '\033[0;0m'
  13 negrito = '\033[1m'
  14 reverso = '\033[2m'
  15 
  16 fundo preto = '\033[40m'
  17 fundo vermelho = '\033[41m'
  18 fundo verde = '\033[42m'
  19 fundo amarelo = '\033[43m'
  20 fundo azul = '\033[44m'
  21 fundo magenta = '\033[45m'
  22 fundo ciano = '\033[46m'
  23 fundo branco = '\033[47m'
'''