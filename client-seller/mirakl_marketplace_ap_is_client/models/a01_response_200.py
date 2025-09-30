import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a01_response_200_applicable_taxes import A01Response200ApplicableTaxes
    from ..models.a01_response_200_billing_info import A01Response200BillingInfo
    from ..models.a01_response_200_contact_informations import A01Response200ContactInformations
    from ..models.a01_response_200_default_billing_information import A01Response200DefaultBillingInformation
    from ..models.a01_response_200_kyc import A01Response200Kyc
    from ..models.a01_response_200_payment_details import A01Response200PaymentDetails
    from ..models.a01_response_200_payment_info import A01Response200PaymentInfo
    from ..models.a01_response_200_pro_details import A01Response200ProDetails
    from ..models.a01_response_200_producer_identifiers import A01Response200ProducerIdentifiers
    from ..models.a01_response_200_shipping import A01Response200Shipping
    from ..models.a01_response_200_shippings import A01Response200Shippings
    from ..models.a01_response_200_shop_additional_fields import A01Response200ShopAdditionalFields
    from ..models.a01_response_200_specific_billing_informations import A01Response200SpecificBillingInformations


T = TypeVar("T", bound="A01Response200")


@_attrs_define
class A01Response200:
    """
    Attributes:
        applicable_taxes (Union[Unset, list['A01Response200ApplicableTaxes']]): List of the shop's applicable taxes
        approval_delay (Union[Unset, int]): Average time for a shop to accept or refuse an order (in seconds)
        approval_rate (Union[Unset, float]): Rate of accepted orders
        banner (Union[Unset, str]): Url of the shop's banner image
        billing_info (Union[Unset, A01Response200BillingInfo]):
        channels (Union[Unset, list[str]]): List of the channel codes associated to the shop
        closed_from (Union[Unset, datetime.datetime]): The start date of the closing of the shop
        closed_to (Union[Unset, datetime.datetime]): The end date of the closing of the shop
        contact_informations (Union[Unset, A01Response200ContactInformations]):
        currency_iso_code (Union[Unset, str]): The currency of the shop (iso format)
        date_created (Union[Unset, datetime.datetime]): Creation date of the shop
        default_billing_information (Union[Unset, A01Response200DefaultBillingInformation]):
        description (Union[Unset, str]): The description of the shop, max length: 3000 characters.
        domains (Union[Unset, list[str]]): Shop domains
        evaluations_count (Union[Unset, int]): Number of evaluations for the shop
        free_shipping (Union[Unset, bool]): Whether or not this shop offers free shipping to customers
        grade (Union[Unset, float]): Global grade of the shop
        is_professional (Union[Unset, bool]): Whether or not the shop is professional
        kyc (Union[Unset, A01Response200Kyc]):
        last_updated_date (Union[Unset, datetime.datetime]): The date of the last modification of the shop.
            Note: The following statistics fields do not update the <code>last_updated</code> date:
            <ul>
                <li><code>orders_count</code></li>
                <li><code>offers_count</code></li>
                <li><code>evaluations_count</code></li>
                <li><code>grade</code></li>
                <li><code>approval_rate</code></li>
                <li><code>approval_delay</code></li>
                <li><code>order_messages_response_delay</code></li>
            </ul>
        logo (Union[Unset, str]): Url of the shop's logo image
        model (Union[Unset, str]): Shop platform model, current possible values :
            <ul>
                <li><code>MARKETPLACE</code></li>
                <li><code>DROPSHIP</code></li>
                <li><code>ONE_CREDITOR</code></li>
            </ul>
        offers_count (Union[Unset, int]): Total count of active offers of the shop
        order_messages_response_delay (Union[Unset, int]): Average time for a shop to answer to an order message (in
            seconds)
        orders_count (Union[Unset, int]): Total count of debited orders (or if Pay on Delivery, accepted) of the shop
        payment_details (Union[Unset, A01Response200PaymentDetails]):
        payment_info (Union[Unset, A01Response200PaymentInfo]):
        payment_method_mandatory (Union[Unset, bool]): Payment method mandatory
        premium (Union[Unset, bool]): Whether or not the shop is premium
        pro_details (Union[Unset, A01Response200ProDetails]):
        producer_identifiers (Union[Unset, list['A01Response200ProducerIdentifiers']]): List of shop’s producer
            identifiers per Extended Producer Responsibility (EPR) categories. Only available if the operator setting
            <em>Activate data collection related to circular economy regulations</em> is enabled.
        recycling_policy (Union[Unset, str]): Recycling policy - only available if the operator setting <em>Activate
            data collection related to circular economy regulations</em> has been enabled.
        return_policy (Union[Unset, str]): Terms of restitution, max length: 60000 characters.
        shipping (Union[Unset, A01Response200Shipping]):
        shipping_country (Union[Unset, str]): Code ISO 3166-1 alpha-3 of the shipping country
        shipping_types (Union[Unset, list[str]]): List of shipping types of the shop
        shipping_zones (Union[Unset, list[str]]): List of shipping zones of the shop
        shippings (Union[Unset, list['A01Response200Shippings']]): All the pair shipping zone / shipping type accepted
            by the shop
        shop_additional_fields (Union[Unset, list['A01Response200ShopAdditionalFields']]): List of additional fields
        shop_id (Union[Unset, int]): The identifier of the shop
        shop_name (Union[Unset, str]): The name of the shop
        shop_state (Union[Unset, str]): The state of the shop
        specific_billing_informations (Union[Unset, list['A01Response200SpecificBillingInformations']]): The list of
            specific billing information of the shop, used for invoicing and reporting purposes
            <br/><i>Applies only when the shop is <code>professional</code></i>
        suspension_type (Union[Unset, str]): Shop suspension type, current possible values:<ul><li><code>MANUAL</code>:
            Shop account has been manually suspended in the back-office</li><li><code>PENDING_APPROVAL</code>: Shop account
            has been suspended at creation</li><li><code>AUTOMATIC_SUSPENSION</code>: Shop account has been suspended by
            Mirakl Quality Control</li><li><code>INCOMPLETE_PROFILE</code>: Shop account is suspended because some mandatory
            fields are missing in its profile</li></ul>
    """

    applicable_taxes: Union[Unset, list["A01Response200ApplicableTaxes"]] = UNSET
    approval_delay: Union[Unset, int] = UNSET
    approval_rate: Union[Unset, float] = UNSET
    banner: Union[Unset, str] = UNSET
    billing_info: Union[Unset, "A01Response200BillingInfo"] = UNSET
    channels: Union[Unset, list[str]] = UNSET
    closed_from: Union[Unset, datetime.datetime] = UNSET
    closed_to: Union[Unset, datetime.datetime] = UNSET
    contact_informations: Union[Unset, "A01Response200ContactInformations"] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    default_billing_information: Union[Unset, "A01Response200DefaultBillingInformation"] = UNSET
    description: Union[Unset, str] = UNSET
    domains: Union[Unset, list[str]] = UNSET
    evaluations_count: Union[Unset, int] = UNSET
    free_shipping: Union[Unset, bool] = UNSET
    grade: Union[Unset, float] = UNSET
    is_professional: Union[Unset, bool] = UNSET
    kyc: Union[Unset, "A01Response200Kyc"] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    logo: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    offers_count: Union[Unset, int] = UNSET
    order_messages_response_delay: Union[Unset, int] = UNSET
    orders_count: Union[Unset, int] = UNSET
    payment_details: Union[Unset, "A01Response200PaymentDetails"] = UNSET
    payment_info: Union[Unset, "A01Response200PaymentInfo"] = UNSET
    payment_method_mandatory: Union[Unset, bool] = UNSET
    premium: Union[Unset, bool] = UNSET
    pro_details: Union[Unset, "A01Response200ProDetails"] = UNSET
    producer_identifiers: Union[Unset, list["A01Response200ProducerIdentifiers"]] = UNSET
    recycling_policy: Union[Unset, str] = UNSET
    return_policy: Union[Unset, str] = UNSET
    shipping: Union[Unset, "A01Response200Shipping"] = UNSET
    shipping_country: Union[Unset, str] = UNSET
    shipping_types: Union[Unset, list[str]] = UNSET
    shipping_zones: Union[Unset, list[str]] = UNSET
    shippings: Union[Unset, list["A01Response200Shippings"]] = UNSET
    shop_additional_fields: Union[Unset, list["A01Response200ShopAdditionalFields"]] = UNSET
    shop_id: Union[Unset, int] = UNSET
    shop_name: Union[Unset, str] = UNSET
    shop_state: Union[Unset, str] = UNSET
    specific_billing_informations: Union[Unset, list["A01Response200SpecificBillingInformations"]] = UNSET
    suspension_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applicable_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.applicable_taxes, Unset):
            applicable_taxes = []
            for applicable_taxes_item_data in self.applicable_taxes:
                applicable_taxes_item = applicable_taxes_item_data.to_dict()
                applicable_taxes.append(applicable_taxes_item)

        approval_delay = self.approval_delay

        approval_rate = self.approval_rate

        banner = self.banner

        billing_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_info, Unset):
            billing_info = self.billing_info.to_dict()

        channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        closed_from: Union[Unset, str] = UNSET
        if not isinstance(self.closed_from, Unset):
            closed_from = self.closed_from.isoformat()

        closed_to: Union[Unset, str] = UNSET
        if not isinstance(self.closed_to, Unset):
            closed_to = self.closed_to.isoformat()

        contact_informations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact_informations, Unset):
            contact_informations = self.contact_informations.to_dict()

        currency_iso_code = self.currency_iso_code

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        default_billing_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_billing_information, Unset):
            default_billing_information = self.default_billing_information.to_dict()

        description = self.description

        domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        evaluations_count = self.evaluations_count

        free_shipping = self.free_shipping

        grade = self.grade

        is_professional = self.is_professional

        kyc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kyc, Unset):
            kyc = self.kyc.to_dict()

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        logo = self.logo

        model = self.model

        offers_count = self.offers_count

        order_messages_response_delay = self.order_messages_response_delay

        orders_count = self.orders_count

        payment_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_details, Unset):
            payment_details = self.payment_details.to_dict()

        payment_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_info, Unset):
            payment_info = self.payment_info.to_dict()

        payment_method_mandatory = self.payment_method_mandatory

        premium = self.premium

        pro_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pro_details, Unset):
            pro_details = self.pro_details.to_dict()

        producer_identifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.producer_identifiers, Unset):
            producer_identifiers = []
            for producer_identifiers_item_data in self.producer_identifiers:
                producer_identifiers_item = producer_identifiers_item_data.to_dict()
                producer_identifiers.append(producer_identifiers_item)

        recycling_policy = self.recycling_policy

        return_policy = self.return_policy

        shipping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        shipping_country = self.shipping_country

        shipping_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shipping_types, Unset):
            shipping_types = self.shipping_types

        shipping_zones: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shipping_zones, Unset):
            shipping_zones = self.shipping_zones

        shippings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shippings, Unset):
            shippings = []
            for shippings_item_data in self.shippings:
                shippings_item = shippings_item_data.to_dict()
                shippings.append(shippings_item)

        shop_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shop_additional_fields, Unset):
            shop_additional_fields = []
            for shop_additional_fields_item_data in self.shop_additional_fields:
                shop_additional_fields_item = shop_additional_fields_item_data.to_dict()
                shop_additional_fields.append(shop_additional_fields_item)

        shop_id = self.shop_id

        shop_name = self.shop_name

        shop_state = self.shop_state

        specific_billing_informations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.specific_billing_informations, Unset):
            specific_billing_informations = []
            for specific_billing_informations_item_data in self.specific_billing_informations:
                specific_billing_informations_item = specific_billing_informations_item_data.to_dict()
                specific_billing_informations.append(specific_billing_informations_item)

        suspension_type = self.suspension_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applicable_taxes is not UNSET:
            field_dict["applicable_taxes"] = applicable_taxes
        if approval_delay is not UNSET:
            field_dict["approval_delay"] = approval_delay
        if approval_rate is not UNSET:
            field_dict["approval_rate"] = approval_rate
        if banner is not UNSET:
            field_dict["banner"] = banner
        if billing_info is not UNSET:
            field_dict["billing_info"] = billing_info
        if channels is not UNSET:
            field_dict["channels"] = channels
        if closed_from is not UNSET:
            field_dict["closed_from"] = closed_from
        if closed_to is not UNSET:
            field_dict["closed_to"] = closed_to
        if contact_informations is not UNSET:
            field_dict["contact_informations"] = contact_informations
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if default_billing_information is not UNSET:
            field_dict["default_billing_information"] = default_billing_information
        if description is not UNSET:
            field_dict["description"] = description
        if domains is not UNSET:
            field_dict["domains"] = domains
        if evaluations_count is not UNSET:
            field_dict["evaluations_count"] = evaluations_count
        if free_shipping is not UNSET:
            field_dict["free_shipping"] = free_shipping
        if grade is not UNSET:
            field_dict["grade"] = grade
        if is_professional is not UNSET:
            field_dict["is_professional"] = is_professional
        if kyc is not UNSET:
            field_dict["kyc"] = kyc
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if logo is not UNSET:
            field_dict["logo"] = logo
        if model is not UNSET:
            field_dict["model"] = model
        if offers_count is not UNSET:
            field_dict["offers_count"] = offers_count
        if order_messages_response_delay is not UNSET:
            field_dict["order_messages_response_delay"] = order_messages_response_delay
        if orders_count is not UNSET:
            field_dict["orders_count"] = orders_count
        if payment_details is not UNSET:
            field_dict["payment_details"] = payment_details
        if payment_info is not UNSET:
            field_dict["payment_info"] = payment_info
        if payment_method_mandatory is not UNSET:
            field_dict["payment_method_mandatory"] = payment_method_mandatory
        if premium is not UNSET:
            field_dict["premium"] = premium
        if pro_details is not UNSET:
            field_dict["pro_details"] = pro_details
        if producer_identifiers is not UNSET:
            field_dict["producer_identifiers"] = producer_identifiers
        if recycling_policy is not UNSET:
            field_dict["recycling_policy"] = recycling_policy
        if return_policy is not UNSET:
            field_dict["return_policy"] = return_policy
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if shipping_country is not UNSET:
            field_dict["shipping_country"] = shipping_country
        if shipping_types is not UNSET:
            field_dict["shipping_types"] = shipping_types
        if shipping_zones is not UNSET:
            field_dict["shipping_zones"] = shipping_zones
        if shippings is not UNSET:
            field_dict["shippings"] = shippings
        if shop_additional_fields is not UNSET:
            field_dict["shop_additional_fields"] = shop_additional_fields
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if shop_state is not UNSET:
            field_dict["shop_state"] = shop_state
        if specific_billing_informations is not UNSET:
            field_dict["specific_billing_informations"] = specific_billing_informations
        if suspension_type is not UNSET:
            field_dict["suspension_type"] = suspension_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a01_response_200_applicable_taxes import A01Response200ApplicableTaxes
        from ..models.a01_response_200_billing_info import A01Response200BillingInfo
        from ..models.a01_response_200_contact_informations import A01Response200ContactInformations
        from ..models.a01_response_200_default_billing_information import A01Response200DefaultBillingInformation
        from ..models.a01_response_200_kyc import A01Response200Kyc
        from ..models.a01_response_200_payment_details import A01Response200PaymentDetails
        from ..models.a01_response_200_payment_info import A01Response200PaymentInfo
        from ..models.a01_response_200_pro_details import A01Response200ProDetails
        from ..models.a01_response_200_producer_identifiers import A01Response200ProducerIdentifiers
        from ..models.a01_response_200_shipping import A01Response200Shipping
        from ..models.a01_response_200_shippings import A01Response200Shippings
        from ..models.a01_response_200_shop_additional_fields import A01Response200ShopAdditionalFields
        from ..models.a01_response_200_specific_billing_informations import A01Response200SpecificBillingInformations

        d = dict(src_dict)
        applicable_taxes = []
        _applicable_taxes = d.pop("applicable_taxes", UNSET)
        for applicable_taxes_item_data in _applicable_taxes or []:
            applicable_taxes_item = A01Response200ApplicableTaxes.from_dict(applicable_taxes_item_data)

            applicable_taxes.append(applicable_taxes_item)

        approval_delay = d.pop("approval_delay", UNSET)

        approval_rate = d.pop("approval_rate", UNSET)

        banner = d.pop("banner", UNSET)

        _billing_info = d.pop("billing_info", UNSET)
        billing_info: Union[Unset, A01Response200BillingInfo]
        if isinstance(_billing_info, Unset):
            billing_info = UNSET
        else:
            billing_info = A01Response200BillingInfo.from_dict(_billing_info)

        channels = cast(list[str], d.pop("channels", UNSET))

        _closed_from = d.pop("closed_from", UNSET)
        closed_from: Union[Unset, datetime.datetime]
        if isinstance(_closed_from, Unset):
            closed_from = UNSET
        else:
            closed_from = isoparse(_closed_from)

        _closed_to = d.pop("closed_to", UNSET)
        closed_to: Union[Unset, datetime.datetime]
        if isinstance(_closed_to, Unset):
            closed_to = UNSET
        else:
            closed_to = isoparse(_closed_to)

        _contact_informations = d.pop("contact_informations", UNSET)
        contact_informations: Union[Unset, A01Response200ContactInformations]
        if isinstance(_contact_informations, Unset):
            contact_informations = UNSET
        else:
            contact_informations = A01Response200ContactInformations.from_dict(_contact_informations)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _default_billing_information = d.pop("default_billing_information", UNSET)
        default_billing_information: Union[Unset, A01Response200DefaultBillingInformation]
        if isinstance(_default_billing_information, Unset):
            default_billing_information = UNSET
        else:
            default_billing_information = A01Response200DefaultBillingInformation.from_dict(
                _default_billing_information
            )

        description = d.pop("description", UNSET)

        domains = cast(list[str], d.pop("domains", UNSET))

        evaluations_count = d.pop("evaluations_count", UNSET)

        free_shipping = d.pop("free_shipping", UNSET)

        grade = d.pop("grade", UNSET)

        is_professional = d.pop("is_professional", UNSET)

        _kyc = d.pop("kyc", UNSET)
        kyc: Union[Unset, A01Response200Kyc]
        if isinstance(_kyc, Unset):
            kyc = UNSET
        else:
            kyc = A01Response200Kyc.from_dict(_kyc)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        logo = d.pop("logo", UNSET)

        model = d.pop("model", UNSET)

        offers_count = d.pop("offers_count", UNSET)

        order_messages_response_delay = d.pop("order_messages_response_delay", UNSET)

        orders_count = d.pop("orders_count", UNSET)

        _payment_details = d.pop("payment_details", UNSET)
        payment_details: Union[Unset, A01Response200PaymentDetails]
        if isinstance(_payment_details, Unset):
            payment_details = UNSET
        else:
            payment_details = A01Response200PaymentDetails.from_dict(_payment_details)

        _payment_info = d.pop("payment_info", UNSET)
        payment_info: Union[Unset, A01Response200PaymentInfo]
        if isinstance(_payment_info, Unset):
            payment_info = UNSET
        else:
            payment_info = A01Response200PaymentInfo.from_dict(_payment_info)

        payment_method_mandatory = d.pop("payment_method_mandatory", UNSET)

        premium = d.pop("premium", UNSET)

        _pro_details = d.pop("pro_details", UNSET)
        pro_details: Union[Unset, A01Response200ProDetails]
        if isinstance(_pro_details, Unset):
            pro_details = UNSET
        else:
            pro_details = A01Response200ProDetails.from_dict(_pro_details)

        producer_identifiers = []
        _producer_identifiers = d.pop("producer_identifiers", UNSET)
        for producer_identifiers_item_data in _producer_identifiers or []:
            producer_identifiers_item = A01Response200ProducerIdentifiers.from_dict(producer_identifiers_item_data)

            producer_identifiers.append(producer_identifiers_item)

        recycling_policy = d.pop("recycling_policy", UNSET)

        return_policy = d.pop("return_policy", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, A01Response200Shipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = A01Response200Shipping.from_dict(_shipping)

        shipping_country = d.pop("shipping_country", UNSET)

        shipping_types = cast(list[str], d.pop("shipping_types", UNSET))

        shipping_zones = cast(list[str], d.pop("shipping_zones", UNSET))

        shippings = []
        _shippings = d.pop("shippings", UNSET)
        for shippings_item_data in _shippings or []:
            shippings_item = A01Response200Shippings.from_dict(shippings_item_data)

            shippings.append(shippings_item)

        shop_additional_fields = []
        _shop_additional_fields = d.pop("shop_additional_fields", UNSET)
        for shop_additional_fields_item_data in _shop_additional_fields or []:
            shop_additional_fields_item = A01Response200ShopAdditionalFields.from_dict(shop_additional_fields_item_data)

            shop_additional_fields.append(shop_additional_fields_item)

        shop_id = d.pop("shop_id", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        shop_state = d.pop("shop_state", UNSET)

        specific_billing_informations = []
        _specific_billing_informations = d.pop("specific_billing_informations", UNSET)
        for specific_billing_informations_item_data in _specific_billing_informations or []:
            specific_billing_informations_item = A01Response200SpecificBillingInformations.from_dict(
                specific_billing_informations_item_data
            )

            specific_billing_informations.append(specific_billing_informations_item)

        suspension_type = d.pop("suspension_type", UNSET)

        a01_response_200 = cls(
            applicable_taxes=applicable_taxes,
            approval_delay=approval_delay,
            approval_rate=approval_rate,
            banner=banner,
            billing_info=billing_info,
            channels=channels,
            closed_from=closed_from,
            closed_to=closed_to,
            contact_informations=contact_informations,
            currency_iso_code=currency_iso_code,
            date_created=date_created,
            default_billing_information=default_billing_information,
            description=description,
            domains=domains,
            evaluations_count=evaluations_count,
            free_shipping=free_shipping,
            grade=grade,
            is_professional=is_professional,
            kyc=kyc,
            last_updated_date=last_updated_date,
            logo=logo,
            model=model,
            offers_count=offers_count,
            order_messages_response_delay=order_messages_response_delay,
            orders_count=orders_count,
            payment_details=payment_details,
            payment_info=payment_info,
            payment_method_mandatory=payment_method_mandatory,
            premium=premium,
            pro_details=pro_details,
            producer_identifiers=producer_identifiers,
            recycling_policy=recycling_policy,
            return_policy=return_policy,
            shipping=shipping,
            shipping_country=shipping_country,
            shipping_types=shipping_types,
            shipping_zones=shipping_zones,
            shippings=shippings,
            shop_additional_fields=shop_additional_fields,
            shop_id=shop_id,
            shop_name=shop_name,
            shop_state=shop_state,
            specific_billing_informations=specific_billing_informations,
            suspension_type=suspension_type,
        )

        a01_response_200.additional_properties = d
        return a01_response_200

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
