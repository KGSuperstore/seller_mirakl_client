from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.of24_request import OF24Request
from ...models.of24_response_201 import OF24Response201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OF24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/offers",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OF24Response201]:
    if response.status_code == 201:
        response_201 = OF24Response201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OF24Response201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OF24Response201]:
    """Create, update, or delete offers

     <p>Returns the import identifier to track the status of the update.</p><p>You must send all offer
    fields. Offer fields that are not sent are reset to their default value.</p>

    Args:
        shop_id (Union[Unset, int]):
        body (OF24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF24Response201]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OF24Response201]:
    """Create, update, or delete offers

     <p>Returns the import identifier to track the status of the update.</p><p>You must send all offer
    fields. Offer fields that are not sent are reset to their default value.</p>

    Args:
        shop_id (Union[Unset, int]):
        body (OF24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF24Response201
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OF24Response201]:
    """Create, update, or delete offers

     <p>Returns the import identifier to track the status of the update.</p><p>You must send all offer
    fields. Offer fields that are not sent are reset to their default value.</p>

    Args:
        shop_id (Union[Unset, int]):
        body (OF24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF24Response201]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF24Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OF24Response201]:
    """Create, update, or delete offers

     <p>Returns the import identifier to track the status of the update.</p><p>You must send all offer
    fields. Offer fields that are not sent are reset to their default value.</p>

    Args:
        shop_id (Union[Unset, int]):
        body (OF24Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF24Response201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
