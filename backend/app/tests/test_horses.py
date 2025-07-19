import pytest

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.mark.anyio
async def test_example():
    assert 1 + 1 == 2
