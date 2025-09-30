from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersInvoiceDetailsPaymentTerms")


@_attrs_define
class OR11Response200OrdersInvoiceDetailsPaymentTerms:
    """
    Attributes:
        days (Union[Unset, int]): Number of days
        type_ (Union[Unset, str]): Payment terms type.<br>Possible values: <ul><li><code>END_OF_MONTH</code>: payment is
            due after a number of calendar days following the invoice issue date, at the end of the given month.
            </li><li><code>NET</code>: payment is due after a number of calendar days following the invoice issue date.
            </li></ul>
    """

    days: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days", UNSET)

        type_ = d.pop("type", UNSET)

        or11_response_200_orders_invoice_details_payment_terms = cls(
            days=days,
            type_=type_,
        )

        or11_response_200_orders_invoice_details_payment_terms.additional_properties = d
        return or11_response_200_orders_invoice_details_payment_terms

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
