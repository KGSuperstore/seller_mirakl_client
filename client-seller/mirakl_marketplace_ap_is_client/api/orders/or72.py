from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.or72_response_200 import OR72Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_ids: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_ids"] = order_ids

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/orders/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OR72Response200]:
    if response.status_code == 200:
        response_200 = OR72Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OR72Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR72Response200]:
    """Lists order's documents

     Returns a list of all the documents available on the order

    Args:
        order_ids (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR72Response200]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR72Response200]:
    """Lists order's documents

     Returns a list of all the documents available on the order

    Args:
        order_ids (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR72Response200
    """

    return sync_detailed(
        client=client,
        order_ids=order_ids,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR72Response200]:
    """Lists order's documents

     Returns a list of all the documents available on the order

    Args:
        order_ids (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR72Response200]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR72Response200]:
    """Lists order's documents

     Returns a list of all the documents available on the order

    Args:
        order_ids (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR72Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            order_ids=order_ids,
            shop_id=shop_id,
        )
    ).parsed
