def create_use_refresh_on_focus():
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

    with open('src/hooks/useRefreshOnFocus.js', 'w') as f:
        f.write(hook_content)

    print("Hook 'useRefreshOnFocus' created.")

if __name__ == "__main__":
    create_use_refresh_on_focus()
