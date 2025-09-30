from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SH12Response200ShippingTypes")


@_attrs_define
class SH12Response200ShippingTypes:
    """
    Attributes:
        click_and_collect (Union[Unset, bool]): Shipping type corresponds to “click&collect”
        code (Union[Unset, str]): Shipping type code
        delivery_by_operator (Union[Unset, bool]): Shipping type is managed by operator on behalf of shops
        description (Union[Unset, str]): Shipping type description
        label (Union[Unset, str]): Shipping type label
        mandatory_tracking (Union[Unset, bool]): Shops must provide tracking details before confirming shipment for a
            given shipping type
        standard_code (Union[Unset, str]): Shipping type standard code
    """

    click_and_collect: Union[Unset, bool] = UNSET
    code: Union[Unset, str] = UNSET
    delivery_by_operator: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    mandatory_tracking: Union[Unset, bool] = UNSET
    standard_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        click_and_collect = self.click_and_collect

        code = self.code

        delivery_by_operator = self.delivery_by_operator

        description = self.description

        label = self.label

        mandatory_tracking = self.mandatory_tracking

        standard_code = self.standard_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if click_and_collect is not UNSET:
            field_dict["click_and_collect"] = click_and_collect
        if code is not UNSET:
            field_dict["code"] = code
        if delivery_by_operator is not UNSET:
            field_dict["delivery_by_operator"] = delivery_by_operator
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if mandatory_tracking is not UNSET:
            field_dict["mandatory_tracking"] = mandatory_tracking
        if standard_code is not UNSET:
            field_dict["standard_code"] = standard_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        click_and_collect = d.pop("click_and_collect", UNSET)

        code = d.pop("code", UNSET)

        delivery_by_operator = d.pop("delivery_by_operator", UNSET)

        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        mandatory_tracking = d.pop("mandatory_tracking", UNSET)

        standard_code = d.pop("standard_code", UNSET)

        sh12_response_200_shipping_types = cls(
            click_and_collect=click_and_collect,
            code=code,
            delivery_by_operator=delivery_by_operator,
            description=description,
            label=label,
            mandatory_tracking=mandatory_tracking,
            standard_code=standard_code,
        )

        sh12_response_200_shipping_types.additional_properties = d
        return sh12_response_200_shipping_types

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
