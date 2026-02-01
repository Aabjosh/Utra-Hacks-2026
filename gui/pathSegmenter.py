from google import genai
from google.genai import types
from PIL import Image

# init constants
# TAPE_WIDTH = 2.0 # inches
# MINIMUM_LENGTH = 220.0
# MAXIMUM_LENGTH = 237.0
FILE_NAME = "messagebank/message.txt"
# SAMPLE_FILE = "messagebank/testMessage.txt"

# TAPE_THICKNESS_KEY = "$THICKNESS$"
# MAX_LENGTH_KEY = "$MAX_LENGTH$"
# MIN_LENGTH_KEY = "$MIN_LENGTH$"

SAMPLE_IMAGE_1_DIRECT = "images/SAMPLE_223_1.png"
SAMPLE_IMAGE_2_DIRECT = "images/SAMPLE_223_2.png"
ATTEMPT_AT_CALCULATING_DIRECT = "images/unnamed (3).jpg"

# def fileReplacer( fileAsString , segmentThickness , boxLength , boxWidth ):
#     output = fileAsString.replace( TAPE_THICKNESS_KEY , str(segmentThickness) )
#     output = output.replace( LENGTH_KEY , str(boxLength) )
#     output = output.replace( WIDTH_KEY , str(boxWidth) )
#     return output

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

# function for the thingy to use
def runImageProcessor( imageFromApp ):
    with open ( FILE_NAME , "r" ) as file:
        fileContents = file.read()

    # messageToGemini = fileReplacer( fileContents , 2 , 10 , 20 )

    with open( SAMPLE_IMAGE_1_DIRECT , "rb" ) as f:
        imageBytes1 = f.read()

    with open( SAMPLE_IMAGE_2_DIRECT , "rb" ) as f:
        imageBytes2 = f.read()

    with open( ATTEMPT_AT_CALCULATING_DIRECT , "rb" ) as f:
        imageBytesData = f.read()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
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
                    ),
                    types.Part.from_bytes(
                        data = imageFromApp,
                        mime_type = "image/jpeg"
                    )
                ]
            )
        ]
    )

    output = response.text.split("\n")

    valueListOutput = "{" + output[1] + "}"
    
    with open( "mapconstants.h" , "w" ) as outfile:
        outfile.write( "#ifndef MAPCONSTANTS_H\n#define MAPCONSTANTS_H\n\n" )
        outfile.write( "const int LENGTH = " + str( output[0] ) + ";\n" )
        outfile.write( "const int VALUE_MAP[] = " + valueListOutput + ";\n" )
        outfile.write( "\n#endif\n" )

# response = client.models.generate_content(
#     model = "gemini-2.5-pro", 
#     contents = messageToGemini
# )

# print( response.text )