<div align="justifye">
Sistema de fichero --> organiza la información. Existen diversos sistemas de fichero como el FAT32, exFAT, NTFS, ext4, HFS+, APFS.
Bloque o claster (No puedo tener dos ficheros distintios en el mismo claster). Bloques más pequeños = más espacio , pero acceso más lento. Los clasters tienen todos el mismo tamaño. Todos los clasters tienen un número, se usa el índice para encontrar los ficheros. Se dedica parte del disco para este índice. Si se pierde el índice no se puede acceder a los ficheros. Cuando borras un fichero borras la lista ( por eso es tan rápido la eliminación) y los ficheros nuevos se sobreescriben sobre los que ya estaban.
Desfragmentación --> Ordena los ficheros dentro del disco duro
Para el sistema de ficheros las carpetas son otors ficheros, en vez de tener los archivos contiene el fichero.
Atributos de fichero --> Oculto, solo lectura, del sistema,etc...
Metadatos --> Datos referentes al propio fichero (fecha de creación, autor, descripción, etc...)
</div>