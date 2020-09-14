#!/usr/bin/env python3
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Clases.JavaScript import JavaScript as js
from Clases.CSS import CSS as css
from Clases.Html import HTML as html
from Clases.Jerarquia import Aritmetica as ar
from Clases.Reporte import Reporte
import os
import re

root = Tk()
root.title("LABORATORIO")
root.configure(background="black")
extension = ["", ""]
root.resizable(0, 0)
archivo = ""


def nuevo():
    global archivo
    editor.delete(1.0, END)  # ELIMINAR EL CONTENIDO
    archivo = ""


def abrir():
    global archivo, extension
    archivo = filedialog.askopenfilename(
        title="Abrir Archivo", initialdir="C:/")
    os.system("cls")
    entrada = open(archivo)
    extension = str(archivo).split('.')
    content = entrada.read()
    editor.delete(1.0, END)
    editor2.delete(1.0, END)
    if extension[1] == 'js':
        a = js()
        for c in a.match(content):
            editor.insert(INSERT, c[0], c[1])
            editor.tag_config(c[1], foreground=c[4])
            if c[1] == 'NO_RECONOCIDO':
                linea = 'linea ' + str(c[2]) + ' columna ' + \
                    str(c[3]) + ' caracter: ' + c[0] + '\n'
                editor2.insert(INSERT, linea)
    elif extension[1] == 'css':
        a = css()
        a.lexer(content)
        for c in a.tokens:
            editor.insert(INSERT, c[0], c[1])
            editor.tag_config(c[1], foreground=c[4])
            if c[1] == 'DESCONOCIDO':
                linea = 'linea ' + str(c[2]) + ' columna ' + \
                    str(c[3]) + ' caracter: ' + c[0] + '\n'
                editor2.insert(INSERT, linea)
    elif extension[1] == 'rmt':
        #editor.insert(END, content)
        content = content.split('\n')
        for linea in content:
            a = ar()
            a.lexer(linea)
            for c in a.errores_lexicos:
                linea = 'linea ' + str(c[2]) + ' columna ' + \
                    str(c[3]) + ' caracter: ' + c[0] + '\n'
                editor2.insert(INSERT, linea)

        for linea in content:
            a = ar()
            a.lexer(linea)
            for c in a.tokens:
                editor.insert(INSERT, c[0], c[1])
                editor.tag_config(c[1], foreground=c[4])
            if a.syntax():
                editor2.insert(INSERT, 'Correcto\n')
            else:
                editor2.insert(INSERT, 'Incorrecto\n')
            editor.insert(INSERT, '\n')

    elif extension[1] == 'html':
        a = html()
        a.lexer(content)
        for c in a.tokens:
            editor.insert(INSERT, c[0], c[1])
            editor.tag_config(c[1], foreground=c[4])
            if c[1] == 'DESCONOCIDO':
                linea = 'linea ' + str(c[2]) + ' columna ' + \
                    str(c[3]) + ' caracter: ' + c[0] + '\n'
                editor2.insert(INSERT, linea)

    print()


def salir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value:
        root.destroy()


def reporte_Js():
    contenido = editor.get("1.0", END)
    a = js()
    b = Reporte(a.match(contenido))
    b.reporte_analisis_lexico('Reporte JavaScript')


def reporte_CSS():
    os.system("cls")
    contenido = editor.get("1.0", END)
    a = css()
    a.lexer(contenido)
    b = Reporte(a.tokens)
    b.reporte_analisis_lexico('Reporte CSS')


def reporte_Html():
    contenido = editor.get("1.0", END)
    a = html()
    a.lexer(contenido)
    b = Reporte(a.tokens)
    b.reporte_analisis_lexico('Reporte html')


def reporte_Sintactico():
    content = editor.get("1.0", END)
    a = ar()
    content = content.split('\n')
    tokens = []
    for linea in content:
        a = ar()
        a.lexer(linea)
        if linea == '\n' or linea == '' or linea == '   ':
            pass
        elif a.syntax():
            tokens.append((linea, True))
        else:
            tokens.append((linea, False))
    b = Reporte(tokens)
    b.reporte_analisis_sintactico('Reporte Analisis Sintactico')


def automata():
    contenido = editor.get("1.0", END)
    a = js()
    a.automata(contenido)


def guardarArchivo():
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, END))
        guardarc.close()
        mi_ruta = 'D:\\david\\Documents\\Otros\\Output'
        if extension[1] == 'js':
            a = js()
            contenido = editor.get("1.0", END)
            tokens = a.match(contenido)
            for i in tokens:
                if ('COMENTARIO_UNILINEA' == i[1] and 'PATHW' in i[0]) or ('COMENTARIO_MULTILINEA' == i[1] and 'PATHW' in i[0]):
                    ruta = re.findall(
                        r'((?:[a-zA-Z]\:){0,1}(?:[\\][\w.]+){1,})', i[0])[0]
                    mi_ruta += ruta.split('output')[1]
                    try:
                        os.stat(mi_ruta)
                    except:
                        os.mkdir(mi_ruta)
                    nombre = archivo.split('/')
                    mi_ruta += "\\" + nombre[len(nombre) - 1]
                    fguardar = open(mi_ruta, "w+")
                    mensaje = ''
                    for i in tokens:
                        if i[1] != 'NO_RECONOCIDO':
                            mensaje += i[0]

                    fguardar.write(mensaje)
                    fguardar.close()
                    break
        elif extension[1] == 'css':
            a = css()
            contenido = editor.get("1.0", END)
            a.lexer(contenido)
            for i in a.tokens:
                if 'COMENTARIO' == i[1] and 'PATHW' in i[0]:
                    ruta = re.findall(
                        r'((?:[a-zA-Z]\:){0,1}(?:[\\][\w.]+){1,})', i[0])[0]
                    mi_ruta += ruta.split('output')[1]
                    try:
                        os.stat(mi_ruta)
                    except:
                        os.mkdir(mi_ruta)
                    nombre = archivo.split('/')
                    mi_ruta += "\\" + nombre[len(nombre) - 1]
                    fguardar = open(mi_ruta, "w+")
                    mensaje = ''
                    for i in a.tokens:
                        if i[1] != 'DESCONOCIDO':
                            mensaje += i[0]

                    fguardar.write(mensaje)
                    fguardar.close()
                    break
        elif extension[1] == 'html':
            a = html()
            contenido = editor.get("1.0", END)
            a.lexer(contenido)
            for i in a.tokens:
                if 'COMENTARIO' == i[1] and 'PATHW' in i[0]:
                    ruta = re.findall(
                        r'((?:[a-zA-Z]\:){0,1}(?:[\\][\w.]+){1,})', i[0])[0]
                    mi_ruta += ruta.split('output')[1]
                    try:
                        os.stat(mi_ruta)
                    except:
                        os.mkdir(mi_ruta)
                    nombre = archivo.split('/')
                    mi_ruta += "\\" + nombre[len(nombre) - 1]
                    fguardar = open(mi_ruta, "w+")
                    mensaje = ''
                    for i in a.tokens:
                        if i[1] != 'DESCONOCIDO':
                            mensaje += i[0]

                    fguardar.write(mensaje)
                    fguardar.close()
                    break
        print(mi_ruta)


def guardarComo():
    global archivo
    guardar = filedialog.asksaveasfilename(
        title="Guardar Archivo", initialdir="C:/")
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, END))
    fguardar.close()
    archivo = guardar


barraMenu = Menu(root)
root.config(menu=barraMenu, width=1100, height=600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command=nuevo)
archivoMenu.add_command(label="Abrir", command=abrir)
archivoMenu.add_command(label="Guardar", command=guardarArchivo)
archivoMenu.add_command(label="Guardar Como...", command=guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

reportes = Menu(barraMenu, tearoff=0)
reportes.add_command(label="Reporte JavaScript", command=reporte_Js)
reportes.add_command(label="Reporte CSS", command=reporte_CSS)
reportes.add_command(label="Reporte HTMl", command=reporte_Html)
reportes.add_command(label="Reporte Analisis sintactico",
                     command=reporte_Sintactico)
reportes.add_command(label="Automata", command=automata)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Reporte", menu=reportes)
barraMenu.add_command(label="Salir",  command=salir)

frame = Frame(root, bg="black")
canvas = Canvas(frame, bg="black")
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scroll = Frame(canvas, bg="LightSkyBlue2")


scroll.bind("<Configure>", lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scroll, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set, width=1500, height=600)

ttk.Label(scroll, text="Analizador Lexico", font=("Arial", 17),
          background='LightSkyBlue2', foreground="black").grid(column=1, row=0)

editor = scrolledtext.ScrolledText(scroll, undo=True, width=80, height=20, font=(
    "Arial", 15), background='white',  foreground="black")

editor.grid(column=1, row=1, pady=10, padx=30)

editor2 = scrolledtext.ScrolledText(scroll, undo=True, width=40, height=20, font=(
    "Arial", 15), background='white',  foreground="black")

editor2.grid(column=2, row=1, pady=25, padx=50)

frame.grid(sticky='news')
canvas.grid(row=0, column=1)


scroll.pack(fill="both", expand="True")
editor.focus()
root.mainloop()
