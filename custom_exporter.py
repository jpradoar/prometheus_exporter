# Prometheus custom exporter.  This project consume a json output from url, parse it and generate prometheus custom metrics. 
#
# from alpine:3.13
# apk update; apk add py-pip
# pip install prometheus_client
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
import time
import json
import requests

http_port=8000
url = "http://192.168.0.22/data"

class CustomCollector(object):
    def collect(self):
        #yield GaugeMetricFamily('my_gauge', 'Help text', value=7)
        metric = GaugeMetricFamily('custom_counter', 'Custom metric for custom resources', labels=['name'])
        json_obj = requests.get(url).json() # Obtengo el json via request url y me aseguro que venga en json()
        xdata = json_obj.items()            # Parseo los items en formato key:value
        for key,value in xdata:             # Genero un bucle y obtengo toda la infor del json
            metric.add_metric([key], value) # Genero la metrica con el nombre del valor taggeado
        yield metric                        # Imprimo todas las metricas en formato OpenMetrics

if __name__ == '__main__':
    start_http_server(http_port)            # Inicio un webserver con el puerto 8000
    REGISTRY.register(CustomCollector())    # Genero un registro de OpenMetrics
    while True:                             # Genero un bucle infinito 
        time.sleep(2)                       # Espero n segundos por cada scraping
