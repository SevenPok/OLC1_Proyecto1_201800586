#!/usr/bin/env python3
import re


class CSS:
    reserve = ['color', 'background-color', 'background-image',
               'border', 'Opacity', 'background',
               'text-align', 'font-family', 'font-style',
               'font-weight', 'font-size', 'font',
               'padding-left', 'padding-right', 'padding-bottom',
               'padding-top', 'padding', 'display',
               'line-height', 'width', 'height',
               'margin-top', 'margin-right', 'margin-bottom',
               'margin-left', 'margin', 'border-style',
               'display', 'position', 'bottom',
               'top', 'right', 'left',
               'float', 'clear', 'max-width',
               'min-width', 'max-height', 'min-height',
               'px', 'em', 'vh', 'vw', 'in',
               'cm', 'mm', 'pt', 'pc', 'relative', 'rgba', 'url', 'width',
               'height', 'content', 'inline-block'
               ]
    operadores = {'"': 'COMILLAS_DOBLES', '/': 'DIGONAL', '{': 'LEFT_KEY', '}': 'RIGHT_KEY', '.': 'DOT', '-': 'MINUS', '%': 'PORCENT', ',': 'COMMA',
                  ';': 'SEMICOLON', ':': 'COLON', '#': 'TAG', '(': 'LEFT_PARENTESIS', ')': 'RIGHT_PARENTESIS', '\'': 'COMILLAS', '*': 'TIMES'
                  }
    ignore = [' ', '\t', '\n']

    def __init__(self):
        self.tokens = []

    def lexer(self, cadena):
        cadena += '#'
        estado = 0
        lexema = ''
        c = ''
        i = 0
        linea = 1
        columna = 1
        while i < len(cadena):
            c = cadena[i]

            if estado == 0:
                if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or c == '_':
                    lexema += c
                    estado = 1
                elif str.isdigit(c):
                    lexema += c
                    estado = 2
                elif c == '"':
                    lexema += c
                    estado = 3
                elif c == '\'':
                    lexema += c
                    estado = 4
                elif c == '/':
                    lexema += c
                    estado = 5
                elif c in self.ignore:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    self.tokens.append((c, 'ESPACIO', linea, columna, 'black'))
                    lexema = ''
                elif c in self.operadores and i != len(cadena) - 1:
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna, 'orange'))
                    print('Estado: ', estado, ' Token: ', c)
                else:
                    if c == '#' and i == len(cadena) - 1:
                        print('TERMINO EL ANALISIS')
                    else:
                        self.tokens.append(
                            (c, 'DESCONOCIDO', linea, columna, 'black'))
                        print('Estado: ', estado, ' Error: ', c)
            elif estado == 1:
                if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or str.isdigit(c) or c == '-' or c == '_':
                    lexema += c
                else:
                    columna -= 1
                    if lexema in self.reserve:
                        self.tokens.append(
                            (lexema, 'RESERVADO', linea, columna, 'red'))
                        print('Estado: ', estado, ' Token: ', lexema.upper())
                    else:
                        self.tokens.append(
                            (lexema, 'IDENTIFICADOR', linea, columna, 'green'))
                        print('Estado: ', estado, ' Token: IDENTIFICADOR')
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 2:
                if str.isdigit(c):
                    lexema += c
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'NUMERO', linea, columna, 'blue'))
                    print('Estado: ', estado, ' Token: NUMERO')
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 3:
                if c == '"':
                    lexema += c
                    self.tokens.append(
                        (lexema, 'STRING', linea, columna, 'yellow'))
                    print('Estado: ', estado, ' Token: STRING')
                    lexema = ''
                    estado = 0
                else:
                    if c == '#' and i == len(cadena) - 1:
                        columna -= 1
                        self.tokens.append(
                            (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                        lexema = ''
                        estado = 0
                        i -= 1
                    else:
                        lexema += c
            elif estado == 4:
                if c == '\'':
                    lexema += c
                    self.tokens.append(
                        (lexema, 'CHAR', linea, columna, 'yellow'))
                    print('Estado: ', estado, ' Token: CHAR')
                    lexema = ''
                    estado = 0
                else:
                    if c == '#' and i == len(cadena) - 1:
                        columna -= 1
                        self.tokens.append(
                            (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                        lexema = ''
                        estado = 0
                        i -= 1
                    else:
                        lexema += c
            elif estado == 5:
                if c == '*':
                    lexema += c
                    estado = 6
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'DIAGONAL', linea, columna, 'black'))
                    print('Estado: ', estado, ' Token: DIAGONAL')
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 6:
                if '*/' in lexema:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'COMENTARIO', linea, columna, 'gray'))
                    print('Estado: ', estado, ' Token: COMENTARIO')
                    lexema = ''
                    estado = 0
                    i -= 1
                elif c == "#" and i == len(cadena)-1:
                    self.tokens.append(
                        (lexema, "DESCONOCIDO", linea, columna, 'black'))
                    print('Estado: ', estado, ' Error: ', lexema)
                else:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
            columna += 1
            i += 1
