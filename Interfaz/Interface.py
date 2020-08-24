from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Clases.JavaScript import JavaScript as js
from Clases.CSS import CSS as css

root = Tk()
root.title("LABORATORIO")
root.configure(background="black")

root.resizable(0, 0)
archivo = ""


def nuevo():
    global archivo
    editor.delete(1.0, END)  # ELIMINAR EL CONTENIDO
    archivo = ""


def abrir():
    global archivo
    archivo = filedialog.askopenfilename(
        title="Abrir Archivo", initialdir="C:/")

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

    print()


def salir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value:
        root.destroy()


def guardarArchivo():
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, END))
        guardarc.close()


def guardarComo():
    global archivo
    guardar = filedialog.asksaveasfilename(
        title="Guardar Archivo", initialdir="C:/")
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, END))
    fguardar.close()
    archivo = guardar


barraMenu = Menu(root)
root.config(menu=barraMenu, width=1000, height=600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command=nuevo)
archivoMenu.add_command(label="Abrir", command=abrir)
archivoMenu.add_command(label="Guardar", command=guardarArchivo)
archivoMenu.add_command(label="Guardar Como...", command=guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
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

editor = scrolledtext.ScrolledText(scroll, undo=True, width=60, height=20, font=(
    "Arial", 15), background='white',  foreground="black")

editor.grid(column=1, row=1, pady=10, padx=30)

editor2 = scrolledtext.ScrolledText(scroll, undo=True, width=60, height=20, font=(
    "Arial", 15), background='white',  foreground="black")

editor2.grid(column=2, row=1, pady=25, padx=50)

frame.grid(sticky='news')
canvas.grid(row=0, column=1)


scroll.pack(fill="both", expand="True")
editor.focus()
root.mainloop()
