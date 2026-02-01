from google import genai

# init constants
TAPE_WIDTH = 2 # inches
FILE_NAME = "message.txt"
LENGTH_KEY = "$LENGTH$"
WIDTH_KEY = "$WIDTH$"
TAPE_THICKNESS_KEY = "$THICKNESS$"

# add locations for images (add to repo)

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=""
)
print(response.text)