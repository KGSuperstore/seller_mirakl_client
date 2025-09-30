from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF22Response200EcoContributions")


@_attrs_define
class OF22Response200EcoContributions:
    """
    Attributes:
        eco_contribution_amount (Union[Unset, float]): Amount of the eco-contribution.
        epr_category_code (Union[Unset, str]): Extended Producer Responsibility (EPR) category code.
        producer_id (Union[Unset, str]): Producer identifier of the eco-contribution.<br/>Not present if the producer
            identifier belongs to the operator.
    """

    eco_contribution_amount: Union[Unset, float] = UNSET
    epr_category_code: Union[Unset, str] = UNSET
    producer_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eco_contribution_amount = self.eco_contribution_amount

        epr_category_code = self.epr_category_code

        producer_id = self.producer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eco_contribution_amount is not UNSET:
            field_dict["eco_contribution_amount"] = eco_contribution_amount
        if epr_category_code is not UNSET:
            field_dict["epr_category_code"] = epr_category_code
        if producer_id is not UNSET:
            field_dict["producer_id"] = producer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eco_contribution_amount = d.pop("eco_contribution_amount", UNSET)

        epr_category_code = d.pop("epr_category_code", UNSET)

        producer_id = d.pop("producer_id", UNSET)

        of22_response_200_eco_contributions = cls(
            eco_contribution_amount=eco_contribution_amount,
            epr_category_code=epr_category_code,
            producer_id=producer_id,
        )

        of22_response_200_eco_contributions.additional_properties = d
        return of22_response_200_eco_contributions

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
