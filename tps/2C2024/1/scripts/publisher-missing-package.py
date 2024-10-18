import paho.mqtt.client as mqtt
import random
import time 

# Configuración
broker_address = "broker.hivemq.com"
# broker_address = "mqtt-dashboard.com"

topic = "tp1/aguilar_klockner"
min_size = 50  # Tamaño mínimo del fragmento
max_size = 70  # Tamaño máximo del fragmento
file_to_publish = 'input.txt'

def on_connect(client, userdata, flags, rc):
    # Al conectarse, configuramos la opción TCP_NODELAY
    client_socket = client._socket().socket  # Accede al socket subyacente
    client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Desactiva Nagle

def on_subscribe(self, mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
        
def publish_file(client, filename, min_size, max_size):
    with open(filename, 'r') as file:
        content = file.read()

    index = 0
    fragment_number = 0
    while index < len(content):
        fragment_size = random.randint(min_size, max_size)
        fragment = content[index:index+fragment_size]

        # Metadatos: número de fragmento, tamaño, y bandera de último fragmento
        is_last = 1 if index + fragment_size >= len(content) else 0
        payload = f'{fragment_number}|{fragment_size}|{is_last}|{fragment}'        

        if fragment_number != 6:
            client.publish(topic, payload, qos=2, retain=False)
            print(f"Fragmento publicado {fragment_number} (size: {fragment_size})")

        fragment_number += 1
        index += fragment_size
        time.sleep(1)

# Configuración del cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect  # Añade el manejador de eventos para cuando se conecte
client.on_subscribe = on_subscribe # Añade el manejador de suscripción
client.connect(broker_address, 1883, 60)

# Publicar el archivo fragmentado
publish_file(client, file_to_publish, min_size, max_size)

client.disconnect()
