#!/bin/bash
set -e

# Math utility module entrypoint
# No database migrations required for this utility module

echo "Math Utility Module - AGV-186"
echo "Container started at $(date)"

# Run any initialization tasks here if needed
# For now, just pass through to CMD

exec "$@"