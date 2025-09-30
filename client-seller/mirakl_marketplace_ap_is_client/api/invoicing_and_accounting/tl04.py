from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tl04_response_200 import TL04Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tracking_id: str,
    *,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/sellerpayment/transactions_logs/async/status/{tracking_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TL04Response200]:
    if response.status_code == 200:
        response_200 = TL04Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TL04Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[TL04Response200]:
    """Poll the status of an asynchronous transaction log export (TL03)

     Retrieve the status for an TL03 transaction log export.<br/>
    When the export is complete, the URLs to retrieve the files are returned.

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL04Response200]
    """

    kwargs = _get_kwargs(
        tracking_id=tracking_id,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[TL04Response200]:
    """Poll the status of an asynchronous transaction log export (TL03)

     Retrieve the status for an TL03 transaction log export.<br/>
    When the export is complete, the URLs to retrieve the files are returned.

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL04Response200
    """

    return sync_detailed(
        tracking_id=tracking_id,
        client=client,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[TL04Response200]:
    """Poll the status of an asynchronous transaction log export (TL03)

     Retrieve the status for an TL03 transaction log export.<br/>
    When the export is complete, the URLs to retrieve the files are returned.

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL04Response200]
    """

    kwargs = _get_kwargs(
        tracking_id=tracking_id,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[TL04Response200]:
    """Poll the status of an asynchronous transaction log export (TL03)

     Retrieve the status for an TL03 transaction log export.<br/>
    When the export is complete, the URLs to retrieve the files are returned.

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL04Response200
    """

    return (
        await asyncio_detailed(
            tracking_id=tracking_id,
            client=client,
            shop_id=shop_id,
        )
    ).parsed
