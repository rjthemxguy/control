import random
import time
import schedule
from astral import LocationInfo
import datetime


from paho.mqtt import client as mqtt_client


broker = '192.168.10.74'
port = 1883
topic = "eye1/power"
effectTopic = "eye1/effect"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'rj'
password = 'Hapkido1!'


loc = LocationInfo(name='SJC', region='CA, USA', timezone='America/Los_Angeles',
                   latitude=37.3713439, longitude=-121.944675)

from astral.sun import sun
s = sun(loc.observer, date=datetime.date.today(), tzinfo=loc.timezone)

sunset = s["sunset"].strftime("%H:%M")



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


client = connect_mqtt()


    

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"off"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:


            break




def allOn(client):
     client.publish("wled/all","on")



def runAllOn():
    allOn(client)





schedule.every().day.at(sunset).do(runAllOn)






def run():
    
    

    while True:	
        client.loop_start()
        
        
        client.loop_stop()
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    run()
