from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.package import Package
from ...types import Response


def _get_kwargs(
    boundary_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/packages/{boundary_name}".format(client.base_url, boundary_name=boundary_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, Package]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Package.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError, Package]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    boundary_name: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError, Package]]:
    """Get Package

     Retrieve information about a specific package (which has been created from a given boundary)

    Args:
        boundary_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Package]]
    """

    kwargs = _get_kwargs(
        boundary_name=boundary_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    boundary_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError, Package]]:
    """Get Package

     Retrieve information about a specific package (which has been created from a given boundary)

    Args:
        boundary_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Package]]
    """

    return sync_detailed(
        boundary_name=boundary_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    boundary_name: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError, Package]]:
    """Get Package

     Retrieve information about a specific package (which has been created from a given boundary)

    Args:
        boundary_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Package]]
    """

    kwargs = _get_kwargs(
        boundary_name=boundary_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    boundary_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError, Package]]:
    """Get Package

     Retrieve information about a specific package (which has been created from a given boundary)

    Args:
        boundary_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Package]]
    """

    return (
        await asyncio_detailed(
            boundary_name=boundary_name,
            client=client,
        )
    ).parsed
