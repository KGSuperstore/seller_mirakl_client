from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.p11_response_200 import P11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product_ids: Union[Unset, str] = UNSET,
    product_references: Union[Unset, str] = UNSET,
    offer_state_codes: Union[Unset, str] = UNSET,
    all_offers: Union[Unset, bool] = False,
    channel_codes: Union[Unset, str] = UNSET,
    all_channels: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    all_shipping_zones: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["product_ids"] = product_ids

    params["product_references"] = product_references

    params["offer_state_codes"] = offer_state_codes

    params["all_offers"] = all_offers

    params["channel_codes"] = channel_codes

    params["all_channels"] = all_channels

    params["pricing_channel_code"] = pricing_channel_code

    params["pricing_customer_organization_id"] = pricing_customer_organization_id

    params["shipping_zones"] = shipping_zones

    params["all_shipping_zones"] = all_shipping_zones

    params["shop_id"] = shop_id

    params["locale"] = locale

    params["max"] = max_

    params["offset"] = offset

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/products/offers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[P11Response200]:
    if response.status_code == 200:
        response_200 = P11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[P11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    product_ids: Union[Unset, str] = UNSET,
    product_references: Union[Unset, str] = UNSET,
    offer_state_codes: Union[Unset, str] = UNSET,
    all_offers: Union[Unset, bool] = False,
    channel_codes: Union[Unset, str] = UNSET,
    all_channels: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    all_shipping_zones: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[P11Response200]:
    """List offers for each given product

    Args:
        product_ids (Union[Unset, str]):
        product_references (Union[Unset, str]):
        offer_state_codes (Union[Unset, str]):
        all_offers (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, str]):
        all_channels (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        all_shipping_zones (Union[Unset, bool]):  Default: False.
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
        Response[P11Response200]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
        product_references=product_references,
        offer_state_codes=offer_state_codes,
        all_offers=all_offers,
        channel_codes=channel_codes,
        all_channels=all_channels,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shipping_zones=shipping_zones,
        all_shipping_zones=all_shipping_zones,
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
    product_ids: Union[Unset, str] = UNSET,
    product_references: Union[Unset, str] = UNSET,
    offer_state_codes: Union[Unset, str] = UNSET,
    all_offers: Union[Unset, bool] = False,
    channel_codes: Union[Unset, str] = UNSET,
    all_channels: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    all_shipping_zones: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[P11Response200]:
    """List offers for each given product

    Args:
        product_ids (Union[Unset, str]):
        product_references (Union[Unset, str]):
        offer_state_codes (Union[Unset, str]):
        all_offers (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, str]):
        all_channels (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        all_shipping_zones (Union[Unset, bool]):  Default: False.
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
        P11Response200
    """

    return sync_detailed(
        client=client,
        product_ids=product_ids,
        product_references=product_references,
        offer_state_codes=offer_state_codes,
        all_offers=all_offers,
        channel_codes=channel_codes,
        all_channels=all_channels,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shipping_zones=shipping_zones,
        all_shipping_zones=all_shipping_zones,
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
    product_ids: Union[Unset, str] = UNSET,
    product_references: Union[Unset, str] = UNSET,
    offer_state_codes: Union[Unset, str] = UNSET,
    all_offers: Union[Unset, bool] = False,
    channel_codes: Union[Unset, str] = UNSET,
    all_channels: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    all_shipping_zones: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[P11Response200]:
    """List offers for each given product

    Args:
        product_ids (Union[Unset, str]):
        product_references (Union[Unset, str]):
        offer_state_codes (Union[Unset, str]):
        all_offers (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, str]):
        all_channels (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        all_shipping_zones (Union[Unset, bool]):  Default: False.
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
        Response[P11Response200]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
        product_references=product_references,
        offer_state_codes=offer_state_codes,
        all_offers=all_offers,
        channel_codes=channel_codes,
        all_channels=all_channels,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shipping_zones=shipping_zones,
        all_shipping_zones=all_shipping_zones,
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
    product_ids: Union[Unset, str] = UNSET,
    product_references: Union[Unset, str] = UNSET,
    offer_state_codes: Union[Unset, str] = UNSET,
    all_offers: Union[Unset, bool] = False,
    channel_codes: Union[Unset, str] = UNSET,
    all_channels: Union[Unset, bool] = False,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    all_shipping_zones: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[P11Response200]:
    """List offers for each given product

    Args:
        product_ids (Union[Unset, str]):
        product_references (Union[Unset, str]):
        offer_state_codes (Union[Unset, str]):
        all_offers (Union[Unset, bool]):  Default: False.
        channel_codes (Union[Unset, str]):
        all_channels (Union[Unset, bool]):  Default: False.
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        all_shipping_zones (Union[Unset, bool]):  Default: False.
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
        P11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            product_ids=product_ids,
            product_references=product_references,
            offer_state_codes=offer_state_codes,
            all_offers=all_offers,
            channel_codes=channel_codes,
            all_channels=all_channels,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shipping_zones=shipping_zones,
            all_shipping_zones=all_shipping_zones,
            shop_id=shop_id,
            locale=locale,
            max_=max_,
            offset=offset,
            sort=sort,
            order=order,
        )
    ).parsed
