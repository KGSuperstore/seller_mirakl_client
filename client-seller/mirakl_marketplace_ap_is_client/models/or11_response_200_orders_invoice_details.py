from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_invoice_details_document_details import (
        OR11Response200OrdersInvoiceDetailsDocumentDetails,
    )
    from ..models.or11_response_200_orders_invoice_details_payment_terms import (
        OR11Response200OrdersInvoiceDetailsPaymentTerms,
    )


T = TypeVar("T", bound="OR11Response200OrdersInvoiceDetails")


@_attrs_define
class OR11Response200OrdersInvoiceDetails:
    """
    Attributes:
        document_details (Union[Unset, list['OR11Response200OrdersInvoiceDetailsDocumentDetails']]): Invoice document
            information
        payment_terms (Union[Unset, OR11Response200OrdersInvoiceDetailsPaymentTerms]):
    """

    document_details: Union[Unset, list["OR11Response200OrdersInvoiceDetailsDocumentDetails"]] = UNSET
    payment_terms: Union[Unset, "OR11Response200OrdersInvoiceDetailsPaymentTerms"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.document_details, Unset):
            document_details = []
            for document_details_item_data in self.document_details:
                document_details_item = document_details_item_data.to_dict()
                document_details.append(document_details_item)

        payment_terms: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_terms, Unset):
            payment_terms = self.payment_terms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_details is not UNSET:
            field_dict["document_details"] = document_details
        if payment_terms is not UNSET:
            field_dict["payment_terms"] = payment_terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_invoice_details_document_details import (
            OR11Response200OrdersInvoiceDetailsDocumentDetails,
        )
        from ..models.or11_response_200_orders_invoice_details_payment_terms import (
            OR11Response200OrdersInvoiceDetailsPaymentTerms,
        )

        d = dict(src_dict)
        document_details = []
        _document_details = d.pop("document_details", UNSET)
        for document_details_item_data in _document_details or []:
            document_details_item = OR11Response200OrdersInvoiceDetailsDocumentDetails.from_dict(
                document_details_item_data
            )

            document_details.append(document_details_item)

        _payment_terms = d.pop("payment_terms", UNSET)
        payment_terms: Union[Unset, OR11Response200OrdersInvoiceDetailsPaymentTerms]
        if isinstance(_payment_terms, Unset):
            payment_terms = UNSET
        else:
            payment_terms = OR11Response200OrdersInvoiceDetailsPaymentTerms.from_dict(_payment_terms)

        or11_response_200_orders_invoice_details = cls(
            document_details=document_details,
            payment_terms=payment_terms,
        )

        or11_response_200_orders_invoice_details.additional_properties = d
        return or11_response_200_orders_invoice_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
