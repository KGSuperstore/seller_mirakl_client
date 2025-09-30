from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR32Response200OrderLinesAdjustedRefundsEcoContributions")


@_attrs_define
class OR32Response200OrderLinesAdjustedRefundsEcoContributions:
    """
    Attributes:
        epr_category_code (Union[Unset, str]): Extended Producer Responsibility category
        producer_id (Union[Unset, str]): Producer identifier of the eco-contribution.<br/>Not present if the producer
            identifier belongs to the operator.
        producer_id_owner (Union[Unset, str]): Owner of the producerId
        total_amount (Union[Unset, float]): Total amount of the eco-contribution
        unit_amount (Union[Unset, float]): Unit amount of the eco-contribution
    """

    epr_category_code: Union[Unset, str] = UNSET
    producer_id: Union[Unset, str] = UNSET
    producer_id_owner: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epr_category_code = self.epr_category_code

        producer_id = self.producer_id

        producer_id_owner = self.producer_id_owner

        total_amount = self.total_amount

        unit_amount = self.unit_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epr_category_code is not UNSET:
            field_dict["epr_category_code"] = epr_category_code
        if producer_id is not UNSET:
            field_dict["producer_id"] = producer_id
        if producer_id_owner is not UNSET:
            field_dict["producer_id_owner"] = producer_id_owner
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if unit_amount is not UNSET:
            field_dict["unit_amount"] = unit_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epr_category_code = d.pop("epr_category_code", UNSET)

        producer_id = d.pop("producer_id", UNSET)

        producer_id_owner = d.pop("producer_id_owner", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        unit_amount = d.pop("unit_amount", UNSET)

        or32_response_200_order_lines_adjusted_refunds_eco_contributions = cls(
            epr_category_code=epr_category_code,
            producer_id=producer_id,
            producer_id_owner=producer_id_owner,
            total_amount=total_amount,
            unit_amount=unit_amount,
        )

        or32_response_200_order_lines_adjusted_refunds_eco_contributions.additional_properties = d
        return or32_response_200_order_lines_adjusted_refunds_eco_contributions

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
