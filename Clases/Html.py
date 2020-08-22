
class HTML:
    reserve = {
        'html': 'HTML', 'head': 'HEAD', 'title': 'TITLE', 'body': 'BODY', 'h1': 'H1', 'h2': 'H2', 'h3': 'H3', 'h4': 'H4', 'h5': 'H5', 'h6': 'H6', 'p': 'PARRAFO',
        'br': 'SALTO_LINEA', 'img': 'IMAGEN', 'a': 'HIPERVINCULO', 'ul': 'LISTA', 'li': 'INDICE', 'style': 'STYLE', 'table': 'TABLE', 'th': 'CABECERA', 'tr': 'FILA_TABLA',
        'td': 'CELDA_TABLA', 'caption': 'CAPTION', 'colgroup': 'COLGROUP', 'col': 'COL', 'thead': 'THEAD', 'tbody': 'TBODY', 'tfoot': 'TFOOT', 'src': 'SRC', 'href': 'HREF'
    }

    operadores = {
        '<': 'ETIQUETA_INICIO', '>': 'ETIQUETA_CIERRE', '/': 'DIAGONAL', '=': 'ASSIGN', '+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '(': 'PARENTESIS_INICIO', ')': 'PARENTESIS_FIN',
        '[': 'CORCHETE_INICIO', ']': 'CORCHETE_FIN'
    }

    ignore = [' ', '    ', '\n']

    def __init__(self):
        self.tokens = []
    