from google import genai
from google.genai import types

# init constants
# TAPE_WIDTH = 2.0 # inches
# MINIMUM_LENGTH = 220.0
# MAXIMUM_LENGTH = 237.0
FILE_NAME = "messagebank/message.txt"

SAMPLE_IMAGE_1_DIRECT = "images/SAMPLE_223_1.png"
SAMPLE_IMAGE_2_DIRECT = "images/SAMPLE_223_2.png"
ATTEMPT_AT_CALCULATING_DIRECT = "images/unnamed (3).jpg"

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

# function for the thingy to use
def runImageProcessor( imageFromApp ):
    
    with open ( FILE_NAME , "r" ) as file:
        fileContents = file.read()

    with open( SAMPLE_IMAGE_1_DIRECT , "rb" ) as f:
        imageBytes1 = f.read()

    with open( SAMPLE_IMAGE_2_DIRECT , "rb" ) as f:
        imageBytes2 = f.read()

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
        outfile.write( "const int LENGTH = " + str( int( float( output[0] ) ) ) + ";\n" )
        outfile.write( "const int VALUE_MAP[] = " + valueListOutput + ";\n" )
        outfile.write( "\n#endif\n" )