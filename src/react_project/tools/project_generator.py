import os
import subprocess

def prompt_project_name():
    project_name = input("Enter the name of the React project: ")
    return project_name

def create_react_project(project_name):
    # Cria o projeto React
    subprocess.run(["npx", "create-react-app", project_name])

    # Instala Tailwind e outros pacotes necessários
    os.chdir(project_name)
    subprocess.run(["npm", "install", "tailwindcss", "react-hook-form", "react-router-dom", "axios", "humanize-string"])

    # Configura Tailwind
    subprocess.run(["npx", "tailwindcss", "init"])

    # Cria o arquivo .tool-versions
    with open('.tool-versions', 'w') as f:
        f.write("nodejs 22.7.0\n")

    # Estrutura de diretórios
    os.makedirs("src/components", exist_ok=True)
    os.makedirs("src/hooks", exist_ok=True)
    os.makedirs("src/context", exist_ok=True)

    print(f"Project '{project_name}' created with Tailwind and necessary packages.")

if __name__ == "__main__":
    project_name = prompt_project_name()
    create_react_project(project_name)
