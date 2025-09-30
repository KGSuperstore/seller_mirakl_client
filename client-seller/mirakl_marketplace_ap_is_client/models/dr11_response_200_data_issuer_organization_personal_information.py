from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR11Response200DataIssuerOrganizationPersonalInformation")


@_attrs_define
class DR11Response200DataIssuerOrganizationPersonalInformation:
    """
    Attributes:
        civility (Union[Unset, str]): The civility of the shop owner
        first_name (Union[Unset, str]): The first name of the shop owner
        last_name (Union[Unset, str]): The last name of the shop owner.
    """

    civility: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        civility = self.civility

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if civility is not UNSET:
            field_dict["civility"] = civility
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        civility = d.pop("civility", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        dr11_response_200_data_issuer_organization_personal_information = cls(
            civility=civility,
            first_name=first_name,
            last_name=last_name,
        )

        dr11_response_200_data_issuer_organization_personal_information.additional_properties = d
        return dr11_response_200_data_issuer_organization_personal_information

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
