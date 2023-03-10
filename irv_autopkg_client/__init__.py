""" A client library for accessing FastAPI """
from .client import AuthenticatedClient, Client

__version__ = "0.2.1"

__all__ = (
    "AuthenticatedClient",
    "Client",
)
