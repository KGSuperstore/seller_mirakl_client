import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of22_response_200_all_prices import OF22Response200AllPrices
    from ..models.of22_response_200_applicable_pricing import OF22Response200ApplicablePricing
    from ..models.of22_response_200_eco_contributions import OF22Response200EcoContributions
    from ..models.of22_response_200_fulfillment import OF22Response200Fulfillment
    from ..models.of22_response_200_logistic_class import OF22Response200LogisticClass
    from ..models.of22_response_200_offer_additional_fields import OF22Response200OfferAdditionalFields
    from ..models.of22_response_200_product_references import OF22Response200ProductReferences
    from ..models.of22_response_200_retail_prices import OF22Response200RetailPrices


T = TypeVar("T", bound="OF22Response200")


@_attrs_define
class OF22Response200:
    """
    Attributes:
        active (Union[Unset, bool]): Is the offer active
        all_prices (Union[Unset, list['OF22Response200AllPrices']]): All prices for the offer
            <br/>
            For Dropship specifically: the list of purchasing prices of the offer, also referred to as costs or wholesale
            prices
        allow_quote_requests (Union[Unset, bool]): Whether the offer is eligible for quotation
        applicable_pricing (Union[Unset, OF22Response200ApplicablePricing]):
        available_end_date (Union[Unset, datetime.datetime]): Available end date
        available_start_date (Union[Unset, datetime.datetime]): Available start date
        category_code (Union[Unset, str]): Product category code
        category_label (Union[Unset, str]): Product category label
        channels (Union[Unset, list[str]]): List of channel codes on which the offer can be sold
        currency_iso_code (Union[Unset, str]): The currency of the shop (iso format)
        description (Union[Unset, str]): Offer description
        eco_contributions (Union[Unset, list['OF22Response200EcoContributions']]): Eco-contributions of the offer - only
            available if the operator setting <em>Activate data collection related to circular economy regulations</em> has
            been enabled.
        favorite_rank (Union[Unset, int]): Favorite rank for the offer, when the favorite feature is enabled and the
            offer is a favorite
        fulfillment (Union[Unset, OF22Response200Fulfillment]):
        inactivity_reasons (Union[Unset, list[str]]): Reasons for offers inactivity, mandatory if an offer is inactive
        internal_description (Union[Unset, str]): The offer's description as shown in the back office
        leadtime_to_ship (Union[Unset, int]): Offer's lead time to ship value. If this value has been set to 0, value is
            returned as 1 (unless platform's default lead time to ship value is also 0). If no lead time to ship was
            specified for the offer, platform's default value is returned.
        logistic_class (Union[Unset, OF22Response200LogisticClass]):
        max_order_quantity (Union[Unset, int]): Highest quantity of product items per order
        min_order_quantity (Union[Unset, int]): Lowest quantity of product items per order
        min_quantity_alert (Union[Unset, int]): Mininum quantity of the offer
        min_shipping_price (Union[Unset, float]): Unit price of the minimum shipping rate
        min_shipping_price_additional (Union[Unset, float]): Additional unit price associated to the minimum shipping
            rate
        min_shipping_type (Union[Unset, str]): Code of the shipping type associated to the minimum shipping rate
        min_shipping_zone (Union[Unset, str]): Code of the shipping zone associated to the minimum shipping rate
        msrp (Union[Unset, float]): The retail price recommendation, also referred to as manufacturer's suggested retail
            price (MSRP) or recommended retail price (RRP).
            <br/>
            Applicable only for Dropship offers.
        offer_additional_fields (Union[Unset, list['OF22Response200OfferAdditionalFields']]): Custom fields of the offer
        offer_id (Union[Unset, int]): Identifier of the offer
        package_quantity (Union[Unset, int]): Indivisible quantity of the same product
        price (Union[Unset, float]): Price of the offer
            <br/>
            For Dropship specifically: the purchasing price of the offer, also referred to as cost or wholesale price
        price_additional_info (Union[Unset, str]): Additional price information for the offer
        product_brand (Union[Unset, str]): Brand of the product
        product_description (Union[Unset, str]): Description of the product
        product_references (Union[Unset, list['OF22Response200ProductReferences']]): Product references
        product_sku (Union[Unset, str]): Product SKU
        product_tax_code (Union[Unset, str]): Offer product tax code
        product_title (Union[Unset, str]): Product title
        quantity (Union[Unset, int]): Available quantity of the offer
        retail_prices (Union[Unset, list['OF22Response200RetailPrices']]): List retail prices for the offer, also
            referred to as selling prices.
            <br/>
            Applicable only for Dropship offers.
        shipping_deadline (Union[Unset, datetime.datetime]): Estimated shipping date, that includes business closing
            days and cut-off configured on the platform. Add the earliest and latest delivery times to calculate the
            estimated delivery date to customers
        shop_sku (Union[Unset, str]): Shop's sku of the offer
        state_code (Union[Unset, str]): Offer condition
        total_price (Union[Unset, float]): Total price of the offer (price + minimum shipping rate)
            <br/>
            For Dropship specifically: the purchasing price of the offer + minimum shipping rate
    """

    active: Union[Unset, bool] = UNSET
    all_prices: Union[Unset, list["OF22Response200AllPrices"]] = UNSET
    allow_quote_requests: Union[Unset, bool] = UNSET
    applicable_pricing: Union[Unset, "OF22Response200ApplicablePricing"] = UNSET
    available_end_date: Union[Unset, datetime.datetime] = UNSET
    available_start_date: Union[Unset, datetime.datetime] = UNSET
    category_code: Union[Unset, str] = UNSET
    category_label: Union[Unset, str] = UNSET
    channels: Union[Unset, list[str]] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    eco_contributions: Union[Unset, list["OF22Response200EcoContributions"]] = UNSET
    favorite_rank: Union[Unset, int] = UNSET
    fulfillment: Union[Unset, "OF22Response200Fulfillment"] = UNSET
    inactivity_reasons: Union[Unset, list[str]] = UNSET
    internal_description: Union[Unset, str] = UNSET
    leadtime_to_ship: Union[Unset, int] = UNSET
    logistic_class: Union[Unset, "OF22Response200LogisticClass"] = UNSET
    max_order_quantity: Union[Unset, int] = UNSET
    min_order_quantity: Union[Unset, int] = UNSET
    min_quantity_alert: Union[Unset, int] = UNSET
    min_shipping_price: Union[Unset, float] = UNSET
    min_shipping_price_additional: Union[Unset, float] = UNSET
    min_shipping_type: Union[Unset, str] = UNSET
    min_shipping_zone: Union[Unset, str] = UNSET
    msrp: Union[Unset, float] = UNSET
    offer_additional_fields: Union[Unset, list["OF22Response200OfferAdditionalFields"]] = UNSET
    offer_id: Union[Unset, int] = UNSET
    package_quantity: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    price_additional_info: Union[Unset, str] = UNSET
    product_brand: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    product_references: Union[Unset, list["OF22Response200ProductReferences"]] = UNSET
    product_sku: Union[Unset, str] = UNSET
    product_tax_code: Union[Unset, str] = UNSET
    product_title: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    retail_prices: Union[Unset, list["OF22Response200RetailPrices"]] = UNSET
    shipping_deadline: Union[Unset, datetime.datetime] = UNSET
    shop_sku: Union[Unset, str] = UNSET
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

        available_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.available_end_date, Unset):
            available_end_date = self.available_end_date.isoformat()

        available_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.available_start_date, Unset):
            available_start_date = self.available_start_date.isoformat()

        category_code = self.category_code

        category_label = self.category_label

        channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        currency_iso_code = self.currency_iso_code

        description = self.description

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        favorite_rank = self.favorite_rank

        fulfillment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()

        inactivity_reasons: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inactivity_reasons, Unset):
            inactivity_reasons = self.inactivity_reasons

        internal_description = self.internal_description

        leadtime_to_ship = self.leadtime_to_ship

        logistic_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logistic_class, Unset):
            logistic_class = self.logistic_class.to_dict()

        max_order_quantity = self.max_order_quantity

        min_order_quantity = self.min_order_quantity

        min_quantity_alert = self.min_quantity_alert

        min_shipping_price = self.min_shipping_price

        min_shipping_price_additional = self.min_shipping_price_additional

        min_shipping_type = self.min_shipping_type

        min_shipping_zone = self.min_shipping_zone

        msrp = self.msrp

        offer_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offer_additional_fields, Unset):
            offer_additional_fields = []
            for offer_additional_fields_item_data in self.offer_additional_fields:
                offer_additional_fields_item = offer_additional_fields_item_data.to_dict()
                offer_additional_fields.append(offer_additional_fields_item)

        offer_id = self.offer_id

        package_quantity = self.package_quantity

        price = self.price

        price_additional_info = self.price_additional_info

        product_brand = self.product_brand

        product_description = self.product_description

        product_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_references, Unset):
            product_references = []
            for product_references_item_data in self.product_references:
                product_references_item = product_references_item_data.to_dict()
                product_references.append(product_references_item)

        product_sku = self.product_sku

        product_tax_code = self.product_tax_code

        product_title = self.product_title

        quantity = self.quantity

        retail_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retail_prices, Unset):
            retail_prices = []
            for retail_prices_item_data in self.retail_prices:
                retail_prices_item = retail_prices_item_data.to_dict()
                retail_prices.append(retail_prices_item)

        shipping_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_deadline, Unset):
            shipping_deadline = self.shipping_deadline.isoformat()

        shop_sku = self.shop_sku

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
        if available_end_date is not UNSET:
            field_dict["available_end_date"] = available_end_date
        if available_start_date is not UNSET:
            field_dict["available_start_date"] = available_start_date
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if category_label is not UNSET:
            field_dict["category_label"] = category_label
        if channels is not UNSET:
            field_dict["channels"] = channels
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if description is not UNSET:
            field_dict["description"] = description
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if favorite_rank is not UNSET:
            field_dict["favorite_rank"] = favorite_rank
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment
        if inactivity_reasons is not UNSET:
            field_dict["inactivity_reasons"] = inactivity_reasons
        if internal_description is not UNSET:
            field_dict["internal_description"] = internal_description
        if leadtime_to_ship is not UNSET:
            field_dict["leadtime_to_ship"] = leadtime_to_ship
        if logistic_class is not UNSET:
            field_dict["logistic_class"] = logistic_class
        if max_order_quantity is not UNSET:
            field_dict["max_order_quantity"] = max_order_quantity
        if min_order_quantity is not UNSET:
            field_dict["min_order_quantity"] = min_order_quantity
        if min_quantity_alert is not UNSET:
            field_dict["min_quantity_alert"] = min_quantity_alert
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
        if offer_additional_fields is not UNSET:
            field_dict["offer_additional_fields"] = offer_additional_fields
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id
        if package_quantity is not UNSET:
            field_dict["package_quantity"] = package_quantity
        if price is not UNSET:
            field_dict["price"] = price
        if price_additional_info is not UNSET:
            field_dict["price_additional_info"] = price_additional_info
        if product_brand is not UNSET:
            field_dict["product_brand"] = product_brand
        if product_description is not UNSET:
            field_dict["product_description"] = product_description
        if product_references is not UNSET:
            field_dict["product_references"] = product_references
        if product_sku is not UNSET:
            field_dict["product_sku"] = product_sku
        if product_tax_code is not UNSET:
            field_dict["product_tax_code"] = product_tax_code
        if product_title is not UNSET:
            field_dict["product_title"] = product_title
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if retail_prices is not UNSET:
            field_dict["retail_prices"] = retail_prices
        if shipping_deadline is not UNSET:
            field_dict["shipping_deadline"] = shipping_deadline
        if shop_sku is not UNSET:
            field_dict["shop_sku"] = shop_sku
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if total_price is not UNSET:
            field_dict["total_price"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of22_response_200_all_prices import OF22Response200AllPrices
        from ..models.of22_response_200_applicable_pricing import OF22Response200ApplicablePricing
        from ..models.of22_response_200_eco_contributions import OF22Response200EcoContributions
        from ..models.of22_response_200_fulfillment import OF22Response200Fulfillment
        from ..models.of22_response_200_logistic_class import OF22Response200LogisticClass
        from ..models.of22_response_200_offer_additional_fields import OF22Response200OfferAdditionalFields
        from ..models.of22_response_200_product_references import OF22Response200ProductReferences
        from ..models.of22_response_200_retail_prices import OF22Response200RetailPrices

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        all_prices = []
        _all_prices = d.pop("all_prices", UNSET)
        for all_prices_item_data in _all_prices or []:
            all_prices_item = OF22Response200AllPrices.from_dict(all_prices_item_data)

            all_prices.append(all_prices_item)

        allow_quote_requests = d.pop("allow_quote_requests", UNSET)

        _applicable_pricing = d.pop("applicable_pricing", UNSET)
        applicable_pricing: Union[Unset, OF22Response200ApplicablePricing]
        if isinstance(_applicable_pricing, Unset):
            applicable_pricing = UNSET
        else:
            applicable_pricing = OF22Response200ApplicablePricing.from_dict(_applicable_pricing)

        _available_end_date = d.pop("available_end_date", UNSET)
        available_end_date: Union[Unset, datetime.datetime]
        if isinstance(_available_end_date, Unset):
            available_end_date = UNSET
        else:
            available_end_date = isoparse(_available_end_date)

        _available_start_date = d.pop("available_start_date", UNSET)
        available_start_date: Union[Unset, datetime.datetime]
        if isinstance(_available_start_date, Unset):
            available_start_date = UNSET
        else:
            available_start_date = isoparse(_available_start_date)

        category_code = d.pop("category_code", UNSET)

        category_label = d.pop("category_label", UNSET)

        channels = cast(list[str], d.pop("channels", UNSET))

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        description = d.pop("description", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OF22Response200EcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        favorite_rank = d.pop("favorite_rank", UNSET)

        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: Union[Unset, OF22Response200Fulfillment]
        if isinstance(_fulfillment, Unset):
            fulfillment = UNSET
        else:
            fulfillment = OF22Response200Fulfillment.from_dict(_fulfillment)

        inactivity_reasons = cast(list[str], d.pop("inactivity_reasons", UNSET))

        internal_description = d.pop("internal_description", UNSET)

        leadtime_to_ship = d.pop("leadtime_to_ship", UNSET)

        _logistic_class = d.pop("logistic_class", UNSET)
        logistic_class: Union[Unset, OF22Response200LogisticClass]
        if isinstance(_logistic_class, Unset):
            logistic_class = UNSET
        else:
            logistic_class = OF22Response200LogisticClass.from_dict(_logistic_class)

        max_order_quantity = d.pop("max_order_quantity", UNSET)

        min_order_quantity = d.pop("min_order_quantity", UNSET)

        min_quantity_alert = d.pop("min_quantity_alert", UNSET)

        min_shipping_price = d.pop("min_shipping_price", UNSET)

        min_shipping_price_additional = d.pop("min_shipping_price_additional", UNSET)

        min_shipping_type = d.pop("min_shipping_type", UNSET)

        min_shipping_zone = d.pop("min_shipping_zone", UNSET)

        msrp = d.pop("msrp", UNSET)

        offer_additional_fields = []
        _offer_additional_fields = d.pop("offer_additional_fields", UNSET)
        for offer_additional_fields_item_data in _offer_additional_fields or []:
            offer_additional_fields_item = OF22Response200OfferAdditionalFields.from_dict(
                offer_additional_fields_item_data
            )

            offer_additional_fields.append(offer_additional_fields_item)

        offer_id = d.pop("offer_id", UNSET)

        package_quantity = d.pop("package_quantity", UNSET)

        price = d.pop("price", UNSET)

        price_additional_info = d.pop("price_additional_info", UNSET)

        product_brand = d.pop("product_brand", UNSET)

        product_description = d.pop("product_description", UNSET)

        product_references = []
        _product_references = d.pop("product_references", UNSET)
        for product_references_item_data in _product_references or []:
            product_references_item = OF22Response200ProductReferences.from_dict(product_references_item_data)

            product_references.append(product_references_item)

        product_sku = d.pop("product_sku", UNSET)

        product_tax_code = d.pop("product_tax_code", UNSET)

        product_title = d.pop("product_title", UNSET)

        quantity = d.pop("quantity", UNSET)

        retail_prices = []
        _retail_prices = d.pop("retail_prices", UNSET)
        for retail_prices_item_data in _retail_prices or []:
            retail_prices_item = OF22Response200RetailPrices.from_dict(retail_prices_item_data)

            retail_prices.append(retail_prices_item)

        _shipping_deadline = d.pop("shipping_deadline", UNSET)
        shipping_deadline: Union[Unset, datetime.datetime]
        if isinstance(_shipping_deadline, Unset):
            shipping_deadline = UNSET
        else:
            shipping_deadline = isoparse(_shipping_deadline)

        shop_sku = d.pop("shop_sku", UNSET)

        state_code = d.pop("state_code", UNSET)

        total_price = d.pop("total_price", UNSET)

        of22_response_200 = cls(
            active=active,
            all_prices=all_prices,
            allow_quote_requests=allow_quote_requests,
            applicable_pricing=applicable_pricing,
            available_end_date=available_end_date,
            available_start_date=available_start_date,
            category_code=category_code,
            category_label=category_label,
            channels=channels,
            currency_iso_code=currency_iso_code,
            description=description,
            eco_contributions=eco_contributions,
            favorite_rank=favorite_rank,
            fulfillment=fulfillment,
            inactivity_reasons=inactivity_reasons,
            internal_description=internal_description,
            leadtime_to_ship=leadtime_to_ship,
            logistic_class=logistic_class,
            max_order_quantity=max_order_quantity,
            min_order_quantity=min_order_quantity,
            min_quantity_alert=min_quantity_alert,
            min_shipping_price=min_shipping_price,
            min_shipping_price_additional=min_shipping_price_additional,
            min_shipping_type=min_shipping_type,
            min_shipping_zone=min_shipping_zone,
            msrp=msrp,
            offer_additional_fields=offer_additional_fields,
            offer_id=offer_id,
            package_quantity=package_quantity,
            price=price,
            price_additional_info=price_additional_info,
            product_brand=product_brand,
            product_description=product_description,
            product_references=product_references,
            product_sku=product_sku,
            product_tax_code=product_tax_code,
            product_title=product_title,
            quantity=quantity,
            retail_prices=retail_prices,
            shipping_deadline=shipping_deadline,
            shop_sku=shop_sku,
            state_code=state_code,
            total_price=total_price,
        )

        of22_response_200.additional_properties = d
        return of22_response_200

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
