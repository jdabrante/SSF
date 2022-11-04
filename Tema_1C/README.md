<div align="justifye">
Sistema de fichero --> organiza la información. Existen diversos sistemas de fichero como el FAT32, exFAT, NTFS, ext4, HFS+, APFS.
Bloque o claster (No puedo tener dos ficheros distintios en el mismo claster). Bloques más pequeños = más espacio , pero acceso más lento. Los clasters tienen todos el mismo tamaño. Todos los clasters tienen un número, se usa el índice para encontrar los ficheros. Se dedica parte del disco para este índice. Si se pierde el índice no se puede acceder a los ficheros. Cuando borras un fichero borras la lista ( por eso es tan rápido la eliminación) y los ficheros nuevos se sobreescriben sobre los que ya estaban.
Desfragmentación --> Ordena los ficheros dentro del disco duro
Para el sistema de ficheros las carpetas son otors ficheros, en vez de tener los archivos contiene el fichero.
Atributos de fichero --> Oculto, solo lectura, del sistema,etc...
Metadatos --> Datos referentes al propio fichero (fecha de creación, autor, descripción, etc...)

04/11/22

Conjunto de discos que se ven como uno solo --> Spanned.
RAID --> Array de discos independientes redundandtes. Se utiliza en servidores.
Alternativas de RAID:
- RAID 0 (Striped)--> Aceleran el acceso. Los datos se encuentran repartidos en los discos por lo que se pueden leer y escribir más rapidamente dependiendo de la cantidad de discos que se tengan. Se usa el 100% de los discos y hay 0% de desperdicio. No se puede perder ningún disco. No se considera un RAID realmente, por eso se llama RAID 0. Se le llama también Striped.
- RAID 1 (mirror) --> La velocidad de escritura es igual que si fuera un disco. En el caso de la lectura se acelera por n. El espacio del disco es el mismo se usa 100%/n. Discos desperdiciados n-1. Se pueden perder n-1 discos.
- RAID 2,3,4 --> El RAID 2 trabajaba con código hamming, se recupera con bits. RAID 3 trabaja con código de paridad par, se recupera con bytes, se resuelve con una puerta XOR, no se utiliza ya que se utiliza con bytes. RAID 4, funciona a nivel de bloques, no byte a byte, y se utiliza el método de paridad par, al igual que el anterior, el disco de redundancia tiene un uso muy elevado, por lo que hay más posibilidades de que falle.
- RAID 5 --> No hay disco de redundancia, la redundancia se alamancena en todos los discos (por trozos). Velocidad de lectura n-1, Velcodiad de escritura <1, capacidad del disco 100%(n-1), siempre se desperdicia el tamaño de un disco, límite de desperdicio será 1 y los discos mínimos serán 3. Es uno de los sistemas más usados.
- RAID 6 --> Se utiliza dos discos de redundancia distribuida. Se pierden 2 discos, pueden fallar hasta 2 discos y se necesitan mínimo 4 discos. La pariedad estaria repratida en varios discos.
- RAID 5E y RAID 6E --> Se deja un disco vacio para cuando un disco falle se comience a usar automáticamente.
- RAID Anidados --> Se combinan tipos de RAID (Problema espacio)
*Mismo fabricante, mismo tamaño, misma velocidad, pero distinto lote.
  
</div>