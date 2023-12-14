import sys

from localUtils import read_png
from componentFinder import get_finalized_files
from componentComposer import get_finalized_code
import time
from flask import Flask, request
from llmUtils import LLMClient

app = Flask(__name__)

@app.after_request
def after_request(response):
    # You might want to make this more specific or configurable
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/generate_code', methods=['POST', 'OPTIONS'])
def generate_code():
    if request.method == 'OPTIONS':
        # For OPTIONS requests, simply return a 200 OK with the required headers
        return '', 200
     
     # Extract string data from the POST request
    data = request.json
    figma_mock_file_path = data['imageUrl']  # assuming the input is a simple string
    llm_client = LLMClient()

    '''
    As a first step, we need to get the common components, libraries and theme files that are relevant for the given mock.
    Here we give LLM the list of all the common components and utilities that are available in the organization's code base.
    The LLM will shortlist the relevant common components and utilities.
    '''
    files_to_read = get_finalized_files(figma_mock_file_path, llm_client)
    if files_to_read is None:
        print("Failed to get finalized files", flush=True)
        sys.exit(1)

    '''
    As a second step, we fetch the code of the shortlisted files and send it to the LLM along with user provided figma mock.
    Finally, the LLM will generate the code for the given mock using the given details of the common components.
    '''
    finalized_code = get_finalized_code(figma_mock_file_path, files_to_read, llm_client)
    print("Finalized code: ...", flush=True)
    return finalized_code

if __name__ == '__main__':
    app.run(port=8989)