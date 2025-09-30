import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_cancelations import OR11Response200OrdersOrderLinesCancelations
    from ..models.or11_response_200_orders_order_lines_commission_taxes import (
        OR11Response200OrdersOrderLinesCommissionTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_eco_contributions import (
        OR11Response200OrdersOrderLinesEcoContributions,
    )
    from ..models.or11_response_200_orders_order_lines_fees import OR11Response200OrdersOrderLinesFees
    from ..models.or11_response_200_orders_order_lines_measurement import OR11Response200OrdersOrderLinesMeasurement
    from ..models.or11_response_200_orders_order_lines_order_line_additional_fields import (
        OR11Response200OrdersOrderLinesOrderLineAdditionalFields,
    )
    from ..models.or11_response_200_orders_order_lines_price_amount_breakdown import (
        OR11Response200OrdersOrderLinesPriceAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_product_medias import (
        OR11Response200OrdersOrderLinesProductMedias,
    )
    from ..models.or11_response_200_orders_order_lines_promotions import OR11Response200OrdersOrderLinesPromotions
    from ..models.or11_response_200_orders_order_lines_purchase_information import (
        OR11Response200OrdersOrderLinesPurchaseInformation,
    )
    from ..models.or11_response_200_orders_order_lines_refunds import OR11Response200OrdersOrderLinesRefunds
    from ..models.or11_response_200_orders_order_lines_shipping_from import OR11Response200OrdersOrderLinesShippingFrom
    from ..models.or11_response_200_orders_order_lines_shipping_price_amount_breakdown import (
        OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_shipping_taxes import (
        OR11Response200OrdersOrderLinesShippingTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_taxes import OR11Response200OrdersOrderLinesTaxes


T = TypeVar("T", bound="OR11Response200OrdersOrderLines")


@_attrs_define
class OR11Response200OrdersOrderLines:
    """
    Attributes:
        can_refund (Union[Unset, bool]): Indicate whether the order line full amount can be refunded
        cancelations (Union[Unset, list['OR11Response200OrdersOrderLinesCancelations']]): List of the cancellations
        category_code (Union[Unset, str]): Category code of the product associated with the order line
        category_label (Union[Unset, str]): Category label of the product associated with the order line
        commission_fee (Union[Unset, float]): Order line's commission fee
        commission_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesCommissionTaxes']]): Commission taxes
        created_date (Union[Unset, datetime.datetime]): Order line's creation date
        debited_date (Union[Unset, datetime.datetime]): Order line's debited date
        description (Union[Unset, str]): Order line's description
        eco_contributions (Union[Unset, list['OR11Response200OrdersOrderLinesEcoContributions']]): List of eco-
            contribution amounts and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        fees (Union[Unset, list['OR11Response200OrdersOrderLinesFees']]): List of fees applied on the order line
        last_updated_date (Union[Unset, datetime.datetime]): Order line's last updated date
        measurement (Union[Unset, OR11Response200OrdersOrderLinesMeasurement]):
        offer_id (Union[Unset, int]): Associated offer's id
        offer_sku (Union[Unset, str]): Associated offer sku (this is the sku of the offer defined by the shop)
        offer_state_code (Union[Unset, str]): State of the offer associated with the order line
        order_line_additional_fields (Union[Unset, list['OR11Response200OrdersOrderLinesOrderLineAdditionalFields']]):
            List of custom fields
        order_line_id (Union[Unset, str]): Order line's identifier
        order_line_index (Union[Unset, int]): Order line's index in the order
        order_line_state (Union[Unset, str]): Order line's state
        order_line_state_reason_code (Union[Unset, str]): Reason's code of the order line's state
        order_line_state_reason_label (Union[Unset, str]): Reason's label of the order line's state
        origin_unit_price (Union[Unset, float]): The original unit price of the offer associated with the order line
        price (Union[Unset, float]): Order line's price without shipping price
        price_additional_info (Union[Unset, str]): Price's additional information of the offer
        price_amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesPriceAmountBreakdown]):
        price_unit (Union[Unset, float]): Unit price for the offer associated with the order line
        product_medias (Union[Unset, list['OR11Response200OrdersOrderLinesProductMedias']]): List of all product's media
            associated to the order line
        product_shop_sku (Union[Unset, str]): Shop SKU of the product associated with the order line
        product_sku (Union[Unset, str]): SKU of the product associated with the order line
        product_title (Union[Unset, str]): Title of the product associated with the order line
        promotions (Union[Unset, list['OR11Response200OrdersOrderLinesPromotions']]): List of promotions
        purchase_information (Union[Unset, OR11Response200OrdersOrderLinesPurchaseInformation]):
        quantity (Union[Unset, int]): Product's quantity for the order line
        received_date (Union[Unset, datetime.datetime]): Product's date of receipt
        refunds (Union[Unset, list['OR11Response200OrdersOrderLinesRefunds']]): List of the refunds
        shipped_date (Union[Unset, datetime.datetime]): Order line's shipped date
        shipping_from (Union[Unset, OR11Response200OrdersOrderLinesShippingFrom]):
        shipping_price (Union[Unset, float]): Total price of the order line's shipping price
        shipping_price_amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown]):
        shipping_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesShippingTaxes']]): List of taxes applied on
            shipping charges
        tax_legal_notice (Union[Unset, str]): The legal notice applying to the order line’s taxes
        taxes (Union[Unset, list['OR11Response200OrdersOrderLinesTaxes']]): List of taxes applied on product price
        total_commission (Union[Unset, float]): Order line's total commission (sum of the commission fee and the
            commission vat)
        total_price (Union[Unset, float]): Order line's price with shipping price and fees.
    """

    can_refund: Union[Unset, bool] = UNSET
    cancelations: Union[Unset, list["OR11Response200OrdersOrderLinesCancelations"]] = UNSET
    category_code: Union[Unset, str] = UNSET
    category_label: Union[Unset, str] = UNSET
    commission_fee: Union[Unset, float] = UNSET
    commission_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesCommissionTaxes"]] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    debited_date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    eco_contributions: Union[Unset, list["OR11Response200OrdersOrderLinesEcoContributions"]] = UNSET
    fees: Union[Unset, list["OR11Response200OrdersOrderLinesFees"]] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    measurement: Union[Unset, "OR11Response200OrdersOrderLinesMeasurement"] = UNSET
    offer_id: Union[Unset, int] = UNSET
    offer_sku: Union[Unset, str] = UNSET
    offer_state_code: Union[Unset, str] = UNSET
    order_line_additional_fields: Union[Unset, list["OR11Response200OrdersOrderLinesOrderLineAdditionalFields"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    order_line_index: Union[Unset, int] = UNSET
    order_line_state: Union[Unset, str] = UNSET
    order_line_state_reason_code: Union[Unset, str] = UNSET
    order_line_state_reason_label: Union[Unset, str] = UNSET
    origin_unit_price: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    price_additional_info: Union[Unset, str] = UNSET
    price_amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesPriceAmountBreakdown"] = UNSET
    price_unit: Union[Unset, float] = UNSET
    product_medias: Union[Unset, list["OR11Response200OrdersOrderLinesProductMedias"]] = UNSET
    product_shop_sku: Union[Unset, str] = UNSET
    product_sku: Union[Unset, str] = UNSET
    product_title: Union[Unset, str] = UNSET
    promotions: Union[Unset, list["OR11Response200OrdersOrderLinesPromotions"]] = UNSET
    purchase_information: Union[Unset, "OR11Response200OrdersOrderLinesPurchaseInformation"] = UNSET
    quantity: Union[Unset, int] = UNSET
    received_date: Union[Unset, datetime.datetime] = UNSET
    refunds: Union[Unset, list["OR11Response200OrdersOrderLinesRefunds"]] = UNSET
    shipped_date: Union[Unset, datetime.datetime] = UNSET
    shipping_from: Union[Unset, "OR11Response200OrdersOrderLinesShippingFrom"] = UNSET
    shipping_price: Union[Unset, float] = UNSET
    shipping_price_amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown"] = UNSET
    shipping_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesShippingTaxes"]] = UNSET
    tax_legal_notice: Union[Unset, str] = UNSET
    taxes: Union[Unset, list["OR11Response200OrdersOrderLinesTaxes"]] = UNSET
    total_commission: Union[Unset, float] = UNSET
    total_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_refund = self.can_refund

        cancelations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cancelations, Unset):
            cancelations = []
            for cancelations_item_data in self.cancelations:
                cancelations_item = cancelations_item_data.to_dict()
                cancelations.append(cancelations_item)

        category_code = self.category_code

        category_label = self.category_label

        commission_fee = self.commission_fee

        commission_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.commission_taxes, Unset):
            commission_taxes = []
            for commission_taxes_item_data in self.commission_taxes:
                commission_taxes_item = commission_taxes_item_data.to_dict()
                commission_taxes.append(commission_taxes_item)

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        debited_date: Union[Unset, str] = UNSET
        if not isinstance(self.debited_date, Unset):
            debited_date = self.debited_date.isoformat()

        description = self.description

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        fees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        measurement: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        offer_id = self.offer_id

        offer_sku = self.offer_sku

        offer_state_code = self.offer_state_code

        order_line_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_line_additional_fields, Unset):
            order_line_additional_fields = []
            for order_line_additional_fields_item_data in self.order_line_additional_fields:
                order_line_additional_fields_item = order_line_additional_fields_item_data.to_dict()
                order_line_additional_fields.append(order_line_additional_fields_item)

        order_line_id = self.order_line_id

        order_line_index = self.order_line_index

        order_line_state = self.order_line_state

        order_line_state_reason_code = self.order_line_state_reason_code

        order_line_state_reason_label = self.order_line_state_reason_label

        origin_unit_price = self.origin_unit_price

        price = self.price

        price_additional_info = self.price_additional_info

        price_amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price_amount_breakdown, Unset):
            price_amount_breakdown = self.price_amount_breakdown.to_dict()

        price_unit = self.price_unit

        product_medias: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_medias, Unset):
            product_medias = []
            for product_medias_item_data in self.product_medias:
                product_medias_item = product_medias_item_data.to_dict()
                product_medias.append(product_medias_item)

        product_shop_sku = self.product_shop_sku

        product_sku = self.product_sku

        product_title = self.product_title

        promotions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.promotions, Unset):
            promotions = []
            for promotions_item_data in self.promotions:
                promotions_item = promotions_item_data.to_dict()
                promotions.append(promotions_item)

        purchase_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_information, Unset):
            purchase_information = self.purchase_information.to_dict()

        quantity = self.quantity

        received_date: Union[Unset, str] = UNSET
        if not isinstance(self.received_date, Unset):
            received_date = self.received_date.isoformat()

        refunds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = []
            for refunds_item_data in self.refunds:
                refunds_item = refunds_item_data.to_dict()
                refunds.append(refunds_item)

        shipped_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_date, Unset):
            shipped_date = self.shipped_date.isoformat()

        shipping_from: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_from, Unset):
            shipping_from = self.shipping_from.to_dict()

        shipping_price = self.shipping_price

        shipping_price_amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_price_amount_breakdown, Unset):
            shipping_price_amount_breakdown = self.shipping_price_amount_breakdown.to_dict()

        shipping_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_taxes, Unset):
            shipping_taxes = []
            for shipping_taxes_item_data in self.shipping_taxes:
                shipping_taxes_item = shipping_taxes_item_data.to_dict()
                shipping_taxes.append(shipping_taxes_item)

        tax_legal_notice = self.tax_legal_notice

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        total_commission = self.total_commission

        total_price = self.total_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_refund is not UNSET:
            field_dict["can_refund"] = can_refund
        if cancelations is not UNSET:
            field_dict["cancelations"] = cancelations
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if category_label is not UNSET:
            field_dict["category_label"] = category_label
        if commission_fee is not UNSET:
            field_dict["commission_fee"] = commission_fee
        if commission_taxes is not UNSET:
            field_dict["commission_taxes"] = commission_taxes
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if debited_date is not UNSET:
            field_dict["debited_date"] = debited_date
        if description is not UNSET:
            field_dict["description"] = description
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if fees is not UNSET:
            field_dict["fees"] = fees
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id
        if offer_sku is not UNSET:
            field_dict["offer_sku"] = offer_sku
        if offer_state_code is not UNSET:
            field_dict["offer_state_code"] = offer_state_code
        if order_line_additional_fields is not UNSET:
            field_dict["order_line_additional_fields"] = order_line_additional_fields
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if order_line_index is not UNSET:
            field_dict["order_line_index"] = order_line_index
        if order_line_state is not UNSET:
            field_dict["order_line_state"] = order_line_state
        if order_line_state_reason_code is not UNSET:
            field_dict["order_line_state_reason_code"] = order_line_state_reason_code
        if order_line_state_reason_label is not UNSET:
            field_dict["order_line_state_reason_label"] = order_line_state_reason_label
        if origin_unit_price is not UNSET:
            field_dict["origin_unit_price"] = origin_unit_price
        if price is not UNSET:
            field_dict["price"] = price
        if price_additional_info is not UNSET:
            field_dict["price_additional_info"] = price_additional_info
        if price_amount_breakdown is not UNSET:
            field_dict["price_amount_breakdown"] = price_amount_breakdown
        if price_unit is not UNSET:
            field_dict["price_unit"] = price_unit
        if product_medias is not UNSET:
            field_dict["product_medias"] = product_medias
        if product_shop_sku is not UNSET:
            field_dict["product_shop_sku"] = product_shop_sku
        if product_sku is not UNSET:
            field_dict["product_sku"] = product_sku
        if product_title is not UNSET:
            field_dict["product_title"] = product_title
        if promotions is not UNSET:
            field_dict["promotions"] = promotions
        if purchase_information is not UNSET:
            field_dict["purchase_information"] = purchase_information
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if received_date is not UNSET:
            field_dict["received_date"] = received_date
        if refunds is not UNSET:
            field_dict["refunds"] = refunds
        if shipped_date is not UNSET:
            field_dict["shipped_date"] = shipped_date
        if shipping_from is not UNSET:
            field_dict["shipping_from"] = shipping_from
        if shipping_price is not UNSET:
            field_dict["shipping_price"] = shipping_price
        if shipping_price_amount_breakdown is not UNSET:
            field_dict["shipping_price_amount_breakdown"] = shipping_price_amount_breakdown
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if tax_legal_notice is not UNSET:
            field_dict["tax_legal_notice"] = tax_legal_notice
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total_commission is not UNSET:
            field_dict["total_commission"] = total_commission
        if total_price is not UNSET:
            field_dict["total_price"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_lines_cancelations import (
            OR11Response200OrdersOrderLinesCancelations,
        )
        from ..models.or11_response_200_orders_order_lines_commission_taxes import (
            OR11Response200OrdersOrderLinesCommissionTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_eco_contributions import (
            OR11Response200OrdersOrderLinesEcoContributions,
        )
        from ..models.or11_response_200_orders_order_lines_fees import OR11Response200OrdersOrderLinesFees
        from ..models.or11_response_200_orders_order_lines_measurement import OR11Response200OrdersOrderLinesMeasurement
        from ..models.or11_response_200_orders_order_lines_order_line_additional_fields import (
            OR11Response200OrdersOrderLinesOrderLineAdditionalFields,
        )
        from ..models.or11_response_200_orders_order_lines_price_amount_breakdown import (
            OR11Response200OrdersOrderLinesPriceAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_product_medias import (
            OR11Response200OrdersOrderLinesProductMedias,
        )
        from ..models.or11_response_200_orders_order_lines_promotions import OR11Response200OrdersOrderLinesPromotions
        from ..models.or11_response_200_orders_order_lines_purchase_information import (
            OR11Response200OrdersOrderLinesPurchaseInformation,
        )
        from ..models.or11_response_200_orders_order_lines_refunds import OR11Response200OrdersOrderLinesRefunds
        from ..models.or11_response_200_orders_order_lines_shipping_from import (
            OR11Response200OrdersOrderLinesShippingFrom,
        )
        from ..models.or11_response_200_orders_order_lines_shipping_price_amount_breakdown import (
            OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_shipping_taxes import (
            OR11Response200OrdersOrderLinesShippingTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_taxes import OR11Response200OrdersOrderLinesTaxes

        d = dict(src_dict)
        can_refund = d.pop("can_refund", UNSET)

        cancelations = []
        _cancelations = d.pop("cancelations", UNSET)
        for cancelations_item_data in _cancelations or []:
            cancelations_item = OR11Response200OrdersOrderLinesCancelations.from_dict(cancelations_item_data)

            cancelations.append(cancelations_item)

        category_code = d.pop("category_code", UNSET)

        category_label = d.pop("category_label", UNSET)

        commission_fee = d.pop("commission_fee", UNSET)

        commission_taxes = []
        _commission_taxes = d.pop("commission_taxes", UNSET)
        for commission_taxes_item_data in _commission_taxes or []:
            commission_taxes_item = OR11Response200OrdersOrderLinesCommissionTaxes.from_dict(commission_taxes_item_data)

            commission_taxes.append(commission_taxes_item)

        _created_date = d.pop("created_date", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _debited_date = d.pop("debited_date", UNSET)
        debited_date: Union[Unset, datetime.datetime]
        if isinstance(_debited_date, Unset):
            debited_date = UNSET
        else:
            debited_date = isoparse(_debited_date)

        description = d.pop("description", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR11Response200OrdersOrderLinesEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR11Response200OrdersOrderLinesFees.from_dict(fees_item_data)

            fees.append(fees_item)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        _measurement = d.pop("measurement", UNSET)
        measurement: Union[Unset, OR11Response200OrdersOrderLinesMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = OR11Response200OrdersOrderLinesMeasurement.from_dict(_measurement)

        offer_id = d.pop("offer_id", UNSET)

        offer_sku = d.pop("offer_sku", UNSET)

        offer_state_code = d.pop("offer_state_code", UNSET)

        order_line_additional_fields = []
        _order_line_additional_fields = d.pop("order_line_additional_fields", UNSET)
        for order_line_additional_fields_item_data in _order_line_additional_fields or []:
            order_line_additional_fields_item = OR11Response200OrdersOrderLinesOrderLineAdditionalFields.from_dict(
                order_line_additional_fields_item_data
            )

            order_line_additional_fields.append(order_line_additional_fields_item)

        order_line_id = d.pop("order_line_id", UNSET)

        order_line_index = d.pop("order_line_index", UNSET)

        order_line_state = d.pop("order_line_state", UNSET)

        order_line_state_reason_code = d.pop("order_line_state_reason_code", UNSET)

        order_line_state_reason_label = d.pop("order_line_state_reason_label", UNSET)

        origin_unit_price = d.pop("origin_unit_price", UNSET)

        price = d.pop("price", UNSET)

        price_additional_info = d.pop("price_additional_info", UNSET)

        _price_amount_breakdown = d.pop("price_amount_breakdown", UNSET)
        price_amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesPriceAmountBreakdown]
        if isinstance(_price_amount_breakdown, Unset):
            price_amount_breakdown = UNSET
        else:
            price_amount_breakdown = OR11Response200OrdersOrderLinesPriceAmountBreakdown.from_dict(
                _price_amount_breakdown
            )

        price_unit = d.pop("price_unit", UNSET)

        product_medias = []
        _product_medias = d.pop("product_medias", UNSET)
        for product_medias_item_data in _product_medias or []:
            product_medias_item = OR11Response200OrdersOrderLinesProductMedias.from_dict(product_medias_item_data)

            product_medias.append(product_medias_item)

        product_shop_sku = d.pop("product_shop_sku", UNSET)

        product_sku = d.pop("product_sku", UNSET)

        product_title = d.pop("product_title", UNSET)

        promotions = []
        _promotions = d.pop("promotions", UNSET)
        for promotions_item_data in _promotions or []:
            promotions_item = OR11Response200OrdersOrderLinesPromotions.from_dict(promotions_item_data)

            promotions.append(promotions_item)

        _purchase_information = d.pop("purchase_information", UNSET)
        purchase_information: Union[Unset, OR11Response200OrdersOrderLinesPurchaseInformation]
        if isinstance(_purchase_information, Unset):
            purchase_information = UNSET
        else:
            purchase_information = OR11Response200OrdersOrderLinesPurchaseInformation.from_dict(_purchase_information)

        quantity = d.pop("quantity", UNSET)

        _received_date = d.pop("received_date", UNSET)
        received_date: Union[Unset, datetime.datetime]
        if isinstance(_received_date, Unset):
            received_date = UNSET
        else:
            received_date = isoparse(_received_date)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = OR11Response200OrdersOrderLinesRefunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        _shipped_date = d.pop("shipped_date", UNSET)
        shipped_date: Union[Unset, datetime.datetime]
        if isinstance(_shipped_date, Unset):
            shipped_date = UNSET
        else:
            shipped_date = isoparse(_shipped_date)

        _shipping_from = d.pop("shipping_from", UNSET)
        shipping_from: Union[Unset, OR11Response200OrdersOrderLinesShippingFrom]
        if isinstance(_shipping_from, Unset):
            shipping_from = UNSET
        else:
            shipping_from = OR11Response200OrdersOrderLinesShippingFrom.from_dict(_shipping_from)

        shipping_price = d.pop("shipping_price", UNSET)

        _shipping_price_amount_breakdown = d.pop("shipping_price_amount_breakdown", UNSET)
        shipping_price_amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown]
        if isinstance(_shipping_price_amount_breakdown, Unset):
            shipping_price_amount_breakdown = UNSET
        else:
            shipping_price_amount_breakdown = OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown.from_dict(
                _shipping_price_amount_breakdown
            )

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR11Response200OrdersOrderLinesShippingTaxes.from_dict(shipping_taxes_item_data)

            shipping_taxes.append(shipping_taxes_item)

        tax_legal_notice = d.pop("tax_legal_notice", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR11Response200OrdersOrderLinesTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        total_commission = d.pop("total_commission", UNSET)

        total_price = d.pop("total_price", UNSET)

        or11_response_200_orders_order_lines = cls(
            can_refund=can_refund,
            cancelations=cancelations,
            category_code=category_code,
            category_label=category_label,
            commission_fee=commission_fee,
            commission_taxes=commission_taxes,
            created_date=created_date,
            debited_date=debited_date,
            description=description,
            eco_contributions=eco_contributions,
            fees=fees,
            last_updated_date=last_updated_date,
            measurement=measurement,
            offer_id=offer_id,
            offer_sku=offer_sku,
            offer_state_code=offer_state_code,
            order_line_additional_fields=order_line_additional_fields,
            order_line_id=order_line_id,
            order_line_index=order_line_index,
            order_line_state=order_line_state,
            order_line_state_reason_code=order_line_state_reason_code,
            order_line_state_reason_label=order_line_state_reason_label,
            origin_unit_price=origin_unit_price,
            price=price,
            price_additional_info=price_additional_info,
            price_amount_breakdown=price_amount_breakdown,
            price_unit=price_unit,
            product_medias=product_medias,
            product_shop_sku=product_shop_sku,
            product_sku=product_sku,
            product_title=product_title,
            promotions=promotions,
            purchase_information=purchase_information,
            quantity=quantity,
            received_date=received_date,
            refunds=refunds,
            shipped_date=shipped_date,
            shipping_from=shipping_from,
            shipping_price=shipping_price,
            shipping_price_amount_breakdown=shipping_price_amount_breakdown,
            shipping_taxes=shipping_taxes,
            tax_legal_notice=tax_legal_notice,
            taxes=taxes,
            total_commission=total_commission,
            total_price=total_price,
        )

        or11_response_200_orders_order_lines.additional_properties = d
        return or11_response_200_orders_order_lines

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
