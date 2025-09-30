from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_issuer_organization import DR11Response200DataIssuerOrganization


T = TypeVar("T", bound="DR11Response200DataIssuer")


@_attrs_define
class DR11Response200DataIssuer:
    """
    Attributes:
        id (Union[Unset, str]): The identifier of the issuer. This will be the operator or seller 'billing information
            identifier'.
        organization (Union[Unset, DR11Response200DataIssuerOrganization]):
        type_ (Union[Unset, str]): The issuer type (operator or shop) of the document.
    """

    id: Union[Unset, str] = UNSET
    organization: Union[Unset, "DR11Response200DataIssuerOrganization"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_issuer_organization import DR11Response200DataIssuerOrganization

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, DR11Response200DataIssuerOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = DR11Response200DataIssuerOrganization.from_dict(_organization)

        type_ = d.pop("type", UNSET)

        dr11_response_200_data_issuer = cls(
            id=id,
            organization=organization,
            type_=type_,
        )

        dr11_response_200_data_issuer.additional_properties = d
        return dr11_response_200_data_issuer

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
