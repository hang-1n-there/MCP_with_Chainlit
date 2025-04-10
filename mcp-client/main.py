import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()
        self.openai = OpenAI()
    # methods will go here
    async def connect_to_server(self, server_script_path: str) -> None:
        """
        Connect to a MCP server

        Args:
            server_script_path (str): Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_javascript = server_script_path.endswith('.js')

        if not is_python and not is_javascript:
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command = command, 
            args = [server_script_path],
            env = None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        response = await self.session.list_tools()
        tools = response.tools

        print("Available tools: ", [tool.name for tool in tools])
    
    async def process_query(self, query: str) -> str:
        "Process a query using the MCP server and available tools"
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_schema
        } for tool in response.tools ]

        response = self.openai.chat.completions.create(
            model = "gpt-4-turbo-2024-04-09",
            messages = messages,
            tools = available_tools,
            tool_choice = "auto"
        )

        final_text = []
        assistant_message_content = []
        
        for content in response.output:
            if content.type ==
        return response.choices[0].message.content
        
