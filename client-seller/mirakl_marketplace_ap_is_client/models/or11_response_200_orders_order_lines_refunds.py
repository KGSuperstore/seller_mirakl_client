import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_refunds_amount_breakdown import (
        OR11Response200OrdersOrderLinesRefundsAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_commission_taxes import (
        OR11Response200OrdersOrderLinesRefundsCommissionTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_eco_contributions import (
        OR11Response200OrdersOrderLinesRefundsEcoContributions,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_fees import OR11Response200OrdersOrderLinesRefundsFees
    from ..models.or11_response_200_orders_order_lines_refunds_purchase_information import (
        OR11Response200OrdersOrderLinesRefundsPurchaseInformation,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_shipping_amount_breakdown import (
        OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_shipping_taxes import (
        OR11Response200OrdersOrderLinesRefundsShippingTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_refunds_taxes import OR11Response200OrdersOrderLinesRefundsTaxes


T = TypeVar("T", bound="OR11Response200OrdersOrderLinesRefunds")


@_attrs_define
class OR11Response200OrdersOrderLinesRefunds:
    """
    Attributes:
        amount (Union[Unset, float]): Refund's amount
        amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesRefundsAmountBreakdown]):
        commission_amount (Union[Unset, float]): Refund's commission amount
        commission_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesRefundsCommissionTaxes']]): Refund's
            commission taxes
        commission_total_amount (Union[Unset, float]): The total commission amount of the refund (commission amount +
            commission taxes)
        created_date (Union[Unset, datetime.datetime]): Refund's creation date
        eco_contributions (Union[Unset, list['OR11Response200OrdersOrderLinesRefundsEcoContributions']]): List of eco-
            contribution amounts and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        fees (Union[Unset, list['OR11Response200OrdersOrderLinesRefundsFees']]): List of fees refunded on the order line
        id (Union[Unset, str]): Refund's id
        order_refund_id (Union[Unset, str]): The group identifier of the refunds created at the same time on the order
        purchase_information (Union[Unset, OR11Response200OrdersOrderLinesRefundsPurchaseInformation]):
        quantity (Union[Unset, int]): The quantity of products refunded (This quantity is informative only).
        reason_code (Union[Unset, str]): Reason's code of the refund
        refund_state (Union[Unset, str]): Refund's state
        shipping_amount (Union[Unset, float]): Refund's shipping amount
        shipping_amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown]):
        shipping_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesRefundsShippingTaxes']]): The taxes on the
            shipping price
        state (Union[Unset, str]): Refund's state
        tax_legal_notice (Union[Unset, str]): The legal notice applying to the refunded order line’s taxes
        taxes (Union[Unset, list['OR11Response200OrdersOrderLinesRefundsTaxes']]): The taxes on the price
        transaction_date (Union[Unset, datetime.datetime]): The transaction date of the refund payment
        transaction_number (Union[Unset, str]): The transaction number of the refund payment
    """

    amount: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesRefundsAmountBreakdown"] = UNSET
    commission_amount: Union[Unset, float] = UNSET
    commission_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesRefundsCommissionTaxes"]] = UNSET
    commission_total_amount: Union[Unset, float] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    eco_contributions: Union[Unset, list["OR11Response200OrdersOrderLinesRefundsEcoContributions"]] = UNSET
    fees: Union[Unset, list["OR11Response200OrdersOrderLinesRefundsFees"]] = UNSET
    id: Union[Unset, str] = UNSET
    order_refund_id: Union[Unset, str] = UNSET
    purchase_information: Union[Unset, "OR11Response200OrdersOrderLinesRefundsPurchaseInformation"] = UNSET
    quantity: Union[Unset, int] = UNSET
    reason_code: Union[Unset, str] = UNSET
    refund_state: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown"] = UNSET
    shipping_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesRefundsShippingTaxes"]] = UNSET
    state: Union[Unset, str] = UNSET
    tax_legal_notice: Union[Unset, str] = UNSET
    taxes: Union[Unset, list["OR11Response200OrdersOrderLinesRefundsTaxes"]] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        commission_amount = self.commission_amount

        commission_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.commission_taxes, Unset):
            commission_taxes = []
            for commission_taxes_item_data in self.commission_taxes:
                commission_taxes_item = commission_taxes_item_data.to_dict()
                commission_taxes.append(commission_taxes_item)

        commission_total_amount = self.commission_total_amount

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

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

        id = self.id

        order_refund_id = self.order_refund_id

        purchase_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_information, Unset):
            purchase_information = self.purchase_information.to_dict()

        quantity = self.quantity

        reason_code = self.reason_code

        refund_state = self.refund_state

        shipping_amount = self.shipping_amount

        shipping_amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_amount_breakdown, Unset):
            shipping_amount_breakdown = self.shipping_amount_breakdown.to_dict()

        shipping_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_taxes, Unset):
            shipping_taxes = []
            for shipping_taxes_item_data in self.shipping_taxes:
                shipping_taxes_item = shipping_taxes_item_data.to_dict()
                shipping_taxes.append(shipping_taxes_item)

        state = self.state

        tax_legal_notice = self.tax_legal_notice

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        transaction_number = self.transaction_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_breakdown is not UNSET:
            field_dict["amount_breakdown"] = amount_breakdown
        if commission_amount is not UNSET:
            field_dict["commission_amount"] = commission_amount
        if commission_taxes is not UNSET:
            field_dict["commission_taxes"] = commission_taxes
        if commission_total_amount is not UNSET:
            field_dict["commission_total_amount"] = commission_total_amount
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if fees is not UNSET:
            field_dict["fees"] = fees
        if id is not UNSET:
            field_dict["id"] = id
        if order_refund_id is not UNSET:
            field_dict["order_refund_id"] = order_refund_id
        if purchase_information is not UNSET:
            field_dict["purchase_information"] = purchase_information
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if refund_state is not UNSET:
            field_dict["refund_state"] = refund_state
        if shipping_amount is not UNSET:
            field_dict["shipping_amount"] = shipping_amount
        if shipping_amount_breakdown is not UNSET:
            field_dict["shipping_amount_breakdown"] = shipping_amount_breakdown
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if state is not UNSET:
            field_dict["state"] = state
        if tax_legal_notice is not UNSET:
            field_dict["tax_legal_notice"] = tax_legal_notice
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if transaction_date is not UNSET:
            field_dict["transaction_date"] = transaction_date
        if transaction_number is not UNSET:
            field_dict["transaction_number"] = transaction_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_lines_refunds_amount_breakdown import (
            OR11Response200OrdersOrderLinesRefundsAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_commission_taxes import (
            OR11Response200OrdersOrderLinesRefundsCommissionTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_eco_contributions import (
            OR11Response200OrdersOrderLinesRefundsEcoContributions,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_fees import (
            OR11Response200OrdersOrderLinesRefundsFees,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_purchase_information import (
            OR11Response200OrdersOrderLinesRefundsPurchaseInformation,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_shipping_amount_breakdown import (
            OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_shipping_taxes import (
            OR11Response200OrdersOrderLinesRefundsShippingTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_refunds_taxes import (
            OR11Response200OrdersOrderLinesRefundsTaxes,
        )

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _amount_breakdown = d.pop("amount_breakdown", UNSET)
        amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesRefundsAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = OR11Response200OrdersOrderLinesRefundsAmountBreakdown.from_dict(_amount_breakdown)

        commission_amount = d.pop("commission_amount", UNSET)

        commission_taxes = []
        _commission_taxes = d.pop("commission_taxes", UNSET)
        for commission_taxes_item_data in _commission_taxes or []:
            commission_taxes_item = OR11Response200OrdersOrderLinesRefundsCommissionTaxes.from_dict(
                commission_taxes_item_data
            )

            commission_taxes.append(commission_taxes_item)

        commission_total_amount = d.pop("commission_total_amount", UNSET)

        _created_date = d.pop("created_date", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR11Response200OrdersOrderLinesRefundsEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR11Response200OrdersOrderLinesRefundsFees.from_dict(fees_item_data)

            fees.append(fees_item)

        id = d.pop("id", UNSET)

        order_refund_id = d.pop("order_refund_id", UNSET)

        _purchase_information = d.pop("purchase_information", UNSET)
        purchase_information: Union[Unset, OR11Response200OrdersOrderLinesRefundsPurchaseInformation]
        if isinstance(_purchase_information, Unset):
            purchase_information = UNSET
        else:
            purchase_information = OR11Response200OrdersOrderLinesRefundsPurchaseInformation.from_dict(
                _purchase_information
            )

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        refund_state = d.pop("refund_state", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        _shipping_amount_breakdown = d.pop("shipping_amount_breakdown", UNSET)
        shipping_amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown]
        if isinstance(_shipping_amount_breakdown, Unset):
            shipping_amount_breakdown = UNSET
        else:
            shipping_amount_breakdown = OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown.from_dict(
                _shipping_amount_breakdown
            )

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR11Response200OrdersOrderLinesRefundsShippingTaxes.from_dict(
                shipping_taxes_item_data
            )

            shipping_taxes.append(shipping_taxes_item)

        state = d.pop("state", UNSET)

        tax_legal_notice = d.pop("tax_legal_notice", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR11Response200OrdersOrderLinesRefundsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        _transaction_date = d.pop("transaction_date", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        transaction_number = d.pop("transaction_number", UNSET)

        or11_response_200_orders_order_lines_refunds = cls(
            amount=amount,
            amount_breakdown=amount_breakdown,
            commission_amount=commission_amount,
            commission_taxes=commission_taxes,
            commission_total_amount=commission_total_amount,
            created_date=created_date,
            eco_contributions=eco_contributions,
            fees=fees,
            id=id,
            order_refund_id=order_refund_id,
            purchase_information=purchase_information,
            quantity=quantity,
            reason_code=reason_code,
            refund_state=refund_state,
            shipping_amount=shipping_amount,
            shipping_amount_breakdown=shipping_amount_breakdown,
            shipping_taxes=shipping_taxes,
            state=state,
            tax_legal_notice=tax_legal_notice,
            taxes=taxes,
            transaction_date=transaction_date,
            transaction_number=transaction_number,
        )

        or11_response_200_orders_order_lines_refunds.additional_properties = d
        return or11_response_200_orders_order_lines_refunds

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
