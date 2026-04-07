import time

class DummySensor:
    """문제 3에서 정의된 가상의 센서 클래스"""
    def get_value(self):
        # 센서 값을 시뮬레이션하기 위한 임의의 값 반환
        return 25.5

class MissionComputer:
    def __init__(self):
        # 화성 기지 환경 값을 저장할 사전(Dict) 객체 속성
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0
        }
        # DummySensor 클래스를 ds라는 이름으로 인스턴스화
        self.ds = DummySensor()

    def get_sensor_data(self):
        """센서 값을 가져와서 JSON 형식으로 출력하는 과정을 5초마다 반복"""
        try:
            while True:
                # 센서의 값을 가져와서 env_values에 담기
                for key in self.env_values:
                    self.env_values[key] = self.ds.get_value()

                # env_values를 별도 모듈(json) 없이 직접 구현하여 출력
                # 가독성을 위해 JSON 포맷 문자열 수동 생성
                json_str = "{\n"
                keys = list(self.env_values.keys())
                for i in range(len(keys)):
                    k = keys[i]
                    v = self.env_values[k]
                    json_str += f'    "{k}": {v}'
                    # 마지막 요소가 아니면 쉼표 추가
                    if i < len(keys) - 1:
                        json_str += ","
                    json_str += "\n"
                json_str += "}"

                print(json_str)
                print("-" * 40)

                #  5초에 한 번씩 반복
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n모니터링이 중단되었습니다.")

# MissionComputer 클래스를 RunComputer라는 이름으로 인스턴스화
RunComputer = MissionComputer()

if __name__ == "__main__":
    # get_sensor_data() 메소드 호출을 통해 지속적 출력 실행
    RunComputer.get_sensor_data()