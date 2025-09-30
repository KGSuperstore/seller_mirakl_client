from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR23Request")


@_attrs_define
class OR23Request:
    """
    Attributes:
        carrier_code (Union[Unset, str]): The code of a carrier. This information is mandatory for a registered carrier.
        carrier_name (Union[Unset, str]): The name of a carrier. This information is mandatory for an unregistered
            carrier.
        carrier_standard_code (Union[Unset, str]): Carrier standard code
        carrier_url (Union[Unset, str]): The tracking url of a carrier. This information is unused for registered
            carriers (because computed automatically). This information is optional for unregistered carriers.
        tracking_number (Union[Unset, str]): The carrier tracking number. This information is mandatory for a registered
            carrier with a URL requiring a tracking number.
    """

    carrier_code: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    carrier_standard_code: Union[Unset, str] = UNSET
    carrier_url: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_code = self.carrier_code

        carrier_name = self.carrier_name

        carrier_standard_code = self.carrier_standard_code

        carrier_url = self.carrier_url

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_code is not UNSET:
            field_dict["carrier_code"] = carrier_code
        if carrier_name is not UNSET:
            field_dict["carrier_name"] = carrier_name
        if carrier_standard_code is not UNSET:
            field_dict["carrier_standard_code"] = carrier_standard_code
        if carrier_url is not UNSET:
            field_dict["carrier_url"] = carrier_url
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier_code = d.pop("carrier_code", UNSET)

        carrier_name = d.pop("carrier_name", UNSET)

        carrier_standard_code = d.pop("carrier_standard_code", UNSET)

        carrier_url = d.pop("carrier_url", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        or23_request = cls(
            carrier_code=carrier_code,
            carrier_name=carrier_name,
            carrier_standard_code=carrier_standard_code,
            carrier_url=carrier_url,
            tracking_number=tracking_number,
        )

        or23_request.additional_properties = d
        return or23_request

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
