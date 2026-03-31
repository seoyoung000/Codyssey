import random

class DummySensor:
    """화성 기지 환경 시뮬레이션을 위한 더미 센서 클래스"""
    
    # 유지보수를 위한 환경 설정 상수 (범위 지정)
    CONFIG = {
        "internal_temp": (18, 30),
        "external_temp": (0, 21),
        "internal_hum": (50, 60),
        "external_illu": (500, 715),
        "internal_co2": (0.02, 0.1),
        "internal_o2": (4, 7)
    }

    def set_env(self):
        c = self.CONFIG
        # random.uniform을 통해 생성
        self._env_values["mars_base_internal_temperature"] = random.uniform(*c["internal_temp"])
        self._env_values["mars_base_external_temperature"] = random.uniform(*c["external_temp"])
        self._env_values["mars_base_internal_humidity"] = random.uniform(*c["internal_hum"])
        self._env_values["mars_base_external_illuminance"] = random.uniform(*c["external_illu"])
        self._env_values["mars_base_internal_co2"] = random.uniform(*c["internal_co2"])
        self._env_values["mars_base_internal_oxygen"] = random.uniform(*c["internal_o2"])

    def get_env(self):
        """현재 저장된 환경 데이터의 복사본을 반환함"""
        return self._env_values.copy()

    def set_env(self):
        """CONFIG 범위 내에서 랜덤 데이터를 생성하여 저장함"""
        c = self.CONFIG
        # random.uniform을 통해 소수점 단위까지 정밀하게 생성
        self._env_values["mars_base_internal_temperature"] = random.uniform(*c["internal_temp"])
        self._env_values["mars_base_external_temperature"] = random.uniform(*c["external_temp"])
        self._env_values["mars_base_internal_humidity"] = random.uniform(*c["internal_hum"])
        self._env_values["mars_base_external_illuminance"] = random.uniform(*c["external_illu"])
        self._env_values["mars_base_internal_co2"] = random.uniform(*c["internal_co2"])
        self._env_values["mars_base_internal_oxygen"] = random.uniform(*c["internal_o2"])

    def get_env(self):
        """현재 저장된 환경 데이터의 복사본을 반환함"""
        return self._env_values.copy()


if __name__ == "__main__":
    # 1. ds라는 이름으로 인스턴스 생성
    ds = DummySensor()

    # 2. 데이터 갱신 및 확인 (순차 호출)
    ds.set_env()             # 값 생성
    result = ds.get_env()    # 값 읽기

    # 3. 결과 출력
    print("--- 화성 기지 환경 보고서 ---")
    for key, value in result.items():
        print(f"{key}: {value:.2f}")
