import requests

def get_weather():
    # Using wttr.in, a free weather service that doesn't require an API key
    city = "Manila"
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
    except Exception:
        return "Could not fetch weather data."

def get_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"\"{data['content']}\" — {data['author']}"
    except Exception:
        return "Keep pushing forward!"

def main():
    print("=" * 40)
    print("     YOUR PERSONAL DAILY BRIEFING     ")
    print("=" * 40)
    
    print("\n🌤️  WEATHER:")
    print(get_weather())
    
    print("\n💡 INSPIRATION OF THE DAY:")
    print(get_quote())
    
    print("\n" + "=" * 40)
    print("Have a productive day!")

if __name__ == "__main__":
    main()