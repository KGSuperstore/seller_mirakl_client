from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or32_response_200_order_lines_adjusted_cancelations import (
        OR32Response200OrderLinesAdjustedCancelations,
    )
    from ..models.or32_response_200_order_lines_adjusted_errors import OR32Response200OrderLinesAdjustedErrors
    from ..models.or32_response_200_order_lines_adjusted_measurement import OR32Response200OrderLinesAdjustedMeasurement
    from ..models.or32_response_200_order_lines_adjusted_refunds import OR32Response200OrderLinesAdjustedRefunds


T = TypeVar("T", bound="OR32Response200OrderLinesAdjusted")


@_attrs_define
class OR32Response200OrderLinesAdjusted:
    """
    Attributes:
        cancelations (Union[Unset, list['OR32Response200OrderLinesAdjustedCancelations']]): List of representations of
            cancellations created by the adjustment
        errors (Union[Unset, list['OR32Response200OrderLinesAdjustedErrors']]): List of errors encountered when updating
            order line
        measurement (Union[Unset, OR32Response200OrderLinesAdjustedMeasurement]):
        order_line_id (Union[Unset, str]): Order line identifier
        refunds (Union[Unset, list['OR32Response200OrderLinesAdjustedRefunds']]): List of representations of refunds
            created by the adjustment
    """

    cancelations: Union[Unset, list["OR32Response200OrderLinesAdjustedCancelations"]] = UNSET
    errors: Union[Unset, list["OR32Response200OrderLinesAdjustedErrors"]] = UNSET
    measurement: Union[Unset, "OR32Response200OrderLinesAdjustedMeasurement"] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    refunds: Union[Unset, list["OR32Response200OrderLinesAdjustedRefunds"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cancelations, Unset):
            cancelations = []
            for cancelations_item_data in self.cancelations:
                cancelations_item = cancelations_item_data.to_dict()
                cancelations.append(cancelations_item)

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        measurement: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        order_line_id = self.order_line_id

        refunds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = []
            for refunds_item_data in self.refunds:
                refunds_item = refunds_item_data.to_dict()
                refunds.append(refunds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelations is not UNSET:
            field_dict["cancelations"] = cancelations
        if errors is not UNSET:
            field_dict["errors"] = errors
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if refunds is not UNSET:
            field_dict["refunds"] = refunds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or32_response_200_order_lines_adjusted_cancelations import (
            OR32Response200OrderLinesAdjustedCancelations,
        )
        from ..models.or32_response_200_order_lines_adjusted_errors import OR32Response200OrderLinesAdjustedErrors
        from ..models.or32_response_200_order_lines_adjusted_measurement import (
            OR32Response200OrderLinesAdjustedMeasurement,
        )
        from ..models.or32_response_200_order_lines_adjusted_refunds import OR32Response200OrderLinesAdjustedRefunds

        d = dict(src_dict)
        cancelations = []
        _cancelations = d.pop("cancelations", UNSET)
        for cancelations_item_data in _cancelations or []:
            cancelations_item = OR32Response200OrderLinesAdjustedCancelations.from_dict(cancelations_item_data)

            cancelations.append(cancelations_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = OR32Response200OrderLinesAdjustedErrors.from_dict(errors_item_data)

            errors.append(errors_item)

        _measurement = d.pop("measurement", UNSET)
        measurement: Union[Unset, OR32Response200OrderLinesAdjustedMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = OR32Response200OrderLinesAdjustedMeasurement.from_dict(_measurement)

        order_line_id = d.pop("order_line_id", UNSET)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = OR32Response200OrderLinesAdjustedRefunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        or32_response_200_order_lines_adjusted = cls(
            cancelations=cancelations,
            errors=errors,
            measurement=measurement,
            order_line_id=order_line_id,
            refunds=refunds,
        )

        or32_response_200_order_lines_adjusted.additional_properties = d
        return or32_response_200_order_lines_adjusted

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
