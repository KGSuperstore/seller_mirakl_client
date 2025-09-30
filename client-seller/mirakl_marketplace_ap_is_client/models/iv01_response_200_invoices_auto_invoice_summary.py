from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IV01Response200InvoicesAutoInvoiceSummary")


@_attrs_define
class IV01Response200InvoicesAutoInvoiceSummary:
    """
    Attributes:
        amount_transferred (Union[Unset, float]): Total amount to be transferred to the seller
        amount_transferred_to_operator (Union[Unset, float]): Total amount to be transferred to the operator
        reserve_funding (Union[Unset, float]): Amount set aside for the seller reserve
        reserve_settlement (Union[Unset, float]): Amount paid out from the seller reserve
        total_commissions_excl_tax (Union[Unset, float]): Total amount of commissions (excluding taxes on orders)
        total_commissions_incl_tax (Union[Unset, float]): Total amount of commissions (including taxes on orders)
        total_fee_excl_tax (Union[Unset, float]): Total amount of fees (excluding taxes on orders)
        total_fee_incl_tax (Union[Unset, float]): Total amount of fees (including taxes on orders)
        total_fee_operator_remitted_excl_tax (Union[Unset, float]): Total amount of fees remitted by the operator
            (excluding taxes on orders)
        total_fee_operator_remitted_incl_tax (Union[Unset, float]): Total amount of fees remitted by the operator
            (including taxes on orders)
        total_non_payable_orders_excl_tax (Union[Unset, float]): Total amount for non payable orders (including shipping
            charges and excluding taxes on orders)
        total_non_payable_orders_incl_tax (Union[Unset, float]): Total amount for non payable orders (including shipping
            charges and taxes on orders)
        total_operator_paid_shipping_charges_excl_tax (Union[Unset, float]): Total amount of shipping charges paid by
            the operator (excluding taxes on orders)
        total_operator_paid_shipping_charges_incl_tax (Union[Unset, float]): Total amount of shipping charges paid by
            the operator (including taxes on orders)
        total_operator_remitted_taxes (Union[Unset, float]): Total amount for order taxes remitted by the operator
        total_other_credits_excl_tax (Union[Unset, float]): Total amount for other manual credits of a payment cycle
            (excluding taxes on stores)
        total_other_credits_incl_tax (Union[Unset, float]): Total amount for other manual credits of a payment cycle
            (including taxes on stores)
        total_other_invoices_excl_tax (Union[Unset, float]): Total amount for other manual invoices of a payment cycle
            (excluding taxes on stores)
        total_other_invoices_incl_tax (Union[Unset, float]): Total amount for other manual invoices of a payment cycle
            (including taxes on stores)
        total_payable_orders_excl_tax (Union[Unset, float]): Total amount for payable orders including shipping charges
            (excluding taxes on stores)
        total_payable_orders_incl_tax (Union[Unset, float]): Total amount for payable orders including taxes (including
            taxes on orders)
        total_purchase_taxes (Union[Unset, float]): Total amount for purchase taxes
        total_refund_commissions_excl_tax (Union[Unset, float]): Total amount of refunded commissions (excluding taxes
            on orders)
        total_refund_commissions_incl_tax (Union[Unset, float]): Total amount of refunded commissions (including taxes
            on orders)
        total_refund_fee_excl_tax (Union[Unset, float]): Total amount of refunded fees (excluding taxes on orders)
        total_refund_fee_incl_tax (Union[Unset, float]): Total amount of refunded fees (including taxes on orders)
        total_refund_fee_operator_remitted_excl_tax (Union[Unset, float]): Total amount of refunded fees remitted by the
            operator (excluding taxes on orders)
        total_refund_fee_operator_remitted_incl_tax (Union[Unset, float]): Total amount of refunded fees remitted by the
            operator (including taxes on orders)
        total_refund_non_payable_orders_excl_tax (Union[Unset, float]): Total amount refunded for non payable orders
            (including shipping charges and excluding taxes on orders)
        total_refund_non_payable_orders_incl_tax (Union[Unset, float]): Total amount refunded for non payable orders
            (excluding shipping charges and including taxes on orders)
        total_refund_operator_paid_shipping_charges_excl_tax (Union[Unset, float]): Total amount of refunded shipping
            charges paid by the operator (excluding taxes on orders)
        total_refund_operator_paid_shipping_charges_incl_tax (Union[Unset, float]): Total amount of refunded shipping
            charges paid by the operator (including taxes on orders)
        total_refund_operator_remitted_taxes (Union[Unset, float]): Total amount of refunded taxes remitted by the
            operator
        total_refund_orders_excl_tax (Union[Unset, float]): Total amount of refunded orders (excluding all refunded
            taxes)
        total_refund_orders_incl_tax (Union[Unset, float]): Total amount of refunded orders (including all refunded
            taxes)
        total_refund_payable_orders_excl_tax (Union[Unset, float]): Total amount refunded for payable orders (excluding
            taxes on orders)
        total_refund_payable_orders_incl_tax (Union[Unset, float]): Total amount refunded for payable orders (including
            taxes on orders)
        total_refund_purchase_taxes (Union[Unset, float]): Total amount of refunded purchase taxes
        total_seller_fees_on_orders_excl_tax (Union[Unset, float]): Total amount of seller fees on orders (excluding
            taxes on orders)
        total_seller_fees_on_orders_incl_tax (Union[Unset, float]): Total amount of seller fees on orders (including
            taxes on orders)
        total_seller_penalty_fees_excl_tax (Union[Unset, float]): Total amount of seller penalty fees (excluding taxes
            on orders)
        total_seller_penalty_fees_incl_tax (Union[Unset, float]): Total amount of seller penalty fees (including taxes
            on orders)
        total_subscription_excl_tax (Union[Unset, float]): Total amount of subscription fees (excluding taxes on stores)
        total_subscription_incl_tax (Union[Unset, float]): Total amount of subscription taxes (including taxes on
            stores)
    """

    amount_transferred: Union[Unset, float] = UNSET
    amount_transferred_to_operator: Union[Unset, float] = UNSET
    reserve_funding: Union[Unset, float] = UNSET
    reserve_settlement: Union[Unset, float] = UNSET
    total_commissions_excl_tax: Union[Unset, float] = UNSET
    total_commissions_incl_tax: Union[Unset, float] = UNSET
    total_fee_excl_tax: Union[Unset, float] = UNSET
    total_fee_incl_tax: Union[Unset, float] = UNSET
    total_fee_operator_remitted_excl_tax: Union[Unset, float] = UNSET
    total_fee_operator_remitted_incl_tax: Union[Unset, float] = UNSET
    total_non_payable_orders_excl_tax: Union[Unset, float] = UNSET
    total_non_payable_orders_incl_tax: Union[Unset, float] = UNSET
    total_operator_paid_shipping_charges_excl_tax: Union[Unset, float] = UNSET
    total_operator_paid_shipping_charges_incl_tax: Union[Unset, float] = UNSET
    total_operator_remitted_taxes: Union[Unset, float] = UNSET
    total_other_credits_excl_tax: Union[Unset, float] = UNSET
    total_other_credits_incl_tax: Union[Unset, float] = UNSET
    total_other_invoices_excl_tax: Union[Unset, float] = UNSET
    total_other_invoices_incl_tax: Union[Unset, float] = UNSET
    total_payable_orders_excl_tax: Union[Unset, float] = UNSET
    total_payable_orders_incl_tax: Union[Unset, float] = UNSET
    total_purchase_taxes: Union[Unset, float] = UNSET
    total_refund_commissions_excl_tax: Union[Unset, float] = UNSET
    total_refund_commissions_incl_tax: Union[Unset, float] = UNSET
    total_refund_fee_excl_tax: Union[Unset, float] = UNSET
    total_refund_fee_incl_tax: Union[Unset, float] = UNSET
    total_refund_fee_operator_remitted_excl_tax: Union[Unset, float] = UNSET
    total_refund_fee_operator_remitted_incl_tax: Union[Unset, float] = UNSET
    total_refund_non_payable_orders_excl_tax: Union[Unset, float] = UNSET
    total_refund_non_payable_orders_incl_tax: Union[Unset, float] = UNSET
    total_refund_operator_paid_shipping_charges_excl_tax: Union[Unset, float] = UNSET
    total_refund_operator_paid_shipping_charges_incl_tax: Union[Unset, float] = UNSET
    total_refund_operator_remitted_taxes: Union[Unset, float] = UNSET
    total_refund_orders_excl_tax: Union[Unset, float] = UNSET
    total_refund_orders_incl_tax: Union[Unset, float] = UNSET
    total_refund_payable_orders_excl_tax: Union[Unset, float] = UNSET
    total_refund_payable_orders_incl_tax: Union[Unset, float] = UNSET
    total_refund_purchase_taxes: Union[Unset, float] = UNSET
    total_seller_fees_on_orders_excl_tax: Union[Unset, float] = UNSET
    total_seller_fees_on_orders_incl_tax: Union[Unset, float] = UNSET
    total_seller_penalty_fees_excl_tax: Union[Unset, float] = UNSET
    total_seller_penalty_fees_incl_tax: Union[Unset, float] = UNSET
    total_subscription_excl_tax: Union[Unset, float] = UNSET
    total_subscription_incl_tax: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_transferred = self.amount_transferred

        amount_transferred_to_operator = self.amount_transferred_to_operator

        reserve_funding = self.reserve_funding

        reserve_settlement = self.reserve_settlement

        total_commissions_excl_tax = self.total_commissions_excl_tax

        total_commissions_incl_tax = self.total_commissions_incl_tax

        total_fee_excl_tax = self.total_fee_excl_tax

        total_fee_incl_tax = self.total_fee_incl_tax

        total_fee_operator_remitted_excl_tax = self.total_fee_operator_remitted_excl_tax

        total_fee_operator_remitted_incl_tax = self.total_fee_operator_remitted_incl_tax

        total_non_payable_orders_excl_tax = self.total_non_payable_orders_excl_tax

        total_non_payable_orders_incl_tax = self.total_non_payable_orders_incl_tax

        total_operator_paid_shipping_charges_excl_tax = self.total_operator_paid_shipping_charges_excl_tax

        total_operator_paid_shipping_charges_incl_tax = self.total_operator_paid_shipping_charges_incl_tax

        total_operator_remitted_taxes = self.total_operator_remitted_taxes

        total_other_credits_excl_tax = self.total_other_credits_excl_tax

        total_other_credits_incl_tax = self.total_other_credits_incl_tax

        total_other_invoices_excl_tax = self.total_other_invoices_excl_tax

        total_other_invoices_incl_tax = self.total_other_invoices_incl_tax

        total_payable_orders_excl_tax = self.total_payable_orders_excl_tax

        total_payable_orders_incl_tax = self.total_payable_orders_incl_tax

        total_purchase_taxes = self.total_purchase_taxes

        total_refund_commissions_excl_tax = self.total_refund_commissions_excl_tax

        total_refund_commissions_incl_tax = self.total_refund_commissions_incl_tax

        total_refund_fee_excl_tax = self.total_refund_fee_excl_tax

        total_refund_fee_incl_tax = self.total_refund_fee_incl_tax

        total_refund_fee_operator_remitted_excl_tax = self.total_refund_fee_operator_remitted_excl_tax

        total_refund_fee_operator_remitted_incl_tax = self.total_refund_fee_operator_remitted_incl_tax

        total_refund_non_payable_orders_excl_tax = self.total_refund_non_payable_orders_excl_tax

        total_refund_non_payable_orders_incl_tax = self.total_refund_non_payable_orders_incl_tax

        total_refund_operator_paid_shipping_charges_excl_tax = self.total_refund_operator_paid_shipping_charges_excl_tax

        total_refund_operator_paid_shipping_charges_incl_tax = self.total_refund_operator_paid_shipping_charges_incl_tax

        total_refund_operator_remitted_taxes = self.total_refund_operator_remitted_taxes

        total_refund_orders_excl_tax = self.total_refund_orders_excl_tax

        total_refund_orders_incl_tax = self.total_refund_orders_incl_tax

        total_refund_payable_orders_excl_tax = self.total_refund_payable_orders_excl_tax

        total_refund_payable_orders_incl_tax = self.total_refund_payable_orders_incl_tax

        total_refund_purchase_taxes = self.total_refund_purchase_taxes

        total_seller_fees_on_orders_excl_tax = self.total_seller_fees_on_orders_excl_tax

        total_seller_fees_on_orders_incl_tax = self.total_seller_fees_on_orders_incl_tax

        total_seller_penalty_fees_excl_tax = self.total_seller_penalty_fees_excl_tax

        total_seller_penalty_fees_incl_tax = self.total_seller_penalty_fees_incl_tax

        total_subscription_excl_tax = self.total_subscription_excl_tax

        total_subscription_incl_tax = self.total_subscription_incl_tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_transferred is not UNSET:
            field_dict["amount_transferred"] = amount_transferred
        if amount_transferred_to_operator is not UNSET:
            field_dict["amount_transferred_to_operator"] = amount_transferred_to_operator
        if reserve_funding is not UNSET:
            field_dict["reserve_funding"] = reserve_funding
        if reserve_settlement is not UNSET:
            field_dict["reserve_settlement"] = reserve_settlement
        if total_commissions_excl_tax is not UNSET:
            field_dict["total_commissions_excl_tax"] = total_commissions_excl_tax
        if total_commissions_incl_tax is not UNSET:
            field_dict["total_commissions_incl_tax"] = total_commissions_incl_tax
        if total_fee_excl_tax is not UNSET:
            field_dict["total_fee_excl_tax"] = total_fee_excl_tax
        if total_fee_incl_tax is not UNSET:
            field_dict["total_fee_incl_tax"] = total_fee_incl_tax
        if total_fee_operator_remitted_excl_tax is not UNSET:
            field_dict["total_fee_operator_remitted_excl_tax"] = total_fee_operator_remitted_excl_tax
        if total_fee_operator_remitted_incl_tax is not UNSET:
            field_dict["total_fee_operator_remitted_incl_tax"] = total_fee_operator_remitted_incl_tax
        if total_non_payable_orders_excl_tax is not UNSET:
            field_dict["total_non_payable_orders_excl_tax"] = total_non_payable_orders_excl_tax
        if total_non_payable_orders_incl_tax is not UNSET:
            field_dict["total_non_payable_orders_incl_tax"] = total_non_payable_orders_incl_tax
        if total_operator_paid_shipping_charges_excl_tax is not UNSET:
            field_dict["total_operator_paid_shipping_charges_excl_tax"] = total_operator_paid_shipping_charges_excl_tax
        if total_operator_paid_shipping_charges_incl_tax is not UNSET:
            field_dict["total_operator_paid_shipping_charges_incl_tax"] = total_operator_paid_shipping_charges_incl_tax
        if total_operator_remitted_taxes is not UNSET:
            field_dict["total_operator_remitted_taxes"] = total_operator_remitted_taxes
        if total_other_credits_excl_tax is not UNSET:
            field_dict["total_other_credits_excl_tax"] = total_other_credits_excl_tax
        if total_other_credits_incl_tax is not UNSET:
            field_dict["total_other_credits_incl_tax"] = total_other_credits_incl_tax
        if total_other_invoices_excl_tax is not UNSET:
            field_dict["total_other_invoices_excl_tax"] = total_other_invoices_excl_tax
        if total_other_invoices_incl_tax is not UNSET:
            field_dict["total_other_invoices_incl_tax"] = total_other_invoices_incl_tax
        if total_payable_orders_excl_tax is not UNSET:
            field_dict["total_payable_orders_excl_tax"] = total_payable_orders_excl_tax
        if total_payable_orders_incl_tax is not UNSET:
            field_dict["total_payable_orders_incl_tax"] = total_payable_orders_incl_tax
        if total_purchase_taxes is not UNSET:
            field_dict["total_purchase_taxes"] = total_purchase_taxes
        if total_refund_commissions_excl_tax is not UNSET:
            field_dict["total_refund_commissions_excl_tax"] = total_refund_commissions_excl_tax
        if total_refund_commissions_incl_tax is not UNSET:
            field_dict["total_refund_commissions_incl_tax"] = total_refund_commissions_incl_tax
        if total_refund_fee_excl_tax is not UNSET:
            field_dict["total_refund_fee_excl_tax"] = total_refund_fee_excl_tax
        if total_refund_fee_incl_tax is not UNSET:
            field_dict["total_refund_fee_incl_tax"] = total_refund_fee_incl_tax
        if total_refund_fee_operator_remitted_excl_tax is not UNSET:
            field_dict["total_refund_fee_operator_remitted_excl_tax"] = total_refund_fee_operator_remitted_excl_tax
        if total_refund_fee_operator_remitted_incl_tax is not UNSET:
            field_dict["total_refund_fee_operator_remitted_incl_tax"] = total_refund_fee_operator_remitted_incl_tax
        if total_refund_non_payable_orders_excl_tax is not UNSET:
            field_dict["total_refund_non_payable_orders_excl_tax"] = total_refund_non_payable_orders_excl_tax
        if total_refund_non_payable_orders_incl_tax is not UNSET:
            field_dict["total_refund_non_payable_orders_incl_tax"] = total_refund_non_payable_orders_incl_tax
        if total_refund_operator_paid_shipping_charges_excl_tax is not UNSET:
            field_dict["total_refund_operator_paid_shipping_charges_excl_tax"] = (
                total_refund_operator_paid_shipping_charges_excl_tax
            )
        if total_refund_operator_paid_shipping_charges_incl_tax is not UNSET:
            field_dict["total_refund_operator_paid_shipping_charges_incl_tax"] = (
                total_refund_operator_paid_shipping_charges_incl_tax
            )
        if total_refund_operator_remitted_taxes is not UNSET:
            field_dict["total_refund_operator_remitted_taxes"] = total_refund_operator_remitted_taxes
        if total_refund_orders_excl_tax is not UNSET:
            field_dict["total_refund_orders_excl_tax"] = total_refund_orders_excl_tax
        if total_refund_orders_incl_tax is not UNSET:
            field_dict["total_refund_orders_incl_tax"] = total_refund_orders_incl_tax
        if total_refund_payable_orders_excl_tax is not UNSET:
            field_dict["total_refund_payable_orders_excl_tax"] = total_refund_payable_orders_excl_tax
        if total_refund_payable_orders_incl_tax is not UNSET:
            field_dict["total_refund_payable_orders_incl_tax"] = total_refund_payable_orders_incl_tax
        if total_refund_purchase_taxes is not UNSET:
            field_dict["total_refund_purchase_taxes"] = total_refund_purchase_taxes
        if total_seller_fees_on_orders_excl_tax is not UNSET:
            field_dict["total_seller_fees_on_orders_excl_tax"] = total_seller_fees_on_orders_excl_tax
        if total_seller_fees_on_orders_incl_tax is not UNSET:
            field_dict["total_seller_fees_on_orders_incl_tax"] = total_seller_fees_on_orders_incl_tax
        if total_seller_penalty_fees_excl_tax is not UNSET:
            field_dict["total_seller_penalty_fees_excl_tax"] = total_seller_penalty_fees_excl_tax
        if total_seller_penalty_fees_incl_tax is not UNSET:
            field_dict["total_seller_penalty_fees_incl_tax"] = total_seller_penalty_fees_incl_tax
        if total_subscription_excl_tax is not UNSET:
            field_dict["total_subscription_excl_tax"] = total_subscription_excl_tax
        if total_subscription_incl_tax is not UNSET:
            field_dict["total_subscription_incl_tax"] = total_subscription_incl_tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_transferred = d.pop("amount_transferred", UNSET)

        amount_transferred_to_operator = d.pop("amount_transferred_to_operator", UNSET)

        reserve_funding = d.pop("reserve_funding", UNSET)

        reserve_settlement = d.pop("reserve_settlement", UNSET)

        total_commissions_excl_tax = d.pop("total_commissions_excl_tax", UNSET)

        total_commissions_incl_tax = d.pop("total_commissions_incl_tax", UNSET)

        total_fee_excl_tax = d.pop("total_fee_excl_tax", UNSET)

        total_fee_incl_tax = d.pop("total_fee_incl_tax", UNSET)

        total_fee_operator_remitted_excl_tax = d.pop("total_fee_operator_remitted_excl_tax", UNSET)

        total_fee_operator_remitted_incl_tax = d.pop("total_fee_operator_remitted_incl_tax", UNSET)

        total_non_payable_orders_excl_tax = d.pop("total_non_payable_orders_excl_tax", UNSET)

        total_non_payable_orders_incl_tax = d.pop("total_non_payable_orders_incl_tax", UNSET)

        total_operator_paid_shipping_charges_excl_tax = d.pop("total_operator_paid_shipping_charges_excl_tax", UNSET)

        total_operator_paid_shipping_charges_incl_tax = d.pop("total_operator_paid_shipping_charges_incl_tax", UNSET)

        total_operator_remitted_taxes = d.pop("total_operator_remitted_taxes", UNSET)

        total_other_credits_excl_tax = d.pop("total_other_credits_excl_tax", UNSET)

        total_other_credits_incl_tax = d.pop("total_other_credits_incl_tax", UNSET)

        total_other_invoices_excl_tax = d.pop("total_other_invoices_excl_tax", UNSET)

        total_other_invoices_incl_tax = d.pop("total_other_invoices_incl_tax", UNSET)

        total_payable_orders_excl_tax = d.pop("total_payable_orders_excl_tax", UNSET)

        total_payable_orders_incl_tax = d.pop("total_payable_orders_incl_tax", UNSET)

        total_purchase_taxes = d.pop("total_purchase_taxes", UNSET)

        total_refund_commissions_excl_tax = d.pop("total_refund_commissions_excl_tax", UNSET)

        total_refund_commissions_incl_tax = d.pop("total_refund_commissions_incl_tax", UNSET)

        total_refund_fee_excl_tax = d.pop("total_refund_fee_excl_tax", UNSET)

        total_refund_fee_incl_tax = d.pop("total_refund_fee_incl_tax", UNSET)

        total_refund_fee_operator_remitted_excl_tax = d.pop("total_refund_fee_operator_remitted_excl_tax", UNSET)

        total_refund_fee_operator_remitted_incl_tax = d.pop("total_refund_fee_operator_remitted_incl_tax", UNSET)

        total_refund_non_payable_orders_excl_tax = d.pop("total_refund_non_payable_orders_excl_tax", UNSET)

        total_refund_non_payable_orders_incl_tax = d.pop("total_refund_non_payable_orders_incl_tax", UNSET)

        total_refund_operator_paid_shipping_charges_excl_tax = d.pop(
            "total_refund_operator_paid_shipping_charges_excl_tax", UNSET
        )

        total_refund_operator_paid_shipping_charges_incl_tax = d.pop(
            "total_refund_operator_paid_shipping_charges_incl_tax", UNSET
        )

        total_refund_operator_remitted_taxes = d.pop("total_refund_operator_remitted_taxes", UNSET)

        total_refund_orders_excl_tax = d.pop("total_refund_orders_excl_tax", UNSET)

        total_refund_orders_incl_tax = d.pop("total_refund_orders_incl_tax", UNSET)

        total_refund_payable_orders_excl_tax = d.pop("total_refund_payable_orders_excl_tax", UNSET)

        total_refund_payable_orders_incl_tax = d.pop("total_refund_payable_orders_incl_tax", UNSET)

        total_refund_purchase_taxes = d.pop("total_refund_purchase_taxes", UNSET)

        total_seller_fees_on_orders_excl_tax = d.pop("total_seller_fees_on_orders_excl_tax", UNSET)

        total_seller_fees_on_orders_incl_tax = d.pop("total_seller_fees_on_orders_incl_tax", UNSET)

        total_seller_penalty_fees_excl_tax = d.pop("total_seller_penalty_fees_excl_tax", UNSET)

        total_seller_penalty_fees_incl_tax = d.pop("total_seller_penalty_fees_incl_tax", UNSET)

        total_subscription_excl_tax = d.pop("total_subscription_excl_tax", UNSET)

        total_subscription_incl_tax = d.pop("total_subscription_incl_tax", UNSET)

        iv01_response_200_invoices_auto_invoice_summary = cls(
            amount_transferred=amount_transferred,
            amount_transferred_to_operator=amount_transferred_to_operator,
            reserve_funding=reserve_funding,
            reserve_settlement=reserve_settlement,
            total_commissions_excl_tax=total_commissions_excl_tax,
            total_commissions_incl_tax=total_commissions_incl_tax,
            total_fee_excl_tax=total_fee_excl_tax,
            total_fee_incl_tax=total_fee_incl_tax,
            total_fee_operator_remitted_excl_tax=total_fee_operator_remitted_excl_tax,
            total_fee_operator_remitted_incl_tax=total_fee_operator_remitted_incl_tax,
            total_non_payable_orders_excl_tax=total_non_payable_orders_excl_tax,
            total_non_payable_orders_incl_tax=total_non_payable_orders_incl_tax,
            total_operator_paid_shipping_charges_excl_tax=total_operator_paid_shipping_charges_excl_tax,
            total_operator_paid_shipping_charges_incl_tax=total_operator_paid_shipping_charges_incl_tax,
            total_operator_remitted_taxes=total_operator_remitted_taxes,
            total_other_credits_excl_tax=total_other_credits_excl_tax,
            total_other_credits_incl_tax=total_other_credits_incl_tax,
            total_other_invoices_excl_tax=total_other_invoices_excl_tax,
            total_other_invoices_incl_tax=total_other_invoices_incl_tax,
            total_payable_orders_excl_tax=total_payable_orders_excl_tax,
            total_payable_orders_incl_tax=total_payable_orders_incl_tax,
            total_purchase_taxes=total_purchase_taxes,
            total_refund_commissions_excl_tax=total_refund_commissions_excl_tax,
            total_refund_commissions_incl_tax=total_refund_commissions_incl_tax,
            total_refund_fee_excl_tax=total_refund_fee_excl_tax,
            total_refund_fee_incl_tax=total_refund_fee_incl_tax,
            total_refund_fee_operator_remitted_excl_tax=total_refund_fee_operator_remitted_excl_tax,
            total_refund_fee_operator_remitted_incl_tax=total_refund_fee_operator_remitted_incl_tax,
            total_refund_non_payable_orders_excl_tax=total_refund_non_payable_orders_excl_tax,
            total_refund_non_payable_orders_incl_tax=total_refund_non_payable_orders_incl_tax,
            total_refund_operator_paid_shipping_charges_excl_tax=total_refund_operator_paid_shipping_charges_excl_tax,
            total_refund_operator_paid_shipping_charges_incl_tax=total_refund_operator_paid_shipping_charges_incl_tax,
            total_refund_operator_remitted_taxes=total_refund_operator_remitted_taxes,
            total_refund_orders_excl_tax=total_refund_orders_excl_tax,
            total_refund_orders_incl_tax=total_refund_orders_incl_tax,
            total_refund_payable_orders_excl_tax=total_refund_payable_orders_excl_tax,
            total_refund_payable_orders_incl_tax=total_refund_payable_orders_incl_tax,
            total_refund_purchase_taxes=total_refund_purchase_taxes,
            total_seller_fees_on_orders_excl_tax=total_seller_fees_on_orders_excl_tax,
            total_seller_fees_on_orders_incl_tax=total_seller_fees_on_orders_incl_tax,
            total_seller_penalty_fees_excl_tax=total_seller_penalty_fees_excl_tax,
            total_seller_penalty_fees_incl_tax=total_seller_penalty_fees_incl_tax,
            total_subscription_excl_tax=total_subscription_excl_tax,
            total_subscription_incl_tax=total_subscription_incl_tax,
        )

        iv01_response_200_invoices_auto_invoice_summary.additional_properties = d
        return iv01_response_200_invoices_auto_invoice_summary

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
