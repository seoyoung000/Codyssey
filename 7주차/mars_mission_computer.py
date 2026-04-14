import platform
import psutil
import json

class SystemInfo:
    """시스템 정보를 수집하는 전용 클래스"""

    @staticmethod
    def get_os():
        return platform.system()

    @staticmethod
    def get_os_version():
        return platform.version()

    @staticmethod
    def get_cpu_type():
        return platform.processor()

    @staticmethod
    def get_cpu_cores():
        return f"{psutil.cpu_count(logical=False)} Cores"

    @staticmethod
    def get_memory_size():
        # GB 단위로 변환
        return round(psutil.virtual_memory().total / (1024**3), 2)
        return f"{total_gb} GB"

    @staticmethod
    def get_cpu_load():
        return f"{psutil.cpu_percent(interval=1)} %"

    @staticmethod
    def get_memory_load():
        return f"{psutil.virtual_memory().percent} %"


class MissionComputer:
    def __init__(self, name):
        self.name = name

    def get_mission_computer_info(self):
        # SystemInfo 클래스의 정적 메소드들을 활용하여 정보 수집
        info = {
            "OS": SystemInfo.get_os(),
            "OS_Version": SystemInfo.get_os_version(),
            "CPU_Type": SystemInfo.get_cpu_type(),
            "CPU_Cores": SystemInfo.get_cpu_cores(),
            "Total_Memory_GB": SystemInfo.get_memory_size()
        }
        print(f"--- [{self.name}] System Info ---")
        print(json.dumps(info, indent=4))
        return info

    def get_mission_computer_load(self):
        # SystemInfo 클래스의 정적 메소드들을 활용하여 부하 수집
        load = {
            "CPU_Usage_Percent": SystemInfo.get_cpu_load(),
            "Memory_Usage_Percent": SystemInfo.get_memory_load()
        }
        print(f"--- [{self.name}] Real-time Load ---")
        print(json.dumps(load, indent=4))
        return load

# 실행부
runComputer = MissionComputer("Mars_Explorer_01")
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
