from mcp.server.fastmcp import FastMCP
from typing import Any
import os


from utils import create_ocrolus_book, upload_files, get_book_status_ocrolus, get_income_calculations,\
    search_book, get_income_summary, get_income_calculations_for_borrowers, get_book_documents


# Create an MCP server
mcp = FastMCP("Ocrolus")

if not (
        os.environ.get("CLIENT_ID") or not
        os.environ.get("CLIENT_SECRET") or not
        os.environ.get("DIR_PATH")
):
    raise ValueError("CLIENT_ID and CLIENT_SECRET and DIR_PATH must be set in environment variables")


@mcp.tool()
def create_book(book_name) -> str:
    """ Create a book in the Ocrolus API """
    return create_ocrolus_book(book_name)


@mcp.tool()
def get_available_files() -> list[str]:
    """ Returns the list of files available to upload """
    path = os.environ.get("DIR_PATH")
    return [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]


@mcp.tool()
def upload_file_to_book(book_uuid: str, file_paths: list[str]) -> Any:
    """ Upload multiple files to the Ocrolus book """
    return upload_files(book_uuid, file_paths)


@mcp.tool()
def get_book_status(book_uuid: str) -> Any:
    """ Get status of all documents uploaded in the book
    Should also be used when asked details about the book """
    return get_book_status_ocrolus(book_uuid)


@mcp.tool()
def get_income_calculations_for_book(book_uuid: str) -> Any:
    """
    Get income calculations for the Ocrolus book
    """
    return get_income_calculations(book_uuid)


@mcp.tool()
def search_book_in_ocrolus(book_name: str) -> Any:
    """
    Search amongst all books in Ocrolus
    """
    return search_book(book_name)

@mcp.tool()
def get_income_summary_for_book(book_uuid: str) -> Any:
    """
    Get Income Summary for a book in Ocrolus.
    When asked for overview for the income of borrowers of a book, we should use this
    """
    return get_income_summary(book_uuid)


@mcp.tool()
def get_income_calculations_for_borrowers_book(book_uuid: str) -> Any:
    """
    Get Income calculations for a book in Ocrolus
    When asked for details / analytics / analysis for income of borrowers of a book, we should use this
    """
    return get_income_calculations_for_borrowers(book_uuid)


@mcp.tool()
def get_details_for_documents_uploaded_in_book(book_uuid: str) -> Any:
    """
    Get details of all documents uploaded in a book
    """
    return get_book_documents(book_uuid)



@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"