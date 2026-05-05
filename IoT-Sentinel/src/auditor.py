import asyncio
import logging
from src.network_resilience import NetworkResilienceAuditor
from src.web_resilience import WebResilienceAuditor
from src.mqtt_resilience import MqttResilienceAuditor
from src.config import Config

# Setting up a professional logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s'
)
logger = logging.getLogger("IoTSentinel")

async def run_audit_sequence():
    """
    The main tasks of auditing system resilience simultaneously.
    """
    logger.info(f"--- Starting IoT Resilience Audit Sequence on {Config.TARGET_IP} ---")
    
   # Valve definition for controlling the number of concurrent tasks (Throttling)

# Value read from the Config.MAX_TASKS we added previously
    throttle = asyncio.Semaphore(Config.MAX_TASKS)

    # Setting up audit classes
    net_auditor = NetworkResilienceAuditor(throttle)
    web_auditor = WebResilienceAuditor(throttle)
    mqtt_auditor = MqttResilienceAuditor(throttle)

   # Running Concurrency Tests

# Note: Job titles have been changed to more professional, defensive terms.
    tasks = [
        net_auditor.verify_ssh_hardening(),
        web_auditor.analyze_web_exposure(),
        mqtt_auditor.check_mqtt_resilience()
    ]

    logger.info(f"Dispatching {len(tasks)} audit tasks with throttle limit: {Config.MAX_TASKS}")
    
   # Execute tasks and wait for results
    results = await asyncio.gather(*tasks, return_exceptions=True)

   # Display results in the log
    for result in results:
        if isinstance(result, Exception):
            logger.error(f"Task encountered an error: {result}")
        else:
            logger.info(result)

    logger.info("--- Resilience Audit Sequence Complete ---")

def main():
    try:
        asyncio.run(run_audit_sequence())
    except KeyboardInterrupt:
        logger.warning("Audit interrupted by user.")
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")

if __name__ == "__main__":
    main()
