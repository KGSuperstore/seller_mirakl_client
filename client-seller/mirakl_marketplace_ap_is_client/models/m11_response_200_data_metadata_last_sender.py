from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.m11_response_200_data_metadata_last_sender_organization_details import (
        M11Response200DataMetadataLastSenderOrganizationDetails,
    )


T = TypeVar("T", bound="M11Response200DataMetadataLastSender")


@_attrs_define
class M11Response200DataMetadataLastSender:
    """
    Attributes:
        display_name (Union[Unset, str]): Sender display name
        organization_details (Union[Unset, M11Response200DataMetadataLastSenderOrganizationDetails]):
        type_ (Union[Unset, str]): Sender type
    """

    display_name: Union[Unset, str] = UNSET
    organization_details: Union[Unset, "M11Response200DataMetadataLastSenderOrganizationDetails"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        organization_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_details, Unset):
            organization_details = self.organization_details.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if organization_details is not UNSET:
            field_dict["organization_details"] = organization_details
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.m11_response_200_data_metadata_last_sender_organization_details import (
            M11Response200DataMetadataLastSenderOrganizationDetails,
        )

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        _organization_details = d.pop("organization_details", UNSET)
        organization_details: Union[Unset, M11Response200DataMetadataLastSenderOrganizationDetails]
        if isinstance(_organization_details, Unset):
            organization_details = UNSET
        else:
            organization_details = M11Response200DataMetadataLastSenderOrganizationDetails.from_dict(
                _organization_details
            )

        type_ = d.pop("type", UNSET)

        m11_response_200_data_metadata_last_sender = cls(
            display_name=display_name,
            organization_details=organization_details,
            type_=type_,
        )

        m11_response_200_data_metadata_last_sender.additional_properties = d
        return m11_response_200_data_metadata_last_sender

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
