#!/bin/bash

# use case of this file,  executed after pulling the latest code from version control. It ensures that the database schema is synchronized with the application code before the application starts serving requests.

# Apply database migrations
echo "Applying database migrations"

# Run database migrations
python manage.py migrate --no-input

# Capture the exit code of the migration command
returnCode=$?

# Check if migration was successful
if [ $returnCode -ne 0 ]; then
    echo "Error: Database migration failed"
    exit 1
fi

echo "Database migration completed successfully"
exit 0
