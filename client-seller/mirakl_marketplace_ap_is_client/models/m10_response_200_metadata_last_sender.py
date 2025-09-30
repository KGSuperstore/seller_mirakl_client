from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.m10_response_200_metadata_last_sender_organization_details import (
        M10Response200MetadataLastSenderOrganizationDetails,
    )


T = TypeVar("T", bound="M10Response200MetadataLastSender")


@_attrs_define
class M10Response200MetadataLastSender:
    """
    Attributes:
        display_name (Union[Unset, str]): Sender display name
        organization_details (Union[Unset, M10Response200MetadataLastSenderOrganizationDetails]):
        type_ (Union[Unset, str]): Sender type
    """

    display_name: Union[Unset, str] = UNSET
    organization_details: Union[Unset, "M10Response200MetadataLastSenderOrganizationDetails"] = UNSET
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
        from ..models.m10_response_200_metadata_last_sender_organization_details import (
            M10Response200MetadataLastSenderOrganizationDetails,
        )

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        _organization_details = d.pop("organization_details", UNSET)
        organization_details: Union[Unset, M10Response200MetadataLastSenderOrganizationDetails]
        if isinstance(_organization_details, Unset):
            organization_details = UNSET
        else:
            organization_details = M10Response200MetadataLastSenderOrganizationDetails.from_dict(_organization_details)

        type_ = d.pop("type", UNSET)

        m10_response_200_metadata_last_sender = cls(
            display_name=display_name,
            organization_details=organization_details,
            type_=type_,
        )

        m10_response_200_metadata_last_sender.additional_properties = d
        return m10_response_200_metadata_last_sender

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
