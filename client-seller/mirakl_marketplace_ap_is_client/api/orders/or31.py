from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.or31_request import OR31Request
from ...models.or31_response_200 import OR31Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    body: OR31Request,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/orders/{order_id}/additional_fields",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OR31Response200]:
    if response.status_code == 200:
        response_200 = OR31Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OR31Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR31Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR31Response200]:
    """Update the custom fields of an order and its order lines

     Only specified custom field values will be updated.<br/>In order to delete an custom field's value,
    set it to null or an empty string. Note that you may not delete the value of a required custom field
    value.<br/>Output will return information on the status of the update attempt by giving:<ul>
    <li>either all of the order and its order lines custom field values after the update</li>    <li>or
    in case of errors, the list of errors and the body of the initial call</li></ul>

    Args:
        order_id (str):
        shop_id (Union[Unset, int]):
        body (OR31Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR31Response200]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR31Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR31Response200]:
    """Update the custom fields of an order and its order lines

     Only specified custom field values will be updated.<br/>In order to delete an custom field's value,
    set it to null or an empty string. Note that you may not delete the value of a required custom field
    value.<br/>Output will return information on the status of the update attempt by giving:<ul>
    <li>either all of the order and its order lines custom field values after the update</li>    <li>or
    in case of errors, the list of errors and the body of the initial call</li></ul>

    Args:
        order_id (str):
        shop_id (Union[Unset, int]):
        body (OR31Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR31Response200
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR31Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OR31Response200]:
    """Update the custom fields of an order and its order lines

     Only specified custom field values will be updated.<br/>In order to delete an custom field's value,
    set it to null or an empty string. Note that you may not delete the value of a required custom field
    value.<br/>Output will return information on the status of the update attempt by giving:<ul>
    <li>either all of the order and its order lines custom field values after the update</li>    <li>or
    in case of errors, the list of errors and the body of the initial call</li></ul>

    Args:
        order_id (str):
        shop_id (Union[Unset, int]):
        body (OR31Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OR31Response200]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: OR31Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OR31Response200]:
    """Update the custom fields of an order and its order lines

     Only specified custom field values will be updated.<br/>In order to delete an custom field's value,
    set it to null or an empty string. Note that you may not delete the value of a required custom field
    value.<br/>Output will return information on the status of the update attempt by giving:<ul>
    <li>either all of the order and its order lines custom field values after the update</li>    <li>or
    in case of errors, the list of errors and the body of the initial call</li></ul>

    Args:
        order_id (str):
        shop_id (Union[Unset, int]):
        body (OR31Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OR31Response200
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
