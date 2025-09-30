import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pri02_response_200 import PRI02Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    import_id: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    origins: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_import_id: Union[Unset, list[str]] = UNSET
    if not isinstance(import_id, Unset):
        json_import_id = import_id

    params["import_id"] = json_import_id

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["status"] = status

    json_origins: Union[Unset, list[str]] = UNSET
    if not isinstance(origins, Unset):
        json_origins = origins

    params["origins"] = json_origins

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/offers/pricing/imports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PRI02Response200]:
    if response.status_code == 200:
        response_200 = PRI02Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PRI02Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    import_id: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    origins: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[PRI02Response200]:
    """Get information and statistics about an offer pricing import

    Args:
        import_id (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        origins (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PRI02Response200]
    """

    kwargs = _get_kwargs(
        import_id=import_id,
        start_date=start_date,
        end_date=end_date,
        status=status,
        origins=origins,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    import_id: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    origins: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[PRI02Response200]:
    """Get information and statistics about an offer pricing import

    Args:
        import_id (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        origins (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PRI02Response200
    """

    return sync_detailed(
        client=client,
        import_id=import_id,
        start_date=start_date,
        end_date=end_date,
        status=status,
        origins=origins,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    import_id: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    origins: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[PRI02Response200]:
    """Get information and statistics about an offer pricing import

    Args:
        import_id (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        origins (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PRI02Response200]
    """

    kwargs = _get_kwargs(
        import_id=import_id,
        start_date=start_date,
        end_date=end_date,
        status=status,
        origins=origins,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    import_id: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    status: Union[Unset, str] = UNSET,
    origins: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[PRI02Response200]:
    """Get information and statistics about an offer pricing import

    Args:
        import_id (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        origins (Union[Unset, list[str]]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PRI02Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            import_id=import_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
            origins=origins,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
