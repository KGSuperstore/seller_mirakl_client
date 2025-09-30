from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of24_request_offers_discount_ranges import OF24RequestOffersDiscountRanges


T = TypeVar("T", bound="OF24RequestOffersDiscount")


@_attrs_define
class OF24RequestOffersDiscount:
    """Discount of an offer. Offer update: if not provided, existing data will be deleted.

    Attributes:
        end_date (Union[Unset, str]): Discount end date. Offer update: if not provided, existing data will be deleted.
        price (Union[Unset, float]): Discount price. Not to be used when ranges are specified. Offer update: if not
            provided, existing data will be deleted. For Dropship specifically: the discount purchasing price of the offer,
            also referred to as discount cost or discount wholesale price.
        ranges (Union[Unset, list['OF24RequestOffersDiscountRanges']]): Discount ranges. Offer update: if not provided,
            existing data will be deleted.
        start_date (Union[Unset, str]): Discount start date. Offer update: if not provided, existing data will be
            deleted.
    """

    end_date: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    ranges: Union[Unset, list["OF24RequestOffersDiscountRanges"]] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        price = self.price

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if price is not UNSET:
            field_dict["price"] = price
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of24_request_offers_discount_ranges import OF24RequestOffersDiscountRanges

        d = dict(src_dict)
        end_date = d.pop("end_date", UNSET)

        price = d.pop("price", UNSET)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = OF24RequestOffersDiscountRanges.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        start_date = d.pop("start_date", UNSET)

        of24_request_offers_discount = cls(
            end_date=end_date,
            price=price,
            ranges=ranges,
            start_date=start_date,
        )

        of24_request_offers_discount.additional_properties = d
        return of24_request_offers_discount

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
