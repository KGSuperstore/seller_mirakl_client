from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesPricing")


@_attrs_define
class PC01Response200FeaturesPricing:
    """
    Attributes:
        channel_pricing (Union[Unset, str]): Allows sellers to create prices applicable on the operator’s different
            storefronts materialized as sales channels in Mirakl. DISABLED: No channel pricing. SINGLE: Allows sellers to
            create one price per channel. MULTI: Allows sellers to create multiple prices per channel.
        scheduled_pricing (Union[Unset, bool]): Allows sellers to set up multiple prices in advance
        volume_discount (Union[Unset, bool]): Allows discounts for bulk purchases
        volume_pricing (Union[Unset, bool]): Allows pricing for bulk purchases
    """

    channel_pricing: Union[Unset, str] = UNSET
    scheduled_pricing: Union[Unset, bool] = UNSET
    volume_discount: Union[Unset, bool] = UNSET
    volume_pricing: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_pricing = self.channel_pricing

        scheduled_pricing = self.scheduled_pricing

        volume_discount = self.volume_discount

        volume_pricing = self.volume_pricing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_pricing is not UNSET:
            field_dict["channel_pricing"] = channel_pricing
        if scheduled_pricing is not UNSET:
            field_dict["scheduled_pricing"] = scheduled_pricing
        if volume_discount is not UNSET:
            field_dict["volume_discount"] = volume_discount
        if volume_pricing is not UNSET:
            field_dict["volume_pricing"] = volume_pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_pricing = d.pop("channel_pricing", UNSET)

        scheduled_pricing = d.pop("scheduled_pricing", UNSET)

        volume_discount = d.pop("volume_discount", UNSET)

        volume_pricing = d.pop("volume_pricing", UNSET)

        pc01_response_200_features_pricing = cls(
            channel_pricing=channel_pricing,
            scheduled_pricing=scheduled_pricing,
            volume_discount=volume_discount,
            volume_pricing=volume_pricing,
        )

        pc01_response_200_features_pricing.additional_properties = d
        return pc01_response_200_features_pricing

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
