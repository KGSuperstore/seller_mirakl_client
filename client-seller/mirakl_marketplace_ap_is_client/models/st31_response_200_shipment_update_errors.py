from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st31_response_200_shipment_update_errors_errors import ST31Response200ShipmentUpdateErrorsErrors


T = TypeVar("T", bound="ST31Response200ShipmentUpdateErrors")


@_attrs_define
class ST31Response200ShipmentUpdateErrors:
    """
    Attributes:
        errors (Union[Unset, list['ST31Response200ShipmentUpdateErrorsErrors']]): List of errors
        shipment_id (Union[Unset, str]): Shipment id
    """

    errors: Union[Unset, list["ST31Response200ShipmentUpdateErrorsErrors"]] = UNSET
    shipment_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        shipment_id = self.shipment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if shipment_id is not UNSET:
            field_dict["shipment_id"] = shipment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st31_response_200_shipment_update_errors_errors import ST31Response200ShipmentUpdateErrorsErrors

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ST31Response200ShipmentUpdateErrorsErrors.from_dict(errors_item_data)

            errors.append(errors_item)

        shipment_id = d.pop("shipment_id", UNSET)

        st31_response_200_shipment_update_errors = cls(
            errors=errors,
            shipment_id=shipment_id,
        )

        st31_response_200_shipment_update_errors.additional_properties = d
        return st31_response_200_shipment_update_errors

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
