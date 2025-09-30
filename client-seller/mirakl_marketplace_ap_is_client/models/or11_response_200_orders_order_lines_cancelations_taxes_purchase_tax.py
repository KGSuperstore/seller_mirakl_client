from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersOrderLinesCancelationsTaxesPurchaseTax")


@_attrs_define
class OR11Response200OrdersOrderLinesCancelationsTaxesPurchaseTax:
    """
    Attributes:
        purchase_amount (Union[Unset, float]): Purchase tax amount
        purchase_rate (Union[Unset, float]): Purchase tax rate
    """

    purchase_amount: Union[Unset, float] = UNSET
    purchase_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_amount = self.purchase_amount

        purchase_rate = self.purchase_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_amount is not UNSET:
            field_dict["purchase_amount"] = purchase_amount
        if purchase_rate is not UNSET:
            field_dict["purchase_rate"] = purchase_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purchase_amount = d.pop("purchase_amount", UNSET)

        purchase_rate = d.pop("purchase_rate", UNSET)

        or11_response_200_orders_order_lines_cancelations_taxes_purchase_tax = cls(
            purchase_amount=purchase_amount,
            purchase_rate=purchase_rate,
        )

        or11_response_200_orders_order_lines_cancelations_taxes_purchase_tax.additional_properties = d
        return or11_response_200_orders_order_lines_cancelations_taxes_purchase_tax

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
