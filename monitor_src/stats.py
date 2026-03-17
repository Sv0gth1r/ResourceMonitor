import psutil
import time

GB_SIZE = (1024**3)
MB_SIZE = (1024**2)

class Stats:
    def __init__(self):
        self.cpu_percent = -1 
        self.memory = -1
        self.disk = -1
        self.net_io = -1
        self.process_nbr = -1

    def update_stats(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory()
        self.disk = psutil.disk_usage('/')
        self.net_io = psutil.net_io_counters()
        self.process_nbr = len(psutil.pids())

    def get_stats(self):
        self.update_stats()
        return {
            "cpu": f"{self.cpu_percent}%",
            "memory_total_gb": round(self.memory.total / GB_SIZE, 2),
            "memory_used_gb": round(self.memory.used / GB_SIZE, 2),
            "memory_percent": self.memory.percent,
            "disk_total_gb": round(self.disk.total / GB_SIZE, 2),
            "disk_used_gb": round(self.disk.used / GB_SIZE, 2),
            "disk_percent": self.disk.percent,
            "network_sent_mb": round(self.net_io.bytes_sent / MB_SIZE, 2),
            "network_recv_mb": round(self.net_io.bytes_recv / MB_SIZE, 2),
            "processes": self.process_nbr,
            "timestamp": time.strftime("%H:%M:%S")
        }

    def __str__():
        stats = self.get_stats()
        for stat in stats:
            print(stat)
