def test_hello_world(client):
    resp = client.get('/')
    assert resp.json()['message'] == 'Hello world!'
