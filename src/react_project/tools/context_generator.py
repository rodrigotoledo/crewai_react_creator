from crewai_tools import BaseTool

class ContextGenerator(BaseTool):
    name: str = 'ContextGenerator'
    description: str = (
        "Generates a React context with a provider class."
    )

    def _run(self, *args, **kwargs):
        # Prompt for context name and create the context
        context_name = self.prompt_context_name()
        self.create_context(context_name)

    def prompt_context_name(self):
        # Prompt for the context name
        context_name = input("Enter the name of the context (e.g., MyContext): ")
        return context_name

    def create_context(self, context_name):
        # Template for the React Context with React Query integration
        template = f"""
import React, {{ createContext, useMemo }} from 'react';
import {{ useQuery, useMutation, useQueryClient }} from '@tanstack/react-query';
import axios from 'axios';

export const {context_name}Context = createContext();

export const {context_name}Provider = ({{ children }}) => {{

  const queryClient = useQueryClient();
  const {{ data, isLoading, refetch }} = useQuery(['{context_name}'], fetch{context_name}Data);

  const destroyMutation = useMutation({{
    mutationFn: ({{ id }}) => {{
      if (window.confirm('Are you sure?')) {{
        return axios.delete(id);
      }}
    }},
    onSuccess: () => {{
      queryClient.invalidateQueries({{ queryKey: ['{context_name}'] }});
    }},
  }});

  const destroy{context_name} = (instance) => {{
    destroyMutation.mutate({{ id: instance.id }});
  }};

  const value = useMemo(() => ({{
    data,
    isLoading{context_name}: isLoading,
    refetch{context_name}: refetch,
    destroy{context_name},
  }}), [data, isLoading, refetch, destroyMutation]);

  return (
    <{context_name}Context.Provider value={{ value }}>
      {{ children }}
    </{context_name}Context.Provider>
  );
}};

const fetch{context_name}Data = async () => {{
  // Fetch data logic
  const response = await axios.get('/api/{context_name}');
  return response.data;
}};
        """

        # Write the generated context to a file
        with open(f'src/context/{context_name}Context.js', 'w') as f:
            f.write(template)

        print(f"Context '{context_name}' created successfully.")
