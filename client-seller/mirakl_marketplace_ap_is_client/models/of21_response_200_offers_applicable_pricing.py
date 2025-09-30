import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of21_response_200_offers_applicable_pricing_context import (
        OF21Response200OffersApplicablePricingContext,
    )
    from ..models.of21_response_200_offers_applicable_pricing_volume_prices import (
        OF21Response200OffersApplicablePricingVolumePrices,
    )


T = TypeVar("T", bound="OF21Response200OffersApplicablePricing")


@_attrs_define
class OF21Response200OffersApplicablePricing:
    """
    Attributes:
        context (Union[Unset, OF21Response200OffersApplicablePricingContext]):
        discount_end_date (Union[Unset, datetime.datetime]): End date of the discount, or null if no discount exists or
            if the discount does not have an end date.
        discount_start_date (Union[Unset, datetime.datetime]): Start date of the discount, or null if no discount exists
            or if the discount does not have a start date.
        price (Union[Unset, float]): Price of the offer.
            <br/>
            For Dropship specifically: the purchasing price of the offer
            <br/>
            If a discount is defined and is currently active (within the validity interval), it represents the
            unit_discount_price.
            <br/>
            In other cases, it represents the unit_origin_price.
        unit_discount_price (Union[Unset, float]): Discount price for a quantity of one, i.e. the discount price for a
            quantity of one.
            <br/>
            For Dropship specifically: the discount purchasing price for a quantity of one
            <br/>
            Set to null if no discount is defined or if no discount price for a quantity of one is defined.
        unit_origin_price (Union[Unset, float]): Original price for a quantity of one, i.e. the price for a quantity of
            one regardless of the discounts.
            <br/>
            For Dropship specifically: the purchasing price for a quantity of one, also referred to as cost or wholesale
            price
        volume_prices (Union[Unset, list['OF21Response200OffersApplicablePricingVolumePrices']]): Volume prices for each
            quantity threshold. Returns at least the price for a quantity threshold of one.
    """

    context: Union[Unset, "OF21Response200OffersApplicablePricingContext"] = UNSET
    discount_end_date: Union[Unset, datetime.datetime] = UNSET
    discount_start_date: Union[Unset, datetime.datetime] = UNSET
    price: Union[Unset, float] = UNSET
    unit_discount_price: Union[Unset, float] = UNSET
    unit_origin_price: Union[Unset, float] = UNSET
    volume_prices: Union[Unset, list["OF21Response200OffersApplicablePricingVolumePrices"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        discount_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.discount_end_date, Unset):
            discount_end_date = self.discount_end_date.isoformat()

        discount_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.discount_start_date, Unset):
            discount_start_date = self.discount_start_date.isoformat()

        price = self.price

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
        if context is not UNSET:
            field_dict["context"] = context
        if discount_end_date is not UNSET:
            field_dict["discount_end_date"] = discount_end_date
        if discount_start_date is not UNSET:
            field_dict["discount_start_date"] = discount_start_date
        if price is not UNSET:
            field_dict["price"] = price
        if unit_discount_price is not UNSET:
            field_dict["unit_discount_price"] = unit_discount_price
        if unit_origin_price is not UNSET:
            field_dict["unit_origin_price"] = unit_origin_price
        if volume_prices is not UNSET:
            field_dict["volume_prices"] = volume_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of21_response_200_offers_applicable_pricing_context import (
            OF21Response200OffersApplicablePricingContext,
        )
        from ..models.of21_response_200_offers_applicable_pricing_volume_prices import (
            OF21Response200OffersApplicablePricingVolumePrices,
        )

        d = dict(src_dict)
        _context = d.pop("context", UNSET)
        context: Union[Unset, OF21Response200OffersApplicablePricingContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = OF21Response200OffersApplicablePricingContext.from_dict(_context)

        _discount_end_date = d.pop("discount_end_date", UNSET)
        discount_end_date: Union[Unset, datetime.datetime]
        if isinstance(_discount_end_date, Unset):
            discount_end_date = UNSET
        else:
            discount_end_date = isoparse(_discount_end_date)

        _discount_start_date = d.pop("discount_start_date", UNSET)
        discount_start_date: Union[Unset, datetime.datetime]
        if isinstance(_discount_start_date, Unset):
            discount_start_date = UNSET
        else:
            discount_start_date = isoparse(_discount_start_date)

        price = d.pop("price", UNSET)

        unit_discount_price = d.pop("unit_discount_price", UNSET)

        unit_origin_price = d.pop("unit_origin_price", UNSET)

        volume_prices = []
        _volume_prices = d.pop("volume_prices", UNSET)
        for volume_prices_item_data in _volume_prices or []:
            volume_prices_item = OF21Response200OffersApplicablePricingVolumePrices.from_dict(volume_prices_item_data)

            volume_prices.append(volume_prices_item)

        of21_response_200_offers_applicable_pricing = cls(
            context=context,
            discount_end_date=discount_end_date,
            discount_start_date=discount_start_date,
            price=price,
            unit_discount_price=unit_discount_price,
            unit_origin_price=unit_origin_price,
            volume_prices=volume_prices,
        )

        of21_response_200_offers_applicable_pricing.additional_properties = d
        return of21_response_200_offers_applicable_pricing

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
