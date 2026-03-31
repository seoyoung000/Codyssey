import random

class DummySensor:
    """화성 기지 환경 시뮬레이션을 위한 더미 센서 클래스"""
    
    CONFIG = {
        "internal_temp": (18, 30),
        "external_temp": (0, 21),
        "internal_hum": (50, 60),
        "external_illu": (500, 715),
        "internal_co2": (0.02, 0.1),
        "internal_o2": (4, 7)
    }

    def __init__(self):
        self._env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0
        }

    def set_env(self):
        c = self.CONFIG
        # random.uniform을 사용하여 실시간 환경의 미세한 변화(실수)를 시뮬레이션
        self._env_values["mars_base_internal_temperature"] = random.uniform(*c["internal_temp"])
        self._env_values["mars_base_external_temperature"] = random.uniform(*c["external_temp"])
        self._env_values["mars_base_internal_humidity"] = random.uniform(*c["internal_hum"])
        self._env_values["mars_base_external_illuminance"] = random.uniform(*c["external_illu"])
        self._env_values["mars_base_internal_co2"] = random.uniform(*c["internal_co2"])
        self._env_values["mars_base_internal_oxygen"] = random.uniform(*c["internal_o2"])

    def get_env(self):
        return self._env_values.copy()


if __name__ == "__main__":
    # 1. ds 인스턴스 생성
    ds = DummySensor()

    # 2. 데이터 생성 및 읽기
    ds.set_env() 
    result = ds.get_env()

    # 3. 결과 출력
    print("--- 화성 기지 환경 보고서 ---")
    for key, value in result.items():
        print(f"{key}: {value:.2f}")
