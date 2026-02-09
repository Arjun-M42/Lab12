from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


from tools.weather_tool import get_weather

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.4
)

# Prompt
trip_prompt = PromptTemplate(
    input_variables=["city", "weather"],
    template="""
You are an intelligent travel planning assistant.

City: {city}

Weather Information:
{weather}

Tasks:
1. Write one paragraph on the cultural and historical significance of the city.
2. Summarize current weather and forecast.
3. Create a weather-aware 3-day itinerary.
4. Suggest a mock flight.
5. Suggest a mock hotel.
"""
)

def plan_trip(city: str):
    # MCP-style tool call
    weather_data = get_weather(city)

    # LLM reasoning
    prompt = trip_prompt.format(
        city=city,
        weather=weather_data
    )

    response = llm.invoke(prompt)
    return response.content
