from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.job import Job
from ...models.submitted_job import SubmittedJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: Job,
    status_code: Union[Unset, None, Any] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/jobs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["status_code"] = status_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SubmittedJob]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubmittedJob.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, SubmittedJob]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Job,
    status_code: Union[Unset, None, Any] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubmittedJob]]:
    """Submit Processing Job

     Submit a job for a given package to run a list of dataset-processors

    Args:
        status_code (Union[Unset, None, Any]):
        json_body (Job):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SubmittedJob]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        status_code=status_code,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: Job,
    status_code: Union[Unset, None, Any] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubmittedJob]]:
    """Submit Processing Job

     Submit a job for a given package to run a list of dataset-processors

    Args:
        status_code (Union[Unset, None, Any]):
        json_body (Job):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SubmittedJob]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        status_code=status_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Job,
    status_code: Union[Unset, None, Any] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SubmittedJob]]:
    """Submit Processing Job

     Submit a job for a given package to run a list of dataset-processors

    Args:
        status_code (Union[Unset, None, Any]):
        json_body (Job):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SubmittedJob]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        status_code=status_code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Job,
    status_code: Union[Unset, None, Any] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SubmittedJob]]:
    """Submit Processing Job

     Submit a job for a given package to run a list of dataset-processors

    Args:
        status_code (Union[Unset, None, Any]):
        json_body (Job):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SubmittedJob]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            status_code=status_code,
        )
    ).parsed
