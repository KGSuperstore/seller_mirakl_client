import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pr01_response_200 import PR01Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: Union[Unset, str] = UNSET,
    types: Union[Unset, str] = UNSET,
    states: Union[Unset, str] = "ACTIVE",
    ending_after: Union[Unset, datetime.datetime] = UNSET,
    starting_before: Union[Unset, datetime.datetime] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    locale: Union[Unset, str] = UNSET,
    trigger_offer_ids: Union[Unset, str] = UNSET,
    reward_offer_ids: Union[Unset, str] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ids"] = ids

    params["types"] = types

    params["states"] = states

    json_ending_after: Union[Unset, str] = UNSET
    if not isinstance(ending_after, Unset):
        json_ending_after = ending_after.isoformat()
    params["ending_after"] = json_ending_after

    json_starting_before: Union[Unset, str] = UNSET
    if not isinstance(starting_before, Unset):
        json_starting_before = starting_before.isoformat()
    params["starting_before"] = json_starting_before

    json_date_created_from: Union[Unset, str] = UNSET
    if not isinstance(date_created_from, Unset):
        json_date_created_from = date_created_from.isoformat()
    params["date_created_from"] = json_date_created_from

    json_date_created_to: Union[Unset, str] = UNSET
    if not isinstance(date_created_to, Unset):
        json_date_created_to = date_created_to.isoformat()
    params["date_created_to"] = json_date_created_to

    json_last_request_date: Union[Unset, str] = UNSET
    if not isinstance(last_request_date, Unset):
        json_last_request_date = last_request_date.isoformat()
    params["last_request_date"] = json_last_request_date

    params["locale"] = locale

    params["trigger_offer_ids"] = trigger_offer_ids

    params["reward_offer_ids"] = reward_offer_ids

    params["channel_codes"] = channel_codes

    params["shop_id"] = shop_id

    params["max"] = max_

    params["offset"] = offset

    params["sort"] = sort

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/promotions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PR01Response200]:
    if response.status_code == 200:
        response_200 = PR01Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PR01Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    types: Union[Unset, str] = UNSET,
    states: Union[Unset, str] = "ACTIVE",
    ending_after: Union[Unset, datetime.datetime] = UNSET,
    starting_before: Union[Unset, datetime.datetime] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    locale: Union[Unset, str] = UNSET,
    trigger_offer_ids: Union[Unset, str] = UNSET,
    reward_offer_ids: Union[Unset, str] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[PR01Response200]:
    """List promotions

    Args:
        ids (Union[Unset, str]):
        types (Union[Unset, str]):
        states (Union[Unset, str]):  Default: 'ACTIVE'.
        ending_after (Union[Unset, datetime.datetime]):
        starting_before (Union[Unset, datetime.datetime]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_request_date (Union[Unset, datetime.datetime]):
        locale (Union[Unset, str]):
        trigger_offer_ids (Union[Unset, str]):
        reward_offer_ids (Union[Unset, str]):
        channel_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PR01Response200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        types=types,
        states=states,
        ending_after=ending_after,
        starting_before=starting_before,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_request_date=last_request_date,
        locale=locale,
        trigger_offer_ids=trigger_offer_ids,
        reward_offer_ids=reward_offer_ids,
        channel_codes=channel_codes,
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
    ids: Union[Unset, str] = UNSET,
    types: Union[Unset, str] = UNSET,
    states: Union[Unset, str] = "ACTIVE",
    ending_after: Union[Unset, datetime.datetime] = UNSET,
    starting_before: Union[Unset, datetime.datetime] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    locale: Union[Unset, str] = UNSET,
    trigger_offer_ids: Union[Unset, str] = UNSET,
    reward_offer_ids: Union[Unset, str] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[PR01Response200]:
    """List promotions

    Args:
        ids (Union[Unset, str]):
        types (Union[Unset, str]):
        states (Union[Unset, str]):  Default: 'ACTIVE'.
        ending_after (Union[Unset, datetime.datetime]):
        starting_before (Union[Unset, datetime.datetime]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_request_date (Union[Unset, datetime.datetime]):
        locale (Union[Unset, str]):
        trigger_offer_ids (Union[Unset, str]):
        reward_offer_ids (Union[Unset, str]):
        channel_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PR01Response200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        types=types,
        states=states,
        ending_after=ending_after,
        starting_before=starting_before,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_request_date=last_request_date,
        locale=locale,
        trigger_offer_ids=trigger_offer_ids,
        reward_offer_ids=reward_offer_ids,
        channel_codes=channel_codes,
        shop_id=shop_id,
        max_=max_,
        offset=offset,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    types: Union[Unset, str] = UNSET,
    states: Union[Unset, str] = "ACTIVE",
    ending_after: Union[Unset, datetime.datetime] = UNSET,
    starting_before: Union[Unset, datetime.datetime] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    locale: Union[Unset, str] = UNSET,
    trigger_offer_ids: Union[Unset, str] = UNSET,
    reward_offer_ids: Union[Unset, str] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Response[PR01Response200]:
    """List promotions

    Args:
        ids (Union[Unset, str]):
        types (Union[Unset, str]):
        states (Union[Unset, str]):  Default: 'ACTIVE'.
        ending_after (Union[Unset, datetime.datetime]):
        starting_before (Union[Unset, datetime.datetime]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_request_date (Union[Unset, datetime.datetime]):
        locale (Union[Unset, str]):
        trigger_offer_ids (Union[Unset, str]):
        reward_offer_ids (Union[Unset, str]):
        channel_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PR01Response200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        types=types,
        states=states,
        ending_after=ending_after,
        starting_before=starting_before,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        last_request_date=last_request_date,
        locale=locale,
        trigger_offer_ids=trigger_offer_ids,
        reward_offer_ids=reward_offer_ids,
        channel_codes=channel_codes,
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
    ids: Union[Unset, str] = UNSET,
    types: Union[Unset, str] = UNSET,
    states: Union[Unset, str] = "ACTIVE",
    ending_after: Union[Unset, datetime.datetime] = UNSET,
    starting_before: Union[Unset, datetime.datetime] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    last_request_date: Union[Unset, datetime.datetime] = UNSET,
    locale: Union[Unset, str] = UNSET,
    trigger_offer_ids: Union[Unset, str] = UNSET,
    reward_offer_ids: Union[Unset, str] = UNSET,
    channel_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
) -> Optional[PR01Response200]:
    """List promotions

    Args:
        ids (Union[Unset, str]):
        types (Union[Unset, str]):
        states (Union[Unset, str]):  Default: 'ACTIVE'.
        ending_after (Union[Unset, datetime.datetime]):
        starting_before (Union[Unset, datetime.datetime]):
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        last_request_date (Union[Unset, datetime.datetime]):
        locale (Union[Unset, str]):
        trigger_offer_ids (Union[Unset, str]):
        reward_offer_ids (Union[Unset, str]):
        channel_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):
        max_ (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PR01Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            types=types,
            states=states,
            ending_after=ending_after,
            starting_before=starting_before,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_request_date=last_request_date,
            locale=locale,
            trigger_offer_ids=trigger_offer_ids,
            reward_offer_ids=reward_offer_ids,
            channel_codes=channel_codes,
            shop_id=shop_id,
            max_=max_,
            offset=offset,
            sort=sort,
            order=order,
        )
    ).parsed
