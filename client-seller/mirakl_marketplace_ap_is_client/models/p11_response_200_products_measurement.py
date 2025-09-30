from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="P11Response200ProductsMeasurement")


@_attrs_define
class P11Response200ProductsMeasurement:
    """
    Attributes:
        total_measurement_of_product (Union[Unset, float]): Product total measurement
        unit (Union[Unset, str]): Product measurement unit
    """

    total_measurement_of_product: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_measurement_of_product = self.total_measurement_of_product

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_measurement_of_product is not UNSET:
            field_dict["total_measurement_of_product"] = total_measurement_of_product
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_measurement_of_product = d.pop("total_measurement_of_product", UNSET)

        unit = d.pop("unit", UNSET)

        p11_response_200_products_measurement = cls(
            total_measurement_of_product=total_measurement_of_product,
            unit=unit,
        )

        p11_response_200_products_measurement.additional_properties = d
        return p11_response_200_products_measurement

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
