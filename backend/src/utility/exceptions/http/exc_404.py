"""
The HTTP 404 Not Found response status code indicates that the server cannot find the requested resource.
"""

import fastapi

from src.utility.messages.exceptions.http.exc_details import (
    http_404_email_details,
    http_404_id_details,
    http_404_name_details,
    http_404_username_details,
)


async def http_exc_404_email_not_found_request(email: str) -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail=http_404_email_details(email=email),
    )


async def http_exc_404_id_not_found_request(id: int) -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail=http_404_id_details(id=id),
    )


async def http_exc_404_username_not_found_request(username: str) -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail=http_404_username_details(username=username),
    )


async def http_exc_404_name_not_found_request(name: str) -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND, detail=http_404_name_details(name=name)
    )
