
class HTML:
    reserve = {
        'html': 'HTML', 'head': 'HEAD', 'title': 'TITLE', 'body': 'BODY', 'h1': 'H1', 'h2': 'H2', 'h3': 'H3', 'h4': 'H4', 'h5': 'H5', 'h6': 'H6', 'p': 'PARRAFO',
        'br': 'SALTO_LINEA', 'img': 'IMAGEN', 'a': 'HIPERVINCULO', 'ul': 'LISTA', 'li': 'INDICE', 'style': 'STYLE', 'table': 'TABLE', 'th': 'CABECERA', 'tr': 'FILA_TABLA',
        'td': 'CELDA_TABLA', 'caption': 'CAPTION', 'colgroup': 'COLGROUP', 'col': 'COL', 'thead': 'THEAD', 'tbody': 'TBODY', 'tfoot': 'TFOOT', 'src': 'SRC', 'href': 'HREF'
    }

    operadores = {
        '<': 'ETIQUETA_INICIO', '>': 'ETIQUETA_CIERRE', '/': 'DIAGONAL', '=': 'ASSIGN', '"': 'COMILLAS', '!': 'EXCLAMACION'
    }

    ignore = [' ', '\t', '\n', '']

    def __init__(self):
        self.tokens = []

    def lexer(self, cadena):
        cadena += '#'
        estado = 0
        c = ''
        lexema = ''
        i = 0
        linea = 1
        columna = 1
        while i < len(cadena):
            c = cadena[i]
            if estado == 0:
                if str.isalpha(c) or c == '_':
                    lexema += c
                    estado = 1
                elif c == '>':
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna, 'orange'))
                    estado = 2
                elif c == '<':
                    lexema += c
                    estado = 4
                elif c == '/':
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna, 'orange'))
                elif c == '=':
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna, 'orange'))
                elif c == '!':
                    self.tokens.append(
                        (c, self.operadores.get(c), linea, columna, 'orange'))
                elif c == '"':
                    lexema += c
                    estado = 3
                elif c in self.ignore:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    self.tokens.append(
                        (c, 'ESPACIO', linea, columna, 'black'))
                else:
                    if c == '#' and i == len(cadena) - 1:
                        print('TERMINO EL ANALISIS')
                    else:
                        self.tokens.append(
                            (c, 'DESCONOCIDO', linea, columna, 'black'))
            elif estado == 1:
                if str.isalpha(c) or c == '_':
                    lexema += c
                else:
                    columna -= 1
                    if lexema in self.reserve.keys():
                        self.tokens.append(
                            (lexema, self.reserve.get(lexema), linea, columna, 'red'))
                    else:
                        self.tokens.append(
                            (lexema, 'IDENTIFICADOR', linea, columna, 'green'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 2:
                if c == '<':
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'TEXTO', linea, columna, 'black'))
                    lexema = ''
                    estado = 0
                    i -= 1
                elif c == '#' and i == len(cadena) - 1 and lexema not in self.ignore:
                    self.tokens.append(
                        (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                else:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
            elif estado == 3:
                if c == '"':
                    lexema += c
                    self.tokens.append(
                        (lexema, 'STRING', linea, columna, 'yellow'))
                    lexema = ''
                    estado = 0
                elif c == '#' and i == len(cadena) - 1:
                    self.tokens.append(
                        (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                else:
                    if c == '\n':
                        linea += 1
                        columna = 0
                    lexema += c
            elif estado == 4:
                if c == '!':
                    lexema += c
                    estado = 5
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, self.operadores.get(lexema), linea, columna, 'orange'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 5:
                if c == '-':
                    lexema += c
                    if '--' in lexema:
                        estado = 6
                else:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'INICIO', linea, columna, 'orange'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 6:
                if '-->' in lexema:
                    columna -= 1
                    self.tokens.append(
                        (lexema, 'COMENTARIO', linea, columna, 'gray'))
                    lexema = ''
                    linea += len(lexema.split('\n'))-1
                    estado = 0
                    i -= 1
                elif c == "#" and i == len(cadena)-1:
                    self.tokens.append(
                        (lexema, 'DESCONOCIDO', linea, columna, 'black'))
                else:
                    lexema += c
            columna += 1
            i += 1


