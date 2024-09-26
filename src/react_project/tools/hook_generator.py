import os
from crewai_tools import BaseTool

class HookGenerator(BaseTool):
    name: str = 'HookGenerator'
    description: str = (
        "Generates a custom React hook called useRefreshOnFocus."
    )

    def _run(self, *args, **kwargs):
        # Implement the logic 
        pass

    def create_use_refresh_on_focus(self):
        hook_content = """
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

export const useRefreshOnFocus = (refreshFunc) => {
  const location = useLocation();

  useEffect(() => {
    const handleFocus = () => {
      if (refreshFunc) {
        refreshFunc();
      }
    };

    window.addEventListener('focus', handleFocus);
    return () => {
      window.removeEventListener('focus', handleFocus);
    };
  }, [location, refreshFunc]);
};
        """

        # Garante que o diretório exista antes de tentar criar o arquivo
        os.makedirs('src/hooks', exist_ok=True)

        # Cria o arquivo do hook no diretório correto
        with open('src/hooks/useRefreshOnFocus.js', 'w') as f:
            f.write(hook_content)

        print("Hook 'useRefreshOnFocus' created.")
