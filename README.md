# Repaso  p2 appweb



C:\Program Files\MongoDB\Tools\100\bin   este es para el mongo tools para poder exportar o imortar la data desde mongo en json

var allRecords = db.registro.find();
while ( allRecords.hasNext() ) {
printjson(allRecords.next());
}

/*Ejemplo de insertar data*/
db.registro.insert({'cedula':'0125463879','nombre':'Monica','apellido':'Ledesmas','direccion':
'Quevedo','telefono':'0988939742'});

/*Exportamos en Json */

mongoexport --db BDD_JhostynG_ZonasAzules --collection registro --type JSON --out C:\Users\DELL-INSPIRION15\Downloads\ArchivoJson\DatosRegistrosBDD_ZonaAzul_JJGS.json

/*importamos en Json */
mongoimport --verbose --db miscelanea --drop --collection books --file
C:\Users\DELL-INSPIRION15\Documents\archivosJson\act-2-books.json

