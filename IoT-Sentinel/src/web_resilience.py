import asyncio
import httpx
import logging
from src.config import Config

# Preparing the records for this module
logger = logging.getLogger("IoTSentinel.Web")

class WebResilienceAuditor:
    """
    It analyzes the web administration interfaces of IoT devices to verify their resilience

against unauthorized exploration and simple denial-of-service attacks.
    """
    def __init__(self, throttle: asyncio.Semaphore):
        self.base_url = f"http://{Config.TARGET_IP}:{Config.PORT_HTTP}"
        self.throttle = throttle

    async def analyze_web_exposure(self, endpoint="/"):
        """
       It examines a specific endpoint to verify the system's response and the protection available.
        """
        #Using a semaphore to ensure the server is not overwhelmed with requests
        async with self.throttle:
            try:
                logger.info(f"Auditing web endpoint: {endpoint}")
                
                # Using HTTPX to send an asynchronous request
                async with httpx.AsyncClient(timeout=5.0) as client:
                    response = await client.get(f"{self.base_url}{endpoint}")
                    
                    if response.status_code == 200:
                        return f"[!] Web Exposure Alert: Accessible endpoint found at {endpoint} (Status 200)."
                    elif response.status_code == 403:
                        return f"[+] Web Resilience: Endpoint {endpoint} is properly secured (403 Forbidden)."
                    else:
                        return f"[*] Web Audit: {endpoint} returned status {response.status_code}."

            except httpx.ConnectError:
                return f"[-] Web Audit Notice: Target web server is unreachable at {self.base_url}."
            except Exception as e:
                return f"[-] Web Audit Error: Unexpected failure during scan ({str(e)})."
