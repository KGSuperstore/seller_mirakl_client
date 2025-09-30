from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vl11_response_200_values_lists import VL11Response200ValuesLists


T = TypeVar("T", bound="VL11Response200")


@_attrs_define
class VL11Response200:
    """
    Attributes:
        values_lists (Union[Unset, list['VL11Response200ValuesLists']]): List of values list
    """

    values_lists: Union[Unset, list["VL11Response200ValuesLists"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values_lists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values_lists, Unset):
            values_lists = []
            for values_lists_item_data in self.values_lists:
                values_lists_item = values_lists_item_data.to_dict()
                values_lists.append(values_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values_lists is not UNSET:
            field_dict["values_lists"] = values_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vl11_response_200_values_lists import VL11Response200ValuesLists

        d = dict(src_dict)
        values_lists = []
        _values_lists = d.pop("values_lists", UNSET)
        for values_lists_item_data in _values_lists or []:
            values_lists_item = VL11Response200ValuesLists.from_dict(values_lists_item_data)

            values_lists.append(values_lists_item)

        vl11_response_200 = cls(
            values_lists=values_lists,
        )

        vl11_response_200.additional_properties = d
        return vl11_response_200

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
