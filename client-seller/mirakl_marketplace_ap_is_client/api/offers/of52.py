from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.of52_request import OF52Request
from ...models.of52_response_200 import OF52Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OF52Request,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/offers/export/async",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OF52Response200]:
    if response.status_code == 200:
        response_200 = OF52Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OF52Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF52Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OF52Response200]:
    r"""Export offers CSV or JSON file asynchronously

     Export status and files links can be retrieved by calling OF53.<br/>Get a CSV or JSON file that
    includes the offers updated and deleted since the last request date.<br/><br/>
    <div class=\"alert alert-warning\" role=\"alert\">
    To ease testing processes, the minimum values for \"megabytes_per_chunk\" and \"items_per_chunk\"
    have been lowered on TEST and DEV environments.<br/>
    Please adapt these values on PROD environments.
    </div>

    Args:
        shop_id (Union[Unset, int]):
        body (OF52Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF52Response200]
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
    body: OF52Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OF52Response200]:
    r"""Export offers CSV or JSON file asynchronously

     Export status and files links can be retrieved by calling OF53.<br/>Get a CSV or JSON file that
    includes the offers updated and deleted since the last request date.<br/><br/>
    <div class=\"alert alert-warning\" role=\"alert\">
    To ease testing processes, the minimum values for \"megabytes_per_chunk\" and \"items_per_chunk\"
    have been lowered on TEST and DEV environments.<br/>
    Please adapt these values on PROD environments.
    </div>

    Args:
        shop_id (Union[Unset, int]):
        body (OF52Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF52Response200
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OF52Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[OF52Response200]:
    r"""Export offers CSV or JSON file asynchronously

     Export status and files links can be retrieved by calling OF53.<br/>Get a CSV or JSON file that
    includes the offers updated and deleted since the last request date.<br/><br/>
    <div class=\"alert alert-warning\" role=\"alert\">
    To ease testing processes, the minimum values for \"megabytes_per_chunk\" and \"items_per_chunk\"
    have been lowered on TEST and DEV environments.<br/>
    Please adapt these values on PROD environments.
    </div>

    Args:
        shop_id (Union[Unset, int]):
        body (OF52Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OF52Response200]
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
    body: OF52Request,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[OF52Response200]:
    r"""Export offers CSV or JSON file asynchronously

     Export status and files links can be retrieved by calling OF53.<br/>Get a CSV or JSON file that
    includes the offers updated and deleted since the last request date.<br/><br/>
    <div class=\"alert alert-warning\" role=\"alert\">
    To ease testing processes, the minimum values for \"megabytes_per_chunk\" and \"items_per_chunk\"
    have been lowered on TEST and DEV environments.<br/>
    Please adapt these values on PROD environments.
    </div>

    Args:
        shop_id (Union[Unset, int]):
        body (OF52Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OF52Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_id=shop_id,
        )
    ).parsed
