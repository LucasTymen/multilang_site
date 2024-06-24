import os

def create_init_py_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # Skip __pycache__ directories
        if '__pycache__' not in root:
            # Create __init__.py in each directory
            init_path = os.path.join(root, '__init__.py')
            if not os.path.exists(init_path):
                with open(init_path, 'w') as f:
                    f.write('# This file ensures the directory is treated as a package.\n')
                print(f'Created: {init_path}')

# Define the root directory for the project
project_root_dir = '/home/lucas/code/LucasTymen/projects/codeAcademy/django/multilang_site'  # Change this to your project root

# Run the function to create __init__.py files
create_init_py_files(project_root_dir)

# Let the user know the script has completed
print(f"__init__.py files created in all necessary directories under {project_root_dir}")
