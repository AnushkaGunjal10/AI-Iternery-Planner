import streamlit as st
from google.generativeai import configure, GenerativeModel
from typing import List

# Configure Gemini API (Replace with your own API key)
configure(api_key="AIzaSyBKTbZgzd2e4ZmNykuQRGdrSc4h7YmhY9g")
gemini_model = GenerativeModel("gemini-2.0-flash")

# Generate an itinerary using Gemini AI
def generate_itinerary(city: str, interests: List[str], days: int) -> str:
    interest_str = ", ".join(interests)
    
    prompt = f"""
    Create a unique {days}-day travel itinerary for {city} based on the following interests: {interest_str}.
    Each day's plan should include:
    - Morning: Activities like sightseeing, nature walks, or cultural visits.
    - Afternoon: Adventure activities, historical tours, or food experiences.
    - Evening: Entertainment, nightlife, or relaxation options.
    
    Ensure each day has different activities and travel tips.
    Format the response in a structured way.
    """

    try:
        response = gemini_model.generate_content(prompt)
        return response.text if response else "⚠️ Could not generate itinerary. Please try again."
    except Exception as e:
        return f"⚠️ Error generating itinerary: {str(e)}"

# Streamlit UI
def create_ui():
    st.title("🌍 AI Travel Planner")

    # User Inputs
    city = st.text_input("Enter City:")
    days = st.number_input("Enter Number of Days:", min_value=1)
    interests = st.text_area("Enter Interests (comma separated):")

    # Generate Itinerary Button
    if st.button("✨ Generate AI Itinerary ✨"):
        # Validate inputs
        if not city or not interests:
            st.error("Please enter a valid city and interests.")
        else:
            interests_list = [i.strip() for i in interests.split(",")]
            itinerary = generate_itinerary(city, interests_list, days)
            st.write(itinerary)

# Start the UI
create_ui()
