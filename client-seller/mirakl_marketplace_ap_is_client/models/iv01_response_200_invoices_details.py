import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iv01_response_200_invoices_details_taxes import IV01Response200InvoicesDetailsTaxes


T = TypeVar("T", bound="IV01Response200InvoicesDetails")


@_attrs_define
class IV01Response200InvoicesDetails:
    """
    Attributes:
        amount_excl_taxes (Union[Unset, float]): Amount excluding taxes
        description (Union[Unset, str]): Description
        operation_date (Union[Unset, datetime.datetime]): Operation date for <code>MANUAL_INVOICE</code> or
            <code>MANUAL_CREDIT</code> type
        order_id (Union[Unset, str]): Associated order id. Only for <code>MANUAL_INVOICE</code> or
            <code>MANUAL_CREDIT</code> type
        quantity (Union[Unset, int]): Quantity
        taxes (Union[Unset, list['IV01Response200InvoicesDetailsTaxes']]): Taxes
    """

    amount_excl_taxes: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    operation_date: Union[Unset, datetime.datetime] = UNSET
    order_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    taxes: Union[Unset, list["IV01Response200InvoicesDetailsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_excl_taxes = self.amount_excl_taxes

        description = self.description

        operation_date: Union[Unset, str] = UNSET
        if not isinstance(self.operation_date, Unset):
            operation_date = self.operation_date.isoformat()

        order_id = self.order_id

        quantity = self.quantity

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_excl_taxes is not UNSET:
            field_dict["amount_excl_taxes"] = amount_excl_taxes
        if description is not UNSET:
            field_dict["description"] = description
        if operation_date is not UNSET:
            field_dict["operation_date"] = operation_date
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iv01_response_200_invoices_details_taxes import IV01Response200InvoicesDetailsTaxes

        d = dict(src_dict)
        amount_excl_taxes = d.pop("amount_excl_taxes", UNSET)

        description = d.pop("description", UNSET)

        _operation_date = d.pop("operation_date", UNSET)
        operation_date: Union[Unset, datetime.datetime]
        if isinstance(_operation_date, Unset):
            operation_date = UNSET
        else:
            operation_date = isoparse(_operation_date)

        order_id = d.pop("order_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = IV01Response200InvoicesDetailsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        iv01_response_200_invoices_details = cls(
            amount_excl_taxes=amount_excl_taxes,
            description=description,
            operation_date=operation_date,
            order_id=order_id,
            quantity=quantity,
            taxes=taxes,
        )

        iv01_response_200_invoices_details.additional_properties = d
        return iv01_response_200_invoices_details

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
