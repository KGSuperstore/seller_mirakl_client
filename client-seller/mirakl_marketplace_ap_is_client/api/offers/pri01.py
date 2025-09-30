from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pri01_body import PRI01Body
from ...models.pri01_response_201 import PRI01Response201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PRI01Body,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/offers/pricing/imports",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PRI01Response201]:
    if response.status_code == 201:
        response_201 = PRI01Response201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PRI01Response201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PRI01Body,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[PRI01Response201]:
    """Import a price file

     Import a .csv file to submit all applicable prices for an offer.<br/>
    The import mode is delete and replace: any existing price that is not submitted will be
    deleted.<br/>
    If Price Approval is enabled, this API creates and updates pending prices; ongoing prices will
    remain.<br/>
    Returns an import identifier to track the status of the import and retrieve an error report if
    applicable.<br/>

    Args:
        shop_id (Union[Unset, int]):
        body (PRI01Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PRI01Response201]
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
    body: PRI01Body,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[PRI01Response201]:
    """Import a price file

     Import a .csv file to submit all applicable prices for an offer.<br/>
    The import mode is delete and replace: any existing price that is not submitted will be
    deleted.<br/>
    If Price Approval is enabled, this API creates and updates pending prices; ongoing prices will
    remain.<br/>
    Returns an import identifier to track the status of the import and retrieve an error report if
    applicable.<br/>

    Args:
        shop_id (Union[Unset, int]):
        body (PRI01Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PRI01Response201
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PRI01Body,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[PRI01Response201]:
    """Import a price file

     Import a .csv file to submit all applicable prices for an offer.<br/>
    The import mode is delete and replace: any existing price that is not submitted will be
    deleted.<br/>
    If Price Approval is enabled, this API creates and updates pending prices; ongoing prices will
    remain.<br/>
    Returns an import identifier to track the status of the import and retrieve an error report if
    applicable.<br/>

    Args:
        shop_id (Union[Unset, int]):
        body (PRI01Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PRI01Response201]
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
    body: PRI01Body,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[PRI01Response201]:
    """Import a price file

     Import a .csv file to submit all applicable prices for an offer.<br/>
    The import mode is delete and replace: any existing price that is not submitted will be
    deleted.<br/>
    If Price Approval is enabled, this API creates and updates pending prices; ongoing prices will
    remain.<br/>
    Returns an import identifier to track the status of the import and retrieve an error report if
    applicable.<br/>

    Args:
        shop_id (Union[Unset, int]):
        body (PRI01Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PRI01Response201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
