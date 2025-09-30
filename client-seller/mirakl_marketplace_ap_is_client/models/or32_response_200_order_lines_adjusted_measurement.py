from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR32Response200OrderLinesAdjustedMeasurement")


@_attrs_define
class OR32Response200OrderLinesAdjustedMeasurement:
    """
    Attributes:
        actual_measurement (Union[Unset, float]): Actual measurement on the order line
        adjustment_limit (Union[Unset, float]): Adjustment limit of the order line
        measurement_unit (Union[Unset, str]): Measurement unit of the order line
        ordered_measurement (Union[Unset, float]): Total measurement ordered on the order line
    """

    actual_measurement: Union[Unset, float] = UNSET
    adjustment_limit: Union[Unset, float] = UNSET
    measurement_unit: Union[Unset, str] = UNSET
    ordered_measurement: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_measurement = self.actual_measurement

        adjustment_limit = self.adjustment_limit

        measurement_unit = self.measurement_unit

        ordered_measurement = self.ordered_measurement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_measurement is not UNSET:
            field_dict["actual_measurement"] = actual_measurement
        if adjustment_limit is not UNSET:
            field_dict["adjustment_limit"] = adjustment_limit
        if measurement_unit is not UNSET:
            field_dict["measurement_unit"] = measurement_unit
        if ordered_measurement is not UNSET:
            field_dict["ordered_measurement"] = ordered_measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_measurement = d.pop("actual_measurement", UNSET)

        adjustment_limit = d.pop("adjustment_limit", UNSET)

        measurement_unit = d.pop("measurement_unit", UNSET)

        ordered_measurement = d.pop("ordered_measurement", UNSET)

        or32_response_200_order_lines_adjusted_measurement = cls(
            actual_measurement=actual_measurement,
            adjustment_limit=adjustment_limit,
            measurement_unit=measurement_unit,
            ordered_measurement=ordered_measurement,
        )

        or32_response_200_order_lines_adjusted_measurement.additional_properties = d
        return or32_response_200_order_lines_adjusted_measurement

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
