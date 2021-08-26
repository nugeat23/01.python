import paho.mqtt.client as mqtt

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
# cf) str.encode() --> binart로 변환

def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f'{msg.topic} {value}')

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






