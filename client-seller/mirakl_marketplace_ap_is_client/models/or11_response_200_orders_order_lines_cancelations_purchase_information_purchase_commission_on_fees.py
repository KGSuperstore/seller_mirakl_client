from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees")


@_attrs_define
class OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees:
    """
    Attributes:
        total_amount (Union[Unset, float]): Cancelation’s purchase commission total amount on fees
    """

    total_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_amount = d.pop("total_amount", UNSET)

        or11_response_200_orders_order_lines_cancelations_purchase_information_purchase_commission_on_fees = cls(
            total_amount=total_amount,
        )

        or11_response_200_orders_order_lines_cancelations_purchase_information_purchase_commission_on_fees.additional_properties = d
        return or11_response_200_orders_order_lines_cancelations_purchase_information_purchase_commission_on_fees

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
