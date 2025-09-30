import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.p51_response_200 import P51Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    has_transformed_file: Union[Unset, bool] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_last_request_date: Union[Unset, str] = UNSET
    if not isinstance(last_request_date, Unset):
        json_last_request_date = last_request_date.isoformat()
    params["last_request_date"] = json_last_request_date

    params["status"] = status

    params["has_transformed_file"] = has_transformed_file

    params["shop_id"] = shop_id

    params["max"] = max_

    params["offset"] = offset

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/products/imports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[P51Response200]:
    if response.status_code == 200:
        response_200 = P51Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[P51Response200]:
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
    status: Union[Unset, str] = UNSET,
    has_transformed_file: Union[Unset, bool] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[P51Response200]:
    """Get information about product import statuses

     If the last_request_date param is not set the api returns all product imports.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        has_transformed_file (Union[Unset, bool]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[P51Response200]
    """

    kwargs = _get_kwargs(
        last_request_date=last_request_date,
        status=status,
        has_transformed_file=has_transformed_file,
        shop_id=shop_id,
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
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    has_transformed_file: Union[Unset, bool] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[P51Response200]:
    """Get information about product import statuses

     If the last_request_date param is not set the api returns all product imports.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        has_transformed_file (Union[Unset, bool]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        P51Response200
    """

    return sync_detailed(
        client=client,
        last_request_date=last_request_date,
        status=status,
        has_transformed_file=has_transformed_file,
        shop_id=shop_id,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    has_transformed_file: Union[Unset, bool] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[P51Response200]:
    """Get information about product import statuses

     If the last_request_date param is not set the api returns all product imports.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        has_transformed_file (Union[Unset, bool]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[P51Response200]
    """

    kwargs = _get_kwargs(
        last_request_date=last_request_date,
        status=status,
        has_transformed_file=has_transformed_file,
        shop_id=shop_id,
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
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    has_transformed_file: Union[Unset, bool] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[P51Response200]:
    """Get information about product import statuses

     If the last_request_date param is not set the api returns all product imports.

    Args:
        last_request_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        has_transformed_file (Union[Unset, bool]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        P51Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            last_request_date=last_request_date,
            status=status,
            has_transformed_file=has_transformed_file,
            shop_id=shop_id,
            max_=max_,
            offset=offset,
            sort=sort,
            order=order,
        )
    ).parsed
