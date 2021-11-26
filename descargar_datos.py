import download as metodos

if __name__ == '__main__':

    empleo = "consultor"
    n_ciudades = range(231, 231+52)

    dict_ciudad_empleos = dict()
    lista_puesto = list()
    lista_empresa = list()
    lista_fecha = list()
    lista_remoto = list()
    lista_jornada = list()
    lista_contrato = list()
    lista_salario = list()

    for n in n_ciudades:
        url_ciudad = f"https://www.tecnoempleo.com/busqueda-empleo.php?te={empleo}&pr=,{n},&pagina=1"
        print(metodos.get_tag_content(url_ciudad, "h1", "h4 h5-xs py-4 text-center"))
        print(metodos.get_tag_content(url_ciudad, "h1", "h4 h5-xs py-4 text-center")[0])

        title = metodos.get_tag_content(url_ciudad, "h1", "h4 h5-xs py-4 text-center")[0]

        if title == "N": break

        ciudad, n_ofertas, n_paginas = metodos.get_ciudad_ofertas_paginas(title)
        lista_paginas = [url_ciudad[:-1] + str(pag) for pag in range(1, n_paginas+1)]


        lista_lenguajes = []
        for url_pg in lista_paginas:

            nombres_empleo = metodos.get_tag_content(url_ciudad, "h5", "h6-xs pl-3 pr-1 pt-2")
            for empleo in nombres_empleo:
                lista_puesto.append(empleo.text.strip())

            nombres_empresa = metodos.get_tag_content(url_ciudad, "a", "text-primary link-muted lead fs--16 font-weight-normal")
            for empresa in nombres_empresa:
                lista_empresa.append(empresa.text)

            info_empleo = metodos.get_tag_content(url_ciudad, "div", "bg-theme-color-light h-100-xs p-3 rounded mb-3 fs--15 text-muted")
            for elemento in info_empleo:
                lista_palabras = metodos.lista_palabras(elemento.text)

                lista_fecha.append(lista_palabras[0])
                if '100%' in lista_palabras:
                    lista_remoto.append(True)
                else:
                    lista_remoto.append(False)
                if 'completa' in lista_palabras:
                    lista_jornada.append("Jornada Completa")
                else:
                    lista_jornada.append("No Jornada Completa")
                if 'indefinido' in lista_palabras:
                    lista_contrato.append("Contrato Indefinido")
                else:
                    lista_contrato.append("Contrato No Indefinido")
                if 'disponible' in lista_palabras:
                    lista_salario.append("Salario No Disponible")
                else:
                    lista_salario.append(lista_palabras[-4] + lista_palabras[-3] + lista_palabras[-2])

    print(lista_puesto)
    print(lista_empresa)
    print(lista_fecha)
    print(lista_remoto)
    print(lista_jornada)
    print(lista_contrato)
    print(lista_salario)
    for i, value in enumerate(lista_puesto):
        print(value, lista_empresa[i], lista_fecha[i], lista_remoto[i], lista_jornada[i], lista_contrato[i], lista_salario[i])



