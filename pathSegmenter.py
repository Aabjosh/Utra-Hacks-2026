from google import genai

# init constants
# TAPE_WIDTH = 2 # inches

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="who is aabjosh singh from uwaterloo mechatronics eng"
)
print(response.text)