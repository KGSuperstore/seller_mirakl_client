from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SH21Response200Carriers")


@_attrs_define
class SH21Response200Carriers:
    """
    Attributes:
        code (Union[Unset, str]): Carrier code
        label (Union[Unset, str]): Carrier label
        standard_code (Union[Unset, str]): Carrier standard code
        tracking_url (Union[Unset, str]): Carrier tracking URL
    """

    code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    standard_code: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        standard_code = self.standard_code

        tracking_url = self.tracking_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if standard_code is not UNSET:
            field_dict["standard_code"] = standard_code
        if tracking_url is not UNSET:
            field_dict["tracking_url"] = tracking_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        standard_code = d.pop("standard_code", UNSET)

        tracking_url = d.pop("tracking_url", UNSET)

        sh21_response_200_carriers = cls(
            code=code,
            label=label,
            standard_code=standard_code,
            tracking_url=tracking_url,
        )

        sh21_response_200_carriers.additional_properties = d
        return sh21_response_200_carriers

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
