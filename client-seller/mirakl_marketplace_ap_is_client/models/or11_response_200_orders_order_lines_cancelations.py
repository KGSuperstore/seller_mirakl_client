import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_cancelations_amount_breakdown import (
        OR11Response200OrdersOrderLinesCancelationsAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_commission_taxes import (
        OR11Response200OrdersOrderLinesCancelationsCommissionTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_eco_contributions import (
        OR11Response200OrdersOrderLinesCancelationsEcoContributions,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_fees import (
        OR11Response200OrdersOrderLinesCancelationsFees,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_purchase_information import (
        OR11Response200OrdersOrderLinesCancelationsPurchaseInformation,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_shipping_amount_breakdown import (
        OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_shipping_taxes import (
        OR11Response200OrdersOrderLinesCancelationsShippingTaxes,
    )
    from ..models.or11_response_200_orders_order_lines_cancelations_taxes import (
        OR11Response200OrdersOrderLinesCancelationsTaxes,
    )


T = TypeVar("T", bound="OR11Response200OrdersOrderLinesCancelations")


@_attrs_define
class OR11Response200OrdersOrderLinesCancelations:
    """
    Attributes:
        amount (Union[Unset, float]): Cancellation's amount
        amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesCancelationsAmountBreakdown]):
        commission_amount (Union[Unset, float]): Cancellation's commission amount
        commission_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesCancelationsCommissionTaxes']]):
            Cancellation's commission taxes
        commission_total_amount (Union[Unset, float]): The total commission amount of the cancellation (commission
            amount + commission taxes)
        created_date (Union[Unset, datetime.datetime]): Cancellation's creation date
        eco_contributions (Union[Unset, list['OR11Response200OrdersOrderLinesCancelationsEcoContributions']]): List of
            eco-contribution amounts and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        fees (Union[Unset, list['OR11Response200OrdersOrderLinesCancelationsFees']]): List of fees canceled on the order
            line
        id (Union[Unset, str]): Cancellation's id
        purchase_information (Union[Unset, OR11Response200OrdersOrderLinesCancelationsPurchaseInformation]):
        quantity (Union[Unset, int]): The quantity of products canceled (This quantity is informative only)
        reason_code (Union[Unset, str]): Cancellation reason's code
        shipping_amount (Union[Unset, float]): Cancellation's shipping amount
        shipping_amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown]):
        shipping_taxes (Union[Unset, list['OR11Response200OrdersOrderLinesCancelationsShippingTaxes']]): The taxes on
            the shipping price
        taxes (Union[Unset, list['OR11Response200OrdersOrderLinesCancelationsTaxes']]): The taxes on the price
    """

    amount: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesCancelationsAmountBreakdown"] = UNSET
    commission_amount: Union[Unset, float] = UNSET
    commission_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesCancelationsCommissionTaxes"]] = UNSET
    commission_total_amount: Union[Unset, float] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    eco_contributions: Union[Unset, list["OR11Response200OrdersOrderLinesCancelationsEcoContributions"]] = UNSET
    fees: Union[Unset, list["OR11Response200OrdersOrderLinesCancelationsFees"]] = UNSET
    id: Union[Unset, str] = UNSET
    purchase_information: Union[Unset, "OR11Response200OrdersOrderLinesCancelationsPurchaseInformation"] = UNSET
    quantity: Union[Unset, int] = UNSET
    reason_code: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown"] = (
        UNSET
    )
    shipping_taxes: Union[Unset, list["OR11Response200OrdersOrderLinesCancelationsShippingTaxes"]] = UNSET
    taxes: Union[Unset, list["OR11Response200OrdersOrderLinesCancelationsTaxes"]] = UNSET
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

        purchase_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_information, Unset):
            purchase_information = self.purchase_information.to_dict()

        quantity = self.quantity

        reason_code = self.reason_code

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

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

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
        if purchase_information is not UNSET:
            field_dict["purchase_information"] = purchase_information
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if shipping_amount is not UNSET:
            field_dict["shipping_amount"] = shipping_amount
        if shipping_amount_breakdown is not UNSET:
            field_dict["shipping_amount_breakdown"] = shipping_amount_breakdown
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_lines_cancelations_amount_breakdown import (
            OR11Response200OrdersOrderLinesCancelationsAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_commission_taxes import (
            OR11Response200OrdersOrderLinesCancelationsCommissionTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_eco_contributions import (
            OR11Response200OrdersOrderLinesCancelationsEcoContributions,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_fees import (
            OR11Response200OrdersOrderLinesCancelationsFees,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_purchase_information import (
            OR11Response200OrdersOrderLinesCancelationsPurchaseInformation,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_shipping_amount_breakdown import (
            OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_shipping_taxes import (
            OR11Response200OrdersOrderLinesCancelationsShippingTaxes,
        )
        from ..models.or11_response_200_orders_order_lines_cancelations_taxes import (
            OR11Response200OrdersOrderLinesCancelationsTaxes,
        )

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _amount_breakdown = d.pop("amount_breakdown", UNSET)
        amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesCancelationsAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = OR11Response200OrdersOrderLinesCancelationsAmountBreakdown.from_dict(_amount_breakdown)

        commission_amount = d.pop("commission_amount", UNSET)

        commission_taxes = []
        _commission_taxes = d.pop("commission_taxes", UNSET)
        for commission_taxes_item_data in _commission_taxes or []:
            commission_taxes_item = OR11Response200OrdersOrderLinesCancelationsCommissionTaxes.from_dict(
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
            eco_contributions_item = OR11Response200OrdersOrderLinesCancelationsEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR11Response200OrdersOrderLinesCancelationsFees.from_dict(fees_item_data)

            fees.append(fees_item)

        id = d.pop("id", UNSET)

        _purchase_information = d.pop("purchase_information", UNSET)
        purchase_information: Union[Unset, OR11Response200OrdersOrderLinesCancelationsPurchaseInformation]
        if isinstance(_purchase_information, Unset):
            purchase_information = UNSET
        else:
            purchase_information = OR11Response200OrdersOrderLinesCancelationsPurchaseInformation.from_dict(
                _purchase_information
            )

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        _shipping_amount_breakdown = d.pop("shipping_amount_breakdown", UNSET)
        shipping_amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown]
        if isinstance(_shipping_amount_breakdown, Unset):
            shipping_amount_breakdown = UNSET
        else:
            shipping_amount_breakdown = OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown.from_dict(
                _shipping_amount_breakdown
            )

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR11Response200OrdersOrderLinesCancelationsShippingTaxes.from_dict(
                shipping_taxes_item_data
            )

            shipping_taxes.append(shipping_taxes_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR11Response200OrdersOrderLinesCancelationsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or11_response_200_orders_order_lines_cancelations = cls(
            amount=amount,
            amount_breakdown=amount_breakdown,
            commission_amount=commission_amount,
            commission_taxes=commission_taxes,
            commission_total_amount=commission_total_amount,
            created_date=created_date,
            eco_contributions=eco_contributions,
            fees=fees,
            id=id,
            purchase_information=purchase_information,
            quantity=quantity,
            reason_code=reason_code,
            shipping_amount=shipping_amount,
            shipping_amount_breakdown=shipping_amount_breakdown,
            shipping_taxes=shipping_taxes,
            taxes=taxes,
        )

        or11_response_200_orders_order_lines_cancelations.additional_properties = d
        return or11_response_200_orders_order_lines_cancelations

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
