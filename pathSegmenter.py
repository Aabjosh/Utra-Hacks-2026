from google import genai

# init constants
TAPE_WIDTH = 2 # inches
FILE_NAME = "messagebank/message.txt"
SAMPLE_FILE = "messagebank/testMessage.txt"

LENGTH_KEY = "$LENGTH$"
WIDTH_KEY = "$WIDTH$"

TAPE_THICKNESS_KEY = "$THICKNESS$"
SAMPLE_IMAGE_1_DIRECT = "images/SAMPLE_223_1.png"
SAMPLE_IMAGE_2_DIRECT = "images/SAMPLE_223_2.png"

# add locations for images (add to repo)

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

with open ( SAMPLE_FILE , "r" ) as file:
    fileContents = file.read()

response = client.models.generate_content(
    model = "gemini-3-flash-preview", 
    contents = fileContents
)
print( response.text )