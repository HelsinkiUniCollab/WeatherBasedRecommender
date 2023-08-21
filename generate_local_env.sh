#!/bin/bash

# script to generate .env.local file

# Before running this script, give it execute permissions with:
# $ chmod +x generate_local_env.sh

# Then run the script with:
# $ ./generate_local_env.sh

# Get the absolute path of the directory where the script is located.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cat > ./recommender-front/.env.local << EOF
# This file contains environment-specific configuration values that
# override the defaults in .env, but are ignored by Git.

REACT_APP_BACKEND_URL=http://localhost:5000

EOF

cat > ./recommender-back/.env << EOF
# This file contains environment-specific configuration values for the Python backend.

REACT_APP_BACKEND_URL=http://localhost:5000
DEVELOPMENT_DB_URI="$1"
CACHE_MODE="simple"
FLASK_DEBUG="True"

# Include the 'recommender-back' directory in the PYTHONPATH.
PYTHONPATH="${PYTHONPATH}:${SCRIPT_DIR}/recommender-back"
EOF