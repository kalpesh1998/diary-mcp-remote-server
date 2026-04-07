# server.py
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("my-custom-tools")

# ✅ Tool 1: Simple greeting tool
@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name"""
    return f"Hello, {name}! 👋"

# ✅ Tool 2: Add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# ✅ Tool 3: Read a file from a folder
@mcp.tool()
def read_my_file(filename: str) -> str:
    """Read contents of a file from Downloads"""
    path = f"/Users/Kalpesh.Jaiswal/Downloads/testing_claude/{filename}"
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{filename}' not found!"

# Run the server
if __name__ == "__main__":
    mcp.run()
    # mcp.run(transport="http", port=8000)