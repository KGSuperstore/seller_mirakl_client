from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.or13_request import OR13Request
from ...models.or13_response_200 import OR13Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OR13Request,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/orders/async-export",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OR13Response200]:
    if response.status_code == 200:
        response_200 = OR13Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OR13Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR13Request,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[OR13Response200]:
    """Export orders asynchronously

     <p>The API returns a tracking id to be used to query API OR14.<br />Mirakl recommends to use API
    OR13 instead of API OR11 as it can handle very large volumes of data.<br />You must give at least
    one date range filter: created or last updated date.<br />API OR13 supports the chunk of the export
    file into multiple files in order to:</p><ul><li>respect a maximum megabyte weight using the
    <code>megabytes_per_chunk</code> parameter.</li><li>respect a maximum amount of exported items using
    the <code>items_per_chunk</code> parameter.</li></ul><br />Only one export request can be created
    for the same shop account.

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        body (OR13Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR13Response200]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR13Request,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[OR13Response200]:
    """Export orders asynchronously

     <p>The API returns a tracking id to be used to query API OR14.<br />Mirakl recommends to use API
    OR13 instead of API OR11 as it can handle very large volumes of data.<br />You must give at least
    one date range filter: created or last updated date.<br />API OR13 supports the chunk of the export
    file into multiple files in order to:</p><ul><li>respect a maximum megabyte weight using the
    <code>megabytes_per_chunk</code> parameter.</li><li>respect a maximum amount of exported items using
    the <code>items_per_chunk</code> parameter.</li></ul><br />Only one export request can be created
    for the same shop account.

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        body (OR13Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR13Response200
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR13Request,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[OR13Response200]:
    """Export orders asynchronously

     <p>The API returns a tracking id to be used to query API OR14.<br />Mirakl recommends to use API
    OR13 instead of API OR11 as it can handle very large volumes of data.<br />You must give at least
    one date range filter: created or last updated date.<br />API OR13 supports the chunk of the export
    file into multiple files in order to:</p><ul><li>respect a maximum megabyte weight using the
    <code>megabytes_per_chunk</code> parameter.</li><li>respect a maximum amount of exported items using
    the <code>items_per_chunk</code> parameter.</li></ul><br />Only one export request can be created
    for the same shop account.

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        body (OR13Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR13Response200]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR13Request,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[OR13Response200]:
    """Export orders asynchronously

     <p>The API returns a tracking id to be used to query API OR14.<br />Mirakl recommends to use API
    OR13 instead of API OR11 as it can handle very large volumes of data.<br />You must give at least
    one date range filter: created or last updated date.<br />API OR13 supports the chunk of the export
    file into multiple files in order to:</p><ul><li>respect a maximum megabyte weight using the
    <code>megabytes_per_chunk</code> parameter.</li><li>respect a maximum amount of exported items using
    the <code>items_per_chunk</code> parameter.</li></ul><br />Only one export request can be created
    for the same shop account.

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        body (OR13Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR13Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
            locale=locale,
        )
    ).parsed
