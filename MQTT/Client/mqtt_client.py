import paho.mqtt.client as mqtt
import ssl

# MQTT Broker details
broker_address = "43.78.31.211"  
broker_port = 8883  
topic = "solarplant/solarplantA"  
client_id = "SOLAR433"  

client_certificate = "env/certificate.pem"
client_key = "env/privatekey.pem"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_publish(client, userdata, mid):
    print("Message Published")

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_publish = on_publish

client.tls_set(ca_certs=ca_certificate, certfile=client_certificate, tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect(broker_address, broker_port, 60)

payload = "Power Output: 100 kWh, Status: Active"
client.publish(topic, payload)

client.disconnect()
