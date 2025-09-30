from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_features_catalog import PC01Response200FeaturesCatalog
    from ..models.pc01_response_200_features_direct_payment_customer_store import (
        PC01Response200FeaturesDirectPaymentCustomerStore,
    )
    from ..models.pc01_response_200_features_order_conditions import PC01Response200FeaturesOrderConditions
    from ..models.pc01_response_200_features_order_workflows import PC01Response200FeaturesOrderWorkflows
    from ..models.pc01_response_200_features_pricing import PC01Response200FeaturesPricing
    from ..models.pc01_response_200_features_shipment import PC01Response200FeaturesShipment
    from ..models.pc01_response_200_features_shop_tax_options import PC01Response200FeaturesShopTaxOptions
    from ..models.pc01_response_200_features_tax_collection import PC01Response200FeaturesTaxCollection
    from ..models.pc01_response_200_features_tax_id_number import PC01Response200FeaturesTaxIdNumber


T = TypeVar("T", bound="PC01Response200Features")


@_attrs_define
class PC01Response200Features:
    """
    Attributes:
        catalog (Union[Unset, PC01Response200FeaturesCatalog]):
        circular_economy_data_collection (Union[Unset, bool]): Allows operators to collect data related to the circular
            economy regulation
        competitive_pricing_tool (Union[Unset, bool]): The competitive pricing tool allows stores to view and possibly
            match competing Marketplace offers
        direct_payment_customer_store (Union[Unset, PC01Response200FeaturesDirectPaymentCustomerStore]):
        disable_seller_alternative_carrier (Union[Unset, bool]): Prevent stores from specifying alternatives carriers
            outside those predefined by the operator
        kyc_status_per_seller (Union[Unset, bool]): Allows PSPs to provide operators with seller KYC statuses
        lead_time_to_ship_by_sellers_enabled (Union[Unset, str]): Allows sellers to override the default lead time to
            ship
        multi_currency (Union[Unset, bool]): Defines if platform support multi currencies
        no_reply_needed (Union[Unset, bool]): Allows to end order-related conversations when the last message sent from
            customer does not specifically require a reply
        offer_prices_decimals (Union[Unset, str]): Defines maximum number of decimals in offer prices
        operator_csv_delimiter (Union[Unset, str]): The delimiter used in the CSV files exported from the back office.
            COMMA: ',' delimiter. SEMICOLON: ';' delimiter.
        order_conditions (Union[Unset, PC01Response200FeaturesOrderConditions]):
        order_tax_mode (Union[Unset, str]): Prices with tax included or excluded in order-related APIs. TAX_INCLUDED:
            Prices with tax included. TAX_EXCLUDED: Prices with tax excluded.
        order_workflows (Union[Unset, PC01Response200FeaturesOrderWorkflows]):
        payment_confirmation (Union[Unset, bool]): Allows the operator to mark an accounting document as "Paid" when the
            corresponding amount is confirmed to be paid to the seller
        pricing (Union[Unset, PC01Response200FeaturesPricing]):
        product_data_validation_by_channel (Union[Unset, bool]): Facilitates the management of attributes in a
            multilingual context
        shipment (Union[Unset, PC01Response200FeaturesShipment]):
        shop_tax_options (Union[Unset, PC01Response200FeaturesShopTaxOptions]):
        tax_collection (Union[Unset, PC01Response200FeaturesTaxCollection]):
        tax_id_number (Union[Unset, PC01Response200FeaturesTaxIdNumber]):
    """

    catalog: Union[Unset, "PC01Response200FeaturesCatalog"] = UNSET
    circular_economy_data_collection: Union[Unset, bool] = UNSET
    competitive_pricing_tool: Union[Unset, bool] = UNSET
    direct_payment_customer_store: Union[Unset, "PC01Response200FeaturesDirectPaymentCustomerStore"] = UNSET
    disable_seller_alternative_carrier: Union[Unset, bool] = UNSET
    kyc_status_per_seller: Union[Unset, bool] = UNSET
    lead_time_to_ship_by_sellers_enabled: Union[Unset, str] = UNSET
    multi_currency: Union[Unset, bool] = UNSET
    no_reply_needed: Union[Unset, bool] = UNSET
    offer_prices_decimals: Union[Unset, str] = UNSET
    operator_csv_delimiter: Union[Unset, str] = UNSET
    order_conditions: Union[Unset, "PC01Response200FeaturesOrderConditions"] = UNSET
    order_tax_mode: Union[Unset, str] = UNSET
    order_workflows: Union[Unset, "PC01Response200FeaturesOrderWorkflows"] = UNSET
    payment_confirmation: Union[Unset, bool] = UNSET
    pricing: Union[Unset, "PC01Response200FeaturesPricing"] = UNSET
    product_data_validation_by_channel: Union[Unset, bool] = UNSET
    shipment: Union[Unset, "PC01Response200FeaturesShipment"] = UNSET
    shop_tax_options: Union[Unset, "PC01Response200FeaturesShopTaxOptions"] = UNSET
    tax_collection: Union[Unset, "PC01Response200FeaturesTaxCollection"] = UNSET
    tax_id_number: Union[Unset, "PC01Response200FeaturesTaxIdNumber"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.catalog, Unset):
            catalog = self.catalog.to_dict()

        circular_economy_data_collection = self.circular_economy_data_collection

        competitive_pricing_tool = self.competitive_pricing_tool

        direct_payment_customer_store: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.direct_payment_customer_store, Unset):
            direct_payment_customer_store = self.direct_payment_customer_store.to_dict()

        disable_seller_alternative_carrier = self.disable_seller_alternative_carrier

        kyc_status_per_seller = self.kyc_status_per_seller

        lead_time_to_ship_by_sellers_enabled = self.lead_time_to_ship_by_sellers_enabled

        multi_currency = self.multi_currency

        no_reply_needed = self.no_reply_needed

        offer_prices_decimals = self.offer_prices_decimals

        operator_csv_delimiter = self.operator_csv_delimiter

        order_conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_conditions, Unset):
            order_conditions = self.order_conditions.to_dict()

        order_tax_mode = self.order_tax_mode

        order_workflows: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_workflows, Unset):
            order_workflows = self.order_workflows.to_dict()

        payment_confirmation = self.payment_confirmation

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        product_data_validation_by_channel = self.product_data_validation_by_channel

        shipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        shop_tax_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shop_tax_options, Unset):
            shop_tax_options = self.shop_tax_options.to_dict()

        tax_collection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_collection, Unset):
            tax_collection = self.tax_collection.to_dict()

        tax_id_number: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_id_number, Unset):
            tax_id_number = self.tax_id_number.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if circular_economy_data_collection is not UNSET:
            field_dict["circular_economy_data_collection"] = circular_economy_data_collection
        if competitive_pricing_tool is not UNSET:
            field_dict["competitive_pricing_tool"] = competitive_pricing_tool
        if direct_payment_customer_store is not UNSET:
            field_dict["direct_payment_customer_store"] = direct_payment_customer_store
        if disable_seller_alternative_carrier is not UNSET:
            field_dict["disable_seller_alternative_carrier"] = disable_seller_alternative_carrier
        if kyc_status_per_seller is not UNSET:
            field_dict["kyc_status_per_seller"] = kyc_status_per_seller
        if lead_time_to_ship_by_sellers_enabled is not UNSET:
            field_dict["lead_time_to_ship_by_sellers_enabled"] = lead_time_to_ship_by_sellers_enabled
        if multi_currency is not UNSET:
            field_dict["multi_currency"] = multi_currency
        if no_reply_needed is not UNSET:
            field_dict["no_reply_needed"] = no_reply_needed
        if offer_prices_decimals is not UNSET:
            field_dict["offer_prices_decimals"] = offer_prices_decimals
        if operator_csv_delimiter is not UNSET:
            field_dict["operator_csv_delimiter"] = operator_csv_delimiter
        if order_conditions is not UNSET:
            field_dict["order_conditions"] = order_conditions
        if order_tax_mode is not UNSET:
            field_dict["order_tax_mode"] = order_tax_mode
        if order_workflows is not UNSET:
            field_dict["order_workflows"] = order_workflows
        if payment_confirmation is not UNSET:
            field_dict["payment_confirmation"] = payment_confirmation
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if product_data_validation_by_channel is not UNSET:
            field_dict["product_data_validation_by_channel"] = product_data_validation_by_channel
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if shop_tax_options is not UNSET:
            field_dict["shop_tax_options"] = shop_tax_options
        if tax_collection is not UNSET:
            field_dict["tax_collection"] = tax_collection
        if tax_id_number is not UNSET:
            field_dict["tax_id_number"] = tax_id_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_features_catalog import PC01Response200FeaturesCatalog
        from ..models.pc01_response_200_features_direct_payment_customer_store import (
            PC01Response200FeaturesDirectPaymentCustomerStore,
        )
        from ..models.pc01_response_200_features_order_conditions import PC01Response200FeaturesOrderConditions
        from ..models.pc01_response_200_features_order_workflows import PC01Response200FeaturesOrderWorkflows
        from ..models.pc01_response_200_features_pricing import PC01Response200FeaturesPricing
        from ..models.pc01_response_200_features_shipment import PC01Response200FeaturesShipment
        from ..models.pc01_response_200_features_shop_tax_options import PC01Response200FeaturesShopTaxOptions
        from ..models.pc01_response_200_features_tax_collection import PC01Response200FeaturesTaxCollection
        from ..models.pc01_response_200_features_tax_id_number import PC01Response200FeaturesTaxIdNumber

        d = dict(src_dict)
        _catalog = d.pop("catalog", UNSET)
        catalog: Union[Unset, PC01Response200FeaturesCatalog]
        if isinstance(_catalog, Unset):
            catalog = UNSET
        else:
            catalog = PC01Response200FeaturesCatalog.from_dict(_catalog)

        circular_economy_data_collection = d.pop("circular_economy_data_collection", UNSET)

        competitive_pricing_tool = d.pop("competitive_pricing_tool", UNSET)

        _direct_payment_customer_store = d.pop("direct_payment_customer_store", UNSET)
        direct_payment_customer_store: Union[Unset, PC01Response200FeaturesDirectPaymentCustomerStore]
        if isinstance(_direct_payment_customer_store, Unset):
            direct_payment_customer_store = UNSET
        else:
            direct_payment_customer_store = PC01Response200FeaturesDirectPaymentCustomerStore.from_dict(
                _direct_payment_customer_store
            )

        disable_seller_alternative_carrier = d.pop("disable_seller_alternative_carrier", UNSET)

        kyc_status_per_seller = d.pop("kyc_status_per_seller", UNSET)

        lead_time_to_ship_by_sellers_enabled = d.pop("lead_time_to_ship_by_sellers_enabled", UNSET)

        multi_currency = d.pop("multi_currency", UNSET)

        no_reply_needed = d.pop("no_reply_needed", UNSET)

        offer_prices_decimals = d.pop("offer_prices_decimals", UNSET)

        operator_csv_delimiter = d.pop("operator_csv_delimiter", UNSET)

        _order_conditions = d.pop("order_conditions", UNSET)
        order_conditions: Union[Unset, PC01Response200FeaturesOrderConditions]
        if isinstance(_order_conditions, Unset):
            order_conditions = UNSET
        else:
            order_conditions = PC01Response200FeaturesOrderConditions.from_dict(_order_conditions)

        order_tax_mode = d.pop("order_tax_mode", UNSET)

        _order_workflows = d.pop("order_workflows", UNSET)
        order_workflows: Union[Unset, PC01Response200FeaturesOrderWorkflows]
        if isinstance(_order_workflows, Unset):
            order_workflows = UNSET
        else:
            order_workflows = PC01Response200FeaturesOrderWorkflows.from_dict(_order_workflows)

        payment_confirmation = d.pop("payment_confirmation", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, PC01Response200FeaturesPricing]
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = PC01Response200FeaturesPricing.from_dict(_pricing)

        product_data_validation_by_channel = d.pop("product_data_validation_by_channel", UNSET)

        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, PC01Response200FeaturesShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = PC01Response200FeaturesShipment.from_dict(_shipment)

        _shop_tax_options = d.pop("shop_tax_options", UNSET)
        shop_tax_options: Union[Unset, PC01Response200FeaturesShopTaxOptions]
        if isinstance(_shop_tax_options, Unset):
            shop_tax_options = UNSET
        else:
            shop_tax_options = PC01Response200FeaturesShopTaxOptions.from_dict(_shop_tax_options)

        _tax_collection = d.pop("tax_collection", UNSET)
        tax_collection: Union[Unset, PC01Response200FeaturesTaxCollection]
        if isinstance(_tax_collection, Unset):
            tax_collection = UNSET
        else:
            tax_collection = PC01Response200FeaturesTaxCollection.from_dict(_tax_collection)

        _tax_id_number = d.pop("tax_id_number", UNSET)
        tax_id_number: Union[Unset, PC01Response200FeaturesTaxIdNumber]
        if isinstance(_tax_id_number, Unset):
            tax_id_number = UNSET
        else:
            tax_id_number = PC01Response200FeaturesTaxIdNumber.from_dict(_tax_id_number)

        pc01_response_200_features = cls(
            catalog=catalog,
            circular_economy_data_collection=circular_economy_data_collection,
            competitive_pricing_tool=competitive_pricing_tool,
            direct_payment_customer_store=direct_payment_customer_store,
            disable_seller_alternative_carrier=disable_seller_alternative_carrier,
            kyc_status_per_seller=kyc_status_per_seller,
            lead_time_to_ship_by_sellers_enabled=lead_time_to_ship_by_sellers_enabled,
            multi_currency=multi_currency,
            no_reply_needed=no_reply_needed,
            offer_prices_decimals=offer_prices_decimals,
            operator_csv_delimiter=operator_csv_delimiter,
            order_conditions=order_conditions,
            order_tax_mode=order_tax_mode,
            order_workflows=order_workflows,
            payment_confirmation=payment_confirmation,
            pricing=pricing,
            product_data_validation_by_channel=product_data_validation_by_channel,
            shipment=shipment,
            shop_tax_options=shop_tax_options,
            tax_collection=tax_collection,
            tax_id_number=tax_id_number,
        )

        pc01_response_200_features.additional_properties = d
        return pc01_response_200_features

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
