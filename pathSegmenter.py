from google import genai
from google.genai import types
from PIL import Image

# init constants
TAPE_WIDTH = 2 # inches
FILE_NAME = "messagebank/message.txt"
SAMPLE_FILE = "messagebank/testMessage.txt"

TAPE_THICKNESS_KEY = "$THICKNESS$"
LENGTH_KEY = "$LENGTH$"
WIDTH_KEY = "$WIDTH$"

SAMPLE_IMAGE_1_DIRECT = "images/SAMPLE_223_1.png"
SAMPLE_IMAGE_2_DIRECT = "images/SAMPLE_223_2.png"

def fileReplacer( fileAsString , segmentThickness , boxLength , boxWidth ):
    output = fileAsString.replace( TAPE_THICKNESS_KEY , str(segmentThickness) )
    output = output.replace( LENGTH_KEY , str(boxLength) )
    output = output.replace( WIDTH_KEY , str(boxWidth) )
    return output

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

with open ( FILE_NAME , "r" ) as file:
    fileContents = file.read()

messageToGemini = fileReplacer( fileContents , 2 , 10 , 20 )

with open( SAMPLE_IMAGE_1_DIRECT , "rb" ) as f:
    imageBytes1 = f.read()

with open( SAMPLE_IMAGE_2_DIRECT , "rb" ) as f:
    imageBytes2 = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash-preview",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text( 
                    text = fileContents 
                ),
                types.Part.from_bytes(
                    data = imageBytes1,
                    mime_type = "image/png"
                ),
                types.Part.from_bytes(
                    data = imageBytes2,
                    mime_type = "image/png"
                )
            ]
        )
    ]
)

# response = client.models.generate_content(
#     model = "gemini-2.5-pro", 
#     contents = messageToGemini
# )
print( response.text )