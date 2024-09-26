from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from react_project.tools.project_generator import ProjectGenerator
from react_project.tools.context_generator import ContextGenerator
from react_project.tools.component_generator import ComponentGenerator
from react_project.tools.hook_generator import HookGenerator

project_generator = ProjectGenerator()
context_generator = ContextGenerator()
component_generator = ComponentGenerator()
hook_generator = HookGenerator()
# form_creation = FormCreation()
# project_listing = ProjectListing()

@CrewBase
class ReactProjectCrew:
    """Crew for setting up a React project"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def project_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['project_creator'],
            verbose=True,
        )

    @agent
    def context_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['context_builder'],
            verbose=True,
        )

    @agent
    def component_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['component_builder'],
            verbose=True,
        )

    @agent
    def field_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['field_creator'],
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the React Project Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    @task
    def project_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_generator_task'],
            execute=project_generator.create_react_project,
            verbose=True
        )

    @task
    def context_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['context_creation_task'],
            tools=[context_generator],
        )

    @task
    def component_setup_task(self) -> Task:
        return Task(
            config=self.tasks_config['component_setup_task'],
            tools=[component_generator],
        )

    @task
    def form_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['form_creation_task'],
            tools=[form_creation],
        )

    @task
    def project_listing_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_listing_task'],
            tools=[project_listing],
        )