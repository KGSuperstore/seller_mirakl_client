from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TL02Response200DataEntitiesOrderTax")


@_attrs_define
class TL02Response200DataEntitiesOrderTax:
    """
    Attributes:
        code (Union[Unset, str]): The code of the transaction log tax
        rate (Union[Unset, float]): Tax rate
    """

    code: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        rate = d.pop("rate", UNSET)

        tl02_response_200_data_entities_order_tax = cls(
            code=code,
            rate=rate,
        )

        tl02_response_200_data_entities_order_tax.additional_properties = d
        return tl02_response_200_data_entities_order_tax

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
