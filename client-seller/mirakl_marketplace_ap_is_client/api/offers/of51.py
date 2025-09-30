import datetime
from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    include_inactive_offers: Union[Unset, bool] = False,
    include_fields: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_last_request_date: Union[Unset, str] = UNSET
    if not isinstance(last_request_date, Unset):
        json_last_request_date = last_request_date.isoformat()
    params["last_request_date"] = json_last_request_date

    params["channel_codes"] = channel_codes

    params["shipping_zones"] = shipping_zones

    params["include_inactive_offers"] = include_inactive_offers

    params["include_fields"] = include_fields

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/offers/export",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    include_inactive_offers: Union[Unset, bool] = False,
    include_fields: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Get offers CSV file

     Get a CSV file that includes the offers updated and deleted since the last request date.<br/>For
    deleted offers, only offer-id, product-sku, shop-id, shop-sku, active and deleted columns are
    returned. <br/>If the last_request_date param is not set the api returns all the active offers
    (inactive offers can be included with include_inactive_offers parameter).<br/>If offers have custom
    fields, a column is added for each existing custom field with as header the code of the custom
    field.<br/><br/>Results are sorted by offer identifier.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        channel_codes (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        include_inactive_offers (Union[Unset, bool]):  Default: False.
        include_fields (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        last_request_date=last_request_date,
        channel_codes=channel_codes,
        shipping_zones=shipping_zones,
        include_inactive_offers=include_inactive_offers,
        include_fields=include_fields,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    include_inactive_offers: Union[Unset, bool] = False,
    include_fields: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Get offers CSV file

     Get a CSV file that includes the offers updated and deleted since the last request date.<br/>For
    deleted offers, only offer-id, product-sku, shop-id, shop-sku, active and deleted columns are
    returned. <br/>If the last_request_date param is not set the api returns all the active offers
    (inactive offers can be included with include_inactive_offers parameter).<br/>If offers have custom
    fields, a column is added for each existing custom field with as header the code of the custom
    field.<br/><br/>Results are sorted by offer identifier.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        channel_codes (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        include_inactive_offers (Union[Unset, bool]):  Default: False.
        include_fields (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        client=client,
        last_request_date=last_request_date,
        channel_codes=channel_codes,
        shipping_zones=shipping_zones,
        include_inactive_offers=include_inactive_offers,
        include_fields=include_fields,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    include_inactive_offers: Union[Unset, bool] = False,
    include_fields: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Get offers CSV file

     Get a CSV file that includes the offers updated and deleted since the last request date.<br/>For
    deleted offers, only offer-id, product-sku, shop-id, shop-sku, active and deleted columns are
    returned. <br/>If the last_request_date param is not set the api returns all the active offers
    (inactive offers can be included with include_inactive_offers parameter).<br/>If offers have custom
    fields, a column is added for each existing custom field with as header the code of the custom
    field.<br/><br/>Results are sorted by offer identifier.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        channel_codes (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        include_inactive_offers (Union[Unset, bool]):  Default: False.
        include_fields (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        last_request_date=last_request_date,
        channel_codes=channel_codes,
        shipping_zones=shipping_zones,
        include_inactive_offers=include_inactive_offers,
        include_fields=include_fields,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shipping_zones: Union[Unset, str] = UNSET,
    include_inactive_offers: Union[Unset, bool] = False,
    include_fields: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Get offers CSV file

     Get a CSV file that includes the offers updated and deleted since the last request date.<br/>For
    deleted offers, only offer-id, product-sku, shop-id, shop-sku, active and deleted columns are
    returned. <br/>If the last_request_date param is not set the api returns all the active offers
    (inactive offers can be included with include_inactive_offers parameter).<br/>If offers have custom
    fields, a column is added for each existing custom field with as header the code of the custom
    field.<br/><br/>Results are sorted by offer identifier.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        channel_codes (Union[Unset, str]):
        shipping_zones (Union[Unset, str]):
        include_inactive_offers (Union[Unset, bool]):  Default: False.
        include_fields (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            client=client,
            last_request_date=last_request_date,
            channel_codes=channel_codes,
            shipping_zones=shipping_zones,
            include_inactive_offers=include_inactive_offers,
            include_fields=include_fields,
            shop_id=shop_id,
        )
    ).parsed
