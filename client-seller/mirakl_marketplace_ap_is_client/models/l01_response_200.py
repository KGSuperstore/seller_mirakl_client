from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.l01_response_200_locales import L01Response200Locales


T = TypeVar("T", bound="L01Response200")


@_attrs_define
class L01Response200:
    """
    Attributes:
        locales (Union[Unset, list['L01Response200Locales']]): List of locales
    """

    locales: Union[Unset, list["L01Response200Locales"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locales: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locales, Unset):
            locales = []
            for locales_item_data in self.locales:
                locales_item = locales_item_data.to_dict()
                locales.append(locales_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locales is not UNSET:
            field_dict["locales"] = locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.l01_response_200_locales import L01Response200Locales

        d = dict(src_dict)
        locales = []
        _locales = d.pop("locales", UNSET)
        for locales_item_data in _locales or []:
            locales_item = L01Response200Locales.from_dict(locales_item_data)

            locales.append(locales_item)

        l01_response_200 = cls(
            locales=locales,
        )

        l01_response_200.additional_properties = d
        return l01_response_200

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
