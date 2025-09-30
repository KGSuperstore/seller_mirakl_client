from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of24_request_offers_all_prices_volume_prices import OF24RequestOffersAllPricesVolumePrices


T = TypeVar("T", bound="OF24RequestOffersAllPrices")


@_attrs_define
class OF24RequestOffersAllPrices:
    """The volume and channel prices.

    Attributes:
        channel_code (Union[Unset, str]): The channel code the prices will be linked to. To set the default prices, set
            it to null.
        discount_end_date (Union[Unset, str]): The end date of the discount. If no discount is desired, set it to null.
        discount_start_date (Union[Unset, str]): The start date of the discount. If no discount is desired, set it to
            null.
        unit_discount_price (Union[Unset, float]): The default unit discount price, i.e. the unit price when the
            discount applied.
        unit_origin_price (Union[Unset, float]): The default unit original price, i.e. the unit price without taking
            discounts nor volume prices into account.
        volume_prices (Union[Unset, list['OF24RequestOffersAllPricesVolumePrices']]): The volume prices applicable for
            the offer.
    """

    channel_code: Union[Unset, str] = UNSET
    discount_end_date: Union[Unset, str] = UNSET
    discount_start_date: Union[Unset, str] = UNSET
    unit_discount_price: Union[Unset, float] = UNSET
    unit_origin_price: Union[Unset, float] = UNSET
    volume_prices: Union[Unset, list["OF24RequestOffersAllPricesVolumePrices"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_code = self.channel_code

        discount_end_date = self.discount_end_date

        discount_start_date = self.discount_start_date

        unit_discount_price = self.unit_discount_price

        unit_origin_price = self.unit_origin_price

        volume_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.volume_prices, Unset):
            volume_prices = []
            for volume_prices_item_data in self.volume_prices:
                volume_prices_item = volume_prices_item_data.to_dict()
                volume_prices.append(volume_prices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_code is not UNSET:
            field_dict["channel_code"] = channel_code
        if discount_end_date is not UNSET:
            field_dict["discount_end_date"] = discount_end_date
        if discount_start_date is not UNSET:
            field_dict["discount_start_date"] = discount_start_date
        if unit_discount_price is not UNSET:
            field_dict["unit_discount_price"] = unit_discount_price
        if unit_origin_price is not UNSET:
            field_dict["unit_origin_price"] = unit_origin_price
        if volume_prices is not UNSET:
            field_dict["volume_prices"] = volume_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of24_request_offers_all_prices_volume_prices import OF24RequestOffersAllPricesVolumePrices

        d = dict(src_dict)
        channel_code = d.pop("channel_code", UNSET)

        discount_end_date = d.pop("discount_end_date", UNSET)

        discount_start_date = d.pop("discount_start_date", UNSET)

        unit_discount_price = d.pop("unit_discount_price", UNSET)

        unit_origin_price = d.pop("unit_origin_price", UNSET)

        volume_prices = []
        _volume_prices = d.pop("volume_prices", UNSET)
        for volume_prices_item_data in _volume_prices or []:
            volume_prices_item = OF24RequestOffersAllPricesVolumePrices.from_dict(volume_prices_item_data)

            volume_prices.append(volume_prices_item)

        of24_request_offers_all_prices = cls(
            channel_code=channel_code,
            discount_end_date=discount_end_date,
            discount_start_date=discount_start_date,
            unit_discount_price=unit_discount_price,
            unit_origin_price=unit_origin_price,
            volume_prices=volume_prices,
        )

        of24_request_offers_all_prices.additional_properties = d
        return of24_request_offers_all_prices

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
