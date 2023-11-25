import random
import time
import schedule
from astral import LocationInfo
import datetime


from paho.mqtt import client as mqtt_client


broker = '192.168.10.74'
port = 1883
topic = "eye1/power"

# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'rj'
password = 'Hapkido1!'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to Home MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


client = connect_mqtt()




def run():
  
    client.publish("test","test")
    print("Sent!")




if __name__ == '__main__':

    run()
