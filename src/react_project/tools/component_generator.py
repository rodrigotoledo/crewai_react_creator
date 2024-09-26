from crewai_tools import BaseTool

class ComponentGenerator(BaseTool):
    name: str = 'Generate Components'
    description: str = (
        "Generate components from commands"
    )

    def _run(self, *args, **kwargs):
        # Implement the logic
        pass

    def create_navbar(self, context_name):
        navbar_template = f"""
import React, {{ useContext }} from 'react';
import {{ {context_name}Context }} from '../context/{context_name}Context';

const Navbar = () => {{
  const {{ state }} = useContext({context_name}Context);

  return (
    <nav className="bg-gray-800 p-4">
      <div className="text-white">Navbar - State: {{ state }}</div>
    </nav>
  );
}};

export default Navbar;
        """

        with open('src/components/Navbar.js', 'w') as f:
            f.write(navbar_template)

        print("Navbar created with context integration.")

    def create_form(self, context_name):
        fields = []
        print("Enter form fields (type 'done' to finish):")

        while True:
            label = input("Label: ")
            if label.lower() == 'done':
                break
            field_name = input("Field Name: ")
            field_type = input("Field Type: ")
            fields.append((label, field_name, field_type))

        field_elements = ""
        for label, field_name, field_type in fields:
            field_elements += f'<label>{{label}}</label>\n'
            field_elements += f'<input type="{{field_type}}" {...{register("{field_name}")}} />\n'

        form_template = f"""
import React from 'react';
import {{ useForm }} from 'react-hook-form';

const {context_name}Form = () => {{
  const {{ register, handleSubmit }} = useForm();

  const onSubmit = (data) => {{
    console.log(data);
  }};

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {{fields}}
      <button type="submit">Submit</button>
    </form>
  );
}};

export default {context_name}Form;
        """

        form_code = form_template.replace("{fields}", field_elements).replace("{context_name}", context_name)

        with open(f'src/components/{context_name}Form.js', 'w') as f:
            f.write(form_code)

        print(f"{context_name}Form created with dynamic fields.")

    def create_projects_component(self, context_name):
        projects_template = f"""
import React, {{ useContext }} from 'react';
import {{ {context_name}Context }} from '../context/{context_name}Context';

const {context_name} = () => {{
  const {{ state }} = useContext({context_name}Context);

  if (!state || !state.{context_name.lower()}s) {{
    return <div>Nothing is available</div>;
  }}

  return (
    <div>
      {{state.{context_name.lower()}s.map((item, index) => (
        <div key={{index}}>
          <h2>{{item.name}}</h2>
          <p>{{item.description}}</p>
        </div>
      ))}}
    </div>
  );
}};

export default {context_name};
        """

        with open(f'src/components/{context_name}.js', 'w') as f:
            f.write(projects_template)

        print(f"{context_name} component created.")
