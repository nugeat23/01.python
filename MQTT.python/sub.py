import paho.mqtt.client as mqtt
import sqlite3

con = sqlite3.connect('iot.db')
cursor = con.cursor()








# 브로커 접속 시도 결과 처리 콜백 함수

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    if rc == 0:
        client.subscribe("iot/#")

    else:
        print('연결 실패: ', rc)

# msg: MQTTMessage 인스턴스
# msg.topic: str타입
# msg.payload: byte(binart) 배열
# binary배열.decode() --> str 변환
# cf) str.encode() --> binary로 변환

def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f'{msg.topic} {value}')
    # topic에서 user, place, sensor 정보를 추출
    # topic: 'iot/hong/bedroom/temp' --> user, place, sensor 추출
    (_, user, place, sensor) = msg.topic.split('/')

    print(f"{user}, {place}, {sensor}, {value}")
    #데이터 베이스에 저장
    sql =f'''
                INSERT INTO sensors(user,place,sensor,value)
                values('{user}','{place}','{sensor}',{value})

         '''

    cursor.execute(sql)
    con.commit()

#1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

#2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try:
    #3. 브로커 연결
    client.connect("localhost")
    #4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨.
    client.loop_forever()

except Exception as err:
    print('에러 : %s'%err)






