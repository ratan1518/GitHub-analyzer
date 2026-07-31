import os
from importlib.util import module_from_spec, spec_from_file_location

PROJECT_ROOT_CANDIDATES = [
    os.path.join(os.path.dirname(__file__), "github-profile-analyzer-main", "github-profile-analyzer-main"),
    os.path.join(os.path.dirname(__file__), "github-profile-analyzer-main"),
]

INNER_APP_PATH = None
for project_root in PROJECT_ROOT_CANDIDATES:
    candidate = os.path.join(project_root, "app.py")
    if os.path.exists(candidate):
        INNER_APP_PATH = candidate
        break

if not INNER_APP_PATH:
    raise FileNotFoundError("Could not find the project app.py entry point")

spec = spec_from_file_location("project_app", INNER_APP_PATH)
module = module_from_spec(spec)
spec.loader.exec_module(module)

app = module.app
