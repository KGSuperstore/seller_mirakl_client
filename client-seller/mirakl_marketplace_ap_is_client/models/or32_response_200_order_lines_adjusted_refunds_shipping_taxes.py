from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR32Response200OrderLinesAdjustedRefundsShippingTaxes")


@_attrs_define
class OR32Response200OrderLinesAdjustedRefundsShippingTaxes:
    """
    Attributes:
        amount (Union[Unset, float]): Tax amount
        code (Union[Unset, str]): Tax code
    """

    amount: Union[Unset, float] = UNSET
    code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        code = d.pop("code", UNSET)

        or32_response_200_order_lines_adjusted_refunds_shipping_taxes = cls(
            amount=amount,
            code=code,
        )

        or32_response_200_order_lines_adjusted_refunds_shipping_taxes.additional_properties = d
        return or32_response_200_order_lines_adjusted_refunds_shipping_taxes

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
