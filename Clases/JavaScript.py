

class JavaScript:

    def __init__(self):
        self.reserve = {'var': 'VAR', 'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE', 'do': 'DO', 'continue': 'CONTINUE', 'break': 'BREAK', 'function': 'FUNCTION',
                        'return': 'RETURN', 'constructor': 'CONSTRUCTOR', 'class': 'CLASS', 'Math': 'MATH', 'pow': 'POW', 'true': 'BOOLEAN', 'false': 'BOOLEAN', 'this': 'THIS'}

        self.token = ['COMENTARIO_UNILINEA', 'COMENTARIO_MULTILINEA', 'ID', 'NUMERO_ENTERO', 'NUMERO_REAL', 'STRING', 'CHAR', 'BOOLEAN', 'PLUS',
                      'MINUS', 'TIMES', 'DIV', 'STATEMENT', 'ASSIGN', 'EQUALS', 'DIFERENT', 'GREATER', 'MINNOR', 'GREATER_EQUALS', 'MINOR_EQULAS',
                      'CONJUNCTION', 'DISJUNCTION', 'NEGATIVE', 'LEFT_PARENTESIS', 'RIGHT_PARENTESIS', 'PATH', 'DOT', 'COMMA', 'SEMICOLON', 'COLON',
                      'LEFT_KEY', 'RIGHT_KEY', 'LEFT_CORCHETE', 'RIGHT_CORCHETE']

        self.ignore = [' ', '    ']

    def match(self, cadena):
        cadena = cadena + "#"
        salida = []
        i = 0
        estado = 0
        lexema = ''
        c = ''
        linea = 1

        while i < len(cadena):
            c = cadena[i]

            if estado == 0:
                if str.isalpha(c):
                    lexema += c
                    estado = 1
                elif str.isdigit(c):
                    lexema += c
                    estado = 2
                elif c == '_':
                    lexema += c
                    estado = 1
                elif c == '+':
                    lexema += c
                    salida.append((lexema, self.token[8], linea, 'orange'))
                    lexema = ''
                elif c == '-':
                    lexema += c
                    salida.append((lexema, self.token[9], linea, 'orange'))
                    lexema = ''
                elif c == '*':
                    lexema += c
                    estado = 4
                elif c == '/':
                    lexema += c
                    estado = 13
                elif c == '=':
                    lexema += c
                    estado = 5
                elif c == '!':
                    lexema += c
                    estado = 6
                elif c == '<':
                    lexema += c
                    estado = 9
                elif c == '>':
                    lexema += c
                    estado = 10
                elif c == '|':
                    lexema += c
                    estado = 11
                elif c == '&':
                    lexema += c
                    estado = 12
                elif c == '(':
                    lexema += c
                    salida.append((lexema, self.token[23], linea, 'orange'))
                    lexema = ''
                elif c == ')':
                    lexema += c
                    salida.append((lexema, self.token[24], linea, 'orange'))
                    lexema = ''
                elif c == '.':
                    lexema += c
                    salida.append((lexema, self.token[26], linea, 'orange'))
                    lexema = ''
                elif c == ':':
                    lexema += c
                    salida.append((lexema, self.token[29], linea, 'orange'))
                    lexema = ''
                elif c == ',':
                    lexema += c
                    salida.append((lexema, self.token[27], linea, 'orange'))
                    lexema = ''
                elif c == ';':
                    lexema += c
                    salida.append((lexema, self.token[28], linea, 'orange'))
                    lexema = ''
                elif c == '"':
                    lexema += c
                    estado = 7
                elif c == '\'':
                    lexema += c
                    estado = 8
                elif c == '{':
                    lexema += c
                    salida.append((lexema, self.token[30], linea, 'orange'))
                    lexema = ''
                elif c == '}':
                    lexema += c
                    salida.append((lexema, self.token[31], linea, 'orange'))
                    lexema = ''
                elif c == '[':
                    lexema += c
                    salida.append((lexema, self.token[32], linea, 'orange'))
                    lexema = ''
                elif c == ']':
                    lexema += c
                    salida.append((lexema, self.token[33], linea, 'orange'))
                    lexema = ''
                else:
                    if c == '#' and i == len(cadena) - 1:
                        print("Termino el analisis")
                    elif c == '\n':
                        linea += 1
                        salida.append((c, "SALTO DE LINEA", linea, 'black'))
                        lexema = ''
                    elif c in self.ignore:
                        salida.append((c, "ESPACIO", linea, 'black'))
                        lexema = ''
                    else:
                        lexema += c
                        salida.append(
                            (lexema, "NO_RECONOCIDO", linea, 'black'))
                        lexema = ''
            elif estado == 1:
                if str.isalpha(c):
                    lexema += c
                elif str.isdigit(c):
                    lexema += c
                elif c == '_':
                    lexema += c
                else:
                    if lexema in self.reserve.keys():
                        if lexema == 'true' or lexema == 'false':
                            salida.append(
                                (lexema, self.reserve.get(lexema), linea, 'blue'))
                        else:
                            salida.append(
                                (lexema, self.reserve.get(lexema), linea, 'red'))
                    else:
                        salida.append((lexema, self.token[2], linea, 'green'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 2:
                if str.isdigit(c):
                    lexema += c
                elif c == '.':
                    lexema += c
                    estado = 3
                else:
                    salida.append((lexema, self.token[3], linea, 'blue'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 3:
                if str.isdigit(c):
                    lexema += c
                else:
                    salida.append((lexema, self.token[4], linea, 'blue'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 4:
                if c == '=':
                    lexema += c
                else:
                    if lexema == '*=':
                        salida.append(
                            (lexema, self.token[13], linea, 'orange'))
                    else:
                        salida.append((lexema, self.token[10], linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 5:
                if c == '=':
                    lexema += c
                else:
                    if lexema == '==':
                        salida.append(
                            (lexema, self.token[14], linea, 'orange'))
                    elif lexema == '=':
                        salida.append(
                            (lexema, self.token[12], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'NO_RECONOCIDO', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 6:
                if c == '=':
                    lexema += c
                else:
                    if lexema == '!=':
                        salida.append(
                            (lexema, self.token[15], linea, 'orange'))
                    elif lexema == '!':
                        salida.append(
                            (lexema, self.token[22], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'NO_RECONOCIDO', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 7:
                if c == '"':
                    lexema += c
                    salida.append((lexema, self.token[5], linea, 'yellow'))
                    lexema = ''
                    estado = 0
                else:
                    if c == "#" and i == len(cadena) - 1:
                        salida.append(
                            (lexema, "NO_RECONOCIDO", linea, 'black'))
                        lexema = ''
                        estado = 0
                        i -= 1
                    else:
                        lexema += c
            elif estado == 8:
                if c == '\'':
                    lexema += c
                    salida.append((lexema, self.token[6], linea, 'yellow'))
                    lexema = ''
                    estado = 0
                else:
                    if c == "#" and i == len(cadena) - 1:
                        salida.append(
                            (lexema, "NO_RECONOCIDO", linea, 'black'))
                        lexema = ''
                        estado = 0
                        i -= 1
                    else:
                        lexema += c
            elif estado == 9:
                if c == '=':
                    lexema += c
                else:
                    if lexema == '<=':
                        salida.append(
                            (lexema, self.token[19], linea, 'orange'))
                    elif lexema == '<':
                        salida.append(
                            (lexema, self.token[17], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'No  reconocido', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 10:
                if c == '=':
                    lexema += c
                else:
                    if lexema == '>=':
                        salida.append(
                            (lexema, self.token[18], linea, 'orange'))
                    elif lexema == '>':
                        salida.append(
                            (lexema, self.token[16], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'No  reconocido', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 11:
                if c == '|':
                    lexema += c
                else:
                    if lexema == '||':
                        salida.append(
                            (lexema, self.token[21], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'No  reconocido', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 12:
                if c == '&':
                    lexema += c
                else:
                    if lexema == '&&':
                        salida.append(
                            (lexema, self.token[20], linea, 'orange'))
                    else:
                        salida.append(
                            (lexema, 'No  reconocido', linea, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 13:
                if c == '/':
                    lexema += c
                    estado = 14
                elif c == '*':
                    lexema += c
                    estado = 15
                else:
                    salida.append((lexema, self.token[11], linea, 'orange'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 14:
                if '\n' in lexema:
                    salida.append((lexema, self.token[0], linea, 'gray'))
                    linea += 1
                    lexema = ''
                    estado = 0
                    i -= 1
                elif c == "#" and i == len(cadena)-1:
                    salida.append((lexema, self.token[0], linea, 'gray'))
                else:
                    lexema += c
            elif estado == 15:
                if '*/' in lexema:
                    salida.append((lexema, self.token[1], linea, 'gray'))
                    linea += len(lexema.split('\n'))-1
                    lexema = ''
                    estado = 0
                    i -= 1
                elif c == "#" and i == len(cadena)-1:
                    salida.append((lexema, "NO_RECONOCIDO", linea, 'black'))
                else:
                    lexema += c
            i += 1
        return salida
