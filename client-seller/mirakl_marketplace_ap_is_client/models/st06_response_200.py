from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st06_response_200_shipment_errors import ST06Response200ShipmentErrors
    from ..models.st06_response_200_shipment_success import ST06Response200ShipmentSuccess


T = TypeVar("T", bound="ST06Response200")


@_attrs_define
class ST06Response200:
    """
    Attributes:
        shipment_errors (Union[Unset, list['ST06Response200ShipmentErrors']]): Shipment workflow update errors
        shipment_success (Union[Unset, list['ST06Response200ShipmentSuccess']]): Shipment workflow update success
    """

    shipment_errors: Union[Unset, list["ST06Response200ShipmentErrors"]] = UNSET
    shipment_success: Union[Unset, list["ST06Response200ShipmentSuccess"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipment_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_errors, Unset):
            shipment_errors = []
            for shipment_errors_item_data in self.shipment_errors:
                shipment_errors_item = shipment_errors_item_data.to_dict()
                shipment_errors.append(shipment_errors_item)

        shipment_success: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_success, Unset):
            shipment_success = []
            for shipment_success_item_data in self.shipment_success:
                shipment_success_item = shipment_success_item_data.to_dict()
                shipment_success.append(shipment_success_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_errors is not UNSET:
            field_dict["shipment_errors"] = shipment_errors
        if shipment_success is not UNSET:
            field_dict["shipment_success"] = shipment_success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st06_response_200_shipment_errors import ST06Response200ShipmentErrors
        from ..models.st06_response_200_shipment_success import ST06Response200ShipmentSuccess

        d = dict(src_dict)
        shipment_errors = []
        _shipment_errors = d.pop("shipment_errors", UNSET)
        for shipment_errors_item_data in _shipment_errors or []:
            shipment_errors_item = ST06Response200ShipmentErrors.from_dict(shipment_errors_item_data)

            shipment_errors.append(shipment_errors_item)

        shipment_success = []
        _shipment_success = d.pop("shipment_success", UNSET)
        for shipment_success_item_data in _shipment_success or []:
            shipment_success_item = ST06Response200ShipmentSuccess.from_dict(shipment_success_item_data)

            shipment_success.append(shipment_success_item)

        st06_response_200 = cls(
            shipment_errors=shipment_errors,
            shipment_success=shipment_success,
        )

        st06_response_200.additional_properties = d
        return st06_response_200

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
