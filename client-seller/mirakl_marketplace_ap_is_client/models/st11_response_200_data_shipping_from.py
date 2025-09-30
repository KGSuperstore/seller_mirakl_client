from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st11_response_200_data_shipping_from_address import ST11Response200DataShippingFromAddress
    from ..models.st11_response_200_data_shipping_from_warehouse import ST11Response200DataShippingFromWarehouse


T = TypeVar("T", bound="ST11Response200DataShippingFrom")


@_attrs_define
class ST11Response200DataShippingFrom:
    """
    Attributes:
        address (Union[Unset, ST11Response200DataShippingFromAddress]):
        warehouse (Union[Unset, ST11Response200DataShippingFromWarehouse]):
    """

    address: Union[Unset, "ST11Response200DataShippingFromAddress"] = UNSET
    warehouse: Union[Unset, "ST11Response200DataShippingFromWarehouse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        warehouse: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st11_response_200_data_shipping_from_address import ST11Response200DataShippingFromAddress
        from ..models.st11_response_200_data_shipping_from_warehouse import ST11Response200DataShippingFromWarehouse

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, ST11Response200DataShippingFromAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = ST11Response200DataShippingFromAddress.from_dict(_address)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, ST11Response200DataShippingFromWarehouse]
        if isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = ST11Response200DataShippingFromWarehouse.from_dict(_warehouse)

        st11_response_200_data_shipping_from = cls(
            address=address,
            warehouse=warehouse,
        )

        st11_response_200_data_shipping_from.additional_properties = d
        return st11_response_200_data_shipping_from

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
