from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersCustomerDeliveryContact")


@_attrs_define
class OR11Response200OrdersCustomerDeliveryContact:
    """
    Attributes:
        civility (Union[Unset, str]): Customer contact's civility
        customer_id (Union[Unset, str]): Customer contact's identifier
        firstname (Union[Unset, str]): Customer contact's firstname
        lastname (Union[Unset, str]): Customer contact's lastname
        locale (Union[Unset, str]): Customer contact's locale
    """

    civility: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        civility = self.civility

        customer_id = self.customer_id

        firstname = self.firstname

        lastname = self.lastname

        locale = self.locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if civility is not UNSET:
            field_dict["civility"] = civility
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        civility = d.pop("civility", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        locale = d.pop("locale", UNSET)

        or11_response_200_orders_customer_delivery_contact = cls(
            civility=civility,
            customer_id=customer_id,
            firstname=firstname,
            lastname=lastname,
            locale=locale,
        )

        or11_response_200_orders_customer_delivery_contact.additional_properties = d
        return or11_response_200_orders_customer_delivery_contact

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
