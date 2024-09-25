from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from react_project.tools.project_setup import ProjectSetup
from react_project.tools.context_creation import ContextCreation
from react_project.tools.component_setup import ComponentSetup
from react_project.tools.form_creation import FormCreation
from react_project.tools.project_listing import ProjectListing

project_setup = ProjectSetup()
context_creation = ContextCreation()
component_setup = ComponentSetup()
form_creation = FormCreation()
project_listing = ProjectListing()

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
    def project_setup_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_setup_task'],
            tools=[project_setup],
        )

    @task
    def context_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['context_creation_task'],
            tools=[context_creation],
        )

    @task
    def component_setup_task(self) -> Task:
        return Task(
            config=self.tasks_config['component_setup_task'],
            tools=[component_setup],
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