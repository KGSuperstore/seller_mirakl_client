import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.m11_response_200 import M11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    entity_type: Union[Unset, str] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    with_messages: Union[Unset, bool] = False,
    channel_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["entity_type"] = entity_type

    json_entity_id: Union[Unset, list[str]] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = entity_id

    params["entity_id"] = json_entity_id

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["with_messages"] = with_messages

    json_channel_codes: Union[Unset, list[str]] = UNSET
    if not isinstance(channel_codes, Unset):
        json_channel_codes = channel_codes

    params["channel_codes"] = json_channel_codes

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/inbox/threads",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[M11Response200]:
    if response.status_code == 200:
        response_200 = M11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[M11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: Union[Unset, str] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    with_messages: Union[Unset, bool] = False,
    channel_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[M11Response200]:
    """List all threads

     You may want to retrieve the threads linked to a specific entity, using both
    <code>entity_type</code> and <code>entity_id</code>.
    <br>For example, to retrieve threads for an order, use <code>entity_type=MMP_ORDER&entity_id=my-
    order-1</code>.
    <br>
    Available values for <code>entity_type</code> are:
    <ul>
    <li><code>MMP_ORDER</code>: for threads on product orders</li>
    <li><code>MMP_OFFER</code>: for threads on offers</li>
    <li><code>MPS_ORDER</code>: for threads on service orders</li>
    <li><code>MPS_SERVICE</code>: for threads on services</li>
    <li><code>SELLER_OPERATOR</code>: for threads between sellers and operator</li>
    </ul>

    This resource uses seek pagination. The default value for parameter <code>limit</code> is 50.

    Args:
        entity_type (Union[Unset, str]):
        entity_id (Union[Unset, list[str]]):
        updated_since (Union[Unset, datetime.datetime]):
        with_messages (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[M11Response200]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
        updated_since=updated_since,
        with_messages=with_messages,
        channel_codes=channel_codes,
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
    entity_type: Union[Unset, str] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    with_messages: Union[Unset, bool] = False,
    channel_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[M11Response200]:
    """List all threads

     You may want to retrieve the threads linked to a specific entity, using both
    <code>entity_type</code> and <code>entity_id</code>.
    <br>For example, to retrieve threads for an order, use <code>entity_type=MMP_ORDER&entity_id=my-
    order-1</code>.
    <br>
    Available values for <code>entity_type</code> are:
    <ul>
    <li><code>MMP_ORDER</code>: for threads on product orders</li>
    <li><code>MMP_OFFER</code>: for threads on offers</li>
    <li><code>MPS_ORDER</code>: for threads on service orders</li>
    <li><code>MPS_SERVICE</code>: for threads on services</li>
    <li><code>SELLER_OPERATOR</code>: for threads between sellers and operator</li>
    </ul>

    This resource uses seek pagination. The default value for parameter <code>limit</code> is 50.

    Args:
        entity_type (Union[Unset, str]):
        entity_id (Union[Unset, list[str]]):
        updated_since (Union[Unset, datetime.datetime]):
        with_messages (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        M11Response200
    """

    return sync_detailed(
        client=client,
        entity_type=entity_type,
        entity_id=entity_id,
        updated_since=updated_since,
        with_messages=with_messages,
        channel_codes=channel_codes,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: Union[Unset, str] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    with_messages: Union[Unset, bool] = False,
    channel_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[M11Response200]:
    """List all threads

     You may want to retrieve the threads linked to a specific entity, using both
    <code>entity_type</code> and <code>entity_id</code>.
    <br>For example, to retrieve threads for an order, use <code>entity_type=MMP_ORDER&entity_id=my-
    order-1</code>.
    <br>
    Available values for <code>entity_type</code> are:
    <ul>
    <li><code>MMP_ORDER</code>: for threads on product orders</li>
    <li><code>MMP_OFFER</code>: for threads on offers</li>
    <li><code>MPS_ORDER</code>: for threads on service orders</li>
    <li><code>MPS_SERVICE</code>: for threads on services</li>
    <li><code>SELLER_OPERATOR</code>: for threads between sellers and operator</li>
    </ul>

    This resource uses seek pagination. The default value for parameter <code>limit</code> is 50.

    Args:
        entity_type (Union[Unset, str]):
        entity_id (Union[Unset, list[str]]):
        updated_since (Union[Unset, datetime.datetime]):
        with_messages (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[M11Response200]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
        updated_since=updated_since,
        with_messages=with_messages,
        channel_codes=channel_codes,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    entity_type: Union[Unset, str] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    with_messages: Union[Unset, bool] = False,
    channel_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[M11Response200]:
    """List all threads

     You may want to retrieve the threads linked to a specific entity, using both
    <code>entity_type</code> and <code>entity_id</code>.
    <br>For example, to retrieve threads for an order, use <code>entity_type=MMP_ORDER&entity_id=my-
    order-1</code>.
    <br>
    Available values for <code>entity_type</code> are:
    <ul>
    <li><code>MMP_ORDER</code>: for threads on product orders</li>
    <li><code>MMP_OFFER</code>: for threads on offers</li>
    <li><code>MPS_ORDER</code>: for threads on service orders</li>
    <li><code>MPS_SERVICE</code>: for threads on services</li>
    <li><code>SELLER_OPERATOR</code>: for threads between sellers and operator</li>
    </ul>

    This resource uses seek pagination. The default value for parameter <code>limit</code> is 50.

    Args:
        entity_type (Union[Unset, str]):
        entity_id (Union[Unset, list[str]]):
        updated_since (Union[Unset, datetime.datetime]):
        with_messages (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        M11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            entity_type=entity_type,
            entity_id=entity_id,
            updated_since=updated_since,
            with_messages=with_messages,
            channel_codes=channel_codes,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
