# 수업 전용

# --- 08.26 --- #

class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

def handle_user_login(event_data):
    return f"로그인 처리 : 사용자 {event_data['username']}가 로그인 했습니다."
    
def handle_user_logout(event_data):
    return f"로그아웃 처리 : 사용자 {event_data['username']}가 로그아웃 했습니다."
    
def handle_data_update(event_data):
    return f"데이터 업데이트 : {event_data['field']}를  {event_data['value']}로 변경합니다."

# 이벤트 타입에 따른 핸드러 매핑 (함수를 데이터로 처리)
event_handlers = {
    "LOGIN" : handle_user_login,
    "LOGOUT" : handle_user_logout,
    "UPDATE" : handle_data_update
}

# 이벤트 처리 함수 (고차 함수)
def process_event(event, handlers):
    if event.type in handlers:
        return handlers[event.type](event.data)
    return f"처리되지 않은 이벤트 타입 : {event.type}"

# 여러 이벤트 처리
events = [
    Event("LOGIN", {"username" : "Lee Tae Soo"}),
    Event("UPDATE", {"field" : "email", "value" : "taesoo@example.com"}),
    Event("LOGOUT", {"username" : "Lee Tae Soo"}),
    Event("UNKNOWn", {"data" : "some data"})
    
]

results = list(map(lambda event : process_event(event, event_handlers), events))
for result in results:
    print(result)