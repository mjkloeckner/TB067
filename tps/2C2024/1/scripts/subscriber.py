import paho.mqtt.client as mqtt

# Configuración
broker = "broker.hivemq.com"
#broker = "mqtt-dashboard.com"

topic = "tp1/kloeckner"
output_file = 'output.txt'
received_fragments = {}
last_fragment = False

def on_subscribe(self, mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    global last_fragment
    
    
    # Decodificar mensaje: número de fragmento, tamaño, bandera de último fragmento, y contenido
    payload = msg.payload.decode('utf-8')
    fragment_info, fragment = payload.rsplit('|', 1)
    fragment_number, fragment_size, is_last = map(int, fragment_info.split('|')[:3])
    
    received_fragments[fragment_number] = (fragment_size, fragment)
    print(f"Fragmento recibido {fragment_number} (size: {fragment_size})")    
    if is_last == 1:
        last_fragment = True
    
    # Reensamblar si es el último fragmento
    if last_fragment:
        reassemble_file(output_file)
        quit()

def reassemble_file(filename):
    with open(filename, 'w') as file:
        for fragment_number in sorted(received_fragments):
            fragment_size, fragment = received_fragments[fragment_number]
            file.write(fragment[:fragment_size])  # Reescribimos usando el largo correcto
    print(f"File reassembled as {filename}")

# Configuración del cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect(broker, 1883, 60)
client.subscribe(topic, qos=2)

# Mantener el cliente en funcionamiento
client.loop_forever()