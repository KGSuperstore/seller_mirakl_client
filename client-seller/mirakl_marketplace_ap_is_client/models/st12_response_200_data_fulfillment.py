from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st12_response_200_data_fulfillment_center import ST12Response200DataFulfillmentCenter


T = TypeVar("T", bound="ST12Response200DataFulfillment")


@_attrs_define
class ST12Response200DataFulfillment:
    """
    Attributes:
        center (Union[Unset, ST12Response200DataFulfillmentCenter]):
    """

    center: Union[Unset, "ST12Response200DataFulfillmentCenter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        center: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.center, Unset):
            center = self.center.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st12_response_200_data_fulfillment_center import ST12Response200DataFulfillmentCenter

        d = dict(src_dict)
        _center = d.pop("center", UNSET)
        center: Union[Unset, ST12Response200DataFulfillmentCenter]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = ST12Response200DataFulfillmentCenter.from_dict(_center)

        st12_response_200_data_fulfillment = cls(
            center=center,
        )

        st12_response_200_data_fulfillment.additional_properties = d
        return st12_response_200_data_fulfillment

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
