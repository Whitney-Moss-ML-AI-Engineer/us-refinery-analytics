# EIA API Integration

Official EIA Open Data portal:
https://www.eia.gov/opendata/

EIA API documentation:
https://www.eia.gov/opendata/documentation.php

EIA petroleum data:
https://www.eia.gov/petroleum/

The pipeline should read the API key from the environment rather than committing credentials.

Example endpoint construction:

```python
import os
import requests

API_KEY = os.environ["EIA_API_KEY"]
url = "https://api.eia.gov/v2/petroleum/"
params = {"api_key": API_KEY}

response = requests.get(url, params=params, timeout=60)
response.raise_for_status()
payload = response.json()
```

The exact dataset route and facets should be configured in `config/data_sources.yaml` after validating the current EIA API schema. Store raw responses before transformation.
