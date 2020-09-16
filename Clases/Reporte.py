import os


class Reporte:
    def __init__(self, tokens):
        self.tokens = tokens

    def reporte_analisis_lexico(self, titulo):
        contador = 1
        contenido = """
<html>
    <head><title>Reporte</title></head>
    <body>
        """
        contenido += "<h1>"+titulo+"</h1>\n"
        tabla = """
        <table  border="1" style="text-align:center;">
        <tr>
        <td><strong>No.</strong></td>
        <td><strong>Linea</strong></td>
        <td><strong>Columna</strong></td>
        <td><strong>Desccripción</strong></td>
         </tr>
        """
        for i in self.tokens:
            if i[1] == 'DESCONOCIDO' or i[1] == 'NO_RECONOCIDO':
                tabla += '      <tr>\n'

                tabla += "      <td>" + str(contador) + "</td>\n"
                tabla += "      <td>" + str(i[2]) + "</td>\n"
                tabla += "      <td>" + str(i[3]) + "</td>\n"
                tabla += "      <td>El caracter \'" + \
                    i[0] + "\' no pertenece al lenguaje" + "</td>\n"

                tabla += "      </tr>\n\n"
                contador += 1

        tabla += "      </table>\n"
        contenido += tabla + """
    </body>
</html>
        """
        titulo = titulo + ".html"
        f = open(titulo, 'wb')
        mensaje = bytes(contenido, 'utf-8')
        f.write(mensaje)
        f.close()
        os.startfile(titulo)

    def reporte_analisis_sintactico(self, titulo):
        contador = 1
        contenido = """
<html>
    <head><title>Reporte</title></head>
    <body>
        """
        contenido += "<h1>"+titulo+"</h1>\n"
        tabla = """
        <table  border="1" style="text-align:center;">
        <tr>
        <td><strong>Linea</strong></td>
        <td><strong>Operacion</strong></td>
        <td><strong>Analisis</strong></td>
         </tr>
        """
        for i in self.tokens:
            tabla += '      <tr>\n'
            tabla += "      <td>" + str(contador) + "</td>\n"
            tabla += '      <td>' + str(i[0]) + '</td>\n'
            if i[1]:
                tabla += '      <td>Correcto</td>\n'
            else:
                tabla += '      <td>Incorrecto</td>\n'
            tabla += "      </tr>\n\n"
            contador += 1

        tabla += "      </table>\n"
        contenido += tabla + """
    </body>
</html>
        """
        titulo = titulo + ".html"
        f = open(titulo, 'wb')
        mensaje = bytes(contenido, 'utf-8')
        f.write(mensaje)
        f.close()
        os.startfile(titulo)
