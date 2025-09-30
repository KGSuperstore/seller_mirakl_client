from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_response_200_cancelations_amount_breakdown_parts import (
        OR30Response200CancelationsAmountBreakdownParts,
    )


T = TypeVar("T", bound="OR30Response200CancelationsAmountBreakdown")


@_attrs_define
class OR30Response200CancelationsAmountBreakdown:
    """
    Attributes:
        parts (Union[Unset, list['OR30Response200CancelationsAmountBreakdownParts']]): The parts which constitute the
            total amount. <br/>Each part can have different invoicing rules. The sum of the amount of each part is equal to
            the total amount. Multiple parts can be returned in tax mode TAX_INCLUDED.
    """

    parts: Union[Unset, list["OR30Response200CancelationsAmountBreakdownParts"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or30_response_200_cancelations_amount_breakdown_parts import (
            OR30Response200CancelationsAmountBreakdownParts,
        )

        d = dict(src_dict)
        parts = []
        _parts = d.pop("parts", UNSET)
        for parts_item_data in _parts or []:
            parts_item = OR30Response200CancelationsAmountBreakdownParts.from_dict(parts_item_data)

            parts.append(parts_item)

        or30_response_200_cancelations_amount_breakdown = cls(
            parts=parts,
        )

        or30_response_200_cancelations_amount_breakdown.additional_properties = d
        return or30_response_200_cancelations_amount_breakdown

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
