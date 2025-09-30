from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of21_response_200_offers import OF21Response200Offers


T = TypeVar("T", bound="OF21Response200")


@_attrs_define
class OF21Response200:
    """
    Attributes:
        offers (Union[Unset, list['OF21Response200Offers']]): Offers for a shop
        total_count (Union[Unset, int]): Offer total count
    """

    offers: Union[Unset, list["OF21Response200Offers"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offers is not UNSET:
            field_dict["offers"] = offers
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of21_response_200_offers import OF21Response200Offers

        d = dict(src_dict)
        offers = []
        _offers = d.pop("offers", UNSET)
        for offers_item_data in _offers or []:
            offers_item = OF21Response200Offers.from_dict(offers_item_data)

            offers.append(offers_item)

        total_count = d.pop("total_count", UNSET)

        of21_response_200 = cls(
            offers=offers,
            total_count=total_count,
        )

        of21_response_200.additional_properties = d
        return of21_response_200

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
