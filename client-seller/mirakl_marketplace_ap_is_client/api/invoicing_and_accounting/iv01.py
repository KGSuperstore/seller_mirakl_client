import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.iv01_response_200 import IV01Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    currency: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    issuing_user_types: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    payment_status: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, str] = "AUTO_INVOICE",
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currency"] = currency

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_issuing_user_types: Union[Unset, list[str]] = UNSET
    if not isinstance(issuing_user_types, Unset):
        json_issuing_user_types = issuing_user_types

    params["issuing_user_types"] = json_issuing_user_types

    json_pay_out_psp_codes: Union[Unset, list[str]] = UNSET
    if not isinstance(pay_out_psp_codes, Unset):
        json_pay_out_psp_codes = pay_out_psp_codes

    params["pay_out_psp_codes"] = json_pay_out_psp_codes

    params["payment_status"] = payment_status

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    params["type"] = type_

    params["shop_id"] = shop_id

    params["max"] = max_

    params["offset"] = offset

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/invoices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IV01Response200]:
    if response.status_code == 200:
        response_200 = IV01Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IV01Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    issuing_user_types: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    payment_status: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, str] = "AUTO_INVOICE",
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[IV01Response200]:
    """List accounting documents

    Args:
        currency (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        issuing_user_types (Union[Unset, list[str]]):
        pay_out_psp_codes (Union[Unset, list[str]]):
        payment_status (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, str]):  Default: 'AUTO_INVOICE'.
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IV01Response200]
    """

    kwargs = _get_kwargs(
        currency=currency,
        end_date=end_date,
        issuing_user_types=issuing_user_types,
        pay_out_psp_codes=pay_out_psp_codes,
        payment_status=payment_status,
        start_date=start_date,
        type_=type_,
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
    currency: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    issuing_user_types: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    payment_status: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, str] = "AUTO_INVOICE",
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[IV01Response200]:
    """List accounting documents

    Args:
        currency (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        issuing_user_types (Union[Unset, list[str]]):
        pay_out_psp_codes (Union[Unset, list[str]]):
        payment_status (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, str]):  Default: 'AUTO_INVOICE'.
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IV01Response200
    """

    return sync_detailed(
        client=client,
        currency=currency,
        end_date=end_date,
        issuing_user_types=issuing_user_types,
        pay_out_psp_codes=pay_out_psp_codes,
        payment_status=payment_status,
        start_date=start_date,
        type_=type_,
        shop_id=shop_id,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    issuing_user_types: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    payment_status: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, str] = "AUTO_INVOICE",
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[IV01Response200]:
    """List accounting documents

    Args:
        currency (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        issuing_user_types (Union[Unset, list[str]]):
        pay_out_psp_codes (Union[Unset, list[str]]):
        payment_status (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, str]):  Default: 'AUTO_INVOICE'.
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IV01Response200]
    """

    kwargs = _get_kwargs(
        currency=currency,
        end_date=end_date,
        issuing_user_types=issuing_user_types,
        pay_out_psp_codes=pay_out_psp_codes,
        payment_status=payment_status,
        start_date=start_date,
        type_=type_,
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
    currency: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    issuing_user_types: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    payment_status: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, str] = "AUTO_INVOICE",
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[IV01Response200]:
    """List accounting documents

    Args:
        currency (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        issuing_user_types (Union[Unset, list[str]]):
        pay_out_psp_codes (Union[Unset, list[str]]):
        payment_status (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, str]):  Default: 'AUTO_INVOICE'.
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IV01Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            end_date=end_date,
            issuing_user_types=issuing_user_types,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_status=payment_status,
            start_date=start_date,
            type_=type_,
            shop_id=shop_id,
            max_=max_,
            offset=offset,
            sort=sort,
            order=order,
        )
    ).parsed
