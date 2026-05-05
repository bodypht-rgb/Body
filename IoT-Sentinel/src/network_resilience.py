import asyncio
import asyncssh
import logging
from src.config import Config

# Preparing the records for this module
logger = logging.getLogger("IoTSentinel.Network")

class NetworkResilienceAuditor:
    """
   It assesses the resilience of network services (SSH) against unauthorized access attempts

and ensures the implementation of robust verification policies.
    """
    def __init__(self, throttle: asyncio.Semaphore):
        self.ip = Config.TARGET_IP
        self.port = Config.PORT_SSH
        self.throttle = throttle

    async def verify_ssh_hardening(self, username="root", password="password"):
        """
       It checks whether the SSH port allows access with weak credentials.
        """
        # Adherence to valve limits to ensure quiet operation
        async with self.throttle:
            try:
                logger.info(f"Initiating security handshake with {self.ip}:{self.port}")
                
              # Attempting to connect asynchronously without verifying the host keys (for inspection purposes)
                async with asyncssh.connect(
                    self.target_host(), 
                    username=username, 
                    password=password, 
                    known_hosts=None,
                    login_timeout=7
                ) as conn:
                    
                    logger.warning(f"SSH Weak Credential Found: {username}:{password}")
                    
                    # Execute a simple command to check permissions (such as id)
                    result = await conn.run("id", check=True)
                    output = result.stdout.strip()
                    
                    return f"[!] SSH Security Alert: Access granted with '{username}'. Identity: {output}"
            
            except (asyncssh.PermissionDenied, asyncssh.ProtocolError) as e:
                return f"[+] SSH Resilience Confirmed: Access denied for '{username}' as expected."
            except Exception as e:
                return f"[-] SSH Audit Notice: Could not complete scan. Reason: {str(e)}"

    def target_host(self):
        """Returns the target address"""
        return self.ip

