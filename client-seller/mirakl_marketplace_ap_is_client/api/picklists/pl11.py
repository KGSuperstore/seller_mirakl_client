import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pl11_response_200 import PL11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pickrun_code: Union[Unset, str] = UNSET,
    pickup_date_min: Union[Unset, datetime.datetime] = UNSET,
    pickup_date_max: Union[Unset, datetime.datetime] = UNSET,
    picklist_id: Union[Unset, list[str]] = UNSET,
    picklist_state: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pickrun_code"] = pickrun_code

    json_pickup_date_min: Union[Unset, str] = UNSET
    if not isinstance(pickup_date_min, Unset):
        json_pickup_date_min = pickup_date_min.isoformat()
    params["pickup_date_min"] = json_pickup_date_min

    json_pickup_date_max: Union[Unset, str] = UNSET
    if not isinstance(pickup_date_max, Unset):
        json_pickup_date_max = pickup_date_max.isoformat()
    params["pickup_date_max"] = json_pickup_date_max

    json_picklist_id: Union[Unset, list[str]] = UNSET
    if not isinstance(picklist_id, Unset):
        json_picklist_id = picklist_id

    params["picklist_id"] = json_picklist_id

    json_picklist_state: Union[Unset, list[str]] = UNSET
    if not isinstance(picklist_state, Unset):
        json_picklist_state = picklist_state

    params["picklist_state"] = json_picklist_state

    json_order_line_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_line_id, Unset):
        json_order_line_id = order_line_id

    params["order_line_id"] = json_order_line_id

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/picklists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PL11Response200]:
    if response.status_code == 200:
        response_200 = PL11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PL11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pickrun_code: Union[Unset, str] = UNSET,
    pickup_date_min: Union[Unset, datetime.datetime] = UNSET,
    pickup_date_max: Union[Unset, datetime.datetime] = UNSET,
    picklist_id: Union[Unset, list[str]] = UNSET,
    picklist_state: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[PL11Response200]:
    """List picklists

    Args:
        pickrun_code (Union[Unset, str]):
        pickup_date_min (Union[Unset, datetime.datetime]):
        pickup_date_max (Union[Unset, datetime.datetime]):
        picklist_id (Union[Unset, list[str]]):
        picklist_state (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PL11Response200]
    """

    kwargs = _get_kwargs(
        pickrun_code=pickrun_code,
        pickup_date_min=pickup_date_min,
        pickup_date_max=pickup_date_max,
        picklist_id=picklist_id,
        picklist_state=picklist_state,
        order_line_id=order_line_id,
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
    pickrun_code: Union[Unset, str] = UNSET,
    pickup_date_min: Union[Unset, datetime.datetime] = UNSET,
    pickup_date_max: Union[Unset, datetime.datetime] = UNSET,
    picklist_id: Union[Unset, list[str]] = UNSET,
    picklist_state: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[PL11Response200]:
    """List picklists

    Args:
        pickrun_code (Union[Unset, str]):
        pickup_date_min (Union[Unset, datetime.datetime]):
        pickup_date_max (Union[Unset, datetime.datetime]):
        picklist_id (Union[Unset, list[str]]):
        picklist_state (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PL11Response200
    """

    return sync_detailed(
        client=client,
        pickrun_code=pickrun_code,
        pickup_date_min=pickup_date_min,
        pickup_date_max=pickup_date_max,
        picklist_id=picklist_id,
        picklist_state=picklist_state,
        order_line_id=order_line_id,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pickrun_code: Union[Unset, str] = UNSET,
    pickup_date_min: Union[Unset, datetime.datetime] = UNSET,
    pickup_date_max: Union[Unset, datetime.datetime] = UNSET,
    picklist_id: Union[Unset, list[str]] = UNSET,
    picklist_state: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[PL11Response200]:
    """List picklists

    Args:
        pickrun_code (Union[Unset, str]):
        pickup_date_min (Union[Unset, datetime.datetime]):
        pickup_date_max (Union[Unset, datetime.datetime]):
        picklist_id (Union[Unset, list[str]]):
        picklist_state (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PL11Response200]
    """

    kwargs = _get_kwargs(
        pickrun_code=pickrun_code,
        pickup_date_min=pickup_date_min,
        pickup_date_max=pickup_date_max,
        picklist_id=picklist_id,
        picklist_state=picklist_state,
        order_line_id=order_line_id,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pickrun_code: Union[Unset, str] = UNSET,
    pickup_date_min: Union[Unset, datetime.datetime] = UNSET,
    pickup_date_max: Union[Unset, datetime.datetime] = UNSET,
    picklist_id: Union[Unset, list[str]] = UNSET,
    picklist_state: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[PL11Response200]:
    """List picklists

    Args:
        pickrun_code (Union[Unset, str]):
        pickup_date_min (Union[Unset, datetime.datetime]):
        pickup_date_max (Union[Unset, datetime.datetime]):
        picklist_id (Union[Unset, list[str]]):
        picklist_state (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PL11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            pickrun_code=pickrun_code,
            pickup_date_min=pickup_date_min,
            pickup_date_max=pickup_date_max,
            picklist_id=picklist_id,
            picklist_state=picklist_state,
            order_line_id=order_line_id,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
