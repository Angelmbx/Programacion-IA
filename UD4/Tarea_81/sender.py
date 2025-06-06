import paho.mqtt.client as mqtt


broker_adress = "192.168.56.103"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker_adress, 1883) 


def on_publish(client, userdata, mid, reason_code, properties):
    print("Datos publicados: {}".format(userdata))

def on_disconnect(client, userdata, rc, properties=None, reason_string=None):
   print("Desconectado correctamente")


client.on_publish = on_publish

client.on_disconnect = on_disconnect

client.connect(broker_adress, 1883)
client.publish("oficina/luz1", "on") 
client.disconnect()