import sys
import os.path

# wrapper to execute shopify.py from 'scripts' in the source directory
# taken from: https://github.com/Shopify/shopify_python_api

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

with open(os.path.join(project_root, 'scripts', 'shopify_api_client.py')) as f:
    code = compile(f.read(), f.name, 'exec')
    exec(code)