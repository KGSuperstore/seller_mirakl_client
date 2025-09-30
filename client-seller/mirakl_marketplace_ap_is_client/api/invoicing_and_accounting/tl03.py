from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tl03_request import TL03Request
from ...models.tl03_response_200 import TL03Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TL03Request,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/sellerpayment/transactions_logs/async",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TL03Response200]:
    if response.status_code == 200:
        response_200 = TL03Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TL03Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TL03Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[TL03Response200]:
    """Export transaction lines JSON file asynchronously

     The export is asynchronous. Export status can be retrieved by calling TL04.

    Args:
        shop_id (Union[Unset, int]):
        body (TL03Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL03Response200]
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
    body: TL03Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[TL03Response200]:
    """Export transaction lines JSON file asynchronously

     The export is asynchronous. Export status can be retrieved by calling TL04.

    Args:
        shop_id (Union[Unset, int]):
        body (TL03Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL03Response200
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TL03Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[TL03Response200]:
    """Export transaction lines JSON file asynchronously

     The export is asynchronous. Export status can be retrieved by calling TL04.

    Args:
        shop_id (Union[Unset, int]):
        body (TL03Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL03Response200]
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
    body: TL03Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[TL03Response200]:
    """Export transaction lines JSON file asynchronously

     The export is asynchronous. Export status can be retrieved by calling TL04.

    Args:
        shop_id (Union[Unset, int]):
        body (TL03Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL03Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
