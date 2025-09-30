from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.of21_response_200 import OF21Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offer_state_codes: Union[Unset, str] = UNSET,
    sku: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    favorite: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offer_state_codes"] = offer_state_codes

    params["sku"] = sku

    params["product_id"] = product_id

    params["favorite"] = favorite

    params["pricing_channel_code"] = pricing_channel_code

    params["pricing_customer_organization_id"] = pricing_customer_organization_id

    params["shop_id"] = shop_id

    params["locale"] = locale

    params["max"] = max_

    params["offset"] = offset

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/offers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OF21Response200]:
    if response.status_code == 200:
        response_200 = OF21Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OF21Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offer_state_codes: Union[Unset, str] = UNSET,
    sku: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    favorite: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[OF21Response200]:
    """List offers of a shop

    Args:
        offer_state_codes (Union[Unset, str]):
        sku (Union[Unset, str]):
        product_id (Union[Unset, str]):
        favorite (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF21Response200]
    """

    kwargs = _get_kwargs(
        offer_state_codes=offer_state_codes,
        sku=sku,
        product_id=product_id,
        favorite=favorite,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    offer_state_codes: Union[Unset, str] = UNSET,
    sku: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    favorite: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[OF21Response200]:
    """List offers of a shop

    Args:
        offer_state_codes (Union[Unset, str]):
        sku (Union[Unset, str]):
        product_id (Union[Unset, str]):
        favorite (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF21Response200
    """

    return sync_detailed(
        client=client,
        offer_state_codes=offer_state_codes,
        sku=sku,
        product_id=product_id,
        favorite=favorite,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offer_state_codes: Union[Unset, str] = UNSET,
    sku: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    favorite: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[OF21Response200]:
    """List offers of a shop

    Args:
        offer_state_codes (Union[Unset, str]):
        sku (Union[Unset, str]):
        product_id (Union[Unset, str]):
        favorite (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF21Response200]
    """

    kwargs = _get_kwargs(
        offer_state_codes=offer_state_codes,
        sku=sku,
        product_id=product_id,
        favorite=favorite,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    offer_state_codes: Union[Unset, str] = UNSET,
    sku: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    favorite: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[OF21Response200]:
    """List offers of a shop

    Args:
        offer_state_codes (Union[Unset, str]):
        sku (Union[Unset, str]):
        product_id (Union[Unset, str]):
        favorite (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF21Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            offer_state_codes=offer_state_codes,
            sku=sku,
            product_id=product_id,
            favorite=favorite,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
            locale=locale,
            max_=max_,
            offset=offset,
            sort=sort,
            order=order,
        )
    ).parsed
