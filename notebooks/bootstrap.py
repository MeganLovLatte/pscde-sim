import yaml
import pprint
from pathlib import Path

schema_path = Path(__file__).parent.parent / "schema.yaml"

with open(schema_path, "r") as f:
    schema = yaml.safe_load(f)

print("✅ Loaded schema:")
pprint.pprint(schema)
