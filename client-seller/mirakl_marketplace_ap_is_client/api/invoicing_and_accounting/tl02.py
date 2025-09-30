import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tl02_response_200 import TL02Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[str]] = UNSET,
    accounting_document_number: Union[Unset, str] = UNSET,
    order_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    order_reference_for_customer: Union[Unset, list[str]] = UNSET,
    order_reference_for_seller: Union[Unset, list[str]] = UNSET,
    accounting_document_id: Union[Unset, str] = UNSET,
    shop_model: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_created_from: Union[Unset, str] = UNSET
    if not isinstance(date_created_from, Unset):
        json_date_created_from = date_created_from.isoformat()
    params["date_created_from"] = json_date_created_from

    json_date_created_to: Union[Unset, str] = UNSET
    if not isinstance(date_created_to, Unset):
        json_date_created_to = date_created_to.isoformat()
    params["date_created_to"] = json_date_created_to

    json_transaction_date_from: Union[Unset, str] = UNSET
    if not isinstance(transaction_date_from, Unset):
        json_transaction_date_from = transaction_date_from.isoformat()
    params["transaction_date_from"] = json_transaction_date_from

    json_transaction_date_to: Union[Unset, str] = UNSET
    if not isinstance(transaction_date_to, Unset):
        json_transaction_date_to = transaction_date_to.isoformat()
    params["transaction_date_to"] = json_transaction_date_to

    json_last_updated_from: Union[Unset, str] = UNSET
    if not isinstance(last_updated_from, Unset):
        json_last_updated_from = last_updated_from.isoformat()
    params["last_updated_from"] = json_last_updated_from

    json_payment_state: Union[Unset, list[str]] = UNSET
    if not isinstance(payment_state, Unset):
        json_payment_state = payment_state

    params["payment_state"] = json_payment_state

    json_transaction_type: Union[Unset, list[str]] = UNSET
    if not isinstance(transaction_type, Unset):
        json_transaction_type = transaction_type

    params["transaction_type"] = json_transaction_type

    params["accounting_document_number"] = accounting_document_number

    json_order_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = order_id

    params["order_id"] = json_order_id

    json_order_line_id: Union[Unset, list[str]] = UNSET
    if not isinstance(order_line_id, Unset):
        json_order_line_id = order_line_id

    params["order_line_id"] = json_order_line_id

    json_order_reference_for_customer: Union[Unset, list[str]] = UNSET
    if not isinstance(order_reference_for_customer, Unset):
        json_order_reference_for_customer = order_reference_for_customer

    params["order_reference_for_customer"] = json_order_reference_for_customer

    json_order_reference_for_seller: Union[Unset, list[str]] = UNSET
    if not isinstance(order_reference_for_seller, Unset):
        json_order_reference_for_seller = order_reference_for_seller

    params["order_reference_for_seller"] = json_order_reference_for_seller

    params["accounting_document_id"] = accounting_document_id

    json_shop_model: Union[Unset, list[str]] = UNSET
    if not isinstance(shop_model, Unset):
        json_shop_model = shop_model

    params["shop_model"] = json_shop_model

    json_pay_out_psp_codes: Union[Unset, list[str]] = UNSET
    if not isinstance(pay_out_psp_codes, Unset):
        json_pay_out_psp_codes = pay_out_psp_codes

    params["pay_out_psp_codes"] = json_pay_out_psp_codes

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/sellerpayment/transactions_logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TL02Response200]:
    if response.status_code == 200:
        response_200 = TL02Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TL02Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[str]] = UNSET,
    accounting_document_number: Union[Unset, str] = UNSET,
    order_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    order_reference_for_customer: Union[Unset, list[str]] = UNSET,
    order_reference_for_seller: Union[Unset, list[str]] = UNSET,
    accounting_document_id: Union[Unset, str] = UNSET,
    shop_model: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[TL02Response200]:
    """List transaction lines

     This resource uses seek pagination. The maximum allowed value for parameter <code>limit</code> is
    <code>2000</code>.

    Args:
        date_created_from (Union[Unset, datetime.datetime]): Creation date for filtering
        date_created_to (Union[Unset, datetime.datetime]): Creation date for filtering
        transaction_date_from (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_date_to (Union[Unset, datetime.datetime]): Transaction date for filtering
        last_updated_from (Union[Unset, datetime.datetime]): Last updated date for filtering
        payment_state (Union[Unset, list[str]]): Payment state for filtering. This parameter can
            be supplied multiple times.
        transaction_type (Union[Unset, list[str]]): Transaction type for filtering. This parameter
            can be supplied multiple times.
        accounting_document_number (Union[Unset, str]):
        order_id (Union[Unset, list[str]]): Order id for filtering. This parameter can be supplied
            multiple times.
        order_line_id (Union[Unset, list[str]]): Order line id for filtering. This parameter can
            be supplied multiple times.
        order_reference_for_customer (Union[Unset, list[str]]): A comma-separated list of order
            references for customer.
        order_reference_for_seller (Union[Unset, list[str]]): A comma-separated list of order
            references for seller.
        accounting_document_id (Union[Unset, str]):
        shop_model (Union[Unset, list[str]]): Shop model for filtering. This parameter can be
            supplied multiple times.
        pay_out_psp_codes (Union[Unset, list[str]]): A comma-separated list of pay-out PSP codes
            for filtering. This parameter requires the Hybrid pay-out PSP feature to be enabled.
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL02Response200]
    """

    kwargs = _get_kwargs(
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        transaction_date_from=transaction_date_from,
        transaction_date_to=transaction_date_to,
        last_updated_from=last_updated_from,
        payment_state=payment_state,
        transaction_type=transaction_type,
        accounting_document_number=accounting_document_number,
        order_id=order_id,
        order_line_id=order_line_id,
        order_reference_for_customer=order_reference_for_customer,
        order_reference_for_seller=order_reference_for_seller,
        accounting_document_id=accounting_document_id,
        shop_model=shop_model,
        pay_out_psp_codes=pay_out_psp_codes,
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
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[str]] = UNSET,
    accounting_document_number: Union[Unset, str] = UNSET,
    order_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    order_reference_for_customer: Union[Unset, list[str]] = UNSET,
    order_reference_for_seller: Union[Unset, list[str]] = UNSET,
    accounting_document_id: Union[Unset, str] = UNSET,
    shop_model: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[TL02Response200]:
    """List transaction lines

     This resource uses seek pagination. The maximum allowed value for parameter <code>limit</code> is
    <code>2000</code>.

    Args:
        date_created_from (Union[Unset, datetime.datetime]): Creation date for filtering
        date_created_to (Union[Unset, datetime.datetime]): Creation date for filtering
        transaction_date_from (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_date_to (Union[Unset, datetime.datetime]): Transaction date for filtering
        last_updated_from (Union[Unset, datetime.datetime]): Last updated date for filtering
        payment_state (Union[Unset, list[str]]): Payment state for filtering. This parameter can
            be supplied multiple times.
        transaction_type (Union[Unset, list[str]]): Transaction type for filtering. This parameter
            can be supplied multiple times.
        accounting_document_number (Union[Unset, str]):
        order_id (Union[Unset, list[str]]): Order id for filtering. This parameter can be supplied
            multiple times.
        order_line_id (Union[Unset, list[str]]): Order line id for filtering. This parameter can
            be supplied multiple times.
        order_reference_for_customer (Union[Unset, list[str]]): A comma-separated list of order
            references for customer.
        order_reference_for_seller (Union[Unset, list[str]]): A comma-separated list of order
            references for seller.
        accounting_document_id (Union[Unset, str]):
        shop_model (Union[Unset, list[str]]): Shop model for filtering. This parameter can be
            supplied multiple times.
        pay_out_psp_codes (Union[Unset, list[str]]): A comma-separated list of pay-out PSP codes
            for filtering. This parameter requires the Hybrid pay-out PSP feature to be enabled.
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL02Response200
    """

    return sync_detailed(
        client=client,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        transaction_date_from=transaction_date_from,
        transaction_date_to=transaction_date_to,
        last_updated_from=last_updated_from,
        payment_state=payment_state,
        transaction_type=transaction_type,
        accounting_document_number=accounting_document_number,
        order_id=order_id,
        order_line_id=order_line_id,
        order_reference_for_customer=order_reference_for_customer,
        order_reference_for_seller=order_reference_for_seller,
        accounting_document_id=accounting_document_id,
        shop_model=shop_model,
        pay_out_psp_codes=pay_out_psp_codes,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[str]] = UNSET,
    accounting_document_number: Union[Unset, str] = UNSET,
    order_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    order_reference_for_customer: Union[Unset, list[str]] = UNSET,
    order_reference_for_seller: Union[Unset, list[str]] = UNSET,
    accounting_document_id: Union[Unset, str] = UNSET,
    shop_model: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[TL02Response200]:
    """List transaction lines

     This resource uses seek pagination. The maximum allowed value for parameter <code>limit</code> is
    <code>2000</code>.

    Args:
        date_created_from (Union[Unset, datetime.datetime]): Creation date for filtering
        date_created_to (Union[Unset, datetime.datetime]): Creation date for filtering
        transaction_date_from (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_date_to (Union[Unset, datetime.datetime]): Transaction date for filtering
        last_updated_from (Union[Unset, datetime.datetime]): Last updated date for filtering
        payment_state (Union[Unset, list[str]]): Payment state for filtering. This parameter can
            be supplied multiple times.
        transaction_type (Union[Unset, list[str]]): Transaction type for filtering. This parameter
            can be supplied multiple times.
        accounting_document_number (Union[Unset, str]):
        order_id (Union[Unset, list[str]]): Order id for filtering. This parameter can be supplied
            multiple times.
        order_line_id (Union[Unset, list[str]]): Order line id for filtering. This parameter can
            be supplied multiple times.
        order_reference_for_customer (Union[Unset, list[str]]): A comma-separated list of order
            references for customer.
        order_reference_for_seller (Union[Unset, list[str]]): A comma-separated list of order
            references for seller.
        accounting_document_id (Union[Unset, str]):
        shop_model (Union[Unset, list[str]]): Shop model for filtering. This parameter can be
            supplied multiple times.
        pay_out_psp_codes (Union[Unset, list[str]]): A comma-separated list of pay-out PSP codes
            for filtering. This parameter requires the Hybrid pay-out PSP feature to be enabled.
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TL02Response200]
    """

    kwargs = _get_kwargs(
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        transaction_date_from=transaction_date_from,
        transaction_date_to=transaction_date_to,
        last_updated_from=last_updated_from,
        payment_state=payment_state,
        transaction_type=transaction_type,
        accounting_document_number=accounting_document_number,
        order_id=order_id,
        order_line_id=order_line_id,
        order_reference_for_customer=order_reference_for_customer,
        order_reference_for_seller=order_reference_for_seller,
        accounting_document_id=accounting_document_id,
        shop_model=shop_model,
        pay_out_psp_codes=pay_out_psp_codes,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET,
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[str]] = UNSET,
    accounting_document_number: Union[Unset, str] = UNSET,
    order_id: Union[Unset, list[str]] = UNSET,
    order_line_id: Union[Unset, list[str]] = UNSET,
    order_reference_for_customer: Union[Unset, list[str]] = UNSET,
    order_reference_for_seller: Union[Unset, list[str]] = UNSET,
    accounting_document_id: Union[Unset, str] = UNSET,
    shop_model: Union[Unset, list[str]] = UNSET,
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[TL02Response200]:
    """List transaction lines

     This resource uses seek pagination. The maximum allowed value for parameter <code>limit</code> is
    <code>2000</code>.

    Args:
        date_created_from (Union[Unset, datetime.datetime]): Creation date for filtering
        date_created_to (Union[Unset, datetime.datetime]): Creation date for filtering
        transaction_date_from (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_date_to (Union[Unset, datetime.datetime]): Transaction date for filtering
        last_updated_from (Union[Unset, datetime.datetime]): Last updated date for filtering
        payment_state (Union[Unset, list[str]]): Payment state for filtering. This parameter can
            be supplied multiple times.
        transaction_type (Union[Unset, list[str]]): Transaction type for filtering. This parameter
            can be supplied multiple times.
        accounting_document_number (Union[Unset, str]):
        order_id (Union[Unset, list[str]]): Order id for filtering. This parameter can be supplied
            multiple times.
        order_line_id (Union[Unset, list[str]]): Order line id for filtering. This parameter can
            be supplied multiple times.
        order_reference_for_customer (Union[Unset, list[str]]): A comma-separated list of order
            references for customer.
        order_reference_for_seller (Union[Unset, list[str]]): A comma-separated list of order
            references for seller.
        accounting_document_id (Union[Unset, str]):
        shop_model (Union[Unset, list[str]]): Shop model for filtering. This parameter can be
            supplied multiple times.
        pay_out_psp_codes (Union[Unset, list[str]]): A comma-separated list of pay-out PSP codes
            for filtering. This parameter requires the Hybrid pay-out PSP feature to be enabled.
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TL02Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            last_updated_from=last_updated_from,
            payment_state=payment_state,
            transaction_type=transaction_type,
            accounting_document_number=accounting_document_number,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            accounting_document_id=accounting_document_id,
            shop_model=shop_model,
            pay_out_psp_codes=pay_out_psp_codes,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
