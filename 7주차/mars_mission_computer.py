import platform
import psutil
import json

class MissionComputer:
    def __init__(self, name):
        self.name = name

    def get_mission_computer_info(self):
        """
        운영체제, CPU, 메모리 등 시스템의 하드웨어 정보를 가져와 JSON으로 출력합니다.
        """
        info = {
            "OS": platform.system(),
            "OS_Version": platform.version(),
            "CPU_Type": platform.processor(),
            "CPU_Cores": psutil.cpu_count(logical=False),  # 물리 코어 수
            "Total_Memory_GB": round(psutil.virtual_memory().total / (1024**3), 2)
        }
        
        print("--- Mission Computer System Info ---")
        print(json.dumps(info, indent=4))
        return info

    def get_mission_computer_load(self):
        """
        CPU 및 메모리의 실시간 사용량을 가져와 JSON으로 출력합니다.
        """
        load = {
            "CPU_Usage_Percent": psutil.cpu_percent(interval=1),
            "Memory_Usage_Percent": psutil.virtual_memory().percent
        }
        
        print("--- Mission Computer Real-time Load ---")
        print(json.dumps(load, indent=4))
        return load

# 1. MissionComputer 클래스를 runComputer라는 이름으로 인스턴스화
runComputer = MissionComputer("Mars_Explorer_01")

# 2. 시스템 정보 출력 메소드 호출
runComputer.get_mission_computer_info()

# 3. 실시간 부하 정보 출력 메소드 호출
runComputer.get_mission_computer_load()