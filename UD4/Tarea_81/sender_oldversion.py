import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect('192.168.56.103')

result = client.publish('/oficina/luz1', 'ON')