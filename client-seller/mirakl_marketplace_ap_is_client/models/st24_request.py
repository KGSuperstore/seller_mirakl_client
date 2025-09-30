from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st24_request_shipments import ST24RequestShipments


T = TypeVar("T", bound="ST24Request")


@_attrs_define
class ST24Request:
    """
    Attributes:
        shipments (Union[Unset, list['ST24RequestShipments']]): Shipment ids
    """

    shipments: Union[Unset, list["ST24RequestShipments"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipments, Unset):
            shipments = []
            for shipments_item_data in self.shipments:
                shipments_item = shipments_item_data.to_dict()
                shipments.append(shipments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipments is not UNSET:
            field_dict["shipments"] = shipments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st24_request_shipments import ST24RequestShipments

        d = dict(src_dict)
        shipments = []
        _shipments = d.pop("shipments", UNSET)
        for shipments_item_data in _shipments or []:
            shipments_item = ST24RequestShipments.from_dict(shipments_item_data)

            shipments.append(shipments_item)

        st24_request = cls(
            shipments=shipments,
        )

        st24_request.additional_properties = d
        return st24_request

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
