"""
Main entry point for the Core API application.
This module imports and exposes the FastAPI app from the app package.
"""
from .app.main import app

__all__ = ["app"]
