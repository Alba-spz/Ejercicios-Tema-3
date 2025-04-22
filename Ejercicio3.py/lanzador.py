from nave import Nave

def GranRallyEspacial():
    
    # Crear instancias de la clase Nave
    naves = [
        Nave("Cometa Veloz", 120, 10, 4),
        Nave("Titán del Cosmos", 200, 15, 100),
        Nave("GX-1 Explorer", 90, 8, 6),
        Nave("GX-2 Voyager", 110, 12, 20),
        Nave("Estrella Fugaz", 150, 3, 5),
        Nave("Nebulosa Andrómeda", 180, 20, 150),
        Nave("Galaxia Centauri", 130, 10, 40),
        Nave("Nave Estelar", 160, 18, 120),
        Nave("Asteroide Azul", 140, 7, 3),
        Nave("Estrella Polar", 170, 25, 200)
    ]

    # 1. Ordena la lista de naves por nombre (ascendente) y por longitud (descendente)
    # Lista de naves únicamente por nombre en orden ascendente
    naves_ordenadas_nombre = sorted(naves, key=lambda x: x.nombre)
    print("\n1.1 Naves ordenadas únicamente por nombre (ascendente):")
    for nave in naves_ordenadas_nombre:
        print(nave)

    # Lista de naves únicamente por longitud en orden descendente
    naves_ordenadas_longitud = sorted(naves, key=lambda x: x.longitud, reverse=True)
    print("\n1.2 Naves ordenadas únicamente por longitud (descendente):")
    for nave in naves_ordenadas_longitud:
        print(nave)

    # 2. Muestra toda la información de las naves "Cometa Veloz" y "Titán del Cosmos"
    print("\n2. Información de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in naves:
        if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]:
            print(nave)

    # 3. Determina cuáles son las cinco naves con mayor cantidad de pasajeros
    naves_mas_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    print("\n3. Las cinco naves con mayor cantidad de pasajeros:")
    for nave in naves_mas_pasajeros:
        print(nave)

    # 4. Indica cuál es la nave que requiere la mayor cantidad de tripulación
    nave_mas_tripulacion = max(naves, key=lambda x: x.tripulacion)
    print("\n4. La nave que requiere la mayor cantidad de tripulación:")
    print(nave_mas_tripulacion)

    # 5. Muestra todas las naves cuyo nombre comience con "GX"
    naves_gx = [nave for nave in naves if nave.nombre.startswith("GX")]
    print("\n5. Naves cuyo nombre comienza con 'GX':")
    for nave in naves_gx:
        print(nave)

    # 6. Lista todas las naves que pueden llevar seis o más pasajeros
    naves_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
    print("\n6. Naves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_pasajeros:
        print(nave)

    # 7. Muestra toda la información de la nave más pequeña y la más grande
    nave_mas_pequena = min(naves, key=lambda x: x.longitud)
    nave_mas_grande = max(naves, key=lambda x: x.longitud)
    print("\n7. Información de la nave más pequeña y la más grande:")
    print("Nave más pequeña:", nave_mas_pequena)
    print("Nave más grande:", nave_mas_grande)
