def connect():
    try:
        print('네트워크 접속')
        # a = 2/0       # 예외가 발생하는 경우
        a = 2/2       # 예외가 발생하지 않는 경우
        print('네트워크 통신 수행')
        return

    except Exception as e:
        print('[에러]', e)


    finally:        # 예외 발생과 무관하게 실행
        print('접속 해제')

    print('작업 완료')


connect()