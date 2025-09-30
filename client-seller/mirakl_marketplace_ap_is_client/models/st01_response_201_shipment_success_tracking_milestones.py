from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st01_response_201_shipment_success_tracking_milestones_additional_info import (
        ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo,
    )
    from ..models.st01_response_201_shipment_success_tracking_milestones_occurrence_date import (
        ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate,
    )


T = TypeVar("T", bound="ST01Response201ShipmentSuccessTrackingMilestones")


@_attrs_define
class ST01Response201ShipmentSuccessTrackingMilestones:
    """
    Attributes:
        additional_info (Union[Unset, ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo]):
        occurrence_date (Union[Unset, ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate]):
        type_ (Union[Unset, str]): Type of milestone
    """

    additional_info: Union[Unset, "ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo"] = UNSET
    occurrence_date: Union[Unset, "ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        occurrence_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.occurrence_date, Unset):
            occurrence_date = self.occurrence_date.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_info is not UNSET:
            field_dict["additional_info"] = additional_info
        if occurrence_date is not UNSET:
            field_dict["occurrence_date"] = occurrence_date
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st01_response_201_shipment_success_tracking_milestones_additional_info import (
            ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo,
        )
        from ..models.st01_response_201_shipment_success_tracking_milestones_occurrence_date import (
            ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate,
        )

        d = dict(src_dict)
        _additional_info = d.pop("additional_info", UNSET)
        additional_info: Union[Unset, ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo]
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo.from_dict(_additional_info)

        _occurrence_date = d.pop("occurrence_date", UNSET)
        occurrence_date: Union[Unset, ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate]
        if isinstance(_occurrence_date, Unset):
            occurrence_date = UNSET
        else:
            occurrence_date = ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate.from_dict(_occurrence_date)

        type_ = d.pop("type", UNSET)

        st01_response_201_shipment_success_tracking_milestones = cls(
            additional_info=additional_info,
            occurrence_date=occurrence_date,
            type_=type_,
        )

        st01_response_201_shipment_success_tracking_milestones.additional_properties = d
        return st01_response_201_shipment_success_tracking_milestones

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
