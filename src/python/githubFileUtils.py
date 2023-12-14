import os
from localUtils import encode_image, load_json

MAX_SNAPSHOTS = 2

def fetch_github_file(filepath: str):
     # Predefined directory path
    base_path = "/Users/naveenls/workspace/scio/typescript/"

    storybook_directory = os.path.join(base_path, 'storybook', '.storybook', '__snapshots__')
    entries = os.listdir(storybook_directory)

    # Filter directories, keep only files
    storybook_files = [entry for entry in entries if os.path.isfile(os.path.join(storybook_directory, entry))]

    # Combine the base path with the file path
    files_to_read = []
    images_to_read = []
    if not filepath.endswith(".ts") and not filepath.endswith(".tsx"):
        path_list = filepath.split("/")
        storybook_prefix = "-".join(path_list[-2:])

        files_to_read.append(os.path.join(base_path, filepath, path_list[-1] + ".tsx"))
        for storybook_file in storybook_files:
            if storybook_prefix.lower() in storybook_file:
                images_to_read.append(os.path.join(storybook_directory, storybook_file))
    else:
        files_to_read.append(base_path + filepath)
    
    # Read the files
    file_contents = []
    for file_to_read in files_to_read:
        try:
            file_contents.append(open(file_to_read, 'r').read())
        except:
            print(f"Error: Cannot read file {file_to_read}")

    storybook_images = []
    images_to_read = images_to_read[:MAX_SNAPSHOTS]
    for image_to_read in images_to_read:
        try:
            storybook_images.append(encode_image(image_to_read))
        except:
            print(f"Error: Cannot read snapshot {image_to_read}")
    
    return file_contents, storybook_images

def construct_file_details(filepaths: list[str]):
    system_message_content = []
    for path_to_read in filepaths:
        file_contents, storybook_images =  fetch_github_file(path_to_read)
        if len(file_contents) > 0:
            system_message_content.append({
                'type': 'text',
                'text': f'Content of {path_to_read}:'
            })

            system_message_content.extend({
                'type': 'text',
                'text': file_content
            } for file_content in file_contents)

        if len(storybook_images) > 0:
            system_message_content.append({
                'type': 'text',
                'text': f'Storybook snapshots of {path_to_read}:'
            })

            system_message_content.extend({
                'type': 'image_url',
                'image_url': {
                    'url': f"data:image/jpeg;base64,{base64_image}",
                    'detail': "high"
                }
            } for base64_image in storybook_images)
        
        system_message_content.append({
            'type': 'text',
            'text': '\n\n'
        })
    return system_message_content

def parse_assistant_response(assistant_response):
    assistant_json_response = load_json(assistant_response)
    if assistant_json_response is None:
        return None
    
    if 'get_code_params' in assistant_json_response:
        paths_to_read = assistant_json_response['get_code_params']
        return construct_file_details(paths_to_read), 'continue'
    elif 'finalized_files' in assistant_json_response:
        return assistant_json_response['finalized_files'], 'end'
    return None