import os
import subprocess
from crewai_tools import BaseTool

class ProjectGenerator(BaseTool):
    name: str = 'Generate Project'
    description: str = (
        "Generate a React project with Tailwind and necessary packages."
    )

    def _run(self, *args, **kwargs):
        # Implement logic if necessary
        pass

    def prompt_project_name(self, project_name):
        # Solicita o nome do projeto e valida a entrada
        while True:
            project_name = input("Enter the name of the React project: ").strip()
            
            # Valida que o nome é alfanumérico, hífen ou underscore
            if project_name and not os.path.exists(project_name) and project_name.isidentifier():
                return project_name
            print(f"The project '{project_name}' already exists or is invalid. Please try again.")

    def create_react_project(self, project_name):
        self.prompt_project_name(project_name)
        try:
            # Cria o projeto React
            self.run_command(["npx", "create-react-app", project_name])

            # Instala Tailwind e outros pacotes necessários
            os.chdir(project_name)
            self.run_command([
                "npm", "install", "tailwindcss", "react-hook-form",
                "react-router-dom", "axios", "humanize-string"
            ])

            # Configura Tailwind
            self.run_command(["npx", "tailwindcss", "init"])

            # Cria o arquivo .tool-versions
            self.create_tool_versions_file()

            # Estrutura de diretórios
            self.create_directories()

            print(f"Project '{project_name}' created with Tailwind and necessary packages.")

        except subprocess.CalledProcessError as e:
            print(f"An error occurred while creating the project: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def run_command(self, command):
        """Helper para rodar comandos subprocess com verificação de erro"""
        subprocess.run(command, check=True)

    def create_tool_versions_file(self):
        """Cria o arquivo .tool-versions com a versão correta de Node.js"""
        with open('.tool-versions', 'w') as f:
            f.write("nodejs 22.7.0\n")

    def create_directories(self):
        """Cria a estrutura básica de diretórios"""
        os.makedirs("src/components", exist_ok=True)
        os.makedirs("src/hooks", exist_ok=True)
        os.makedirs("src/context", exist_ok=True)
