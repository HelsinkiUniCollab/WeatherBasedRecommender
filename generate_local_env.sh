#!/bin/bash

# script to generate .env.local file

# Before running this script, give it execute permissions with:
# $ chmod +x generate_local_env.sh

# Then run the script with:
# $ ./generate_local_env.sh

cat > ./recommender-front/.env.local << EOF
# This file contains environment-specific configuration values that
# override the defaults in .env, but are ignored by Git.

REACT_APP_BACKEND_URL=http://localhost:5000
EOF