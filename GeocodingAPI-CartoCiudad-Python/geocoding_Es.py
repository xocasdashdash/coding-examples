import urllib2
import urllib
from lxml import etree

basic_data = open('geocoding_es_xml.xml').read();
url = 'http://www.cartociudad.es/wps/WebProcessingService'
longitud = '-3.180908';
latitud = '40.632369'
xml_string = basic_data.replace('$$LONGITUD',longitud).replace('$$LATITUD',latitud);
request = urllib2.Request(url=url, 
                      data=xml_string, 
                      headers={'Content-Type': 'application/xml'})
print 'Peticion enviada...:' 

response = urllib2.urlopen(request)
respuesta = response.read()
root = etree.fromstring(respuesta)
#Devuelve todas las provincias, municipios y codigos postales usando XPath
provincia = root.findall('.//provincia')
municipio = root.findall('.//municipio')
codigopostal = root.findall('.//cp')
#Ejemplo con una sola provincia, municipio y codigo postal
print 'Provincia: ' + provincia[0].text + '|| Municipio: ' + municipio[0].text + '|| Codigo Postal:' + codigopostal[0].text