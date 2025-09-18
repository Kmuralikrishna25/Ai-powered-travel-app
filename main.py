# travel_planner.py

import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.prompts import PromptTemplate
import requests
import dotenv

# Load environment varuiables
dotenv.load_dotenv()
# ---------------- CONFIG ----------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # set your Gemini API key
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")  # optional, for flights/hotels
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # for attractions
# ----------------------------------------

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=GOOGLE_API_KEY, temperature=0.7)

# Dummy functions (replace with Amadeus + SerpAPI)
def fetch_hotels(destination):
    # Here you’d call Amadeus API (mocking for now)
    return [f"Hotel {i} in {destination}" for i in range(1, 4)]

def fetch_attractions(destination):
    url = f"https://serpapi.com/search.json?q=top+attractions+in+{destination}&engine=google&api_key={SERPAPI_KEY}"
    resp = requests.get(url).json()
    results = [r["title"] for r in resp.get("organic_results", [])[:5]]
    return results if results else ["Beach", "Museum", "City Tour"]

# Create Tools for LangChain Agent
def hotel_search_tool(destination: str):
    return "\n".join(fetch_hotels(destination))

def attraction_search_tool(destination: str):
    return "\n".join(fetch_attractions(destination))

tools = [
    Tool(
        name="HotelSearch",
        func=hotel_search_tool,
        description="Get best hotels in a destination city"
    ),
    Tool(
        name="AttractionSearch",
        func=attraction_search_tool,
        description="Get top attractions in a destination city"
    )
]

# Initialize Agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,  handle_parsing_errors=True)

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.title("🌍 AI-Powered Travel Planner")

destination = st.text_input("Enter your destination:", "Bali")
days = st.number_input("Number of days:", min_value=1, max_value=30, value=4)
budget = st.number_input("Enter your budget ($):", min_value=100, value=1000)

if st.button("Generate plan"):
    with st.spinner("Planning your trip with Gemini..."):
        query = f"Plan a {days}-day trip to {destination} within a budget of ${budget}. Include estimated costs."
        result = agent.run(query)

        st.subheader("✈️ Your AI-Generated plan")
        st.write(result)

        # Hotels
        st.subheader("🏨 Suggested Hotels")
        hotels = fetch_hotels(destination)
        for h in hotels:
            st.write(" " + h)

        # Attractions
        st.subheader("📍 Must-Visit Attractions")
        attractions = fetch_attractions(destination)
        for a in attractions:
            st.write(" " + a)
