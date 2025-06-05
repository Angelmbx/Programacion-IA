import paho.mqtt.client as mqtt
import uuid

broker_adress = "192.168.56.103"
clienteID = uuid.uuid4
client = mqtt.Client("Cliente{}".format(clienteID))

def recibirMensaje(client, userdata, message):

    orden = str(message.payload.decode("utf-8"))

    if orden.lower() == "on":
        print("Bombilla encendida!")
    elif orden.lower() == "off":
        print("Bombilla apagada!")
    else:
        print("Orden desconocida. ON/OFF para encender o apagar bombilla.")



client.on_message = recibirMensaje
client.connect(broker_adress, 1883) 
client.suscribe("oficina/luz1")
client.loop_start()