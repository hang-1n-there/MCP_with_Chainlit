# MCP 클라이언트

MCP 서버와 통신하기 위한 비동기 클라이언트 라이브러리입니다.

## 설치 방법

1. 저장소를 클론합니다:
```bash
git clone <repository-url>
cd mcp-client
```

2. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

## 사용 방법

### 기본 사용법

```python
import asyncio
from mcp_client import MCPClient

async def main():
    async with MCPClient() as client:
        # 주식 정보 조회
        stock_info = await client.get_stock_info("AAPL")
        
        # 가격 히스토리 조회
        history = await client.get_stock_history("AAPL", period="1mo")
        
        # 재무제표 조회
        financials = await client.get_financials("AAPL", statement_type="income")

if __name__ == "__main__":
    asyncio.run(main())
```

### API 엔드포인트

- `get_stock_info(ticker)`: 주식 기본 정보 조회
- `get_stock_history(ticker, period)`: 주식 가격 히스토리 조회
- `get_financials(ticker, statement_type)`: 재무제표 정보 조회

### 설정

기본적으로 클라이언트는 `http://localhost:8000`에 연결됩니다. 다른 서버 주소를 사용하려면:

```python
client = MCPClient(base_url="http://your-server-address:port")
```

## 라이센스

MIT 