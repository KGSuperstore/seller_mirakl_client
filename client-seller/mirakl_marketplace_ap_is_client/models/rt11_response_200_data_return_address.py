from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RT11Response200DataReturnAddress")


@_attrs_define
class RT11Response200DataReturnAddress:
    """
    Attributes:
        city (Union[Unset, str]): City
        country_iso_code (Union[Unset, str]): Country ISO code
        state (Union[Unset, str]): State
        street1 (Union[Unset, str]): First line of the return address
        street2 (Union[Unset, str]): Second line of the return address
        zip_code (Union[Unset, str]): Zip code
    """

    city: Union[Unset, str] = UNSET
    country_iso_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street1: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country_iso_code = self.country_iso_code

        state = self.state

        street1 = self.street1

        street2 = self.street2

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country_iso_code is not UNSET:
            field_dict["country_iso_code"] = country_iso_code
        if state is not UNSET:
            field_dict["state"] = state
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country_iso_code = d.pop("country_iso_code", UNSET)

        state = d.pop("state", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        rt11_response_200_data_return_address = cls(
            city=city,
            country_iso_code=country_iso_code,
            state=state,
            street1=street1,
            street2=street2,
            zip_code=zip_code,
        )

        rt11_response_200_data_return_address.additional_properties = d
        return rt11_response_200_data_return_address

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
