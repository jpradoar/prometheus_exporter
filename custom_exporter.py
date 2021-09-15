# Prometheus custom exporter.  This project consume a json output from url 
# parse it and generate prometheus custom metrics. 
#
# docker run -it -p 8000:8000 -v /tmp/prometheus_exporter.py:/app/prometheus_exporter.py alpine:3.14
# apk update; apk add py-pip; pip install prometheus_client
from prometheus_client import start_http_server # usado para levantar el http_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY # usado para armar los custom metrics
import time     # usado para el sleep del while final
import json     # usado para manejar los json de los servicios expuestos/consumidos
import requests # 

# https://github.com/prometheus/prometheus/wiki/Default-port-allocations
http_port=8000  # Puerto que expone el exporter
# Endpoints donde consulto data en formato json
endpoints=["http://192.168.0.22:81/data",
           "http://192.168.0.22:82/data",
           "http://192.168.0.22:83/data"]


class CustomCollector(object):
    def collect(self):
        #yield GaugeMetricFamily('my_gauge', 'Help text', value=1)
        for svc in endpoints:                       # Hago un loop por todos los servicios de la lista de endpoints
            json_obj = requests.get(svc).json()     # Obtengo el json via request de cada url en la lista de endpoints
            metric = GaugeMetricFamily('custom_counter', 'Custom metric from service '+ svc +'',labels=['name']) # Genero un HELP con la descripcion de la metrica
            xdata = json_obj.items()                # Parseo los items en formato key:value
            for key,value in xdata:                 # Genero un bucle y obtengo toda la infor del json
                origin = svc.replace("http://","")  # Remuevo el http 
                endp = origin.split(':',1)[0]       # Remuevo todo el path e la url
                key = key+"-"+endp                  # Genero un valor unico para discriminar cada metrica por separado. 
                metric.add_metric([key], value) # Genero la metrica con el nombre de la URL + el valor taggeado
            yield metric                        # Imprimo todas las metricas en formato OpenMetrics


if __name__ == '__main__':
    start_http_server(http_port)            # Inicio un webserver con el puerto 8000 
    REGISTRY.register(CustomCollector())    # Genero un registro de OpenMetrics
    while True:                             # Genero un bucle infinito para correr el programa
        time.sleep(1)                       # Espero n segundos por cada scraping
