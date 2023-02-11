async def test_startup_asynchronous_backend_server(async_client):
    response = await async_client.get("/docs")
    assert response.status_code == 200
