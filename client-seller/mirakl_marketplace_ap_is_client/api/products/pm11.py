from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pm11_response_200 import PM11Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hierarchy: Union[Unset, str] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    all_operator_attributes: Union[Unset, bool] = False,
    with_roles: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hierarchy"] = hierarchy

    params["max_level"] = max_level

    params["all_operator_attributes"] = all_operator_attributes

    params["with_roles"] = with_roles

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/products/attributes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PM11Response200]:
    if response.status_code == 200:
        response_200 = PM11Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PM11Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy: Union[Unset, str] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    all_operator_attributes: Union[Unset, bool] = False,
    with_roles: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[PM11Response200]:
    """Get the product attribute configuration

     Retrieves all attributes for parents and children of the requested hierarchy

    Args:
        hierarchy (Union[Unset, str]):
        max_level (Union[Unset, int]):
        all_operator_attributes (Union[Unset, bool]):  Default: False.
        with_roles (Union[Unset, bool]):  Default: False.
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PM11Response200]
    """

    kwargs = _get_kwargs(
        hierarchy=hierarchy,
        max_level=max_level,
        all_operator_attributes=all_operator_attributes,
        with_roles=with_roles,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy: Union[Unset, str] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    all_operator_attributes: Union[Unset, bool] = False,
    with_roles: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[PM11Response200]:
    """Get the product attribute configuration

     Retrieves all attributes for parents and children of the requested hierarchy

    Args:
        hierarchy (Union[Unset, str]):
        max_level (Union[Unset, int]):
        all_operator_attributes (Union[Unset, bool]):  Default: False.
        with_roles (Union[Unset, bool]):  Default: False.
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PM11Response200
    """

    return sync_detailed(
        client=client,
        hierarchy=hierarchy,
        max_level=max_level,
        all_operator_attributes=all_operator_attributes,
        with_roles=with_roles,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy: Union[Unset, str] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    all_operator_attributes: Union[Unset, bool] = False,
    with_roles: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[PM11Response200]:
    """Get the product attribute configuration

     Retrieves all attributes for parents and children of the requested hierarchy

    Args:
        hierarchy (Union[Unset, str]):
        max_level (Union[Unset, int]):
        all_operator_attributes (Union[Unset, bool]):  Default: False.
        with_roles (Union[Unset, bool]):  Default: False.
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PM11Response200]
    """

    kwargs = _get_kwargs(
        hierarchy=hierarchy,
        max_level=max_level,
        all_operator_attributes=all_operator_attributes,
        with_roles=with_roles,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy: Union[Unset, str] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    all_operator_attributes: Union[Unset, bool] = False,
    with_roles: Union[Unset, bool] = False,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[PM11Response200]:
    """Get the product attribute configuration

     Retrieves all attributes for parents and children of the requested hierarchy

    Args:
        hierarchy (Union[Unset, str]):
        max_level (Union[Unset, int]):
        all_operator_attributes (Union[Unset, bool]):  Default: False.
        with_roles (Union[Unset, bool]):  Default: False.
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PM11Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            hierarchy=hierarchy,
            max_level=max_level,
            all_operator_attributes=all_operator_attributes,
            with_roles=with_roles,
            shop_id=shop_id,
        )
    ).parsed
