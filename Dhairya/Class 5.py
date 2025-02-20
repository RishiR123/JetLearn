import google.generativeai as genai

genai.configure(api_key="AIzaSyAZaxy4HUOOmyzRV9Jl20Co6Ixl6lOnGqw")

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("who is dhairya?")
print(response.text)