from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.boundary_summary import BoundarySummary
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    latitude: Union[Unset, None, float] = UNSET,
    longitude: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/boundaries/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["latitude"] = latitude

    params["longitude"] = longitude

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BoundarySummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    latitude: Union[Unset, None, float] = UNSET,
    longitude: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    """Search Boundary

     Search for boundaries by name or coordinates.

    Args:
        name (Union[Unset, None, str]):
        latitude (Union[Unset, None, float]):
        longitude (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['BoundarySummary']]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        latitude=latitude,
        longitude=longitude,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    latitude: Union[Unset, None, float] = UNSET,
    longitude: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    """Search Boundary

     Search for boundaries by name or coordinates.

    Args:
        name (Union[Unset, None, str]):
        latitude (Union[Unset, None, float]):
        longitude (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['BoundarySummary']]]
    """

    return sync_detailed(
        client=client,
        name=name,
        latitude=latitude,
        longitude=longitude,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    latitude: Union[Unset, None, float] = UNSET,
    longitude: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    """Search Boundary

     Search for boundaries by name or coordinates.

    Args:
        name (Union[Unset, None, str]):
        latitude (Union[Unset, None, float]):
        longitude (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['BoundarySummary']]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        latitude=latitude,
        longitude=longitude,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    latitude: Union[Unset, None, float] = UNSET,
    longitude: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, List["BoundarySummary"]]]:
    """Search Boundary

     Search for boundaries by name or coordinates.

    Args:
        name (Union[Unset, None, str]):
        latitude (Union[Unset, None, float]):
        longitude (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['BoundarySummary']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            latitude=latitude,
            longitude=longitude,
        )
    ).parsed