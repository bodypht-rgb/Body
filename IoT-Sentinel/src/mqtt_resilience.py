import asyncio
import logging
from aiomqtt import Client, MqttError
from src.config import Config

# Preparing the records for this module
logger = logging.getLogger("IoTSentinel.MQTT")

class MqttResilienceAuditor:
    """
   It checks the resilience of the message broker (MQTT Broker) against unauthorized data injections.
    """
    def __init__(self, throttle: asyncio.Semaphore):
        self.ip = Config.TARGET_IP
        self.port = Config.PORT_MQTT
        self.topic = Config.MQTT_TOPIC
        self.throttle = throttle

    async def check_mqtt_resilience(self, payload="RESILIENCE_TEST_DATA"):
        """
       It attempts to send a scan message to check for vulnerabilities in the Access Control system..
        """
        # Use the semaphore to ensure that the number of allowed tasks is not exceeded
        async with self.throttle:
            try:
               # Asynchronous connection to the mediator
                async with Client(self.ip, port=self.port, timeout=5) as client:
                    logger.info(f"Attempting to verify topic integrity: {self.topic}")
                    
                    # Send message
                    await client.publish(self.topic, payload=payload)
                    
                    return f"[!] MQTT Resilience Result: Topic '{self.topic}' is open for unauthenticated publishing."
            
            except MqttError as e:
                return f"[+] MQTT Resilience Result: Access Denied or Connection Failed as expected ({e})."
            except Exception as e:
                return f"[-] MQTT Audit Error: Unexpected issue during scan ({str(e)})."

