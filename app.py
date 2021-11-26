import metodos as metodos

if __name__ == '__main__':
    empleo = "consultor"
    n_ciudades = range(231, 231+52)

    lista_puesto = list()
    lista_empresa = list()
    lista_fecha = list()
    lista_remoto = list()
    lista_jornada = list()
    lista_contrato = list()
    lista_salario = list()

    for n in n_ciudades:
        url_ciudad = f"https://www.tecnoempleo.com/busqueda-empleo.php?te={empleo}&pr=,{n},&pagina=1"
        html_ciudad = metodos.connect_url(url_ciudad)
        title = html_ciudad.find("h1", "h4 h5-xs py-4 text-center")

        ciudad, n_ofertas, n_paginas = metodos.get_ciudad_ofertas_paginas(title)
        lista_paginas = [url_ciudad[:-1] + str(pag) for pag in range(1, n_paginas+1)]
        print(ciudad, n_ofertas, n_paginas)
        for pag in range(1, n_paginas+1):
            print(url_ciudad[:-1] + str(pag))
        print(lista_paginas)
        for url_pag in lista_paginas:
            html_ciudad_pagina = metodos.connect_url(url_pag)

            nombres_empleo = html_ciudad_pagina.find_all("h5", "h6-xs pl-3 pr-1 pt-2")
            lista_puesto += [empleo.text.strip() for empleo in nombres_empleo]

            nombres_empresa = html_ciudad_pagina.find_all("a", "text-primary link-muted lead fs--16 font-weight-normal")
            lista_empresa += [empresa.text for empresa in nombres_empresa]
            # for i in nombres_empresa:
            #     if i != "":
            #         print(i.text)
            #     else:
            #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


            info_empleos = html_ciudad_pagina.find_all("div", "bg-theme-color-light h-100-xs p-3 rounded mb-3 fs--15 text-muted")
            for info in info_empleos:
                lista_palabras = metodos.lista_palabras(info.text)

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

    print(
        len(lista_puesto),
        len(lista_empresa),
        len(lista_fecha),
        len(lista_remoto),
        len(lista_jornada),
        len(lista_contrato),
        len(lista_salario)
    )
    for i, value in enumerate(lista_puesto):
        print(value, lista_empresa[i], lista_fecha[i], lista_remoto[i], lista_jornada[i], lista_contrato[i], lista_salario[i])

