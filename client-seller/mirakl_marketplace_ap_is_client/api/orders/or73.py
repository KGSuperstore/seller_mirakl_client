from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    order_ids: Union[Unset, str] = UNSET,
    document_ids: Union[Unset, str] = UNSET,
    document_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_ids"] = order_ids

    params["document_ids"] = document_ids

    params["document_codes"] = document_codes

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/orders/documents/download",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    document_ids: Union[Unset, str] = UNSET,
    document_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Download one or multiple documents attached to one or multiple orders

     <ul>   <li>If a list of document identifiers is specified only these documents are downloaded.
    <ul>           <li>If more than one document id is specified, the documents will be wrapped in a ZIP
    archive</li>           <li>If only one document id is specified the document will not be zipped</li>
    </ul>   </li>   <li>If a list of order identifiers is specified, all documents from those orders are
    downloaded.<br/>   Use a list of order document type codes to retrieve specific types from those
    orders.<br/>   In this case, the output of the API will always be a ZIP archive even if there is
    only one document to retrieve.   </li></ul>When documents are retrieved, they're wrapped into a ZIP
    archive except when only one document id is specified. The tree structure of this archive is as
    follow:<pre>
    documents-timestamp.zip
    |
    |__ order_id_x/
    |   |__ foo.txt
    |   |__ bar.txt
    |   |__ baz.pdf
    |
    |__ order_id_y/
    |   |__ image.png
    |   |__ image(1).png
    </pre>

    Args:
        order_ids (Union[Unset, str]):
        document_ids (Union[Unset, str]):
        document_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        document_ids=document_ids,
        document_codes=document_codes,
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    document_ids: Union[Unset, str] = UNSET,
    document_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Download one or multiple documents attached to one or multiple orders

     <ul>   <li>If a list of document identifiers is specified only these documents are downloaded.
    <ul>           <li>If more than one document id is specified, the documents will be wrapped in a ZIP
    archive</li>           <li>If only one document id is specified the document will not be zipped</li>
    </ul>   </li>   <li>If a list of order identifiers is specified, all documents from those orders are
    downloaded.<br/>   Use a list of order document type codes to retrieve specific types from those
    orders.<br/>   In this case, the output of the API will always be a ZIP archive even if there is
    only one document to retrieve.   </li></ul>When documents are retrieved, they're wrapped into a ZIP
    archive except when only one document id is specified. The tree structure of this archive is as
    follow:<pre>
    documents-timestamp.zip
    |
    |__ order_id_x/
    |   |__ foo.txt
    |   |__ bar.txt
    |   |__ baz.pdf
    |
    |__ order_id_y/
    |   |__ image.png
    |   |__ image(1).png
    </pre>

    Args:
        order_ids (Union[Unset, str]):
        document_ids (Union[Unset, str]):
        document_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        client=client,
        order_ids=order_ids,
        document_ids=document_ids,
        document_codes=document_codes,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    document_ids: Union[Unset, str] = UNSET,
    document_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Response[File]:
    """Download one or multiple documents attached to one or multiple orders

     <ul>   <li>If a list of document identifiers is specified only these documents are downloaded.
    <ul>           <li>If more than one document id is specified, the documents will be wrapped in a ZIP
    archive</li>           <li>If only one document id is specified the document will not be zipped</li>
    </ul>   </li>   <li>If a list of order identifiers is specified, all documents from those orders are
    downloaded.<br/>   Use a list of order document type codes to retrieve specific types from those
    orders.<br/>   In this case, the output of the API will always be a ZIP archive even if there is
    only one document to retrieve.   </li></ul>When documents are retrieved, they're wrapped into a ZIP
    archive except when only one document id is specified. The tree structure of this archive is as
    follow:<pre>
    documents-timestamp.zip
    |
    |__ order_id_x/
    |   |__ foo.txt
    |   |__ bar.txt
    |   |__ baz.pdf
    |
    |__ order_id_y/
    |   |__ image.png
    |   |__ image(1).png
    </pre>

    Args:
        order_ids (Union[Unset, str]):
        document_ids (Union[Unset, str]):
        document_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        document_ids=document_ids,
        document_codes=document_codes,
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_ids: Union[Unset, str] = UNSET,
    document_ids: Union[Unset, str] = UNSET,
    document_codes: Union[Unset, str] = UNSET,
    shop_id: Union[Unset, int] = UNSET,
) -> Optional[File]:
    """Download one or multiple documents attached to one or multiple orders

     <ul>   <li>If a list of document identifiers is specified only these documents are downloaded.
    <ul>           <li>If more than one document id is specified, the documents will be wrapped in a ZIP
    archive</li>           <li>If only one document id is specified the document will not be zipped</li>
    </ul>   </li>   <li>If a list of order identifiers is specified, all documents from those orders are
    downloaded.<br/>   Use a list of order document type codes to retrieve specific types from those
    orders.<br/>   In this case, the output of the API will always be a ZIP archive even if there is
    only one document to retrieve.   </li></ul>When documents are retrieved, they're wrapped into a ZIP
    archive except when only one document id is specified. The tree structure of this archive is as
    follow:<pre>
    documents-timestamp.zip
    |
    |__ order_id_x/
    |   |__ foo.txt
    |   |__ bar.txt
    |   |__ baz.pdf
    |
    |__ order_id_y/
    |   |__ image.png
    |   |__ image(1).png
    </pre>

    Args:
        order_ids (Union[Unset, str]):
        document_ids (Union[Unset, str]):
        document_codes (Union[Unset, str]):
        shop_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            client=client,
            order_ids=order_ids,
            document_ids=document_ids,
            document_codes=document_codes,
            shop_id=shop_id,
        )
    ).parsed
