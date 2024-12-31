#!/bin/bash

# ==========================
# Intellihome Setup Script
# ==========================
# Author: Priyanshu Yadav-Ubuntu-24lTS
# Purpose: Automates environment setup, dependency installation, and Flask API server management.

# ==========================
# Variables
# ==========================
PROJECT_DIR="/path/to/Desktop"  
FLASK_APP="test.py"  
LOG_FILE="$PROJECT_DIR/test.log"

# ==========================
# Functions
# ==========================
# Update system packages
update_system() {
    echo "Updating system packages..."
    sudo apt-get update && sudo apt-get upgrade -y
    echo "System updated successfully."
}

install_dependencies() {
    echo "Installing Python3 and pip..."
    sudo apt-get install -y python3 python3-pip
    echo "Installing Python packages..."
    pip3 install flask RPi.GPIO numpy pandas sklearn tensorflow joblib
    echo "Dependencies installed successfully."
}

# Setup Flask environment
setup_flask_env() {
    echo "Setting up Flask environment..."
    if [ ! -d "$PROJECT_DIR" ]; then
        echo "Error: Project directory $PROJECT_DIR does not exist."
        exit 1
    fi
    cd "$PROJECT_DIR"
    echo "Flask environment ready."
}

# Start Flask server
start_server() {
    echo "Starting Flask server..."
    cd "$PROJECT_DIR"
    nohup python3 "$FLASK_APP" > "$LOG_FILE" 2>&1 &
    SERVER_PID=$!
    echo $SERVER_PID > "$PROJECT_DIR/server.pid"
    echo "Flask server started with PID $SERVER_PID."
    echo "Logs are being written to $LOG_FILE."
}

# Stop Flask server
stop_server() {
    if [ -f "$PROJECT_DIR/server.pid" ]; then
        SERVER_PID=$(cat "$PROJECT_DIR/server.pid")
        echo "Stopping Flask server with PID $SERVER_PID..."
        kill $SERVER_PID
        rm "$PROJECT_DIR/server.pid"
        echo "Flask server stopped."
    else
        echo "No server is running."
    fi
}

# Display usage instructions
display_usage() {
    echo "Usage: $0 {install|start|stop|restart|status}"
    echo "  install   - Set up the system and install dependencies."
    echo "  start     - Start the Flask server."
    echo "  stop      - Stop the Flask server."
    echo "  restart   - Restart the Flask server."
    echo "  status    - Check the Flask server status."
}

# Check server status
check_status() {
    if [ -f "$PROJECT_DIR/server.pid" ]; then
        SERVER_PID=$(cat "$PROJECT_DIR/server.pid")
        if ps -p $SERVER_PID > /dev/null; then
            echo "Flask server is running with PID $SERVER_PID."
        else
            echo "Server PID file exists, but the server is not running."
        fi
    else
        echo "Flask server is not running."
    fi
}

# ==========================
# Main Script Logic
# ==========================
case "$1" in
    install)
        update_system
        install_dependencies
        ;;
    start)
        setup_flask_env
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        stop_server
        setup_flask_env
        start_server
        ;;
    status)
        check_status
        ;;
    *)
        display_usage
        ;;
esac

# ==========================
# End of Script
# ==========================
