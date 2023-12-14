import os

base_path = "/Users/naveenls/workspace/scio/typescript/"

def list_files(directory):
    """List all files in the given directory."""
    try:
        joined_path = os.path.join(base_path, directory)
        files =  [os.path.join(directory, f) for f in os.listdir(joined_path) if os.path.isfile(os.path.join(joined_path, f))]
        return ' '.join(files)
    except FileNotFoundError:
        return f"Directory not found: {directory}"

def list_folders(directory):
    """List all folders in the given directory."""
    try:
        joined_path = os.path.join(base_path, directory)
        folders = [os.path.join(directory, f) for f in os.listdir(joined_path) if os.path.isdir(os.path.join(joined_path, f))]
        return ' '.join(folders)
    except FileNotFoundError:
        return f"Directory not found: {directory}"
    
file_directories = [
    'core/hooks', 
    'core/lib', 
    'core/redux/selectors', 
    'core/theme'
]

folder_directories = [
    'web/common',
    'web/elements'
]

COMMON_COMPONENTS = f'''
Here are the common design system components that are used in the organization:
{list_folders('web/elements')}
{list_folders('web/common')}
Here are the common libraries that are used in the organization:
{list_files('core/lib')}
{list_files('core/redux/selectors')}
Here are the common theme files that are used in the organization:
{list_files('core/theme')}
Here are the common hooks that are used in the organization:
{list_files('core/hooks')}
'''