import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dr11_response_200 import DR11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    document_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    issue_date_from: Union[Unset, datetime.datetime] = UNSET,
    issue_date_to: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    issuer_type: Union[Unset, list[str]] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    entity_type: Union[Unset, list[str]] = UNSET,
    billing_cycle_from: Union[Unset, datetime.datetime] = UNSET,
    billing_cycle_to: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["document_number"] = document_number

    json_date_created_from: Union[Unset, str] = UNSET
    if not isinstance(date_created_from, Unset):
        json_date_created_from = date_created_from.isoformat()
    params["date_created_from"] = json_date_created_from

    json_date_created_to: Union[Unset, str] = UNSET
    if not isinstance(date_created_to, Unset):
        json_date_created_to = date_created_to.isoformat()
    params["date_created_to"] = json_date_created_to

    json_last_updated_from: Union[Unset, str] = UNSET
    if not isinstance(last_updated_from, Unset):
        json_last_updated_from = last_updated_from.isoformat()
    params["last_updated_from"] = json_last_updated_from

    json_last_updated_to: Union[Unset, str] = UNSET
    if not isinstance(last_updated_to, Unset):
        json_last_updated_to = last_updated_to.isoformat()
    params["last_updated_to"] = json_last_updated_to

    json_issue_date_from: Union[Unset, str] = UNSET
    if not isinstance(issue_date_from, Unset):
        json_issue_date_from = issue_date_from.isoformat()
    params["issue_date_from"] = json_issue_date_from

    json_issue_date_to: Union[Unset, str] = UNSET
    if not isinstance(issue_date_to, Unset):
        json_issue_date_to = issue_date_to.isoformat()
    params["issue_date_to"] = json_issue_date_to

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_issuer_type: Union[Unset, list[str]] = UNSET
    if not isinstance(issuer_type, Unset):
        json_issuer_type = issuer_type

    params["issuer_type"] = json_issuer_type

    json_entity_id: Union[Unset, list[str]] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = entity_id

    params["entity_id"] = json_entity_id

    json_entity_type: Union[Unset, list[str]] = UNSET
    if not isinstance(entity_type, Unset):
        json_entity_type = entity_type

    params["entity_type"] = json_entity_type

    json_billing_cycle_from: Union[Unset, str] = UNSET
    if not isinstance(billing_cycle_from, Unset):
        json_billing_cycle_from = billing_cycle_from.isoformat()
    params["billing_cycle_from"] = json_billing_cycle_from

    json_billing_cycle_to: Union[Unset, str] = UNSET
    if not isinstance(billing_cycle_to, Unset):
        json_billing_cycle_to = billing_cycle_to.isoformat()
    params["billing_cycle_to"] = json_billing_cycle_to

    params["payment_state"] = payment_state

    params["shop_id"] = shop_id

    params["page_token"] = page_token

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/document-request/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DR11Response200]:
    if response.status_code == 200:
        response_200 = DR11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DR11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    document_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    issue_date_from: Union[Unset, datetime.datetime] = UNSET,
    issue_date_to: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    issuer_type: Union[Unset, list[str]] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    entity_type: Union[Unset, list[str]] = UNSET,
    billing_cycle_from: Union[Unset, datetime.datetime] = UNSET,
    billing_cycle_to: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[DR11Response200]:
    """List accounting documents requests

    Args:
        id (Union[Unset, str]):
        document_number (Union[Unset, str]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_updated_from (Union[Unset, datetime.datetime]):
        last_updated_to (Union[Unset, datetime.datetime]):
        issue_date_from (Union[Unset, datetime.datetime]):
        issue_date_to (Union[Unset, datetime.datetime]):
        state (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        issuer_type (Union[Unset, list[str]]):
        entity_id (Union[Unset, list[str]]):
        entity_type (Union[Unset, list[str]]):
        billing_cycle_from (Union[Unset, datetime.datetime]):
        billing_cycle_to (Union[Unset, datetime.datetime]):
        payment_state (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DR11Response200]
    """

    kwargs = _get_kwargs(
        id=id,
        document_number=document_number,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_updated_from=last_updated_from,
        last_updated_to=last_updated_to,
        issue_date_from=issue_date_from,
        issue_date_to=issue_date_to,
        state=state,
        type_=type_,
        issuer_type=issuer_type,
        entity_id=entity_id,
        entity_type=entity_type,
        billing_cycle_from=billing_cycle_from,
        billing_cycle_to=billing_cycle_to,
        payment_state=payment_state,
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
    id: Union[Unset, str] = UNSET,
    document_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    issue_date_from: Union[Unset, datetime.datetime] = UNSET,
    issue_date_to: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    issuer_type: Union[Unset, list[str]] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    entity_type: Union[Unset, list[str]] = UNSET,
    billing_cycle_from: Union[Unset, datetime.datetime] = UNSET,
    billing_cycle_to: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[DR11Response200]:
    """List accounting documents requests

    Args:
        id (Union[Unset, str]):
        document_number (Union[Unset, str]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_updated_from (Union[Unset, datetime.datetime]):
        last_updated_to (Union[Unset, datetime.datetime]):
        issue_date_from (Union[Unset, datetime.datetime]):
        issue_date_to (Union[Unset, datetime.datetime]):
        state (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        issuer_type (Union[Unset, list[str]]):
        entity_id (Union[Unset, list[str]]):
        entity_type (Union[Unset, list[str]]):
        billing_cycle_from (Union[Unset, datetime.datetime]):
        billing_cycle_to (Union[Unset, datetime.datetime]):
        payment_state (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DR11Response200
    """

    return sync_detailed(
        client=client,
        id=id,
        document_number=document_number,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_updated_from=last_updated_from,
        last_updated_to=last_updated_to,
        issue_date_from=issue_date_from,
        issue_date_to=issue_date_to,
        state=state,
        type_=type_,
        issuer_type=issuer_type,
        entity_id=entity_id,
        entity_type=entity_type,
        billing_cycle_from=billing_cycle_from,
        billing_cycle_to=billing_cycle_to,
        payment_state=payment_state,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    document_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    issue_date_from: Union[Unset, datetime.datetime] = UNSET,
    issue_date_to: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    issuer_type: Union[Unset, list[str]] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    entity_type: Union[Unset, list[str]] = UNSET,
    billing_cycle_from: Union[Unset, datetime.datetime] = UNSET,
    billing_cycle_to: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[DR11Response200]:
    """List accounting documents requests

    Args:
        id (Union[Unset, str]):
        document_number (Union[Unset, str]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_updated_from (Union[Unset, datetime.datetime]):
        last_updated_to (Union[Unset, datetime.datetime]):
        issue_date_from (Union[Unset, datetime.datetime]):
        issue_date_to (Union[Unset, datetime.datetime]):
        state (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        issuer_type (Union[Unset, list[str]]):
        entity_id (Union[Unset, list[str]]):
        entity_type (Union[Unset, list[str]]):
        billing_cycle_from (Union[Unset, datetime.datetime]):
        billing_cycle_to (Union[Unset, datetime.datetime]):
        payment_state (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DR11Response200]
    """

    kwargs = _get_kwargs(
        id=id,
        document_number=document_number,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_updated_from=last_updated_from,
        last_updated_to=last_updated_to,
        issue_date_from=issue_date_from,
        issue_date_to=issue_date_to,
        state=state,
        type_=type_,
        issuer_type=issuer_type,
        entity_id=entity_id,
        entity_type=entity_type,
        billing_cycle_from=billing_cycle_from,
        billing_cycle_to=billing_cycle_to,
        payment_state=payment_state,
        shop_id=shop_id,
        page_token=page_token,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    document_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_updated_from: Union[Unset, datetime.datetime] = UNSET,
    last_updated_to: Union[Unset, datetime.datetime] = UNSET,
    issue_date_from: Union[Unset, datetime.datetime] = UNSET,
    issue_date_to: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    issuer_type: Union[Unset, list[str]] = UNSET,
    entity_id: Union[Unset, list[str]] = UNSET,
    entity_type: Union[Unset, list[str]] = UNSET,
    billing_cycle_from: Union[Unset, datetime.datetime] = UNSET,
    billing_cycle_to: Union[Unset, datetime.datetime] = UNSET,
    payment_state: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[DR11Response200]:
    """List accounting documents requests

    Args:
        id (Union[Unset, str]):
        document_number (Union[Unset, str]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_updated_from (Union[Unset, datetime.datetime]):
        last_updated_to (Union[Unset, datetime.datetime]):
        issue_date_from (Union[Unset, datetime.datetime]):
        issue_date_to (Union[Unset, datetime.datetime]):
        state (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        issuer_type (Union[Unset, list[str]]):
        entity_id (Union[Unset, list[str]]):
        entity_type (Union[Unset, list[str]]):
        billing_cycle_from (Union[Unset, datetime.datetime]):
        billing_cycle_to (Union[Unset, datetime.datetime]):
        payment_state (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DR11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            document_number=document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            issue_date_from=issue_date_from,
            issue_date_to=issue_date_to,
            state=state,
            type_=type_,
            issuer_type=issuer_type,
            entity_id=entity_id,
            entity_type=entity_type,
            billing_cycle_from=billing_cycle_from,
            billing_cycle_to=billing_cycle_to,
            payment_state=payment_state,
            shop_id=shop_id,
            page_token=page_token,
            sort=sort,
        )
    ).parsed
