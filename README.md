# 🧠 Claude + MCP Tool-Enabled Chatbot (with Chainlit)

> Anthropic Claude + FastMCP + Chainlit 기반의 실시간 스트리밍 멀티모달 도구 사용 챗봇 🎯
---

## 🛠️ 주요 기능 (Features)

- ✅ **Anthropic Claude 3.5 Sonnet 연동** (향후 GPT , sLLM 추가 에정)
- 🛠️ **MCP 도구 자동 탐색 및 호출**
- 📡 **Chainlit 인터페이스를 통한 실시간 채팅**
- 🔁 **사용자 질의 -> LLM 스트리밍  → MCP  tool calls (React) ->  최종 응답 
- 📚 **다중 MCP 연결 지원**

---
## 🛠️현재  MCP 목록 (Enabled MCP List)
- yahoo finance로 주식 목록 조회 (https://github.com/ferdousbhai/investor-agent)
---
## 📦 기술 스택

| 기술 | 설명 |
|------|------|
| [Chainlit](https://www.chainlit.io/) | LLM 기반 챗봇 인터페이스 |
| [Chainlit_MCP_cookbook](https://github.com/Chainlit/cookbook/blob/main/mcp/app.py) | Chainlit과 MCP sse 연결 |
| [https://modelcontextprotocol.io/) | MCP reference |
| [Anthropic Claude](https://www.anthropic.com/) | Claude 3.5 Sonnet LLM |
| Python (async/await) | 비동기 기반 실행 환경 |

---

## 🚀 설치 및 실행

### 1. 레포 클론 및 의존성 설치

```bash
git clone https://github.com/your-username/claude-mcp-chatbot.git
cd claude-mcp-chatbot
pip install -r requirements.txt
