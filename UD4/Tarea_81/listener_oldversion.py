import paho.mqtt.client as mqtt

def message_recibe(client, userdata, message):
    mensaje = str(message.payload.decode('utf-8'))
    if message == 'OFF':
        print('Light off')
    elif message == 'ON':
        print('Light on')
    else:
        print("That's a nono command")
    
client = mqtt.Client(client_id='Cliente2')
client.connect("192.168.56.103")
client.subscribe('/oficina/luz1')
client.on_message = message_recibe

client.loop_start
while True:
    pass