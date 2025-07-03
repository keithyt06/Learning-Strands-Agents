import json
from strands import Agent, tool

@tool
def weather_info(location: str) -> str:
    """
    Get weather information for a location.
    
    Args:
        location (str): City or location name
        
    Returns:
        str: Weather information for the location
    """
    # Mock data for demonstration
    weather_data = {
        "new york": "72°F, Partly Cloudy",
        "london": "64°F, Rainy",
        "tokyo": "79°F, Sunny"
    }
    
    return weather_data.get(location.lower(), "Weather information not available")

# Create the agent outside the handler to benefit from container reuse
agent = Agent(
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    tools=[weather_info],
    system_prompt="You are a helpful weather assistant."
)

def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """
    try:
        # Extract the user message
        body = json.loads(event.get('body', '{}'))
        user_message = body.get('message', '')
        
        if not user_message:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No message provided'})
            }
        
        # Process with our agent
        response = agent(user_message)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': response.message})
        }
        
    except Exception as e:
        # Log the error
        print(f"Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }
