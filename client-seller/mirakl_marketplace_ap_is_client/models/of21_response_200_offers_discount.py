import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of21_response_200_offers_discount_ranges import OF21Response200OffersDiscountRanges


T = TypeVar("T", bound="OF21Response200OffersDiscount")


@_attrs_define
class OF21Response200OffersDiscount:
    """
    Attributes:
        discount_price (Union[Unset, float]): Discount price. Not to be read if discount with ranges is specified (i.e.
            discount with at least one range with quantity threshold greater than one). <br/>For Dropship specifically: the
            purchasing discount price.
        end_date (Union[Unset, datetime.datetime]): Discount end date
        origin_price (Union[Unset, float]): Origin price <br/>For Dropship specifically: the origin purchasing price
        ranges (Union[Unset, list['OF21Response200OffersDiscountRanges']]): Discount ranges
        start_date (Union[Unset, datetime.datetime]): Discount start date
    """

    discount_price: Union[Unset, float] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    origin_price: Union[Unset, float] = UNSET
    ranges: Union[Unset, list["OF21Response200OffersDiscountRanges"]] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_price = self.discount_price

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        origin_price = self.origin_price

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_price is not UNSET:
            field_dict["discount_price"] = discount_price
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if origin_price is not UNSET:
            field_dict["origin_price"] = origin_price
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of21_response_200_offers_discount_ranges import OF21Response200OffersDiscountRanges

        d = dict(src_dict)
        discount_price = d.pop("discount_price", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        origin_price = d.pop("origin_price", UNSET)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = OF21Response200OffersDiscountRanges.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        of21_response_200_offers_discount = cls(
            discount_price=discount_price,
            end_date=end_date,
            origin_price=origin_price,
            ranges=ranges,
            start_date=start_date,
        )

        of21_response_200_offers_discount.additional_properties = d
        return of21_response_200_offers_discount

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
