from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_customer_accounting_contact import (
        OR11Response200OrdersCustomerAccountingContact,
    )
    from ..models.or11_response_200_orders_customer_billing_address import OR11Response200OrdersCustomerBillingAddress
    from ..models.or11_response_200_orders_customer_delivery_contact import OR11Response200OrdersCustomerDeliveryContact
    from ..models.or11_response_200_orders_customer_organization import OR11Response200OrdersCustomerOrganization
    from ..models.or11_response_200_orders_customer_shipping_address import OR11Response200OrdersCustomerShippingAddress


T = TypeVar("T", bound="OR11Response200OrdersCustomer")


@_attrs_define
class OR11Response200OrdersCustomer:
    """
    Attributes:
        accounting_contact (Union[Unset, OR11Response200OrdersCustomerAccountingContact]):
        billing_address (Union[Unset, OR11Response200OrdersCustomerBillingAddress]):
        civility (Union[Unset, str]): Customer's civility
        customer_id (Union[Unset, str]): Customer's identifier
        delivery_contact (Union[Unset, OR11Response200OrdersCustomerDeliveryContact]):
        firstname (Union[Unset, str]): Customer's first name
        lastname (Union[Unset, str]): Customer's last name
        locale (Union[Unset, str]): Customer's locale
        organization (Union[Unset, OR11Response200OrdersCustomerOrganization]):
        shipping_address (Union[Unset, OR11Response200OrdersCustomerShippingAddress]):
    """

    accounting_contact: Union[Unset, "OR11Response200OrdersCustomerAccountingContact"] = UNSET
    billing_address: Union[Unset, "OR11Response200OrdersCustomerBillingAddress"] = UNSET
    civility: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    delivery_contact: Union[Unset, "OR11Response200OrdersCustomerDeliveryContact"] = UNSET
    firstname: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    organization: Union[Unset, "OR11Response200OrdersCustomerOrganization"] = UNSET
    shipping_address: Union[Unset, "OR11Response200OrdersCustomerShippingAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accounting_contact, Unset):
            accounting_contact = self.accounting_contact.to_dict()

        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        civility = self.civility

        customer_id = self.customer_id

        delivery_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.delivery_contact, Unset):
            delivery_contact = self.delivery_contact.to_dict()

        firstname = self.firstname

        lastname = self.lastname

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
        if accounting_contact is not UNSET:
            field_dict["accounting_contact"] = accounting_contact
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if civility is not UNSET:
            field_dict["civility"] = civility
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if delivery_contact is not UNSET:
            field_dict["delivery_contact"] = delivery_contact
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if locale is not UNSET:
            field_dict["locale"] = locale
        if organization is not UNSET:
            field_dict["organization"] = organization
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_customer_accounting_contact import (
            OR11Response200OrdersCustomerAccountingContact,
        )
        from ..models.or11_response_200_orders_customer_billing_address import (
            OR11Response200OrdersCustomerBillingAddress,
        )
        from ..models.or11_response_200_orders_customer_delivery_contact import (
            OR11Response200OrdersCustomerDeliveryContact,
        )
        from ..models.or11_response_200_orders_customer_organization import OR11Response200OrdersCustomerOrganization
        from ..models.or11_response_200_orders_customer_shipping_address import (
            OR11Response200OrdersCustomerShippingAddress,
        )

        d = dict(src_dict)
        _accounting_contact = d.pop("accounting_contact", UNSET)
        accounting_contact: Union[Unset, OR11Response200OrdersCustomerAccountingContact]
        if isinstance(_accounting_contact, Unset):
            accounting_contact = UNSET
        else:
            accounting_contact = OR11Response200OrdersCustomerAccountingContact.from_dict(_accounting_contact)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, OR11Response200OrdersCustomerBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = OR11Response200OrdersCustomerBillingAddress.from_dict(_billing_address)

        civility = d.pop("civility", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        _delivery_contact = d.pop("delivery_contact", UNSET)
        delivery_contact: Union[Unset, OR11Response200OrdersCustomerDeliveryContact]
        if isinstance(_delivery_contact, Unset):
            delivery_contact = UNSET
        else:
            delivery_contact = OR11Response200OrdersCustomerDeliveryContact.from_dict(_delivery_contact)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        locale = d.pop("locale", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, OR11Response200OrdersCustomerOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = OR11Response200OrdersCustomerOrganization.from_dict(_organization)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, OR11Response200OrdersCustomerShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = OR11Response200OrdersCustomerShippingAddress.from_dict(_shipping_address)

        or11_response_200_orders_customer = cls(
            accounting_contact=accounting_contact,
            billing_address=billing_address,
            civility=civility,
            customer_id=customer_id,
            delivery_contact=delivery_contact,
            firstname=firstname,
            lastname=lastname,
            locale=locale,
            organization=organization,
            shipping_address=shipping_address,
        )

        or11_response_200_orders_customer.additional_properties = d
        return or11_response_200_orders_customer

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
