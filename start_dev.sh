#!/bin/bash

# Paths
WORKSPACE_DIR="/home/thuan/workspace/grapple"
GRAPPLE_WEB_DIR="$WORKSPACE_DIR/grapple-website/apps/grapple-web"
GRAPPLE_PLUS_APP_DIR="$WORKSPACE_DIR/grapple-plus-app"
GRAPPLE_PLUS_API_DIR="$WORKSPACE_DIR/grapple-plus-api"

# Function to check if a process is running
is_process_running() {
    local pid=$1
    if ps -p "$pid" > /dev/null 2>&1; then
        return 0 # True
    else
        return 1 # False
    fi
}

# Start grapple-web
echo "Starting grapple-web..."
cd "$GRAPPLE_WEB_DIR" || { echo "Directory $GRAPPLE_WEB_DIR not found"; exit 1; }
pnpm run dev &
WEB_PID=$!
echo "grapple-web started with PID $WEB_PID"

# Start grapple-plus-api debugger in VS Code
echo "Starting grapple-plus-api debugger..."
cd "$GRAPPLE_PLUS_API_DIR" || { echo "Directory $GRAPPLE_PLUS_API_DIR not found"; exit 1; }
code --folder-uri "$GRAPPLE_PLUS_API_DIR" --launch-name "Launch Program" &
API_VSCODE_PID=$!

# Wait for grapple-plus-api to start (simplified check)
echo "Waiting for grapple-plus-api to be ready..."
sleep 5 # Adjust delay based on startup time; replace with a better check if needed

# Start grapple-plus-app after grapple-plus-api
echo "Starting grapple-plus-app..."
cd "$GRAPPLE_PLUS_APP_DIR" || { echo "Directory $GRAPPLE_PLUS_APP_DIR not found"; exit 1; }
pnpm run dev &
APP_PID=$!
echo "grapple-plus-app started with PID $APP_PID"

echo "Development environment started!"
echo "PIDs: grapple-web ($WEB_PID), grapple-plus-api (VS Code: $API_VSCODE_PID), grapple-plus-app ($APP_PID)"
