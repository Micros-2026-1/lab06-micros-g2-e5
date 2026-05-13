[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MCJunYEq)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23739449&assignment_repo_type=AssignmentRepo)
# Lab06: Comunicación UART con PIC18F45K22

## Integrantes

* [Liliana Carreño](https://github.com/Liliana-Carreno)
* [Salome Ramirez](https://github.com/salomeramirezpi-eng)
* [Gabriel Ortega](https://github.com/gabrieldaortegaro-arch)

### 1.1 Introducción

<p align="justify" style="text-indent:40px;">
En este laboratorio se implementó una comunicación serial UART entre un microcontrolador PIC y un computador, con el objetivo de transmitir datos mediante el protocolo serial asíncrono. Para ello, se configuró el módulo UART trabajando con un oscilador interno de 16 MHz y una velocidad de transmisión de 9600 baudios, permitiendo el envío continuo de mensajes desde el microcontrolador hacia el puerto serial del computador. Esta práctica permitió comprender el funcionamiento básico de la transmisión y recepción de datos en sistemas embebidos.<p>

<p align="justify" style="text-indent:40px;">
Además, se desarrolló un programa en Python utilizando las librerías serial y matplotlib para leer y visualizar en tiempo real la información recibida por UART. El sistema permitió interpretar los datos transmitidos y representarlos gráficamente, integrando conceptos de programación, obtención de datos y monitoreo de señales. De esta manera, se evidenció la importancia de la comunicación UART en aplicaciones electrónicas y de instrumentación digital.
</p>




### 1.2 Objetivos

* Configurar el módulo UART del microcontrolador PIC para establecer comunicación serial.

* Transmitir datos desde el microcontrolador hacia el computador mediante UART.

* Leer y procesar los datos recibidos utilizando Python y el puerto serial.

* Visualizar en tiempo real la información transmitida mediante gráficas dinámicas.



## Documentación

### ¿Qué es el conversor USB a Serial UART?
### 2.1 Descripción del Laboratorio.

<p align="justify" style="text-indent:40px;">
Se realizó la implementación de una comunicación serial UART entre un microcontrolador PIC y un computador, utilizando programación en lenguaje C y Python. Inicialmente, se configuró el módulo UART del microcontrolador para transmitir datos a una velocidad de 9600 baudios mediante el uso del oscilador interno de 16 MHz. Posteriormente, se verificó el envío de mensajes a través del puerto serial utilizando funciones de transmisión de caracteres y cadenas de texto.<p>

<p align="justify" style="text-indent:40px;">
Adicionalmente, se desarrolló un programa en Python encargado de leer los datos recibidos y representarlos gráficamente en tiempo real utilizando la librería matplotlib. En el computador se observó una gráfica de voltaje en función del tiempo, donde los valores variaban entre 0 y 5 V, permitiendo visualizar el comportamiento de la señal recibida mediante UART.<p>

### 2.2 Explicacion del codigo implementado.

### Código en Python

<p align="justify" style="text-indent:40px;">
Este código tiene como función leer los datos enviados por el microcontrolador a través del puerto serial y mostrarlos gráficamente en tiempo real. Primero, se importan las librerías necesarias como serial para la comunicación UART, matplotlib para las gráficas, animation para actualizar la gráfica dinámicamente y re para buscar patrones de texto dentro de los datos recibidos.<p>

Posteriormente, se configura el puerto serial con:

```c
SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
```

Aquí se define el puerto de comunicación y la velocidad de transmisión, la cual debe coincidir con la configurada en el microcontrolador.

La instrucción:
```c
ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
```

abre la comunicación serial entre Python y el PIC.

Luego, se utilizan estructuras deque para almacenar una cantidad limitada de muestras:
````c
voltages = deque(maxlen=MAX_POINTS)
times = deque(maxlen=MAX_POINTS)
````

Esto evita que la memoria aumente indefinidamente mientras se reciben datos.

Ahora el corazon de esta sección es:
````c
regex = re.compile(r"Voltaje:\s*([0-9.]+)")
 def update(frame):
  global time_counter line = ser.readline().decode('utf-8').strip()
   match = regex.search(line)
    if match: voltage = float(match.group(1))
        voltages.append(voltage)
        times.append(time_counter)
        time_counter += 1
````
<p align="justify" style="text-indent:40px;">
La primera parte del código se encarga de leer y procesar los datos recibidos mediante la comunicación UART. Inicialmente, se utiliza una expresión regular con <code> regex=re.compile(r"Voltaje:\s*([0-9.]+)")</code> para identificar y extraer únicamente el valor numérico del voltaje enviado por el microcontrolador. Posteriormente, dentro de la función <code> update(frame)</code>, el programa lee una línea proveniente del puerto serial usando <code> ser.readline()</code>, la decodifica en formato UTF-8 y elimina caracteres innecesarios. Luego, mediante <code> regex.search(line)</code> se verifica si el dato recibido coincide con el formato esperado; en caso de ser válido, el valor es convertido a tipo decimal (float) y almacenado para ser utilizado posteriormente en la representación gráfica.<p>

````c
ax.clear()
 ax.plot(times, voltages, color='blue')
  ax.set_ylim(0, 5)
   ax.set_title("Voltaje leído por UART")
   ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.grid(True)
````

<p align="justify" style="text-indent:40px;">
La segunda parte del código es la actualización y visualización de la gráfica en tiempo real. Una vez obtenido el valor de voltaje, este se almacena junto con el tiempo utilizando las listas "voltages" y "times", mientras el contador de tiempo incrementa continuamente para representar la evolución de la señal. Después, la instrucción <code> ax.clear()</code> limpia la gráfica anterior y <code> ax.plot(times, voltages, color='blue')</code> dibuja nuevamente los datos actualizados. Además, se establece un rango de visualización entre 0 y 5 voltios, permitiendo observar claramente las variaciones de la señal recibida desde el microcontrolador. Finalmente, se agregan el título, etiquetas de los ejes y una cuadrícula para mejorar la interpretación de la gráfica mostrada en pantalla.
<p>

Y por ultimo:
````c
animation.FuncAnimation(...)
````
permite refrescar continuamente la gráfica, mostrando el comportamiento del voltaje recibido desde el microcontrolador.


### Main.c
<p align="justify" style="text-indent:40px;">
Este código corresponde al programa principal ejecutado por el microcontrolador PIC. Su función principal es inicializar la comunicación UART y enviar mensajes de prueba continuamente.<p>

Dentro del main se configura la frecuencia del oscilador:
````c
OSCCON = 0b01110000;
````

estableciendo una velocidad de 16 MHz.<p>
La instrucción más importante es:
````c
UART_Init();
````

Posteriormente, dentro del ciclo infinito el microcontrolador envía constantemente el mensaje:

````c
UART_WriteString("Hola, UART funcionando!\r\n");
````

Esto permite verificar que la comunicación UART funciona correctamente.

### UART.c

Este archivo contiene las funciones encargadas de configurar y controlar la transmisión serial UART del PIC.

La función principal es:
````c
void UART_Init(void)
````

Aquí se configuran los pines donde RC6 funciona como transmisión (TX) y RC7 como recepción (RX).
````c
TRISC6 = 0;
TRISC7 = 1;
````

La siguiente configuración define la velocidad de transmisión de 9600 baudios para un oscilador de 16 MHz.
````c
SPBRG1 = 25;
````
Esta función envía un carácter individual esperando primero que el buffer esté libre.
````c
UART_WriteChar(char data)
````



Y finalmente esta linea permite enviar cadenas completas recorriendo cada carácter hasta encontrar el final del texto.
````c
UART_WriteString(const char* str)
````

### Uart.h

Este archivo define las librerías, constantes y prototipos de funciones utilizadas en uart.c.

Esta siguiente línea es fundamental porque establece la frecuencia de trabajo del microcontrolador, necesaria para que las funciones de retardo funcionen correctamente.
````c
#define _XTAL_FREQ 16000000UL
````
Además, se declaran las funciones permitiendo que puedan ser utilizadas desde otros archivos del programa.
````c
void UART_Init(void);
void UART_WriteChar(char data);
void UART_WriteString(const char* str);
````

## Diagramas

## Evidencias de implementación

## Conclusiones