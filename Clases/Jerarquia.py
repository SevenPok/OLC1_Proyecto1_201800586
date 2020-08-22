class Aritmetica:

    operadores = {'+': 'PLUS', '-': 'MINUS', '*': 'TIMES',
                  '/': 'DIV', '(': 'LEFT_PARENTESIS', ')': 'RIGHT_PARENTESIS'}
    ignore = [' ', '\t', '\n']

    def __init__(self):
        self.tokens = []
        self.errores_lexicos = []
        self.errores_sintacticos = []

    def lexer(self, cadena):
        cadena += '#'
        lexema = ''
        estado = 0
        c = ''
        i = 0
        linea = 1
        columna = 1
        while i < len(cadena):
            c = cadena[i]
            if estado == 0:
                if str.isdigit(c):
                    lexema += c
                    estado = 1
                elif str.isalpha(c) or c == '_':
                    lexema += c
                    estado = 4
                elif c in self.operadores.keys():
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna))
                elif c in self.ignore:
                    if c == '\n':
                        linea += 1
                        columna = 0
                else:
                    if c == '#' and i == len(cadena) - 1:
                        print('ANALISIS LEXICO TERMINADO')
                    else:
                        self.errores_lexicos.append(
                            (c, 'DESCONOCIDO', linea, columna))
            elif estado == 1:
                if str.isdigit(c):
                    lexema += c
                elif c == '.':
                    lexema += c
                    estado = 2
                else:
                    columna -= 1
                    self.tokens.append((lexema, 'ENTERO', linea, columna))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 2:
                if str.isdigit(c):
                    lexema += c
                    estado = 3
                else:
                    columna -= 1
                    self.errores_lexicos.append(
                        (lexema, 'DESCONOCIDO', linea, columna))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 3:
                if str.isdigit(c):
                    lexema += c
                else:
                    columna -= 1
                    self.tokens.append((lexema, 'DECIMAL', linea, columna))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 4:
                if str.isalpha(c) or str.isdigit(c) or c == '_':
                    lexema += c
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'IDENTIFICADOR', linea, columna))
                    lexema = ''
                    estado = 0
                    i -= 1
            i += 1
            columna += 1

    def sintax(self):
        pass


a = Aritmetica()
a.lexer('455\n*/ @ _var1 52')
print('=========TOKENS=========')
for i in a.tokens:
    print(i)
print('=========ERRORES========')
for i in a.errores_lexicos:
    print(i)
