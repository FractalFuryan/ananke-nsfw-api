"""Generate OpenAPI spec for public auditing."""
import json
from app.main import app

if __name__ == "__main__":
    spec = app.openapi()
    print(json.dumps(spec, indent=2))
