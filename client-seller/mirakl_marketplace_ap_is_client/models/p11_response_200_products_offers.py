import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p11_response_200_products_offers_all_prices import P11Response200ProductsOffersAllPrices
    from ..models.p11_response_200_products_offers_applicable_pricing import (
        P11Response200ProductsOffersApplicablePricing,
    )
    from ..models.p11_response_200_products_offers_eco_contributions import P11Response200ProductsOffersEcoContributions
    from ..models.p11_response_200_products_offers_retail_prices import P11Response200ProductsOffersRetailPrices
    from ..models.p11_response_200_products_offers_shipping_types import P11Response200ProductsOffersShippingTypes


T = TypeVar("T", bound="P11Response200ProductsOffers")


@_attrs_define
class P11Response200ProductsOffers:
    """
    Attributes:
        active (Union[Unset, bool]): Is the offer active
        all_prices (Union[Unset, list['P11Response200ProductsOffersAllPrices']]): All prices for the offer
            <br/>
            For Dropship specifically: the list of purchasing prices of the offer, also referred to as costs or wholesale
            prices
        allow_quote_requests (Union[Unset, bool]): Whether the offer is eligible for quotation
        applicable_pricing (Union[Unset, P11Response200ProductsOffersApplicablePricing]):
        currency_iso_code (Union[Unset, str]): The currency of the shop (iso format)
        description (Union[Unset, str]): Offer description
        eco_contributions (Union[Unset, list['P11Response200ProductsOffersEcoContributions']]): Eco-contributions of the
            offer - only available if the operator setting <em>Activate data collection related to circular economy
            regulations</em> has been enabled.
        inactivity_reasons (Union[Unset, list[str]]): Reasons for offers inactivity, mandatory if an offer is inactive
        is_professional (Union[Unset, bool]): Whether or not the shop is professional
        leadtime_to_ship (Union[Unset, int]): Offer's lead time to ship value. If this value has been set to 0, value is
            returned as 1 (unless platform's default lead time to ship value is also 0). If no lead time to ship was
            specified for the offer, platform's default value is returned.
        min_shipping_price (Union[Unset, float]): Unit price of the minimum shipping rate
        min_shipping_price_additional (Union[Unset, float]): Additional unit price associated to the minimum shipping
            rate
        min_shipping_type (Union[Unset, str]): Code of the shipping type associated to the minimum shipping rate
        min_shipping_zone (Union[Unset, str]): Code of the shipping zone associated to the minimum shipping rate
        msrp (Union[Unset, float]): The retail price recommendation, also referred to as manufacturer's suggested retail
            price (MSRP) or recommended retail price (RRP).
            <br/>
            Applicable only for Dropship offers.
        nb_evaluation (Union[Unset, int]): Number of customers evaluations
        price (Union[Unset, float]): Price of the offer
            <br/>
            For Dropship specifically: the purchasing price of the offer, also referred to as cost or wholesale price
        price_additional_info (Union[Unset, str]): Additional price information for the offer
        retail_prices (Union[Unset, list['P11Response200ProductsOffersRetailPrices']]): List retail prices for the
            offer, also referred to as selling prices.
            <br/>
            Applicable only for Dropship offers.
        shipping_deadline (Union[Unset, datetime.datetime]): Estimated shipping date, that includes business closing
            days and cut-off configured on the platform. Add the earliest and latest delivery times to calculate the
            estimated delivery date to customers
        shipping_types (Union[Unset, list['P11Response200ProductsOffersShippingTypes']]): List of shipping types
            compatible with the given offer
        shop_grade (Union[Unset, float]): Grade of the shop which proposes the offer
        shop_name (Union[Unset, str]): Name of the shop which proposes the offer
        state_code (Union[Unset, str]): Offer condition
        total_price (Union[Unset, float]): Total price of the offer (price + minimum shipping rate)
            <br/>
            For Dropship specifically: the purchasing price of the offer + minimum shipping rate
    """

    active: Union[Unset, bool] = UNSET
    all_prices: Union[Unset, list["P11Response200ProductsOffersAllPrices"]] = UNSET
    allow_quote_requests: Union[Unset, bool] = UNSET
    applicable_pricing: Union[Unset, "P11Response200ProductsOffersApplicablePricing"] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    eco_contributions: Union[Unset, list["P11Response200ProductsOffersEcoContributions"]] = UNSET
    inactivity_reasons: Union[Unset, list[str]] = UNSET
    is_professional: Union[Unset, bool] = UNSET
    leadtime_to_ship: Union[Unset, int] = UNSET
    min_shipping_price: Union[Unset, float] = UNSET
    min_shipping_price_additional: Union[Unset, float] = UNSET
    min_shipping_type: Union[Unset, str] = UNSET
    min_shipping_zone: Union[Unset, str] = UNSET
    msrp: Union[Unset, float] = UNSET
    nb_evaluation: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    price_additional_info: Union[Unset, str] = UNSET
    retail_prices: Union[Unset, list["P11Response200ProductsOffersRetailPrices"]] = UNSET
    shipping_deadline: Union[Unset, datetime.datetime] = UNSET
    shipping_types: Union[Unset, list["P11Response200ProductsOffersShippingTypes"]] = UNSET
    shop_grade: Union[Unset, float] = UNSET
    shop_name: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    total_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        all_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.all_prices, Unset):
            all_prices = []
            for all_prices_item_data in self.all_prices:
                all_prices_item = all_prices_item_data.to_dict()
                all_prices.append(all_prices_item)

        allow_quote_requests = self.allow_quote_requests

        applicable_pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.applicable_pricing, Unset):
            applicable_pricing = self.applicable_pricing.to_dict()

        currency_iso_code = self.currency_iso_code

        description = self.description

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        inactivity_reasons: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inactivity_reasons, Unset):
            inactivity_reasons = self.inactivity_reasons

        is_professional = self.is_professional

        leadtime_to_ship = self.leadtime_to_ship

        min_shipping_price = self.min_shipping_price

        min_shipping_price_additional = self.min_shipping_price_additional

        min_shipping_type = self.min_shipping_type

        min_shipping_zone = self.min_shipping_zone

        msrp = self.msrp

        nb_evaluation = self.nb_evaluation

        price = self.price

        price_additional_info = self.price_additional_info

        retail_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retail_prices, Unset):
            retail_prices = []
            for retail_prices_item_data in self.retail_prices:
                retail_prices_item = retail_prices_item_data.to_dict()
                retail_prices.append(retail_prices_item)

        shipping_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_deadline, Unset):
            shipping_deadline = self.shipping_deadline.isoformat()

        shipping_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_types, Unset):
            shipping_types = []
            for shipping_types_item_data in self.shipping_types:
                shipping_types_item = shipping_types_item_data.to_dict()
                shipping_types.append(shipping_types_item)

        shop_grade = self.shop_grade

        shop_name = self.shop_name

        state_code = self.state_code

        total_price = self.total_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if all_prices is not UNSET:
            field_dict["all_prices"] = all_prices
        if allow_quote_requests is not UNSET:
            field_dict["allow_quote_requests"] = allow_quote_requests
        if applicable_pricing is not UNSET:
            field_dict["applicable_pricing"] = applicable_pricing
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if description is not UNSET:
            field_dict["description"] = description
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if inactivity_reasons is not UNSET:
            field_dict["inactivity_reasons"] = inactivity_reasons
        if is_professional is not UNSET:
            field_dict["is_professional"] = is_professional
        if leadtime_to_ship is not UNSET:
            field_dict["leadtime_to_ship"] = leadtime_to_ship
        if min_shipping_price is not UNSET:
            field_dict["min_shipping_price"] = min_shipping_price
        if min_shipping_price_additional is not UNSET:
            field_dict["min_shipping_price_additional"] = min_shipping_price_additional
        if min_shipping_type is not UNSET:
            field_dict["min_shipping_type"] = min_shipping_type
        if min_shipping_zone is not UNSET:
            field_dict["min_shipping_zone"] = min_shipping_zone
        if msrp is not UNSET:
            field_dict["msrp"] = msrp
        if nb_evaluation is not UNSET:
            field_dict["nb_evaluation"] = nb_evaluation
        if price is not UNSET:
            field_dict["price"] = price
        if price_additional_info is not UNSET:
            field_dict["price_additional_info"] = price_additional_info
        if retail_prices is not UNSET:
            field_dict["retail_prices"] = retail_prices
        if shipping_deadline is not UNSET:
            field_dict["shipping_deadline"] = shipping_deadline
        if shipping_types is not UNSET:
            field_dict["shipping_types"] = shipping_types
        if shop_grade is not UNSET:
            field_dict["shop_grade"] = shop_grade
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if total_price is not UNSET:
            field_dict["total_price"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p11_response_200_products_offers_all_prices import P11Response200ProductsOffersAllPrices
        from ..models.p11_response_200_products_offers_applicable_pricing import (
            P11Response200ProductsOffersApplicablePricing,
        )
        from ..models.p11_response_200_products_offers_eco_contributions import (
            P11Response200ProductsOffersEcoContributions,
        )
        from ..models.p11_response_200_products_offers_retail_prices import P11Response200ProductsOffersRetailPrices
        from ..models.p11_response_200_products_offers_shipping_types import P11Response200ProductsOffersShippingTypes

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        all_prices = []
        _all_prices = d.pop("all_prices", UNSET)
        for all_prices_item_data in _all_prices or []:
            all_prices_item = P11Response200ProductsOffersAllPrices.from_dict(all_prices_item_data)

            all_prices.append(all_prices_item)

        allow_quote_requests = d.pop("allow_quote_requests", UNSET)

        _applicable_pricing = d.pop("applicable_pricing", UNSET)
        applicable_pricing: Union[Unset, P11Response200ProductsOffersApplicablePricing]
        if isinstance(_applicable_pricing, Unset):
            applicable_pricing = UNSET
        else:
            applicable_pricing = P11Response200ProductsOffersApplicablePricing.from_dict(_applicable_pricing)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        description = d.pop("description", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = P11Response200ProductsOffersEcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        inactivity_reasons = cast(list[str], d.pop("inactivity_reasons", UNSET))

        is_professional = d.pop("is_professional", UNSET)

        leadtime_to_ship = d.pop("leadtime_to_ship", UNSET)

        min_shipping_price = d.pop("min_shipping_price", UNSET)

        min_shipping_price_additional = d.pop("min_shipping_price_additional", UNSET)

        min_shipping_type = d.pop("min_shipping_type", UNSET)

        min_shipping_zone = d.pop("min_shipping_zone", UNSET)

        msrp = d.pop("msrp", UNSET)

        nb_evaluation = d.pop("nb_evaluation", UNSET)

        price = d.pop("price", UNSET)

        price_additional_info = d.pop("price_additional_info", UNSET)

        retail_prices = []
        _retail_prices = d.pop("retail_prices", UNSET)
        for retail_prices_item_data in _retail_prices or []:
            retail_prices_item = P11Response200ProductsOffersRetailPrices.from_dict(retail_prices_item_data)

            retail_prices.append(retail_prices_item)

        _shipping_deadline = d.pop("shipping_deadline", UNSET)
        shipping_deadline: Union[Unset, datetime.datetime]
        if isinstance(_shipping_deadline, Unset):
            shipping_deadline = UNSET
        else:
            shipping_deadline = isoparse(_shipping_deadline)

        shipping_types = []
        _shipping_types = d.pop("shipping_types", UNSET)
        for shipping_types_item_data in _shipping_types or []:
            shipping_types_item = P11Response200ProductsOffersShippingTypes.from_dict(shipping_types_item_data)

            shipping_types.append(shipping_types_item)

        shop_grade = d.pop("shop_grade", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        state_code = d.pop("state_code", UNSET)

        total_price = d.pop("total_price", UNSET)

        p11_response_200_products_offers = cls(
            active=active,
            all_prices=all_prices,
            allow_quote_requests=allow_quote_requests,
            applicable_pricing=applicable_pricing,
            currency_iso_code=currency_iso_code,
            description=description,
            eco_contributions=eco_contributions,
            inactivity_reasons=inactivity_reasons,
            is_professional=is_professional,
            leadtime_to_ship=leadtime_to_ship,
            min_shipping_price=min_shipping_price,
            min_shipping_price_additional=min_shipping_price_additional,
            min_shipping_type=min_shipping_type,
            min_shipping_zone=min_shipping_zone,
            msrp=msrp,
            nb_evaluation=nb_evaluation,
            price=price,
            price_additional_info=price_additional_info,
            retail_prices=retail_prices,
            shipping_deadline=shipping_deadline,
            shipping_types=shipping_types,
            shop_grade=shop_grade,
            shop_name=shop_name,
            state_code=state_code,
            total_price=total_price,
        )

        p11_response_200_products_offers.additional_properties = d
        return p11_response_200_products_offers

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
