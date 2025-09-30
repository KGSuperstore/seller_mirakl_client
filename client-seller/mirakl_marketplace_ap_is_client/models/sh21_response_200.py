from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sh21_response_200_carriers import SH21Response200Carriers


T = TypeVar("T", bound="SH21Response200")


@_attrs_define
class SH21Response200:
    """
    Attributes:
        carriers (Union[Unset, list['SH21Response200Carriers']]): List of carriers
    """

    carriers: Union[Unset, list["SH21Response200Carriers"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carriers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.carriers, Unset):
            carriers = []
            for carriers_item_data in self.carriers:
                carriers_item = carriers_item_data.to_dict()
                carriers.append(carriers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carriers is not UNSET:
            field_dict["carriers"] = carriers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sh21_response_200_carriers import SH21Response200Carriers

        d = dict(src_dict)
        carriers = []
        _carriers = d.pop("carriers", UNSET)
        for carriers_item_data in _carriers or []:
            carriers_item = SH21Response200Carriers.from_dict(carriers_item_data)

            carriers.append(carriers_item)

        sh21_response_200 = cls(
            carriers=carriers,
        )

        sh21_response_200.additional_properties = d
        return sh21_response_200

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
