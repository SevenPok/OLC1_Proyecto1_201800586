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
    operadores = {'>': 'GREATER', '<': 'MINOR', '+': 'PLUS', '\\': 'SLASH', '"': 'COMILLAS_DOBLES',
                  '/': 'DIGONAL', '{': 'LEFT_KEY', '}': 'RIGHT_KEY', '.': 'DOT', '-': 'MINUS', '*': 'TIMES', '%': 'PORCENT', ',': 'COMMA',
                  ';': 'SEMICOLON', ':': 'COLON', '#': 'TAG', '=': 'ASSIGN', '(': 'LEFT_PARENTESIS', ')': 'RIGHT_PARENTESIS', '\'': 'COMILLAS'
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
                if str.isalpha(c) or c == '_':
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
                else:
                    if c == '#' and i == len(cadena) - 1:
                        print('TERMINO EL ANALISIS')
                    else:
                        self.tokens.append(
                            (c, 'DESCONOCIDO', linea, columna, 'black'))
            elif estado == 1:
                if str.isalpha(c) or str.isdigit(c) or c == '-' or c == '_':
                    lexema += c
                else:
                    columna -= 1
                    if lexema in self.reserve:
                        self.tokens.append(
                            (lexema, 'RESERVADO', linea, columna, 'green'))
                    else:
                        self.tokens.append(
                            (lexema, 'IDENTIFICADOR', linea, columna, 'red'))
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
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 3:
                if c == '"':
                    lexema += c
                    self.tokens.append(
                        (lexema, 'STRING', linea, columna, 'yellow'))
                    lexema = ''
                    estado = 0
                elif str.isalpha(c) or str.isdigit(c) or c in self.operadores or c == '_' or c in self.ignore:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 4:
                if c == '\'':
                    lexema += c
                    self.tokens.append(
                        (lexema, 'CHAR', linea, columna, 'yellow'))
                    lexema = ''
                    estado = 0
                elif str.isalpha(c) or str.isdigit(c) or c in self.operadores or c == '_' or c in self.ignore:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 5:
                if c == '*':
                    lexema += c
                    estado = 6
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, self.operadores.get('/'), linea, columna, 'orange'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 6:
                if '*/' in lexema:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'COMENTARIO', linea, columna, 'gray'))
                    lexema = ''
                    estado = 0
                    i -= 1
                elif c == "#" and i == len(cadena)-1:
                    self.tokens.append(
                        (lexema, "NO_RECONOCIDO", linea, columna, 'black'))
                else:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
            columna += 1
            i += 1

