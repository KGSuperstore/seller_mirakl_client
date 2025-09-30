from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr12_response_200_data_shipping_to_address import DR12Response200DataShippingToAddress


T = TypeVar("T", bound="DR12Response200DataShippingTo")


@_attrs_define
class DR12Response200DataShippingTo:
    """
    Attributes:
        address (Union[Unset, DR12Response200DataShippingToAddress]):
    """

    address: Union[Unset, "DR12Response200DataShippingToAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr12_response_200_data_shipping_to_address import DR12Response200DataShippingToAddress

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, DR12Response200DataShippingToAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DR12Response200DataShippingToAddress.from_dict(_address)

        dr12_response_200_data_shipping_to = cls(
            address=address,
        )

        dr12_response_200_data_shipping_to.additional_properties = d
        return dr12_response_200_data_shipping_to

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
