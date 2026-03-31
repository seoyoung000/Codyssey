import random


class DummySensor:
    """
    화성 기지의 환경 데이터를 시뮬레이션하기 위한 더미 센서 클래스.
    실제 센서 하드웨어가 연결되기 전 로직 테스트용으로 사용함.
    """

    def __init__(self):
        # 환경 데이터를 저장할 사전(dict) 객체 초기화
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0
        }

    def set_env(self):
        """
        각 환경 항목에 대해 지정된 범위 내의 랜덤 값을 생성하여 저장함.
        """
        # 내부 온도: 18~30도
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        
        # 외부 온도: 0~21도
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        
        # 내부 습도: 50~60%
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        
        # 외부 광량: 500~715 W/m2
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        
        # 내부 이산화탄소 농도: 0.02~0.1%
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        
        # 내부 산소 농도: 4%~7%
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    def get_env(self):
        """
        현재 저장된 환경 데이터 사전 객체를 반환함.
        """
        return self.env_values


if __name__ == "__main__":
    # 1. DummySensor 인스턴스 생성
    ds = DummySensor()

    # 2. 데이터 생성 (set_env 호출)
    ds.set_env()

    # 3. 데이터 획득 및 출력 (get_env 호출)
    current_env = ds.get_env()

    print("=== 화성 기지 미션 컴퓨터: 환경 모니터링 시스템 ===")
    for key, value in current_env.items():
        # 보기 편하도록 소수점 둘째 자리까지 출력
        print(f"{key}: {value:.2f}")