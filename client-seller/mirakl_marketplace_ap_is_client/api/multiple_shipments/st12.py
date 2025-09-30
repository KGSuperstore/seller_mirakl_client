import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.st12_response_200 import ST12Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_id: Union[Unset, list[str]] = UNSET,
    fulfillment_center_code: Union[Unset, list[str]] = UNSET,
    shipping_date_from: Union[Unset, datetime.datetime] = UNSET,
    shipping_date_to: Union[Unset, datetime.datetime] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_order_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = order_id

    params["order_id"] = json_order_id

    json_fulfillment_center_code: Union[Unset, list[str]] = UNSET
    if not isinstance(fulfillment_center_code, Unset):
        json_fulfillment_center_code = fulfillment_center_code

    params["fulfillment_center_code"] = json_fulfillment_center_code

    json_shipping_date_from: Union[Unset, str] = UNSET
    if not isinstance(shipping_date_from, Unset):
        json_shipping_date_from = shipping_date_from.isoformat()
    params["shipping_date_from"] = json_shipping_date_from

    json_shipping_date_to: Union[Unset, str] = UNSET
    if not isinstance(shipping_date_to, Unset):
        json_shipping_date_to = shipping_date_to.isoformat()
    params["shipping_date_to"] = json_shipping_date_to

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/shipments/items_to_ship",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ST12Response200]:
    if response.status_code == 200:
        response_200 = ST12Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ST12Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_id: Union[Unset, list[str]] = UNSET,
    fulfillment_center_code: Union[Unset, list[str]] = UNSET,
    shipping_date_from: Union[Unset, datetime.datetime] = UNSET,
    shipping_date_to: Union[Unset, datetime.datetime] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[ST12Response200]:
    """List items to ship

    Args:
        order_id (Union[Unset, list[str]]):
        fulfillment_center_code (Union[Unset, list[str]]):
        shipping_date_from (Union[Unset, datetime.datetime]):
        shipping_date_to (Union[Unset, datetime.datetime]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ST12Response200]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        fulfillment_center_code=fulfillment_center_code,
        shipping_date_from=shipping_date_from,
        shipping_date_to=shipping_date_to,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    order_id: Union[Unset, list[str]] = UNSET,
    fulfillment_center_code: Union[Unset, list[str]] = UNSET,
    shipping_date_from: Union[Unset, datetime.datetime] = UNSET,
    shipping_date_to: Union[Unset, datetime.datetime] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[ST12Response200]:
    """List items to ship

    Args:
        order_id (Union[Unset, list[str]]):
        fulfillment_center_code (Union[Unset, list[str]]):
        shipping_date_from (Union[Unset, datetime.datetime]):
        shipping_date_to (Union[Unset, datetime.datetime]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ST12Response200
    """

    return sync_detailed(
        client=client,
        order_id=order_id,
        fulfillment_center_code=fulfillment_center_code,
        shipping_date_from=shipping_date_from,
        shipping_date_to=shipping_date_to,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_id: Union[Unset, list[str]] = UNSET,
    fulfillment_center_code: Union[Unset, list[str]] = UNSET,
    shipping_date_from: Union[Unset, datetime.datetime] = UNSET,
    shipping_date_to: Union[Unset, datetime.datetime] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[ST12Response200]:
    """List items to ship

    Args:
        order_id (Union[Unset, list[str]]):
        fulfillment_center_code (Union[Unset, list[str]]):
        shipping_date_from (Union[Unset, datetime.datetime]):
        shipping_date_to (Union[Unset, datetime.datetime]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ST12Response200]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        fulfillment_center_code=fulfillment_center_code,
        shipping_date_from=shipping_date_from,
        shipping_date_to=shipping_date_to,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_id: Union[Unset, list[str]] = UNSET,
    fulfillment_center_code: Union[Unset, list[str]] = UNSET,
    shipping_date_from: Union[Unset, datetime.datetime] = UNSET,
    shipping_date_to: Union[Unset, datetime.datetime] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[ST12Response200]:
    """List items to ship

    Args:
        order_id (Union[Unset, list[str]]):
        fulfillment_center_code (Union[Unset, list[str]]):
        shipping_date_from (Union[Unset, datetime.datetime]):
        shipping_date_to (Union[Unset, datetime.datetime]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ST12Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            order_id=order_id,
            fulfillment_center_code=fulfillment_center_code,
            shipping_date_from=shipping_date_from,
            shipping_date_to=shipping_date_to,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
