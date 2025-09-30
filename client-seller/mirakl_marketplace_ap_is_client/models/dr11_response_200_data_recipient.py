from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_recipient_billing_address import DR11Response200DataRecipientBillingAddress
    from ..models.dr11_response_200_data_recipient_organization import DR11Response200DataRecipientOrganization
    from ..models.dr11_response_200_data_recipient_shipping_address import DR11Response200DataRecipientShippingAddress


T = TypeVar("T", bound="DR11Response200DataRecipient")


@_attrs_define
class DR11Response200DataRecipient:
    """
    Attributes:
        billing_address (Union[Unset, DR11Response200DataRecipientBillingAddress]):
        id (Union[Unset, str]): The identifier of the recipient.<br/> In the case of a customer, this will be the
            customer identifier.<br/> In the case of a operator, this will be the operator 'billing information identifier'
        locale (Union[Unset, str]): The recipient locale
        organization (Union[Unset, DR11Response200DataRecipientOrganization]):
        shipping_address (Union[Unset, DR11Response200DataRecipientShippingAddress]):
    """

    billing_address: Union[Unset, "DR11Response200DataRecipientBillingAddress"] = UNSET
    id: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    organization: Union[Unset, "DR11Response200DataRecipientOrganization"] = UNSET
    shipping_address: Union[Unset, "DR11Response200DataRecipientShippingAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        id = self.id

        locale = self.locale

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        shipping_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if organization is not UNSET:
            field_dict["organization"] = organization
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_recipient_billing_address import DR11Response200DataRecipientBillingAddress
        from ..models.dr11_response_200_data_recipient_organization import DR11Response200DataRecipientOrganization
        from ..models.dr11_response_200_data_recipient_shipping_address import (
            DR11Response200DataRecipientShippingAddress,
        )

        d = dict(src_dict)
        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, DR11Response200DataRecipientBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = DR11Response200DataRecipientBillingAddress.from_dict(_billing_address)

        id = d.pop("id", UNSET)

        locale = d.pop("locale", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, DR11Response200DataRecipientOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = DR11Response200DataRecipientOrganization.from_dict(_organization)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, DR11Response200DataRecipientShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = DR11Response200DataRecipientShippingAddress.from_dict(_shipping_address)

        dr11_response_200_data_recipient = cls(
            billing_address=billing_address,
            id=id,
            locale=locale,
            organization=organization,
            shipping_address=shipping_address,
        )

        dr11_response_200_data_recipient.additional_properties = d
        return dr11_response_200_data_recipient

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
