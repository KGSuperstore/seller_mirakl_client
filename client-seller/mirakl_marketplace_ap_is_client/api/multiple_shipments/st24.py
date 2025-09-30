from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.st24_request import ST24Request
from ...models.st24_response_200 import ST24Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ST24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/shipments/ship",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ST24Response200]:
    if response.status_code == 200:
        response_200 = ST24Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ST24Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ST24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[ST24Response200]:
    """Validate shipments as shipped

     Limited to 1000 shipments at a time

    Args:
        shop_id (Union[Unset, int]):
        body (ST24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ST24Response200]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ST24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[ST24Response200]:
    """Validate shipments as shipped

     Limited to 1000 shipments at a time

    Args:
        shop_id (Union[Unset, int]):
        body (ST24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ST24Response200
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ST24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[ST24Response200]:
    """Validate shipments as shipped

     Limited to 1000 shipments at a time

    Args:
        shop_id (Union[Unset, int]):
        body (ST24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ST24Response200]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ST24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[ST24Response200]:
    """Validate shipments as shipped

     Limited to 1000 shipments at a time

    Args:
        shop_id (Union[Unset, int]):
        body (ST24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ST24Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
