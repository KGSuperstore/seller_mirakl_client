from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_fulfillment_center import OR11Response200OrdersFulfillmentCenter


T = TypeVar("T", bound="OR11Response200OrdersFulfillment")


@_attrs_define
class OR11Response200OrdersFulfillment:
    """
    Attributes:
        center (Union[Unset, OR11Response200OrdersFulfillmentCenter]):
    """

    center: Union[Unset, "OR11Response200OrdersFulfillmentCenter"] = UNSET
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
        from ..models.or11_response_200_orders_fulfillment_center import OR11Response200OrdersFulfillmentCenter

        d = dict(src_dict)
        _center = d.pop("center", UNSET)
        center: Union[Unset, OR11Response200OrdersFulfillmentCenter]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = OR11Response200OrdersFulfillmentCenter.from_dict(_center)

        or11_response_200_orders_fulfillment = cls(
            center=center,
        )

        or11_response_200_orders_fulfillment.additional_properties = d
        return or11_response_200_orders_fulfillment

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
