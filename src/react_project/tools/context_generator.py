from crewai_tools import BaseTool

class ContextGenerator(BaseTool):
    name: str = 'ContextGenerator'
    description: str = (
        "Generates a React context with a provider class."
    )

    def _run(self, *args, **kwargs):
        context_name = self.prompt_context_name()
        self.create_context(context_name)

    def prompt_context_name(self):
        context_name = input("Enter the name of the context (e.g., MyContext): ")
        return context_name

    def create_context(self, context_name):
        template = f"""
import React, {{ createContext, useState }} from 'react';

export const {context_name}Context = createContext();

export class {context_name}Provider extends React.Component {{
  constructor(props) {{
    super(props);
    this.state = {{
      // Initial state values can go here
    }};
  }}

  setState = (newState) => {{
    this.setState(newState);
  }}

  render() {{
    return (
      <{context_name}Context.Provider value={{{
        state: this.state,
        setState: this.setState,
      }}}
      >
        {{this.props.children}}
      </{context_name}Context.Provider>
    );
  }}
}}
        """

        with open(f'src/context/{context_name}Context.js', 'w') as f:
            f.write(template)

        print(f"Context '{context_name}' created.")