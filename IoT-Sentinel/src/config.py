import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TARGET_IP = os.getenv("TARGET_IP", "127.0.0.1")
    PORT_SSH = int(os.getenv("TARGET_PORT_SSH", 22))
    PORT_HTTP = int(os.getenv("TARGET_PORT_HTTP", 80))
    PORT_MQTT = int(os.getenv("TARGET_PORT_MQTT", 1883))
    MQTT_TOPIC = os.getenv("MQTT_TOPIC", "audit/test/device")
    # Ax16be68
    MAX_TASKS = int(os.getenv("MAX_CONCURRENT_TASKS", 2))
