from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st01_request_shipments_shipping_from_warehouse import ST01RequestShipmentsShippingFromWarehouse


T = TypeVar("T", bound="ST01RequestShipmentsShippingFrom")


@_attrs_define
class ST01RequestShipmentsShippingFrom:
    """Shipment's shipping origin

    Attributes:
        warehouse (Union[Unset, ST01RequestShipmentsShippingFromWarehouse]): The warehouse from where the shipment is
            shipped
    """

    warehouse: Union[Unset, "ST01RequestShipmentsShippingFromWarehouse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.warehouse, Unset):
            warehouse = self.warehouse.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st01_request_shipments_shipping_from_warehouse import ST01RequestShipmentsShippingFromWarehouse

        d = dict(src_dict)
        _warehouse = d.pop("warehouse", UNSET)
        warehouse: Union[Unset, ST01RequestShipmentsShippingFromWarehouse]
        if isinstance(_warehouse, Unset):
            warehouse = UNSET
        else:
            warehouse = ST01RequestShipmentsShippingFromWarehouse.from_dict(_warehouse)

        st01_request_shipments_shipping_from = cls(
            warehouse=warehouse,
        )

        st01_request_shipments_shipping_from.additional_properties = d
        return st01_request_shipments_shipping_from

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
