const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const BASE_WS = `${wsProtocol}//${window.location.host}/ws`;
// const BASE_WS = 'ws://localhost:8001/'

export function createSocket(path, onMessage, onClose) {
  const token = localStorage.getItem('token')
  console.log('WS creating')
  const ws = new WebSocket(`${BASE_WS}${path}?token=${token}`)

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    onMessage(data)
  }

  ws.onclose = () => {
    if (onClose) onClose()
  }

  ws.onerror = (e) => console.error('WS error:', e)

  return ws
}
