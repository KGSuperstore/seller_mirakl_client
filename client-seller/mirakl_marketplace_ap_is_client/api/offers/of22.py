from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.of22_response_200 import OF22Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    offer: int,
    *,
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pricing_channel_code"] = pricing_channel_code

    params["pricing_customer_organization_id"] = pricing_customer_organization_id

    params["shop_id"] = shop_id

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/offers/{offer}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OF22Response200]:
    if response.status_code == 200:
        response_200 = OF22Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OF22Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    offer: int,
    *,
    client: Union[AuthenticatedClient, Client],
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[OF22Response200]:
    """Get information about an offer

    Args:
        offer (int):
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF22Response200]
    """

    kwargs = _get_kwargs(
        offer=offer,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    offer: int,
    *,
    client: Union[AuthenticatedClient, Client],
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[OF22Response200]:
    """Get information about an offer

    Args:
        offer (int):
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF22Response200
    """

    return sync_detailed(
        offer=offer,
        client=client,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    offer: int,
    *,
    client: Union[AuthenticatedClient, Client],
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[OF22Response200]:
    """Get information about an offer

    Args:
        offer (int):
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF22Response200]
    """

    kwargs = _get_kwargs(
        offer=offer,
        pricing_channel_code=pricing_channel_code,
        pricing_customer_organization_id=pricing_customer_organization_id,
        shop_id=shop_id,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    offer: int,
    *,
    client: Union[AuthenticatedClient, Client],
    pricing_channel_code: Union[Unset, str] = UNSET,
    pricing_customer_organization_id: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[OF22Response200]:
    """Get information about an offer

    Args:
        offer (int):
        pricing_channel_code (Union[Unset, str]):
        pricing_customer_organization_id (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF22Response200
    """

    return (
        await asyncio_detailed(
            offer=offer,
            client=client,
            pricing_channel_code=pricing_channel_code,
            pricing_customer_organization_id=pricing_customer_organization_id,
            shop_id=shop_id,
            locale=locale,
        )
    ).parsed
