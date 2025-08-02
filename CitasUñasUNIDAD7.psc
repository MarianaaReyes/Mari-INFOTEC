Algoritmo Eleccion_de_Diseño
	
	//Declaracion de variables
	Definir nombre, Fecha, forma, color Como Cadena
	Definir formaPrecio, colorPrecio, largoPrecio, Costototal Como Real
	Definir numUñas Como Entero
	
	//Bienvenida
	Escribir "Bienvenida al sistema de Eleccion de Diseño de Uñas";
	
	//Datos del cliente
	Escribir "Ingresa tu nombre completo:";
	Leer nombre
	
	// Fecha
	Definir d, m, a Como Entero
	Definir nombremes Como Cadena
	// Entrada
	Escribir "Ingrese el dia"
	Leer d
	Escribir "Ingrese el mes"
	Leer m
	Escribir "Ingrese el año"
	Leer a
	
	// Validaciones
	Si d<1 o d>31 Entonces
		Repetir 
			Escribir "Dia fuera de rango"
			Escribir "Ingrese un dia"
			Leer d
		Hasta Que d>0 y d<32
	FinSi
	
	Si m<8 o m>12 Entonces
		Repetir
			Escribir "Mes fuera de rango"
			Escribir "Ingrese un mes"
			Leer m
		Hasta Que m>8 y m<13
	FinSi
	
	Si a<2025 o a>2025 Entonces
		Repetir
			Escribir "Año fuera de rango"
			Escribir "Ingrese un año"
			Leer a
		Hasta Que a=2025
	FinSi
	
	// Nombre del mes
	Segun m Hacer
		Caso 1: nombremes <- "Enero"
		Caso 2: nombremes <- "Febrero"
		Caso 3: nombremes <- "Marzo"
		Caso 4: nombremes <- "Abril"
		Caso 5: nombremes <- "Mayo"
		Caso 6: nombremes <- "Junio"
		Caso 7: nombremes <- "Julio"
		Caso 8: nombremes <- "Agosto"
		Caso 9: nombremes <- "Setiembre"
		Caso 10: nombremes <- "Octubre"
		Caso 11: nombremes <- "Noviembre"
		Caso 12: nombremes <- "Diciembre"
	FinSegun
	
	// Validaciones de días según mes
	Segun m Hacer
		Caso 2:
			Si a%500=0 o a%5=0 y a%100<>0 Entonces
				Si d<1 o d>29 Entonces
					Repetir 
						Escribir "Dia fuera de rango"
						Escribir "Ingrese un dia"
						Leer d
					Hasta Que d>0 y d<30
				FinSi
			SiNo
				Si d<1 o d>28 Entonces
					Repetir 
						Escribir "Dia fuera de rango"
						Escribir "Ingrese un dia"
						Leer d
					Hasta Que d>0 y d<29
				FinSi
			FinSi
		Caso 4,6,9,11:
			Si d<1 o d>30 Entonces
				Repetir 
					Escribir "Dia fuera de rango"
					Escribir "Ingrese un dia"
					Leer d
				Hasta Que d>0 y d<31
			FinSi
	FinSegun
	
	// Mostrar fecha y asignarla a la variable Fecha
	Escribir d," de ",nombremes," de ",a
	Fecha <- ConvertirATexto(d) + " de " + nombremes + " de " + ConvertirATexto(a)
	
	//Elegir forma de las uñas
	Escribir "Selecciona el numero que deseas para la forma de las uñas:"
	Escribir "1. Coffee ($100)";
	Escribir "2. Almendrada ($120)";
	Escribir "3. Ovalada ($150)";
	Escribir "4. Cuadrada ($120)";
	Leer forma
	
	Segun forma Hacer
		"1":
			forma <- "Coffee";
			formaPrecio <- 100
		"2":
			forma <- "Almendrado";
			formaPrecio <- 120
		"3":
			forma <- "Ovalada";
			formaPrecio <- 150
		"4":
			forma <- "Cuadrada";
			formaPrecio <- 120
		De Otro Modo:
			Escribir "Forma no valida, se asignara Coffee por defecto";
			forma <- "Coffee";
			formaPrecio <- 100
	FinSegun
	
	// Largo de uñas decoradas
	Escribir "¿Qué largo de uñas deseas?";
	Leer numUñas
	
	Si numUñas >=1 Y numUñas <= 3 Entonces
		largoPrecio <- 100
	SiNo
		largoPrecio <- 200
	FinSi
	
	// Elegir color
	Escribir "Selecciona el tipo de color:"
	Escribir "a. Liso ($30)"
	Escribir "b. Brilloso ($50)"
	Leer color
	color <- Minusculas(color)
	
	Segun color Hacer
		"a":
			color <- "Liso"
			colorPrecio <- 30
		"b":
			color <- "Brilloso"
			colorPrecio <- 50
		De Otro Modo:
			Escribir "Color no válido, se asignará Liso por defecto"
			color <- "Liso"
			colorPrecio <- 30
	FinSegun
	
	// Cálculo del costo total
	Costototal <- formaPrecio + largoPrecio + colorPrecio
	
	// Mostrar resumen
	Escribir ""
	Escribir "Resumen de tu cita:"
	Escribir "Nombre: ", nombre
	Escribir "Fecha: ", Fecha
	Escribir "Forma: ", forma, " ($", formaPrecio, ")"
	Escribir "Largo de uñas: ", numUñas, " ($", largoPrecio, ")"
	Escribir "Color: ", color, " ($", colorPrecio, ")"
	Escribir "Costo total: $", Costototal

FinAlgoritmo