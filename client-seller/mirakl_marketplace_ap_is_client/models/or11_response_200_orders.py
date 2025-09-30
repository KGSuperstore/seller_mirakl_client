import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_channel import OR11Response200OrdersChannel
    from ..models.or11_response_200_orders_customer import OR11Response200OrdersCustomer
    from ..models.or11_response_200_orders_delivery_date import OR11Response200OrdersDeliveryDate
    from ..models.or11_response_200_orders_fulfillment import OR11Response200OrdersFulfillment
    from ..models.or11_response_200_orders_invoice_details import OR11Response200OrdersInvoiceDetails
    from ..models.or11_response_200_orders_order_additional_fields import OR11Response200OrdersOrderAdditionalFields
    from ..models.or11_response_200_orders_order_lines import OR11Response200OrdersOrderLines
    from ..models.or11_response_200_orders_order_refunds import OR11Response200OrdersOrderRefunds
    from ..models.or11_response_200_orders_order_taxes import OR11Response200OrdersOrderTaxes
    from ..models.or11_response_200_orders_promotions import OR11Response200OrdersPromotions
    from ..models.or11_response_200_orders_references import OR11Response200OrdersReferences


T = TypeVar("T", bound="OR11Response200Orders")


@_attrs_define
class OR11Response200Orders:
    """
    Attributes:
        acceptance_decision_date (Union[Unset, datetime.datetime]): The date where the shop decided to accept or refuse
            the order. Null when the order was automatically refused or accepted.
        can_cancel (Union[Unset, bool]): Indicate if the order can be cancelled
        can_shop_ship (Union[Unset, bool]): Indicates if shops can or cannot ship orders
        channel (Union[Unset, OR11Response200OrdersChannel]):
        commercial_id (Union[Unset, str]): Commercial order's identifier
        created_date (Union[Unset, datetime.datetime]): Order's creation date
        currency_iso_code (Union[Unset, str]): Shop's currency (iso format)
        customer (Union[Unset, OR11Response200OrdersCustomer]):
        customer_debited_date (Union[Unset, datetime.datetime]): The payment's date of the order by the customer
        customer_directly_pays_seller (Union[Unset, bool]): True if order is paid directly to seller. False otherwise.
        customer_notification_email (Union[Unset, str]): Anonymized customer email usable for notifications that do not
            expect an answer
        delivery_date (Union[Unset, OR11Response200OrdersDeliveryDate]):
        fulfillment (Union[Unset, OR11Response200OrdersFulfillment]):
        fully_refunded (Union[Unset, bool]): Refunds have been requested and their cumulated amounts correspond to the
            sum of all remaining active order lines.
        has_customer_message (Union[Unset, bool]): Indicate if the customer has sent a message related to this order
        has_incident (Union[Unset, bool]): Indicate if order has incident on at least one order line
        has_invoice (Union[Unset, bool]): Is an invoice available for this order.
        invoice_details (Union[Unset, OR11Response200OrdersInvoiceDetails]):
        last_updated_date (Union[Unset, datetime.datetime]): Order's last updated date
        order_additional_fields (Union[Unset, list['OR11Response200OrdersOrderAdditionalFields']]): Order's custom
            fields
        order_id (Union[Unset, str]): Order's identifier
        order_lines (Union[Unset, list['OR11Response200OrdersOrderLines']]): Order lines
        order_refunds (Union[Unset, list['OR11Response200OrdersOrderRefunds']]): The list of refunds aggregated by group
            identifier<br/>Available when feature ‘order level tax calculation’ is enabled
        order_state (Union[Unset, str]): Order's state
        order_state_reason_code (Union[Unset, str]): Reason's code of the order state
        order_state_reason_label (Union[Unset, str]): Reason's label of the order state
        order_tax_mode (Union[Unset, str]): Please note: In case there is no tax, the prices will show the same amount
            in TAX_EXCLUDED and TAX_INCLUDED mode. The tax mode is only useful if taxes are specified in the
            order.<br>Possible values: <ul><li><code>TAX_EXCLUDED</code>: the price fields (price, unit price, shipping
            price, cancellation amount, refund amount and order total prices) are expressed without tax (taxes should be
            added to these prices in order to get the full amount including taxes).</li><li><code>TAX_INCLUDED</code>: the
            price fields include the tax amount. </li></ul>
        order_taxes (Union[Unset, list['OR11Response200OrdersOrderTaxes']]): Total amount of taxes aggregated per tax
            code and rate<br/>Available when feature ‘order level tax calculation’ is enabled
        payment_duration (Union[Unset, int]): The payment's duration (i.e. the delay after which the order is supposed
            to be paid), in days.<br/>Only applicable for <code>PAY_ON_DUE_DATE</code> orders, null otherwise.<br/>Note that
            this field has currently no impact on the order workflow, it is provided for information purposes.
        payment_type (Union[Unset, str]): The payment's type used by the customer to pay this order
        payment_workflow (Union[Unset, str]): The payment workflow followed by the order
        price (Union[Unset, float]): Order's price (sum of order line's price)
        promotions (Union[Unset, OR11Response200OrdersPromotions]):
        quote_id (Union[Unset, str]): Quote's id from which the order has been placed, or null if it was not from a
            quote
        references (Union[Unset, OR11Response200OrdersReferences]):
        shipping_carrier_code (Union[Unset, str]): Shipping carrier code (associated with the Shipping company label)
        shipping_carrier_standard_code (Union[Unset, str]): Shipping carrier standard code (associated with the shipping
            carrier code)
        shipping_company (Union[Unset, str]): Shipping company
        shipping_deadline (Union[Unset, datetime.datetime]): Order's shipping deadline
        shipping_price (Union[Unset, float]): Order's shipping price (sum of order line's shipping price)
        shipping_pudo_id (Union[Unset, str]): PickUp DropOff (PUDO) point identifier
        shipping_tracking (Union[Unset, str]): Shipping tracking
        shipping_tracking_url (Union[Unset, str]): Shipping tracking url
        shipping_type_code (Union[Unset, str]): Code of shipping's type
        shipping_type_label (Union[Unset, str]): Label of shipping's type
        shipping_type_standard_code (Union[Unset, str]): Shipping type's standard code
        shipping_zone_code (Union[Unset, str]): Code of shipping's zone
        shipping_zone_label (Union[Unset, str]): Label of shipping's zone
        total_commission (Union[Unset, float]): Order's total commission (sum of the order line's total commission)
        total_price (Union[Unset, float]): Total order's price (sum of the order's price with shipping price and fees).
        transaction_date (Union[Unset, datetime.datetime]): Payment's transaction date
        transaction_number (Union[Unset, str]): Payment's transaction number
    """

    acceptance_decision_date: Union[Unset, datetime.datetime] = UNSET
    can_cancel: Union[Unset, bool] = UNSET
    can_shop_ship: Union[Unset, bool] = UNSET
    channel: Union[Unset, "OR11Response200OrdersChannel"] = UNSET
    commercial_id: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    customer: Union[Unset, "OR11Response200OrdersCustomer"] = UNSET
    customer_debited_date: Union[Unset, datetime.datetime] = UNSET
    customer_directly_pays_seller: Union[Unset, bool] = UNSET
    customer_notification_email: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, "OR11Response200OrdersDeliveryDate"] = UNSET
    fulfillment: Union[Unset, "OR11Response200OrdersFulfillment"] = UNSET
    fully_refunded: Union[Unset, bool] = UNSET
    has_customer_message: Union[Unset, bool] = UNSET
    has_incident: Union[Unset, bool] = UNSET
    has_invoice: Union[Unset, bool] = UNSET
    invoice_details: Union[Unset, "OR11Response200OrdersInvoiceDetails"] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    order_additional_fields: Union[Unset, list["OR11Response200OrdersOrderAdditionalFields"]] = UNSET
    order_id: Union[Unset, str] = UNSET
    order_lines: Union[Unset, list["OR11Response200OrdersOrderLines"]] = UNSET
    order_refunds: Union[Unset, list["OR11Response200OrdersOrderRefunds"]] = UNSET
    order_state: Union[Unset, str] = UNSET
    order_state_reason_code: Union[Unset, str] = UNSET
    order_state_reason_label: Union[Unset, str] = UNSET
    order_tax_mode: Union[Unset, str] = UNSET
    order_taxes: Union[Unset, list["OR11Response200OrdersOrderTaxes"]] = UNSET
    payment_duration: Union[Unset, int] = UNSET
    payment_type: Union[Unset, str] = UNSET
    payment_workflow: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    promotions: Union[Unset, "OR11Response200OrdersPromotions"] = UNSET
    quote_id: Union[Unset, str] = UNSET
    references: Union[Unset, "OR11Response200OrdersReferences"] = UNSET
    shipping_carrier_code: Union[Unset, str] = UNSET
    shipping_carrier_standard_code: Union[Unset, str] = UNSET
    shipping_company: Union[Unset, str] = UNSET
    shipping_deadline: Union[Unset, datetime.datetime] = UNSET
    shipping_price: Union[Unset, float] = UNSET
    shipping_pudo_id: Union[Unset, str] = UNSET
    shipping_tracking: Union[Unset, str] = UNSET
    shipping_tracking_url: Union[Unset, str] = UNSET
    shipping_type_code: Union[Unset, str] = UNSET
    shipping_type_label: Union[Unset, str] = UNSET
    shipping_type_standard_code: Union[Unset, str] = UNSET
    shipping_zone_code: Union[Unset, str] = UNSET
    shipping_zone_label: Union[Unset, str] = UNSET
    total_commission: Union[Unset, float] = UNSET
    total_price: Union[Unset, float] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceptance_decision_date: Union[Unset, str] = UNSET
        if not isinstance(self.acceptance_decision_date, Unset):
            acceptance_decision_date = self.acceptance_decision_date.isoformat()

        can_cancel = self.can_cancel

        can_shop_ship = self.can_shop_ship

        channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        commercial_id = self.commercial_id

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        currency_iso_code = self.currency_iso_code

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        customer_debited_date: Union[Unset, str] = UNSET
        if not isinstance(self.customer_debited_date, Unset):
            customer_debited_date = self.customer_debited_date.isoformat()

        customer_directly_pays_seller = self.customer_directly_pays_seller

        customer_notification_email = self.customer_notification_email

        delivery_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.to_dict()

        fulfillment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()

        fully_refunded = self.fully_refunded

        has_customer_message = self.has_customer_message

        has_incident = self.has_incident

        has_invoice = self.has_invoice

        invoice_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.invoice_details, Unset):
            invoice_details = self.invoice_details.to_dict()

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        order_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_additional_fields, Unset):
            order_additional_fields = []
            for order_additional_fields_item_data in self.order_additional_fields:
                order_additional_fields_item = order_additional_fields_item_data.to_dict()
                order_additional_fields.append(order_additional_fields_item)

        order_id = self.order_id

        order_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            order_lines = []
            for order_lines_item_data in self.order_lines:
                order_lines_item = order_lines_item_data.to_dict()
                order_lines.append(order_lines_item)

        order_refunds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_refunds, Unset):
            order_refunds = []
            for order_refunds_item_data in self.order_refunds:
                order_refunds_item = order_refunds_item_data.to_dict()
                order_refunds.append(order_refunds_item)

        order_state = self.order_state

        order_state_reason_code = self.order_state_reason_code

        order_state_reason_label = self.order_state_reason_label

        order_tax_mode = self.order_tax_mode

        order_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_taxes, Unset):
            order_taxes = []
            for order_taxes_item_data in self.order_taxes:
                order_taxes_item = order_taxes_item_data.to_dict()
                order_taxes.append(order_taxes_item)

        payment_duration = self.payment_duration

        payment_type = self.payment_type

        payment_workflow = self.payment_workflow

        price = self.price

        promotions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.promotions, Unset):
            promotions = self.promotions.to_dict()

        quote_id = self.quote_id

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        shipping_carrier_code = self.shipping_carrier_code

        shipping_carrier_standard_code = self.shipping_carrier_standard_code

        shipping_company = self.shipping_company

        shipping_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_deadline, Unset):
            shipping_deadline = self.shipping_deadline.isoformat()

        shipping_price = self.shipping_price

        shipping_pudo_id = self.shipping_pudo_id

        shipping_tracking = self.shipping_tracking

        shipping_tracking_url = self.shipping_tracking_url

        shipping_type_code = self.shipping_type_code

        shipping_type_label = self.shipping_type_label

        shipping_type_standard_code = self.shipping_type_standard_code

        shipping_zone_code = self.shipping_zone_code

        shipping_zone_label = self.shipping_zone_label

        total_commission = self.total_commission

        total_price = self.total_price

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        transaction_number = self.transaction_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acceptance_decision_date is not UNSET:
            field_dict["acceptance_decision_date"] = acceptance_decision_date
        if can_cancel is not UNSET:
            field_dict["can_cancel"] = can_cancel
        if can_shop_ship is not UNSET:
            field_dict["can_shop_ship"] = can_shop_ship
        if channel is not UNSET:
            field_dict["channel"] = channel
        if commercial_id is not UNSET:
            field_dict["commercial_id"] = commercial_id
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if customer is not UNSET:
            field_dict["customer"] = customer
        if customer_debited_date is not UNSET:
            field_dict["customer_debited_date"] = customer_debited_date
        if customer_directly_pays_seller is not UNSET:
            field_dict["customer_directly_pays_seller"] = customer_directly_pays_seller
        if customer_notification_email is not UNSET:
            field_dict["customer_notification_email"] = customer_notification_email
        if delivery_date is not UNSET:
            field_dict["delivery_date"] = delivery_date
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment
        if fully_refunded is not UNSET:
            field_dict["fully_refunded"] = fully_refunded
        if has_customer_message is not UNSET:
            field_dict["has_customer_message"] = has_customer_message
        if has_incident is not UNSET:
            field_dict["has_incident"] = has_incident
        if has_invoice is not UNSET:
            field_dict["has_invoice"] = has_invoice
        if invoice_details is not UNSET:
            field_dict["invoice_details"] = invoice_details
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if order_additional_fields is not UNSET:
            field_dict["order_additional_fields"] = order_additional_fields
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines
        if order_refunds is not UNSET:
            field_dict["order_refunds"] = order_refunds
        if order_state is not UNSET:
            field_dict["order_state"] = order_state
        if order_state_reason_code is not UNSET:
            field_dict["order_state_reason_code"] = order_state_reason_code
        if order_state_reason_label is not UNSET:
            field_dict["order_state_reason_label"] = order_state_reason_label
        if order_tax_mode is not UNSET:
            field_dict["order_tax_mode"] = order_tax_mode
        if order_taxes is not UNSET:
            field_dict["order_taxes"] = order_taxes
        if payment_duration is not UNSET:
            field_dict["payment_duration"] = payment_duration
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if payment_workflow is not UNSET:
            field_dict["payment_workflow"] = payment_workflow
        if price is not UNSET:
            field_dict["price"] = price
        if promotions is not UNSET:
            field_dict["promotions"] = promotions
        if quote_id is not UNSET:
            field_dict["quote_id"] = quote_id
        if references is not UNSET:
            field_dict["references"] = references
        if shipping_carrier_code is not UNSET:
            field_dict["shipping_carrier_code"] = shipping_carrier_code
        if shipping_carrier_standard_code is not UNSET:
            field_dict["shipping_carrier_standard_code"] = shipping_carrier_standard_code
        if shipping_company is not UNSET:
            field_dict["shipping_company"] = shipping_company
        if shipping_deadline is not UNSET:
            field_dict["shipping_deadline"] = shipping_deadline
        if shipping_price is not UNSET:
            field_dict["shipping_price"] = shipping_price
        if shipping_pudo_id is not UNSET:
            field_dict["shipping_pudo_id"] = shipping_pudo_id
        if shipping_tracking is not UNSET:
            field_dict["shipping_tracking"] = shipping_tracking
        if shipping_tracking_url is not UNSET:
            field_dict["shipping_tracking_url"] = shipping_tracking_url
        if shipping_type_code is not UNSET:
            field_dict["shipping_type_code"] = shipping_type_code
        if shipping_type_label is not UNSET:
            field_dict["shipping_type_label"] = shipping_type_label
        if shipping_type_standard_code is not UNSET:
            field_dict["shipping_type_standard_code"] = shipping_type_standard_code
        if shipping_zone_code is not UNSET:
            field_dict["shipping_zone_code"] = shipping_zone_code
        if shipping_zone_label is not UNSET:
            field_dict["shipping_zone_label"] = shipping_zone_label
        if total_commission is not UNSET:
            field_dict["total_commission"] = total_commission
        if total_price is not UNSET:
            field_dict["total_price"] = total_price
        if transaction_date is not UNSET:
            field_dict["transaction_date"] = transaction_date
        if transaction_number is not UNSET:
            field_dict["transaction_number"] = transaction_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_channel import OR11Response200OrdersChannel
        from ..models.or11_response_200_orders_customer import OR11Response200OrdersCustomer
        from ..models.or11_response_200_orders_delivery_date import OR11Response200OrdersDeliveryDate
        from ..models.or11_response_200_orders_fulfillment import OR11Response200OrdersFulfillment
        from ..models.or11_response_200_orders_invoice_details import OR11Response200OrdersInvoiceDetails
        from ..models.or11_response_200_orders_order_additional_fields import OR11Response200OrdersOrderAdditionalFields
        from ..models.or11_response_200_orders_order_lines import OR11Response200OrdersOrderLines
        from ..models.or11_response_200_orders_order_refunds import OR11Response200OrdersOrderRefunds
        from ..models.or11_response_200_orders_order_taxes import OR11Response200OrdersOrderTaxes
        from ..models.or11_response_200_orders_promotions import OR11Response200OrdersPromotions
        from ..models.or11_response_200_orders_references import OR11Response200OrdersReferences

        d = dict(src_dict)
        _acceptance_decision_date = d.pop("acceptance_decision_date", UNSET)
        acceptance_decision_date: Union[Unset, datetime.datetime]
        if isinstance(_acceptance_decision_date, Unset):
            acceptance_decision_date = UNSET
        else:
            acceptance_decision_date = isoparse(_acceptance_decision_date)

        can_cancel = d.pop("can_cancel", UNSET)

        can_shop_ship = d.pop("can_shop_ship", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, OR11Response200OrdersChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = OR11Response200OrdersChannel.from_dict(_channel)

        commercial_id = d.pop("commercial_id", UNSET)

        _created_date = d.pop("created_date", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, OR11Response200OrdersCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = OR11Response200OrdersCustomer.from_dict(_customer)

        _customer_debited_date = d.pop("customer_debited_date", UNSET)
        customer_debited_date: Union[Unset, datetime.datetime]
        if isinstance(_customer_debited_date, Unset):
            customer_debited_date = UNSET
        else:
            customer_debited_date = isoparse(_customer_debited_date)

        customer_directly_pays_seller = d.pop("customer_directly_pays_seller", UNSET)

        customer_notification_email = d.pop("customer_notification_email", UNSET)

        _delivery_date = d.pop("delivery_date", UNSET)
        delivery_date: Union[Unset, OR11Response200OrdersDeliveryDate]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = OR11Response200OrdersDeliveryDate.from_dict(_delivery_date)

        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: Union[Unset, OR11Response200OrdersFulfillment]
        if isinstance(_fulfillment, Unset):
            fulfillment = UNSET
        else:
            fulfillment = OR11Response200OrdersFulfillment.from_dict(_fulfillment)

        fully_refunded = d.pop("fully_refunded", UNSET)

        has_customer_message = d.pop("has_customer_message", UNSET)

        has_incident = d.pop("has_incident", UNSET)

        has_invoice = d.pop("has_invoice", UNSET)

        _invoice_details = d.pop("invoice_details", UNSET)
        invoice_details: Union[Unset, OR11Response200OrdersInvoiceDetails]
        if isinstance(_invoice_details, Unset):
            invoice_details = UNSET
        else:
            invoice_details = OR11Response200OrdersInvoiceDetails.from_dict(_invoice_details)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        order_additional_fields = []
        _order_additional_fields = d.pop("order_additional_fields", UNSET)
        for order_additional_fields_item_data in _order_additional_fields or []:
            order_additional_fields_item = OR11Response200OrdersOrderAdditionalFields.from_dict(
                order_additional_fields_item_data
            )

            order_additional_fields.append(order_additional_fields_item)

        order_id = d.pop("order_id", UNSET)

        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OR11Response200OrdersOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        order_refunds = []
        _order_refunds = d.pop("order_refunds", UNSET)
        for order_refunds_item_data in _order_refunds or []:
            order_refunds_item = OR11Response200OrdersOrderRefunds.from_dict(order_refunds_item_data)

            order_refunds.append(order_refunds_item)

        order_state = d.pop("order_state", UNSET)

        order_state_reason_code = d.pop("order_state_reason_code", UNSET)

        order_state_reason_label = d.pop("order_state_reason_label", UNSET)

        order_tax_mode = d.pop("order_tax_mode", UNSET)

        order_taxes = []
        _order_taxes = d.pop("order_taxes", UNSET)
        for order_taxes_item_data in _order_taxes or []:
            order_taxes_item = OR11Response200OrdersOrderTaxes.from_dict(order_taxes_item_data)

            order_taxes.append(order_taxes_item)

        payment_duration = d.pop("payment_duration", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        payment_workflow = d.pop("payment_workflow", UNSET)

        price = d.pop("price", UNSET)

        _promotions = d.pop("promotions", UNSET)
        promotions: Union[Unset, OR11Response200OrdersPromotions]
        if isinstance(_promotions, Unset):
            promotions = UNSET
        else:
            promotions = OR11Response200OrdersPromotions.from_dict(_promotions)

        quote_id = d.pop("quote_id", UNSET)

        _references = d.pop("references", UNSET)
        references: Union[Unset, OR11Response200OrdersReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = OR11Response200OrdersReferences.from_dict(_references)

        shipping_carrier_code = d.pop("shipping_carrier_code", UNSET)

        shipping_carrier_standard_code = d.pop("shipping_carrier_standard_code", UNSET)

        shipping_company = d.pop("shipping_company", UNSET)

        _shipping_deadline = d.pop("shipping_deadline", UNSET)
        shipping_deadline: Union[Unset, datetime.datetime]
        if isinstance(_shipping_deadline, Unset):
            shipping_deadline = UNSET
        else:
            shipping_deadline = isoparse(_shipping_deadline)

        shipping_price = d.pop("shipping_price", UNSET)

        shipping_pudo_id = d.pop("shipping_pudo_id", UNSET)

        shipping_tracking = d.pop("shipping_tracking", UNSET)

        shipping_tracking_url = d.pop("shipping_tracking_url", UNSET)

        shipping_type_code = d.pop("shipping_type_code", UNSET)

        shipping_type_label = d.pop("shipping_type_label", UNSET)

        shipping_type_standard_code = d.pop("shipping_type_standard_code", UNSET)

        shipping_zone_code = d.pop("shipping_zone_code", UNSET)

        shipping_zone_label = d.pop("shipping_zone_label", UNSET)

        total_commission = d.pop("total_commission", UNSET)

        total_price = d.pop("total_price", UNSET)

        _transaction_date = d.pop("transaction_date", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        transaction_number = d.pop("transaction_number", UNSET)

        or11_response_200_orders = cls(
            acceptance_decision_date=acceptance_decision_date,
            can_cancel=can_cancel,
            can_shop_ship=can_shop_ship,
            channel=channel,
            commercial_id=commercial_id,
            created_date=created_date,
            currency_iso_code=currency_iso_code,
            customer=customer,
            customer_debited_date=customer_debited_date,
            customer_directly_pays_seller=customer_directly_pays_seller,
            customer_notification_email=customer_notification_email,
            delivery_date=delivery_date,
            fulfillment=fulfillment,
            fully_refunded=fully_refunded,
            has_customer_message=has_customer_message,
            has_incident=has_incident,
            has_invoice=has_invoice,
            invoice_details=invoice_details,
            last_updated_date=last_updated_date,
            order_additional_fields=order_additional_fields,
            order_id=order_id,
            order_lines=order_lines,
            order_refunds=order_refunds,
            order_state=order_state,
            order_state_reason_code=order_state_reason_code,
            order_state_reason_label=order_state_reason_label,
            order_tax_mode=order_tax_mode,
            order_taxes=order_taxes,
            payment_duration=payment_duration,
            payment_type=payment_type,
            payment_workflow=payment_workflow,
            price=price,
            promotions=promotions,
            quote_id=quote_id,
            references=references,
            shipping_carrier_code=shipping_carrier_code,
            shipping_carrier_standard_code=shipping_carrier_standard_code,
            shipping_company=shipping_company,
            shipping_deadline=shipping_deadline,
            shipping_price=shipping_price,
            shipping_pudo_id=shipping_pudo_id,
            shipping_tracking=shipping_tracking,
            shipping_tracking_url=shipping_tracking_url,
            shipping_type_code=shipping_type_code,
            shipping_type_label=shipping_type_label,
            shipping_type_standard_code=shipping_type_standard_code,
            shipping_zone_code=shipping_zone_code,
            shipping_zone_label=shipping_zone_label,
            total_commission=total_commission,
            total_price=total_price,
            transaction_date=transaction_date,
            transaction_number=transaction_number,
        )

        or11_response_200_orders.additional_properties = d
        return or11_response_200_orders

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
