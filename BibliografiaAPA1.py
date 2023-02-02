def autor():
    apellido = (input("Apellidos: ").lower()).title().strip()
    nombre = (input("Nombre: ").upper()).strip().split()

    if len(nombre) > 1:
        iniciales = ""
        for palabra in nombre:
            iniciales += palabra[0]+". "
        return "{}, {}.,".format(apellido, iniciales[:-2])
    else:
        return "{}, {}.,".format(apellido, nombre[0][0])

def libro():
    autores = " ".join(sorted([autor() for i in range(int(input("¿Cuántos autores tiene el libro? ")))]))
    if autores[-1] == ",":
        autores = autores[:-1]

    titulo = input("Titulo: ").strip()
    año = input("Año: ").strip()
    editorial = input("Editorial: ").strip()

    return print("\nEl título de la obra va en cursivas\n{} ({}). {}. {}.".format(autores, año, titulo, editorial))

def web():
    autores = " ".join(sorted([autor() for i in range(int(input("¿Cuántos autores tiene la página web? ")))]))
    if autores[-1] == ",":
        autores = autores[:-1]

    titulo = input("Titulo del artículo: ").strip()
    pagina = input("Nombre de la página web: ").strip()
    fecha = input("Fecha del último día de consulta: ").strip()
    link = input("Link: ").strip()

    return print("\nEl título del artículo va en cursivas\n{} {}. {}. Consultado por última vez el {} de {}".format(autores, titulo, pagina, fecha, link))

if __name__ == "__main__":
    while True:
        opcion = input("\n1. Cita para libro\n2. Cita para página web\n3. Cerrar programa\n").strip()
        if opcion == "1":
            libro()
        elif opcion == "2":
            web()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
