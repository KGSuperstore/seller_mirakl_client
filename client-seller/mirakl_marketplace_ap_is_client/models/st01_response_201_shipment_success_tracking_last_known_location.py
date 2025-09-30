from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st01_response_201_shipment_success_tracking_last_known_location_occurrence_date import (
        ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate,
    )


T = TypeVar("T", bound="ST01Response201ShipmentSuccessTrackingLastKnownLocation")


@_attrs_define
class ST01Response201ShipmentSuccessTrackingLastKnownLocation:
    """
    Attributes:
        location (Union[Unset, str]): Last known location of the shipment
        occurrence_date (Union[Unset, ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate]):
    """

    location: Union[Unset, str] = UNSET
    occurrence_date: Union[Unset, "ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        occurrence_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.occurrence_date, Unset):
            occurrence_date = self.occurrence_date.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if occurrence_date is not UNSET:
            field_dict["occurrence_date"] = occurrence_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st01_response_201_shipment_success_tracking_last_known_location_occurrence_date import (
            ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate,
        )

        d = dict(src_dict)
        location = d.pop("location", UNSET)

        _occurrence_date = d.pop("occurrence_date", UNSET)
        occurrence_date: Union[Unset, ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate]
        if isinstance(_occurrence_date, Unset):
            occurrence_date = UNSET
        else:
            occurrence_date = ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate.from_dict(
                _occurrence_date
            )

        st01_response_201_shipment_success_tracking_last_known_location = cls(
            location=location,
            occurrence_date=occurrence_date,
        )

        st01_response_201_shipment_success_tracking_last_known_location.additional_properties = d
        return st01_response_201_shipment_success_tracking_last_known_location

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
