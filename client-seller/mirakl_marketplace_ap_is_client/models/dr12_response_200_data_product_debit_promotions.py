from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR12Response200DataProductDebitPromotions")


@_attrs_define
class DR12Response200DataProductDebitPromotions:
    """
    Attributes:
        deduced_amount (Union[Unset, float]): Promotion amount for this line
        id (Union[Unset, str]): Promotion id
        type_ (Union[Unset, str]): Promotion's type, whether it is applied to this item (ITEM), or every item in the
            basket for this shop (BASKET)
    """

    deduced_amount: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deduced_amount = self.deduced_amount

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deduced_amount is not UNSET:
            field_dict["deduced_amount"] = deduced_amount
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deduced_amount = d.pop("deduced_amount", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        dr12_response_200_data_product_debit_promotions = cls(
            deduced_amount=deduced_amount,
            id=id,
            type_=type_,
        )

        dr12_response_200_data_product_debit_promotions.additional_properties = d
        return dr12_response_200_data_product_debit_promotions

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
