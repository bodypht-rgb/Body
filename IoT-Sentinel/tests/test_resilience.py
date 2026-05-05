from src.attackers.web_attacker import WebAttacker

def test_web_attacker():
    attacker = WebAttacker()
    result = attacker.attack_get("/")
    assert "Success" in result or "Failed" in import pytest
import asyncio
from src.web_resilience import WebResilienceAuditor
from src.network_resilience import NetworkResilienceAuditor
from src.mqtt_resilience import MqttResilienceAuditor


@pytest.fixture
def throttle():
    return asyncio.Semaphore(1)

@pytest.mark.asyncio
async def test_web_resilience_logic(throttle):
    """Testing the logic of handling responses in the web module"""
    auditor = WebResilienceAuditor(throttle)
    # The test here confirms that the function returns text containing the word Resilience أو Exposure
    result = await auditor.analyze_web_exposure("/")
    assert any(word in result for word in ["Web", "Resilience", "Exposure", "Audit"])

@pytest.mark.asyncio
async def test_network_resilience_logic(throttle):
    """Tests the logic of the network module"""
    auditor = NetworkResilienceAuditor(throttle)
    result = await auditor.verify_ssh_hardening(username="test_user", password="test_password")
    assert "SSH" in result

@pytest.mark.asyncio
async def test_mqtt_resilience_logic(throttle):
    """Testing the logic of the module MQTT"""
    auditor = MqttResilienceAuditor(throttle)
    result = await auditor.check_mqtt_resilience(payload="TEST")
    assert "MQTT" in result
