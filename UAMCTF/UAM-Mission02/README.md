# Write-up y Flag de UAM misión #002

- [http://unaaldia.hispasec.com/2017/12/segunda-entrega-una-al-mes-mision-002.html](http://unaaldia.hispasec.com/2017/12/segunda-entrega-una-al-mes-mision-002.html ")

- Texto:
*"En esta misión Rick debe encontrar los datos ocultos en una imagen, pero tiene un problema, parece que no puede acceder a ella. Necesita tu ayuda..."*

- URL datos mision #002 : http://34.253.233.243/mission2.php

- Texto: "(ES)
*Hemos encontrado un servidor vulnerable de la empresa 'Santa Claus Inc' el cuál solo es accesible desde el país donde se encuentra la fábrica. Debemos de encontrar la manera de entrar y sacar la información oculta de la imagen que nos aparece. Mucha suerte."*

- Nivel: *Fácil (según el organizador)*

- Categoría: *Esteganografía // Criptografía //...*

URL del servidor: http://34.253.233.243/navidad/index.php

###Pasos a la solución:

1.- La URL de la misión al visitarla nos da el siguiente análisis de codigo:

Postal

2.- Seguimos el link de Postal que nos presenta la index.php y como nos informa en el texto de la misión es inaccesible  con un si no es desde el país de "Santa Claus Inc" que según el análisis del anterior punto es Canada. El análisis de la URL visitada [http://34.253.233.243/navidad/img/renitos.jpg]http://34.253.233.243/navidad/img/renitos.jpg es el siguiente de donde obtenemos un error 403:

Forbidden
You don't have permission to access /navidad/img/renitos.jpg
on this server.
Apache/2.4.25 (Debian) Server at 34.253.233.243 Port 80

3.- Con lo cual tomamos la decisión de utilizar un WebProxy que salga en Cánada a Internet que este caso será https://www.vpnbook.com/webproxy y sin más introducimos la URL http://34.253.233.243/navidad/img/renitos.jpg . Conseguimos el objetivo de visualizar renitos.jpg y lo descargamos a nuestro escritorio.

4.- Pero sospechábamos que no era tan sencillo y que renitos.jpg podría esconder un mensaje o un archivo como nos avisan en la misión. Pasamos a utilizar la herramienta de Steghide de Kali. Obteniendo el siguiente análisis:

```bash
1v4n@kali:~/Escritorio$ steghide info renitos.jpg
"renitos.jpg":
formato: jpeg
capacidad: 68,0 KB
Intenta informarse sobre los datos adjuntos? (s/n) s
Anotar salvoconducto:
archivo adjunto "renitos.txt":
  tamaño: 88,0 Byte
  encriptado: rijndael-128, cbc
  compactado: si
```

5.- Nos desvela que el archivo renitos.jpg esconde un archivo de texto en formato .txt y que vamos a extraer mediante:

```bash
1v4n@kali:~/Escritorio$ steghide extract -sf renitos.jpg
Anotar salvoconducto:
anota los datos extraidos en"renitos.txt".
```

6.- El archivo reitos.txt esconde un texto codificado KVAU262NMVZHE6K7INUHE2LTORWWC427MFXGIX2IMFYHA6K7JZSXOX2ZMVQXEX3GOJXW2X2INFZXAYLTMVRX2=== que esta en base32. En este caso vamos a utilizar la herramienta online gratuita https://emn178.github.io/online-tools/ y por fin conseguimos la FLAG de este reto.

#### FLAG

`UAM{Merry_Christmas_and_Happy_New_Year_from_Hispasec}`
