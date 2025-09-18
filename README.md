# Travel Planner App

A web/mobile app to help users plan trips: find information about attractions in a destination, search & book hotels, and get AI-assisted travel planning using Google Gemini.

---

## 🛠 Tech Stack & APIs

| Component | Purpose |
|-----------|---------|
| **Google Gemini API** | Provides generative AI capabilities (chat, suggestions, itinerary generation, trip summaries, etc.) |
| **Amadeus API** | Used for searching hotel listings, availability, pricing, hotel details & booking. :contentReference[oaicite:0]{index=0} |
| **SerpAPI** | Used to fetch data on attractions / points of interest in the selected destination (top sights, things to do) by scraping/parsing structured Google Search results. :contentReference[oaicite:1]{index=1} |

---

## 🚀 Features

- Input destination + dates → get a suggested itinerary (attractions, hotels, things to do)  
- Search for hotels via Amadeus by budget, star rating, amenities, etc.  
- Explore attractions / sightseeing spots via SerpAPI (top sights, local favorites, etc.)  
- Use Google Gemini to provide conversational assistance: itinerary editing, travel tips, packing suggestions, etc.  
- Book hotels (if booking flow supported via Amadeus)  
- Save / export itinerary

---

## 🔧 Setup & Installation

### Prerequisites

- Python 3.8+ / Node.js (depending on your stack)  
- Accounts & API keys:  
  - Google Gemini (or Google GenAI) API key  
  - Amadeus Developer account & API key / credentials :contentReference[oaicite:2]{index=2}  
  - SerpAPI key for accessing Google Search / Top Sights / Places endpoints :contentReference[oaicite:3]{index=3}  

### Local setup

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/travel-planner-app.git
   cd travel-planner-app
2. create and actiavte the virtual environment

python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

3. install dependencies

pip install -r requirements.txt

4. Set environment variables (in .env or your shell):
   you can do it 2 wayss either by providing the credentials in .dotenv or google cloud credentials in json format and accescing it using powershell

5. Configure other settings (e.g. default model for Gemini, region / locale for Amadeus / SerpAPI) in a config file or via environment.