from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.active_connections: dict[int, list[WebSocket]] = {} # TODO: redis

    async def connect(self, id: int, websocket: WebSocket):
        if not self.active_connections.get(id):
            self.active_connections[id] = []
        self.active_connections[id].append(websocket)

    async def disconnect(self, id: int, websocket: WebSocket):
        if self.active_connections.get(id):
            self.active_connections[id].remove(websocket)

    async def broadcast(self, id: int, message):
        if self.active_connections[id]:
           for connection in self.active_connections[id]:
               await connection.send_json(message.model_dump())
               

websocket_manager = ConnectionManager()