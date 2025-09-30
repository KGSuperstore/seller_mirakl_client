from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesOrderWorkflows")


@_attrs_define
class PC01Response200FeaturesOrderWorkflows:
    """
    Attributes:
        no_customer_payment_confirmation (Union[Unset, bool]): Allows seller payments to be completely separated from
            customer debits
        order_acceptance (Union[Unset, str]): Indicate if shop accounts must accept new orders and take responsibility
            for the transaction. NOT_AUTOMATIC: All shop accounts must accept their orders manually. AUTOMATIC: Orders are
            automatically accepted. BOTH: AUTOMATIC or NOT_AUTOMATIC mode depending on the store account
        pause_debit_workflow (Union[Unset, bool]): Pause the order debit workflow when taxes must be recalculated
        pay_on_due_date (Union[Unset, bool]): Allows professionals to pay their orders after the receipt of the items or
            an explicit invoice
        pay_on_shipment (Union[Unset, bool]): Allows operators to debit orders before they have been fully shipped
        sellers_edit_shipping_origin (Union[Unset, bool]): Allow shop accounts to edit shipping origin to ensures
            accurate tax calculations with shipping origin data
        shipping_and_billing_details_before_acceptance (Union[Unset, bool]): Indicate if shipping and billing details
            are displayed before order acceptance
    """

    no_customer_payment_confirmation: Union[Unset, bool] = UNSET
    order_acceptance: Union[Unset, str] = UNSET
    pause_debit_workflow: Union[Unset, bool] = UNSET
    pay_on_due_date: Union[Unset, bool] = UNSET
    pay_on_shipment: Union[Unset, bool] = UNSET
    sellers_edit_shipping_origin: Union[Unset, bool] = UNSET
    shipping_and_billing_details_before_acceptance: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_customer_payment_confirmation = self.no_customer_payment_confirmation

        order_acceptance = self.order_acceptance

        pause_debit_workflow = self.pause_debit_workflow

        pay_on_due_date = self.pay_on_due_date

        pay_on_shipment = self.pay_on_shipment

        sellers_edit_shipping_origin = self.sellers_edit_shipping_origin

        shipping_and_billing_details_before_acceptance = self.shipping_and_billing_details_before_acceptance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_customer_payment_confirmation is not UNSET:
            field_dict["no_customer_payment_confirmation"] = no_customer_payment_confirmation
        if order_acceptance is not UNSET:
            field_dict["order_acceptance"] = order_acceptance
        if pause_debit_workflow is not UNSET:
            field_dict["pause_debit_workflow"] = pause_debit_workflow
        if pay_on_due_date is not UNSET:
            field_dict["pay_on_due_date"] = pay_on_due_date
        if pay_on_shipment is not UNSET:
            field_dict["pay_on_shipment"] = pay_on_shipment
        if sellers_edit_shipping_origin is not UNSET:
            field_dict["sellers_edit_shipping_origin"] = sellers_edit_shipping_origin
        if shipping_and_billing_details_before_acceptance is not UNSET:
            field_dict["shipping_and_billing_details_before_acceptance"] = (
                shipping_and_billing_details_before_acceptance
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no_customer_payment_confirmation = d.pop("no_customer_payment_confirmation", UNSET)

        order_acceptance = d.pop("order_acceptance", UNSET)

        pause_debit_workflow = d.pop("pause_debit_workflow", UNSET)

        pay_on_due_date = d.pop("pay_on_due_date", UNSET)

        pay_on_shipment = d.pop("pay_on_shipment", UNSET)

        sellers_edit_shipping_origin = d.pop("sellers_edit_shipping_origin", UNSET)

        shipping_and_billing_details_before_acceptance = d.pop("shipping_and_billing_details_before_acceptance", UNSET)

        pc01_response_200_features_order_workflows = cls(
            no_customer_payment_confirmation=no_customer_payment_confirmation,
            order_acceptance=order_acceptance,
            pause_debit_workflow=pause_debit_workflow,
            pay_on_due_date=pay_on_due_date,
            pay_on_shipment=pay_on_shipment,
            sellers_edit_shipping_origin=sellers_edit_shipping_origin,
            shipping_and_billing_details_before_acceptance=shipping_and_billing_details_before_acceptance,
        )

        pc01_response_200_features_order_workflows.additional_properties = d
        return pc01_response_200_features_order_workflows

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
