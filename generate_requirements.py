import os
import subprocess

def generate_requirements():
    project_dir = os.path.abspath(os.path.dirname(__file__))  


    print("Generating initial requirements.txt using pipreqs...")
    subprocess.run(['pipreqs', project_dir])

    compile_requirements()

def compile_requirements():
    if os.path.exists('requirements.txt'):
        print("Compiling requirements.txt using pip-tools...")
        subprocess.run(['pip-compile', 'requirements.txt'])

if __name__ == '__main__':
    generate_requirements()
