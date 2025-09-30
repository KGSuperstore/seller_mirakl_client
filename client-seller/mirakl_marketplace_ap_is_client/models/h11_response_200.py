from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.h11_response_200_hierarchies import H11Response200Hierarchies


T = TypeVar("T", bound="H11Response200")


@_attrs_define
class H11Response200:
    """
    Attributes:
        hierarchies (Union[Unset, list['H11Response200Hierarchies']]): List of hierarchies
    """

    hierarchies: Union[Unset, list["H11Response200Hierarchies"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hierarchies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hierarchies, Unset):
            hierarchies = []
            for hierarchies_item_data in self.hierarchies:
                hierarchies_item = hierarchies_item_data.to_dict()
                hierarchies.append(hierarchies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hierarchies is not UNSET:
            field_dict["hierarchies"] = hierarchies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.h11_response_200_hierarchies import H11Response200Hierarchies

        d = dict(src_dict)
        hierarchies = []
        _hierarchies = d.pop("hierarchies", UNSET)
        for hierarchies_item_data in _hierarchies or []:
            hierarchies_item = H11Response200Hierarchies.from_dict(hierarchies_item_data)

            hierarchies.append(hierarchies_item)

        h11_response_200 = cls(
            hierarchies=hierarchies,
        )

        h11_response_200.additional_properties = d
        return h11_response_200

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
