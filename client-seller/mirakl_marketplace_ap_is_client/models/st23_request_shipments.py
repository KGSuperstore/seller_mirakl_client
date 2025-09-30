from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st23_request_shipments_tracking import ST23RequestShipmentsTracking


T = TypeVar("T", bound="ST23RequestShipments")


@_attrs_define
class ST23RequestShipments:
    """Shipments list

    Attributes:
        id (Union[Unset, str]): Shipment id
        tracking (Union[Unset, ST23RequestShipmentsTracking]): Shipment tracking details
    """

    id: Union[Unset, str] = UNSET
    tracking: Union[Unset, "ST23RequestShipmentsTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st23_request_shipments_tracking import ST23RequestShipmentsTracking

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, ST23RequestShipmentsTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = ST23RequestShipmentsTracking.from_dict(_tracking)

        st23_request_shipments = cls(
            id=id,
            tracking=tracking,
        )

        st23_request_shipments.additional_properties = d
        return st23_request_shipments

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
