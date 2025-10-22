#!/bin/bash
# Start script for Streamlit frontend on Render
streamlit run frontend.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false
