from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together and returns the result."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
