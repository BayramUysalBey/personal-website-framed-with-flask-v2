#!/bin/sh
set -e

# --- Wait Loop (Necessary to wait for Neon connection stabilization) ---
# We use the DATABASE_URL directly now.
python -c "
import socket
import time
import os
from urllib.parse import urlparse
url = os.environ.get('DATABASE_URL')
if url:
    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port if parsed.port else 5432
    
    # Loop until the external host is reachable
    while True: 
        try: 
            s = socket.create_connection((host, port), timeout=5)
            s.close()
            break
        except socket.error: 
            print(f'Waiting for external database at {host}:{port}...')
            time.sleep(1)
"

# --- Start the Real Server ---
# Starts the Gunicorn server to handle web traffic.
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app