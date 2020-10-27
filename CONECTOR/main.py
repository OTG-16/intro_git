import mysql.connector

bd = mysql.connector.connect(
    user='oscar', password='12345678',
    database='proyecto_arbolado')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar usuarios')
    print('3) Agregar arbol')
    print('4) Mostrar arboles')
    print('0) Salir')
    op = input()

    if op == '1':
        correo_U = input('correo: ')
        contrasena_U = input('contraseña: ')

        consulta = "INSERT INTO usuario (correo_U, contrasena_U) " \
                   "VALUES (%s, %s)" 
        cursor.execute(consulta, (correo_U, contrasena_U))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print("Error: No se pudo completar la acción correctamente")

    elif op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('id: ', row[0])
            print('correo: ', row[1])
            print('contraseña: ', row[2])

    elif op == '3':
        especie_A = input('especie_arbol: ')
        estado_A = input('estado_arbol: ')
        foto_A = input('foto_arbol: ')
        calle_U = input('calle_usuario: ')
        colonia_U = input('colonia_usuario: ')
        cp_U = input('cp_usuario: ')
        municipio_U = input('municipio_usuario: ')

        consulta = "INSERT INTO usuario (especie_A, estado_A, foto_A,  calle_U, colonia_U, cp_U, municipio_U ) " \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)" 
        cursor.execute(consulta, (especie_A, estado_A, foto_A, calle_U, colonia_U, cp_U, municipio_U ))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó un arbol')
        else:
            print("Error. No se pudo completar la accion correctamente")

    elif op == '4':
        consulta = "SELECT * FROM arbol"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('especie_A: ', row[0])
            print('estado_A: ', row[1])
            print('foto_A: ', row[2])
            print('calle_U: ', row[3])
            print('colonia_U: ', row[4])
            print('cp_U: ', row[5])
            print('municipio_U: ', row[6])

            
    elif op == '0':
        break