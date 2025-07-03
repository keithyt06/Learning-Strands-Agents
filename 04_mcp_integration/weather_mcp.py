from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("demo-weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get demo weather for a city (simplified example)"""
    demo_data = {
        "Beijing": "Sunny, 25°C",
        "Shanghai": "Cloudy, 23°C",
        "New York": "Rainy, 18°C"
    }
    return demo_data.get(city, f"Weather data not available for {city}")

if __name__ == "__main__":
    # Run server in stdio mode (simplest for demo)
    mcp.run(transport='stdio')
