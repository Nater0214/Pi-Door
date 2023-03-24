import requests as r

# server listening on port 13337
# posts door status to pi server machine
def send_door_status(doorId, isOpen, timeStamp):
    req = r.post('pi-server-url', json={
        "door_id": doorId,
        "open": isOpen,
        "timestamp": timeStamp,
    })

send_door_status()