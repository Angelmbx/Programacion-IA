import paho.mqtt.client as mqtt


broker_adress = "192.168.56.103"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username="dispositivo", password="abc123.")
client.connect(broker_adress, 1883) 


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Número de mensajes publicados en esta ejecución: {mid}")

def on_disconnect(client, userdata, rc, properties=None, reason_string=None):
   print("Desconectado correctamente")


client.on_publish = on_publish

client.on_disconnect = on_disconnect

client.publish("oficina/luz1", "on") 
client.publish("oficina/luz1", "mensaje erróneo. $@1!") 
client.publish("oficina/luz1", "oFf") 

client.disconnect()