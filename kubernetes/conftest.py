import kubernetes
import pytest

@pytest.fixture(scope="session")
def kubernetes_test_client():
    kubernetes.config.load_config()
    return kubernetes.client.CoreV1Api(), kubernetes.client.AppsV1Api()
