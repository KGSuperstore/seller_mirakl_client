from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders import OR04Response200UpdatedOrders


T = TypeVar("T", bound="OR04Response200")


@_attrs_define
class OR04Response200:
    """
    Attributes:
        updated_orders (Union[Unset, list['OR04Response200UpdatedOrders']]): A list of updated orders and orders in
            error objects
    """

    updated_orders: Union[Unset, list["OR04Response200UpdatedOrders"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_orders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.updated_orders, Unset):
            updated_orders = []
            for updated_orders_item_data in self.updated_orders:
                updated_orders_item = updated_orders_item_data.to_dict()
                updated_orders.append(updated_orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_orders is not UNSET:
            field_dict["updated_orders"] = updated_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders import OR04Response200UpdatedOrders

        d = dict(src_dict)
        updated_orders = []
        _updated_orders = d.pop("updated_orders", UNSET)
        for updated_orders_item_data in _updated_orders or []:
            updated_orders_item = OR04Response200UpdatedOrders.from_dict(updated_orders_item_data)

            updated_orders.append(updated_orders_item)

        or04_response_200 = cls(
            updated_orders=updated_orders,
        )

        or04_response_200.additional_properties = d
        return or04_response_200

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
