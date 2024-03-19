import tarea23

def menu():
    url = input("Ingrese la URL: ")
    url_nueva = tarea23.cheacador(url)
    html = tarea23.conexion_request(url_nueva)
    
    print(html)


if __name__=='__main__':
    menu()