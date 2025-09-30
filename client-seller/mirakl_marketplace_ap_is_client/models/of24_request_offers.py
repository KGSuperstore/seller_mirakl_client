from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of24_request_offers_all_prices import OF24RequestOffersAllPrices
    from ..models.of24_request_offers_discount import OF24RequestOffersDiscount
    from ..models.of24_request_offers_eco_contributions import OF24RequestOffersEcoContributions
    from ..models.of24_request_offers_offer_additional_fields import OF24RequestOffersOfferAdditionalFields
    from ..models.of24_request_offers_retail_prices import OF24RequestOffersRetailPrices


T = TypeVar("T", bound="OF24RequestOffers")


@_attrs_define
class OF24RequestOffers:
    """Offers list

    Attributes:
        all_prices (Union[Unset, list['OF24RequestOffersAllPrices']]): The volume and channel prices.
        allow_quote_requests (Union[Unset, bool]): Whether the offer is eligible for quotation. Offer update: if not
            provided, will be set to false.
        available_ended (Union[Unset, str]): End date of the period of availability. Offer update: if not provided,
            existing data will be deleted.
        available_started (Union[Unset, str]): Started date of the period of availability. Offer update: if not
            provided, existing data will be deleted.
        description (Union[Unset, str]): Description of the offer. Offer update: if not provided, existing data will be
            deleted.
        discount (Union[Unset, OF24RequestOffersDiscount]): Discount of an offer. Offer update: if not provided,
            existing data will be deleted.
        eco_contributions (Union[Unset, list['OF24RequestOffersEcoContributions']]): Eco-contributions of the offer -
            only available if the operator setting <em>Activate data collection related to circular economy regulations</em>
            has been enabled. Offer update: if not provided, existing data will be deleted.
        internal_description (Union[Unset, str]): Internal description of the offer. Offer update: if not provided,
            existing data will be deleted.
        leadtime_to_ship (Union[Unset, int]): Leadtime to ship of the offer, in days. Offer update: if not provided,
            existing data will be deleted.
        logistic_class (Union[Unset, str]): Offer logistic class. Offer update: if not provided, existing data will be
            deleted.
        max_order_quantity (Union[Unset, int]): The maximum quantity of product items per order. Offer update: if not
            provided, existing data will be deleted.
        min_order_quantity (Union[Unset, int]): The minimum quantity of product items per order. Offer update: if not
            provided, existing data will be deleted.
        min_quantity_alert (Union[Unset, int]): The minimum stock level that triggers an email alert. No alerts are sent
            if this field is not specified. Offer update: if not provided, existing data will be deleted.
        msrp (Union[Unset, float]): The retail price recommendation, also referred to as manufacturer's suggested retail
            price (MSRP) or recommended retail price (RRP). Only applicable for Dropship offers.
        offer_additional_fields (Union[Unset, list['OF24RequestOffersOfferAdditionalFields']]): Custom fields of the
            offer
        package_quantity (Union[Unset, int]): The indivisible selling quantity of the same product. Offer update: if not
            provided, existing data will be deleted.
        price (Union[Unset, float]): Price of the offer. For Dropship specifically: the purchasing price of the offer,
            also referred to as cost or wholesale price.
        price_additional_info (Union[Unset, str]): Price additional information of the offer. Offer update: if not
            provided, existing data will be deleted.
        pricing_unit (Union[Unset, str]): The unit corresponding to the submitted price when the price per measurement
            unit feature is used.
        product_id (Union[Unset, str]): Reference of the product associated with the offer. Required at offer creation.
            Optional at offer update.
        product_id_type (Union[Unset, str]): Reference type of the product associated with the offer. Required at offer
            creation. Optional at offer update.
        product_tax_code (Union[Unset, str]): Product tax code associated to the offer. When Operator mandatorily
            collects product tax codes on offers, required at offer creation and update. When Operator optionally collects
            product tax codes on offers, if no value is provided at offer update, existing data will be deleted.
        quantity (Union[Unset, int]): Quantity available of the offer. Offer update: if not provided, will be set to 0.
        retail_prices (Union[Unset, list['OF24RequestOffersRetailPrices']]): The retail prices of the offer, also
            referred to as selling prices. Applicable only for Dropship offers.
        shop_sku (Union[Unset, str]): Sku of the offer
        state_code (Union[Unset, str]): State of the offer
        update_delete (Union[Unset, str]): Update delete flag. Could be empty (means "update"), "update" or "delete".
    """

    all_prices: Union[Unset, list["OF24RequestOffersAllPrices"]] = UNSET
    allow_quote_requests: Union[Unset, bool] = UNSET
    available_ended: Union[Unset, str] = UNSET
    available_started: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    discount: Union[Unset, "OF24RequestOffersDiscount"] = UNSET
    eco_contributions: Union[Unset, list["OF24RequestOffersEcoContributions"]] = UNSET
    internal_description: Union[Unset, str] = UNSET
    leadtime_to_ship: Union[Unset, int] = UNSET
    logistic_class: Union[Unset, str] = UNSET
    max_order_quantity: Union[Unset, int] = UNSET
    min_order_quantity: Union[Unset, int] = UNSET
    min_quantity_alert: Union[Unset, int] = UNSET
    msrp: Union[Unset, float] = UNSET
    offer_additional_fields: Union[Unset, list["OF24RequestOffersOfferAdditionalFields"]] = UNSET
    package_quantity: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    price_additional_info: Union[Unset, str] = UNSET
    pricing_unit: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    product_id_type: Union[Unset, str] = UNSET
    product_tax_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    retail_prices: Union[Unset, list["OF24RequestOffersRetailPrices"]] = UNSET
    shop_sku: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    update_delete: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.all_prices, Unset):
            all_prices = []
            for all_prices_item_data in self.all_prices:
                all_prices_item = all_prices_item_data.to_dict()
                all_prices.append(all_prices_item)

        allow_quote_requests = self.allow_quote_requests

        available_ended = self.available_ended

        available_started = self.available_started

        description = self.description

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        internal_description = self.internal_description

        leadtime_to_ship = self.leadtime_to_ship

        logistic_class = self.logistic_class

        max_order_quantity = self.max_order_quantity

        min_order_quantity = self.min_order_quantity

        min_quantity_alert = self.min_quantity_alert

        msrp = self.msrp

        offer_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offer_additional_fields, Unset):
            offer_additional_fields = []
            for offer_additional_fields_item_data in self.offer_additional_fields:
                offer_additional_fields_item = offer_additional_fields_item_data.to_dict()
                offer_additional_fields.append(offer_additional_fields_item)

        package_quantity = self.package_quantity

        price = self.price

        price_additional_info = self.price_additional_info

        pricing_unit = self.pricing_unit

        product_id = self.product_id

        product_id_type = self.product_id_type

        product_tax_code = self.product_tax_code

        quantity = self.quantity

        retail_prices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retail_prices, Unset):
            retail_prices = []
            for retail_prices_item_data in self.retail_prices:
                retail_prices_item = retail_prices_item_data.to_dict()
                retail_prices.append(retail_prices_item)

        shop_sku = self.shop_sku

        state_code = self.state_code

        update_delete = self.update_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_prices is not UNSET:
            field_dict["all_prices"] = all_prices
        if allow_quote_requests is not UNSET:
            field_dict["allow_quote_requests"] = allow_quote_requests
        if available_ended is not UNSET:
            field_dict["available_ended"] = available_ended
        if available_started is not UNSET:
            field_dict["available_started"] = available_started
        if description is not UNSET:
            field_dict["description"] = description
        if discount is not UNSET:
            field_dict["discount"] = discount
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
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
        if msrp is not UNSET:
            field_dict["msrp"] = msrp
        if offer_additional_fields is not UNSET:
            field_dict["offer_additional_fields"] = offer_additional_fields
        if package_quantity is not UNSET:
            field_dict["package_quantity"] = package_quantity
        if price is not UNSET:
            field_dict["price"] = price
        if price_additional_info is not UNSET:
            field_dict["price_additional_info"] = price_additional_info
        if pricing_unit is not UNSET:
            field_dict["pricing_unit"] = pricing_unit
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_id_type is not UNSET:
            field_dict["product_id_type"] = product_id_type
        if product_tax_code is not UNSET:
            field_dict["product_tax_code"] = product_tax_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if retail_prices is not UNSET:
            field_dict["retail_prices"] = retail_prices
        if shop_sku is not UNSET:
            field_dict["shop_sku"] = shop_sku
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if update_delete is not UNSET:
            field_dict["update_delete"] = update_delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of24_request_offers_all_prices import OF24RequestOffersAllPrices
        from ..models.of24_request_offers_discount import OF24RequestOffersDiscount
        from ..models.of24_request_offers_eco_contributions import OF24RequestOffersEcoContributions
        from ..models.of24_request_offers_offer_additional_fields import OF24RequestOffersOfferAdditionalFields
        from ..models.of24_request_offers_retail_prices import OF24RequestOffersRetailPrices

        d = dict(src_dict)
        all_prices = []
        _all_prices = d.pop("all_prices", UNSET)
        for all_prices_item_data in _all_prices or []:
            all_prices_item = OF24RequestOffersAllPrices.from_dict(all_prices_item_data)

            all_prices.append(all_prices_item)

        allow_quote_requests = d.pop("allow_quote_requests", UNSET)

        available_ended = d.pop("available_ended", UNSET)

        available_started = d.pop("available_started", UNSET)

        description = d.pop("description", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, OF24RequestOffersDiscount]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = OF24RequestOffersDiscount.from_dict(_discount)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OF24RequestOffersEcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        internal_description = d.pop("internal_description", UNSET)

        leadtime_to_ship = d.pop("leadtime_to_ship", UNSET)

        logistic_class = d.pop("logistic_class", UNSET)

        max_order_quantity = d.pop("max_order_quantity", UNSET)

        min_order_quantity = d.pop("min_order_quantity", UNSET)

        min_quantity_alert = d.pop("min_quantity_alert", UNSET)

        msrp = d.pop("msrp", UNSET)

        offer_additional_fields = []
        _offer_additional_fields = d.pop("offer_additional_fields", UNSET)
        for offer_additional_fields_item_data in _offer_additional_fields or []:
            offer_additional_fields_item = OF24RequestOffersOfferAdditionalFields.from_dict(
                offer_additional_fields_item_data
            )

            offer_additional_fields.append(offer_additional_fields_item)

        package_quantity = d.pop("package_quantity", UNSET)

        price = d.pop("price", UNSET)

        price_additional_info = d.pop("price_additional_info", UNSET)

        pricing_unit = d.pop("pricing_unit", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_id_type = d.pop("product_id_type", UNSET)

        product_tax_code = d.pop("product_tax_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        retail_prices = []
        _retail_prices = d.pop("retail_prices", UNSET)
        for retail_prices_item_data in _retail_prices or []:
            retail_prices_item = OF24RequestOffersRetailPrices.from_dict(retail_prices_item_data)

            retail_prices.append(retail_prices_item)

        shop_sku = d.pop("shop_sku", UNSET)

        state_code = d.pop("state_code", UNSET)

        update_delete = d.pop("update_delete", UNSET)

        of24_request_offers = cls(
            all_prices=all_prices,
            allow_quote_requests=allow_quote_requests,
            available_ended=available_ended,
            available_started=available_started,
            description=description,
            discount=discount,
            eco_contributions=eco_contributions,
            internal_description=internal_description,
            leadtime_to_ship=leadtime_to_ship,
            logistic_class=logistic_class,
            max_order_quantity=max_order_quantity,
            min_order_quantity=min_order_quantity,
            min_quantity_alert=min_quantity_alert,
            msrp=msrp,
            offer_additional_fields=offer_additional_fields,
            package_quantity=package_quantity,
            price=price,
            price_additional_info=price_additional_info,
            pricing_unit=pricing_unit,
            product_id=product_id,
            product_id_type=product_id_type,
            product_tax_code=product_tax_code,
            quantity=quantity,
            retail_prices=retail_prices,
            shop_sku=shop_sku,
            state_code=state_code,
            update_delete=update_delete,
        )

        of24_request_offers.additional_properties = d
        return of24_request_offers

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
