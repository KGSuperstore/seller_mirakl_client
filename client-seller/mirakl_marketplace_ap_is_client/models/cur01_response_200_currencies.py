from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CUR01Response200Currencies")


@_attrs_define
class CUR01Response200Currencies:
    """
    Attributes:
        code (Union[Unset, str]): Currency code
        label (Union[Unset, str]): Currency label
        platform_default (Union[Unset, bool]): Default currency of the platform
    """

    code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    platform_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        platform_default = self.platform_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if platform_default is not UNSET:
            field_dict["platform_default"] = platform_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        platform_default = d.pop("platform_default", UNSET)

        cur01_response_200_currencies = cls(
            code=code,
            label=label,
            platform_default=platform_default,
        )

        cur01_response_200_currencies.additional_properties = d
        return cur01_response_200_currencies

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
