from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersOrderRefundsTaxes")


@_attrs_define
class OR11Response200OrdersOrderRefundsTaxes:
    """
    Attributes:
        code (Union[Unset, str]): Order tax code
        rate (Union[Unset, float]): Order tax rate
        total_amount (Union[Unset, float]): Order total refunded tax amount for product and shipping, for a defined tax
            code and rate
    """

    code: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        rate = self.rate

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if rate is not UNSET:
            field_dict["rate"] = rate
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        rate = d.pop("rate", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        or11_response_200_orders_order_refunds_taxes = cls(
            code=code,
            rate=rate,
            total_amount=total_amount,
        )

        or11_response_200_orders_order_refunds_taxes.additional_properties = d
        return or11_response_200_orders_order_refunds_taxes

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
