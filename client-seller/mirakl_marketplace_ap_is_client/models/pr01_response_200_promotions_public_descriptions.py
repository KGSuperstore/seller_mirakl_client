from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PR01Response200PromotionsPublicDescriptions")


@_attrs_define
class PR01Response200PromotionsPublicDescriptions:
    """
    Attributes:
        locale (Union[Unset, str]): Description's locale
        value (Union[Unset, str]): The description itself
    """

    locale: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        value = d.pop("value", UNSET)

        pr01_response_200_promotions_public_descriptions = cls(
            locale=locale,
            value=value,
        )

        pr01_response_200_promotions_public_descriptions.additional_properties = d
        return pr01_response_200_promotions_public_descriptions

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
