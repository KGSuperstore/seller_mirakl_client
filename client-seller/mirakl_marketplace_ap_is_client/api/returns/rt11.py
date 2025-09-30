import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rt11_response_200 import RT11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    return_id: Union[Unset, list[str]] = UNSET,
    return_state: Union[Unset, list[str]] = UNSET,
    return_creation_date_from: Union[Unset, datetime.datetime] = UNSET,
    return_creation_date_to: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    order_commercial_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    return_rma: Union[Unset, list[str]] = UNSET,
    customer_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_return_id: Union[Unset, list[str]] = UNSET
    if not isinstance(return_id, Unset):
        json_return_id = return_id

    params["return_id"] = json_return_id

    json_return_state: Union[Unset, list[str]] = UNSET
    if not isinstance(return_state, Unset):
        json_return_state = return_state

    params["return_state"] = json_return_state

    json_return_creation_date_from: Union[Unset, str] = UNSET
    if not isinstance(return_creation_date_from, Unset):
        json_return_creation_date_from = return_creation_date_from.isoformat()
    params["return_creation_date_from"] = json_return_creation_date_from

    json_return_creation_date_to: Union[Unset, str] = UNSET
    if not isinstance(return_creation_date_to, Unset):
        json_return_creation_date_to = return_creation_date_to.isoformat()
    params["return_creation_date_to"] = json_return_creation_date_to

    json_return_last_updated_from: Union[Unset, str] = UNSET
    if not isinstance(return_last_updated_from, Unset):
        json_return_last_updated_from = return_last_updated_from.isoformat()
    params["return_last_updated_from"] = json_return_last_updated_from

    json_return_last_updated_to: Union[Unset, str] = UNSET
    if not isinstance(return_last_updated_to, Unset):
        json_return_last_updated_to = return_last_updated_to.isoformat()
    params["return_last_updated_to"] = json_return_last_updated_to

    json_order_commercial_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_commercial_id, Unset):
        json_order_commercial_id = order_commercial_id

    params["order_commercial_id"] = json_order_commercial_id

    json_order_line_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_line_id, Unset):
        json_order_line_id = order_line_id

    params["order_line_id"] = json_order_line_id

    json_return_rma: Union[Unset, list[str]] = UNSET
    if not isinstance(return_rma, Unset):
        json_return_rma = return_rma

    params["return_rma"] = json_return_rma

    json_customer_id: Union[Unset, list[str]] = UNSET
    if not isinstance(customer_id, Unset):
        json_customer_id = customer_id

    params["customer_id"] = json_customer_id

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/returns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RT11Response200]:
    if response.status_code == 200:
        response_200 = RT11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RT11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    return_id: Union[Unset, list[str]] = UNSET,
    return_state: Union[Unset, list[str]] = UNSET,
    return_creation_date_from: Union[Unset, datetime.datetime] = UNSET,
    return_creation_date_to: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    order_commercial_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    return_rma: Union[Unset, list[str]] = UNSET,
    customer_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[RT11Response200]:
    """List returns

    Args:
        return_id (Union[Unset, list[str]]):
        return_state (Union[Unset, list[str]]):
        return_creation_date_from (Union[Unset, datetime.datetime]):
        return_creation_date_to (Union[Unset, datetime.datetime]):
        return_last_updated_from (Union[Unset, datetime.datetime]):
        return_last_updated_to (Union[Unset, datetime.datetime]):
        order_commercial_id (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        return_rma (Union[Unset, list[str]]):
        customer_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RT11Response200]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        return_state=return_state,
        return_creation_date_from=return_creation_date_from,
        return_creation_date_to=return_creation_date_to,
        return_last_updated_from=return_last_updated_from,
        return_last_updated_to=return_last_updated_to,
        order_commercial_id=order_commercial_id,
        order_line_id=order_line_id,
        return_rma=return_rma,
        customer_id=customer_id,
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
    return_id: Union[Unset, list[str]] = UNSET,
    return_state: Union[Unset, list[str]] = UNSET,
    return_creation_date_from: Union[Unset, datetime.datetime] = UNSET,
    return_creation_date_to: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    order_commercial_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    return_rma: Union[Unset, list[str]] = UNSET,
    customer_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[RT11Response200]:
    """List returns

    Args:
        return_id (Union[Unset, list[str]]):
        return_state (Union[Unset, list[str]]):
        return_creation_date_from (Union[Unset, datetime.datetime]):
        return_creation_date_to (Union[Unset, datetime.datetime]):
        return_last_updated_from (Union[Unset, datetime.datetime]):
        return_last_updated_to (Union[Unset, datetime.datetime]):
        order_commercial_id (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        return_rma (Union[Unset, list[str]]):
        customer_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RT11Response200
    """

    return sync_detailed(
        client=client,
        return_id=return_id,
        return_state=return_state,
        return_creation_date_from=return_creation_date_from,
        return_creation_date_to=return_creation_date_to,
        return_last_updated_from=return_last_updated_from,
        return_last_updated_to=return_last_updated_to,
        order_commercial_id=order_commercial_id,
        order_line_id=order_line_id,
        return_rma=return_rma,
        customer_id=customer_id,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    return_id: Union[Unset, list[str]] = UNSET,
    return_state: Union[Unset, list[str]] = UNSET,
    return_creation_date_from: Union[Unset, datetime.datetime] = UNSET,
    return_creation_date_to: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    order_commercial_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    return_rma: Union[Unset, list[str]] = UNSET,
    customer_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[RT11Response200]:
    """List returns

    Args:
        return_id (Union[Unset, list[str]]):
        return_state (Union[Unset, list[str]]):
        return_creation_date_from (Union[Unset, datetime.datetime]):
        return_creation_date_to (Union[Unset, datetime.datetime]):
        return_last_updated_from (Union[Unset, datetime.datetime]):
        return_last_updated_to (Union[Unset, datetime.datetime]):
        order_commercial_id (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        return_rma (Union[Unset, list[str]]):
        customer_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RT11Response200]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        return_state=return_state,
        return_creation_date_from=return_creation_date_from,
        return_creation_date_to=return_creation_date_to,
        return_last_updated_from=return_last_updated_from,
        return_last_updated_to=return_last_updated_to,
        order_commercial_id=order_commercial_id,
        order_line_id=order_line_id,
        return_rma=return_rma,
        customer_id=customer_id,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    return_id: Union[Unset, list[str]] = UNSET,
    return_state: Union[Unset, list[str]] = UNSET,
    return_creation_date_from: Union[Unset, datetime.datetime] = UNSET,
    return_creation_date_to: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    return_last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    order_commercial_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    return_rma: Union[Unset, list[str]] = UNSET,
    customer_id: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[RT11Response200]:
    """List returns

    Args:
        return_id (Union[Unset, list[str]]):
        return_state (Union[Unset, list[str]]):
        return_creation_date_from (Union[Unset, datetime.datetime]):
        return_creation_date_to (Union[Unset, datetime.datetime]):
        return_last_updated_from (Union[Unset, datetime.datetime]):
        return_last_updated_to (Union[Unset, datetime.datetime]):
        order_commercial_id (Union[Unset, list[str]]):
        order_line_id (Union[Unset, list[str]]):
        return_rma (Union[Unset, list[str]]):
        customer_id (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RT11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            return_id=return_id,
            return_state=return_state,
            return_creation_date_from=return_creation_date_from,
            return_creation_date_to=return_creation_date_to,
            return_last_updated_from=return_last_updated_from,
            return_last_updated_to=return_last_updated_to,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            return_rma=return_rma,
            customer_id=customer_id,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
