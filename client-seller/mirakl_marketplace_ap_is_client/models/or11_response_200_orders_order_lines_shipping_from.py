from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_shipping_from_address import (
        OR11Response200OrdersOrderLinesShippingFromAddress,
    )
    from ..models.or11_response_200_orders_order_lines_shipping_from_warehouse import (
        OR11Response200OrdersOrderLinesShippingFromWarehouse,
    )


T = TypeVar("T", bound="OR11Response200OrdersOrderLinesShippingFrom")


@_attrs_define
class OR11Response200OrdersOrderLinesShippingFrom:
    """
    Attributes:
        address (Union[Unset, OR11Response200OrdersOrderLinesShippingFromAddress]):
        warehouse (Union[Unset, OR11Response200OrdersOrderLinesShippingFromWarehouse]):
    """

    address: Union[Unset, "OR11Response200OrdersOrderLinesShippingFromAddress"] = UNSET
    warehouse: Union[Unset, "OR11Response200OrdersOrderLinesShippingFromWarehouse"] = UNSET
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
        from ..models.or11_response_200_orders_order_lines_shipping_from_address import (
            OR11Response200OrdersOrderLinesShippingFromAddress,
        )
        from ..models.or11_response_200_orders_order_lines_shipping_from_warehouse import (
            OR11Response200OrdersOrderLinesShippingFromWarehouse,
        )

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, OR11Response200OrdersOrderLinesShippingFromAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = OR11Response200OrdersOrderLinesShippingFromAddress.from_dict(_address)

        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, OR11Response200OrdersOrderLinesShippingFromWarehouse]
        if isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = OR11Response200OrdersOrderLinesShippingFromWarehouse.from_dict(_warehouse)

        or11_response_200_orders_order_lines_shipping_from = cls(
            address=address,
            warehouse=warehouse,
        )

        or11_response_200_orders_order_lines_shipping_from.additional_properties = d
        return or11_response_200_orders_order_lines_shipping_from

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
