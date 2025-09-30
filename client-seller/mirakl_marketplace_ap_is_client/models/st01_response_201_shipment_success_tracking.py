from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st01_response_201_shipment_success_tracking_last_known_location import (
        ST01Response201ShipmentSuccessTrackingLastKnownLocation,
    )
    from ..models.st01_response_201_shipment_success_tracking_milestones import (
        ST01Response201ShipmentSuccessTrackingMilestones,
    )


T = TypeVar("T", bound="ST01Response201ShipmentSuccessTracking")


@_attrs_define
class ST01Response201ShipmentSuccessTracking:
    """
    Attributes:
        carrier_code (Union[Unset, str]): The code of a carrier. This information is mandatory for a registered carrier.
        carrier_name (Union[Unset, str]): The name of a carrier. This information is mandatory for an unregistered
            carrier.
        carrier_standard_code (Union[Unset, str]): The standard code of a carrier based on mirakl carrier referential
        last_known_location (Union[Unset, ST01Response201ShipmentSuccessTrackingLastKnownLocation]):
        milestones (Union[Unset, list['ST01Response201ShipmentSuccessTrackingMilestones']]): Retrieves the main stages
            of the delivery of a shipment coming from carrier's systems
        tracking_number (Union[Unset, str]): The carrier tracking number. This information is mandatory for a registered
            carrier with a URL requiring a tracking number.
        tracking_url (Union[Unset, str]): The tracking url of a carrier. This information is unused for registered
            carriers (because computed automatically). This information is optional for unregistered carriers.
        validity_status (Union[Unset, str]): Retrieves if mirakl is able to get tracking information (if not, then
            unverified) and if we manage to get tracking information and if we do get tracking information on this tracking,
            then it moves to verified, if we don't it remains in unverified
    """

    carrier_code: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    carrier_standard_code: Union[Unset, str] = UNSET
    last_known_location: Union[Unset, "ST01Response201ShipmentSuccessTrackingLastKnownLocation"] = UNSET
    milestones: Union[Unset, list["ST01Response201ShipmentSuccessTrackingMilestones"]] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    validity_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_code = self.carrier_code

        carrier_name = self.carrier_name

        carrier_standard_code = self.carrier_standard_code

        last_known_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_known_location, Unset):
            last_known_location = self.last_known_location.to_dict()

        milestones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = []
            for milestones_item_data in self.milestones:
                milestones_item = milestones_item_data.to_dict()
                milestones.append(milestones_item)

        tracking_number = self.tracking_number

        tracking_url = self.tracking_url

        validity_status = self.validity_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_code is not UNSET:
            field_dict["carrier_code"] = carrier_code
        if carrier_name is not UNSET:
            field_dict["carrier_name"] = carrier_name
        if carrier_standard_code is not UNSET:
            field_dict["carrier_standard_code"] = carrier_standard_code
        if last_known_location is not UNSET:
            field_dict["last_known_location"] = last_known_location
        if milestones is not UNSET:
            field_dict["milestones"] = milestones
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if tracking_url is not UNSET:
            field_dict["tracking_url"] = tracking_url
        if validity_status is not UNSET:
            field_dict["validity_status"] = validity_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st01_response_201_shipment_success_tracking_last_known_location import (
            ST01Response201ShipmentSuccessTrackingLastKnownLocation,
        )
        from ..models.st01_response_201_shipment_success_tracking_milestones import (
            ST01Response201ShipmentSuccessTrackingMilestones,
        )

        d = dict(src_dict)
        carrier_code = d.pop("carrier_code", UNSET)

        carrier_name = d.pop("carrier_name", UNSET)

        carrier_standard_code = d.pop("carrier_standard_code", UNSET)

        _last_known_location = d.pop("last_known_location", UNSET)
        last_known_location: Union[Unset, ST01Response201ShipmentSuccessTrackingLastKnownLocation]
        if isinstance(_last_known_location, Unset):
            last_known_location = UNSET
        else:
            last_known_location = ST01Response201ShipmentSuccessTrackingLastKnownLocation.from_dict(
                _last_known_location
            )

        milestones = []
        _milestones = d.pop("milestones", UNSET)
        for milestones_item_data in _milestones or []:
            milestones_item = ST01Response201ShipmentSuccessTrackingMilestones.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        tracking_number = d.pop("tracking_number", UNSET)

        tracking_url = d.pop("tracking_url", UNSET)

        validity_status = d.pop("validity_status", UNSET)

        st01_response_201_shipment_success_tracking = cls(
            carrier_code=carrier_code,
            carrier_name=carrier_name,
            carrier_standard_code=carrier_standard_code,
            last_known_location=last_known_location,
            milestones=milestones,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            validity_status=validity_status,
        )

        st01_response_201_shipment_success_tracking.additional_properties = d
        return st01_response_201_shipment_success_tracking

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
