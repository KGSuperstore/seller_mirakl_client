from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.or14_response_200 import OR14Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tracking_id: str,
    *,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/orders/async-export/status/{tracking_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OR14Response200]:
    if response.status_code == 200:
        response_200 = OR14Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OR14Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR14Response200]:
    """Get the status of an asynchronous order export.

     <p>Use this API to query the order export status after an API OR13 call.<br />Until the export via
    API OR13 is complete, the status returned by API OR14 is <code>PENDING</code>.<br />You must call
    API OR14 until you get the <code>COMPLETED</code> status which correspond to a completed and
    successful export from API OR13.<br />The URLs in API OR14 response contain all the files from API
    OR13 export.<br />Browse those urls and query them using the GET method.<br />In case of error, the
    status is <code>FAILED</code>.<br />In case of export canceled, the status is
    <code>CANCELED</code>.<br /></p>

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR14Response200]
    """

    kwargs = _get_kwargs(
        tracking_id=tracking_id,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR14Response200]:
    """Get the status of an asynchronous order export.

     <p>Use this API to query the order export status after an API OR13 call.<br />Until the export via
    API OR13 is complete, the status returned by API OR14 is <code>PENDING</code>.<br />You must call
    API OR14 until you get the <code>COMPLETED</code> status which correspond to a completed and
    successful export from API OR13.<br />The URLs in API OR14 response contain all the files from API
    OR13 export.<br />Browse those urls and query them using the GET method.<br />In case of error, the
    status is <code>FAILED</code>.<br />In case of export canceled, the status is
    <code>CANCELED</code>.<br /></p>

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR14Response200
    """

    return sync_detailed(
        tracking_id=tracking_id,
        client=client,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR14Response200]:
    """Get the status of an asynchronous order export.

     <p>Use this API to query the order export status after an API OR13 call.<br />Until the export via
    API OR13 is complete, the status returned by API OR14 is <code>PENDING</code>.<br />You must call
    API OR14 until you get the <code>COMPLETED</code> status which correspond to a completed and
    successful export from API OR13.<br />The URLs in API OR14 response contain all the files from API
    OR13 export.<br />Browse those urls and query them using the GET method.<br />In case of error, the
    status is <code>FAILED</code>.<br />In case of export canceled, the status is
    <code>CANCELED</code>.<br /></p>

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR14Response200]
    """

    kwargs = _get_kwargs(
        tracking_id=tracking_id,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tracking_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR14Response200]:
    """Get the status of an asynchronous order export.

     <p>Use this API to query the order export status after an API OR13 call.<br />Until the export via
    API OR13 is complete, the status returned by API OR14 is <code>PENDING</code>.<br />You must call
    API OR14 until you get the <code>COMPLETED</code> status which correspond to a completed and
    successful export from API OR13.<br />The URLs in API OR14 response contain all the files from API
    OR13 export.<br />Browse those urls and query them using the GET method.<br />In case of error, the
    status is <code>FAILED</code>.<br />In case of export canceled, the status is
    <code>CANCELED</code>.<br /></p>

    Args:
        tracking_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR14Response200
    """

    return (
        await asyncio_detailed(
            tracking_id=tracking_id,
            client=client,
            shop_id=shop_id,
        )
    ).parsed
