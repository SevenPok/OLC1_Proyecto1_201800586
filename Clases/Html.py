
class HTML:
    reserve = {
        'html': 'HTML', 'head': 'HEAD', 'title': 'TITLE', 'body': 'BODY', 'h1': 'H1', 'h2': 'H2', 'h3': 'H3', 'h4': 'H4', 'h5': 'H5', 'h6': 'H6', 'p': 'PARRAFO',
        'br': 'SALTO_LINEA', 'img': 'IMAGEN', 'a': 'HIPERVINCULO', 'ul': 'LISTA', 'li': 'INDICE', 'style': 'STYLE', 'table': 'TABLE', 'th': 'CABECERA', 'tr': 'FILA_TABLA',
        'td': 'CELDA_TABLA', 'caption': 'CAPTION', 'colgroup': 'COLGROUP', 'col': 'COL', 'thead': 'THEAD', 'tbody': 'TBODY', 'tfoot': 'TFOOT', 'src': 'SRC', 'href': 'HREF'
    }

    operadores = {
        '<': 'ETIQUETA_INICIO', '>': 'ETIQUETA_CIERRE', '/': 'DIAGONAL', '=': 'ASSIGN', '+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '(': 'PARENTESIS_INICIO', ')': 'PARENTESIS_FIN',
        '[': 'CORCHETE_INICIO', ']': 'CORCHETE_FIN', '{': 'LEFT_KEY', '}': 'RIGHT_KEY', '.': 'dot'
    }

    ignore = [' ', '\t', '\n']

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
                if str.isalpha(c):
                    lexema += c
                    estado = 1
                elif str.isdigit(c):
                    lexema += c
                    estado = 2
                elif c in self.operadores:
                    lexema += c
                    estado = 4
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
                if str.isalpha(c) or str.isdigit(c) or c == '_':
                    lexema += c
                else:
                    columna = -1
                    if lexema in self.reserve.keys():
                        self.tokens.append(
                            (lexema, self.reserve.get(lexema), linea, columna, 'green'))
                    else:
                        self.tokens.append(
                            (lexema, 'IDENTIFICADOR', linea, columna, 'green'))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 2:
                if str.isdigit(c):
                    lexema += c
                elif c == '.':
                    pass
            columna += 1
            i += 1
