class automata:
    def __init__(self, cadena):
        self.cadena = cadena

    def pushdown(self):
        self.cadena.append('')
        # estado = 'i'
        pila = []
        # estado = 'p'
        pila.append('#')
        pila.append('E')
        # estado = 'q'
        c = self.cadena.pop(0)
        while pila[len(pila) - 1] != '#':

            if pila[len(pila) - 1] == 'E':
                if c == ')':
                    pila.pop()
                else:
                    pila.pop()
                    pila.append('E\'')
                    pila.append('T')
            elif pila[len(pila) - 1] == 'E\'':
                if c == '+':
                    pila.pop()
                    pila.append('E\'')
                    pila.append('T')
                    pila.append('+')
                elif c == '-':
                    pila.pop()
                    pila.append('E\'')
                    pila.append('T')
                    pila.append('-')
                else:
                    pila.pop()
            elif pila[len(pila) - 1] == 'T':
                pila.pop()
                pila.append('T\'')
                pila.append('F')
            elif pila[len(pila) - 1] == 'T\'':
                if c == '*':
                    pila.pop()
                    pila.append('T\'')
                    pila.append('F')
                    pila.append('*')
                elif c == '/':
                    pila.pop()
                    pila.append('T\'')
                    pila.append('F')
                    pila.append('/')
                else:
                    pila.pop()
            elif pila[len(pila) - 1] == 'F':
                if c == '(':
                    pila.pop()
                    pila.append(')')
                    pila.append('E')
                    pila.append('(')
                elif c == 'ENTERO':
                    pila.pop()
                    pila.append('ENTERO')
                elif c == 'DECIMAL':
                    pila.pop()
                    pila.append('DECIMAL')
                elif c == 'IDENTIFICADOR':
                    pila.pop()
                    pila.append('IDENTIFICADOR')
                else:
                    return False
            elif pila[len(pila) - 1] == c:
                if c == '(':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == ')':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == '+':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == '-':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == '*':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == '/':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == 'ENTERO':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == 'DECIMAL':
                    pila.pop()
                    c = self.cadena.pop(0)
                elif c == 'IDENTIFICADOR':
                    pila.pop()
                    c = self.cadena.pop(0)
                else:
                    return False
            else:
                return False

        pila.pop()
        if len(pila) == 0 and c == '':
            # estado = f
            return True
        return False
