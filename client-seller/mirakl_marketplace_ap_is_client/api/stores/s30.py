from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s30_response_200 import S30Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/shops/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[S30Response200]:
    if response.status_code == 200:
        response_200 = S30Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[S30Response200]:
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
) -> Response[S30Response200]:
    """List shop's documents

     You must specify at least one of the following parameters: <code>shop_ids</code>,
    <code>updated_since</code>

    Args:
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S30Response200]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[S30Response200]:
    """List shop's documents

     You must specify at least one of the following parameters: <code>shop_ids</code>,
    <code>updated_since</code>

    Args:
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S30Response200
    """

    return sync_detailed(
        client=client,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[S30Response200]:
    """List shop's documents

     You must specify at least one of the following parameters: <code>shop_ids</code>,
    <code>updated_since</code>

    Args:
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S30Response200]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[S30Response200]:
    """List shop's documents

     You must specify at least one of the following parameters: <code>shop_ids</code>,
    <code>updated_since</code>

    Args:
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S30Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            shop_id=shop_id,
        )
    ).parsed
