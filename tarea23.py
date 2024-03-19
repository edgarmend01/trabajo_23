#! python3

import requests, os, bs4

def cheacador(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url
    
def conexion_request(url_nueva):
    os.makedirs('hola', exist_ok=True)
    os.makedirs('pdfss', exist_ok=True)
    print('Downloading page %s...' % url_nueva)
    res = requests.get(url_nueva)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    imagenes = soup.find_all('img')
    if imagenes == []:
        print('No se encontró.')
    else:
        for img in imagenes:
            imgUrl = img.get('src')
            if imgUrl.startswith("http"):
                print('Descargando %s...' % (imgUrl))
                response = requests.get(imgUrl)
                if response.status_code == 200:
                    imageFile = open(os.path.join('hola', os.path.basename(imgUrl)),'wb')
                    for chunk in response.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
            else:
                print('Descargando %s...' % (imgUrl))
                imgUrl = url_nueva + imgUrl
                response = requests.get(imgUrl)
                if response.status_code == 200:
                    imageFile = open(os.path.join('hola', os.path.basename(imgUrl)),'wb')
                    for chunk in response.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
    
    hipervinculos = soup.find_all('a')
    with open("hipervinculos.txt", "w") as f:
        for hi in hipervinculos:
            link = hi.get("href")
            if link:
                f.write(link + "\n")
        print("se guardados correctamente los hipervinulos")

    
    pdfs = soup.find_all('a')
    for p in pdfs:
        if ('.pdf' in p.get('href', [])):
            response = requests.get(p.get('href'))
            nombre = p.get('href')
            pdf = open(os.path.join('pdfss', os.path.basename(nombre)), 'wb')
            pdf.write(response.content)
            pdf.close()
            print("archivo ", nombre , " fue descargado")
    print("se descargaron todos los pdfs")







