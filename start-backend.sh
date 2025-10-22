#!/bin/bash
# Start script for FastAPI backend on Render
uvicorn app:app --host 0.0.0.0 --port $PORT
