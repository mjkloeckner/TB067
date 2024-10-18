import paho.mqtt.client as mqtt
import random
import time 
# Configuración
broker_address = "broker.hivemq.com"
#broker_address = "mqtt-dashboard.com"

topic = "tp1/aguilar_klockner"     # <<<<<<<<<<====== Completar con el nombre del grupo
min_size = 100  # Tamaño mínimo del fragmento
max_size = 150  # Tamaño máximo del fragmento
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
    total_size = len(content)
    control_size = 0
    while index < total_size:
        fragment_size = random.randint(min_size, max_size)
        fragment = content[index:index+fragment_size]
        
        # Metadatos: número de fragmento, tamaño, y bandera de último fragmento
        is_last = 0
        if random.randint(1, 100) > 10: #Establezco un 10% de perder el fragmento
            payload = f'{fragment_number}|{fragment_size}|{is_last}|{fragment}'        
            client.publish(topic, payload, qos=2, retain=False)
            control_size += fragment_size
        print(f"Fragmento publicado {fragment_number} (size: {fragment_size})")
        index += fragment_size
        fragment_number += 1
        time.sleep(1)

    if control_size < total_size: # Detecto si se perdio un fragmento y reinicio el envio en ese caso enviando un mensansaje de error
        payload = f'{-1}|{4}|{is_last}|{1}'        
        client.publish(topic, payload, qos=2, retain=False)
        print(f"Fragmento publicado {-1} (size: {4})")
        print(f"Error de transmision. Reiniciando secuencia")
        publish_file(client, filename, min_size, max_size)
    else: #En caso de exito envio mensaje de exito y finalizo
        is_last = 1
        payload = f'{100}|{4}|{is_last}|{0}'       
        client.publish(topic, payload, qos=2, retain=False)
        print(f"Fragmento publicado {-0} (size: {4})")
        print(f"Transmision exitosa. Finalizando secuencia")

# Configuración del cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect  # Añade el manejador de eventos para cuando se conecte
client.on_subscribe = on_subscribe # Añade el manejador de suscripción
client.connect(broker_address, 1883, 60)

# Publicar el archivo fragmentado
publish_file(client, file_to_publish, min_size, max_size)

client.disconnect()
