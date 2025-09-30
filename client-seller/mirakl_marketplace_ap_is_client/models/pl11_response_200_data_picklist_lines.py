from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PL11Response200DataPicklistLines")


@_attrs_define
class PL11Response200DataPicklistLines:
    """
    Attributes:
        offer_id (Union[Unset, int]): Identifier of the offer to pick
        quantity (Union[Unset, int]): Quantity of offers to pick
    """

    offer_id: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_id = self.offer_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offer_id = d.pop("offer_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        pl11_response_200_data_picklist_lines = cls(
            offer_id=offer_id,
            quantity=quantity,
        )

        pl11_response_200_data_picklist_lines.additional_properties = d
        return pl11_response_200_data_picklist_lines

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
