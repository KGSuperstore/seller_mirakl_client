from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    import_id: str,
    *,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/offers/pricing/imports/{import_id}/error_report",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    import_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Get the error report for a price import in CSV format

     Only returns lines of offers with at least one offer price in error.<br/>
    The first column contains the line number in error. The second column contains the error
    reason.<br/>
    The returned file is ready to be reimported after the values have been fixed.<br/>
    Offer prices that were submitted in the price import but don't appear in the error report were
    successfully imported.

    Args:
        import_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        import_id=import_id,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    import_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Get the error report for a price import in CSV format

     Only returns lines of offers with at least one offer price in error.<br/>
    The first column contains the line number in error. The second column contains the error
    reason.<br/>
    The returned file is ready to be reimported after the values have been fixed.<br/>
    Offer prices that were submitted in the price import but don't appear in the error report were
    successfully imported.

    Args:
        import_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        import_id=import_id,
        client=client,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    import_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Get the error report for a price import in CSV format

     Only returns lines of offers with at least one offer price in error.<br/>
    The first column contains the line number in error. The second column contains the error
    reason.<br/>
    The returned file is ready to be reimported after the values have been fixed.<br/>
    Offer prices that were submitted in the price import but don't appear in the error report were
    successfully imported.

    Args:
        import_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        import_id=import_id,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    import_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Get the error report for a price import in CSV format

     Only returns lines of offers with at least one offer price in error.<br/>
    The first column contains the line number in error. The second column contains the error
    reason.<br/>
    The returned file is ready to be reimported after the values have been fixed.<br/>
    Offer prices that were submitted in the price import but don't appear in the error report were
    successfully imported.

    Args:
        import_id (str):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            import_id=import_id,
            client=client,
            shop_id=shop_id,
        )
    ).parsed
