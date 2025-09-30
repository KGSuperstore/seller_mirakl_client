from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_customer_organization_address import (
        OR11Response200OrdersCustomerOrganizationAddress,
    )


T = TypeVar("T", bound="OR11Response200OrdersCustomerOrganization")


@_attrs_define
class OR11Response200OrdersCustomerOrganization:
    """
    Attributes:
        address (Union[Unset, OR11Response200OrdersCustomerOrganizationAddress]):
        identification_number (Union[Unset, str]): Number used to identify the customer organization as an established
            business in a country. E.g: SIRET number in France, NIF in Spain. Required for new organizations.<br/>Null
            before shipping (or acceptance, depending on platform setting).
        name (Union[Unset, str]): Name of the organization. Required for new organizations.
        organization_id (Union[Unset, str]): Customer's organization id (from the operator's system).<br/>Null before
            shipping (or acceptance, depending on platform setting).
        tax_identification_number (Union[Unset, str]): Tax identification number of the organization.<br/>Null before
            shipping (or acceptance, depending on platform setting).
    """

    address: Union[Unset, "OR11Response200OrdersCustomerOrganizationAddress"] = UNSET
    identification_number: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    tax_identification_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        identification_number = self.identification_number

        name = self.name

        organization_id = self.organization_id

        tax_identification_number = self.tax_identification_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if identification_number is not UNSET:
            field_dict["identification_number"] = identification_number
        if name is not UNSET:
            field_dict["name"] = name
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_customer_organization_address import (
            OR11Response200OrdersCustomerOrganizationAddress,
        )

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, OR11Response200OrdersCustomerOrganizationAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = OR11Response200OrdersCustomerOrganizationAddress.from_dict(_address)

        identification_number = d.pop("identification_number", UNSET)

        name = d.pop("name", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        tax_identification_number = d.pop("tax_identification_number", UNSET)

        or11_response_200_orders_customer_organization = cls(
            address=address,
            identification_number=identification_number,
            name=name,
            organization_id=organization_id,
            tax_identification_number=tax_identification_number,
        )

        or11_response_200_orders_customer_organization.additional_properties = d
        return or11_response_200_orders_customer_organization

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
