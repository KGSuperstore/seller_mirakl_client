from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sh31_response_200 import SH31Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/shipping/logistic_classes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SH31Response200]:
    if response.status_code == 200:
        response_200 = SH31Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SH31Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[SH31Response200]:
    """List all logistic classes

     Results are sorted by index, set in the back-office

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SH31Response200]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[SH31Response200]:
    """List all logistic classes

     Results are sorted by index, set in the back-office

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SH31Response200
    """

    return sync_detailed(
        client=client,
        shop_id=shop_id,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Response[SH31Response200]:
    """List all logistic classes

     Results are sorted by index, set in the back-office

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SH31Response200]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
    locale: Union[Unset, str] = UNSET,
) -> Optional[SH31Response200]:
    """List all logistic classes

     Results are sorted by index, set in the back-office

    Args:
        shop_id (Union[Unset, int]):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SH31Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            shop_id=shop_id,
            locale=locale,
        )
    ).parsed
