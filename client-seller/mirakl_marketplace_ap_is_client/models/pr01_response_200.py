from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pr01_response_200_promotions import PR01Response200Promotions


T = TypeVar("T", bound="PR01Response200")


@_attrs_define
class PR01Response200:
    """
    Attributes:
        promotions (Union[Unset, list['PR01Response200Promotions']]): List of promotions
        total_count (Union[Unset, int]):
    """

    promotions: Union[Unset, list["PR01Response200Promotions"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        promotions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.promotions, Unset):
            promotions = []
            for promotions_item_data in self.promotions:
                promotions_item = promotions_item_data.to_dict()
                promotions.append(promotions_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotions is not UNSET:
            field_dict["promotions"] = promotions
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pr01_response_200_promotions import PR01Response200Promotions

        d = dict(src_dict)
        promotions = []
        _promotions = d.pop("promotions", UNSET)
        for promotions_item_data in _promotions or []:
            promotions_item = PR01Response200Promotions.from_dict(promotions_item_data)

            promotions.append(promotions_item)

        total_count = d.pop("total_count", UNSET)

        pr01_response_200 = cls(
            promotions=promotions,
            total_count=total_count,
        )

        pr01_response_200.additional_properties = d
        return pr01_response_200

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
