# Write my own prometheus_exporter

### The problem.
My applications dont expose metrics in "OpenMetrics" format, and I need to extract json data that is exposed in my them. This applications don't send any information outside, only expose json output in this format
*  app : port / metrics
*  service01:80/metrics

### The idea/solution.
Write a prometheus_custom_expoter:  [CustomExporter](https://github.com/jpradoar/prometheus_exporter/blob/main/prom-exporter/custom_exporter.py)

Generate a custom prometheus exporter to scrape all applications, extract json outputs, parse it, and finally transform all json in a OpenMetrics format to will be consumed by prometheus server and show it in grafana.

<div align="center">

<br>

### General dashboard status
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/service-status-grafana.png "> 

<br>

### Architecture
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/arch.png"> 

<br>

### My app exposing their json outputs
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/service-demo.png"> 

<br>

### My Prometheus custom exporter consuming all service metrics :) 
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/exporter.png"> 

<br>

### PromQL query to get all services 
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/prom-custom.png"> 

<br>

### PromQL query to get sum of status 
<img src="https://raw.githubusercontent.com/jpradoar/prometheus_exporter/main/img/prom-custom-sum.png"> 

</div>
