import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iv01_response_200_invoices_details import IV01Response200InvoicesDetails
    from ..models.iv01_response_200_invoices_issuing_user import IV01Response200InvoicesIssuingUser
    from ..models.iv01_response_200_invoices_payment import IV01Response200InvoicesPayment
    from ..models.iv01_response_200_invoices_shop_address import IV01Response200InvoicesShopAddress
    from ..models.iv01_response_200_invoices_total_taxes import IV01Response200InvoicesTotalTaxes


T = TypeVar("T", bound="IV01Response200Invoices")


@_attrs_define
class IV01Response200Invoices:
    """
    Attributes:
        currency_iso_code (Union[Unset, str]): The currency of the shop
        date_created (Union[Unset, datetime.datetime]): Accounting document creation date
        details (Union[Unset, list['IV01Response200InvoicesDetails']]): Accounting details
        due_date (Union[Unset, datetime.datetime]): Due date for the payment of the accounting document
        id (Union[Unset, str]): Accounting document identifier (use it for draft document)
        invoice_id (Union[Unset, int]): Accounting document identifier (present if the accounting document is issued)
        issue_date (Union[Unset, datetime.datetime]): Issue date of an accounting document
        issuing_user (Union[Unset, IV01Response200InvoicesIssuingUser]):
        pay_out_psp_code (Union[Unset, str]): PSP code for Pay-out
        payment (Union[Unset, IV01Response200InvoicesPayment]):
        shop_address (Union[Unset, IV01Response200InvoicesShopAddress]):
        shop_corporate_name (Union[Unset, str]): Shop corporate name if it is a professional shop
        shop_id (Union[Unset, int]): Shop id
        shop_model (Union[Unset, str]): Shop model
        shop_name (Union[Unset, str]): Shop name
        shop_operator_internal_id (Union[Unset, str]): Operator internal id for the shop
        shop_tax_number (Union[Unset, str]): Shop tax number if it is a professional shop
        state (Union[Unset, str]): Accounting document state
        total_amount_excl_taxes (Union[Unset, float]): Total amount charged to the shop (excluding taxes)
        total_amount_incl_taxes (Union[Unset, float]): Total amount charged to the shop (including taxes)
        total_taxes (Union[Unset, list['IV01Response200InvoicesTotalTaxes']]): Total taxes
        type_ (Union[Unset, str]): Accounting document type
    """

    currency_iso_code: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    details: Union[Unset, list["IV01Response200InvoicesDetails"]] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, int] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    issuing_user: Union[Unset, "IV01Response200InvoicesIssuingUser"] = UNSET
    pay_out_psp_code: Union[Unset, str] = UNSET
    payment: Union[Unset, "IV01Response200InvoicesPayment"] = UNSET
    shop_address: Union[Unset, "IV01Response200InvoicesShopAddress"] = UNSET
    shop_corporate_name: Union[Unset, str] = UNSET
    shop_id: Union[Unset, int] = UNSET
    shop_model: Union[Unset, str] = UNSET
    shop_name: Union[Unset, str] = UNSET
    shop_operator_internal_id: Union[Unset, str] = UNSET
    shop_tax_number: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    total_amount_excl_taxes: Union[Unset, float] = UNSET
    total_amount_incl_taxes: Union[Unset, float] = UNSET
    total_taxes: Union[Unset, list["IV01Response200InvoicesTotalTaxes"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_iso_code = self.currency_iso_code

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        id = self.id

        invoice_id = self.invoice_id

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        issuing_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issuing_user, Unset):
            issuing_user = self.issuing_user.to_dict()

        pay_out_psp_code = self.pay_out_psp_code

        payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        shop_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shop_address, Unset):
            shop_address = self.shop_address.to_dict()

        shop_corporate_name = self.shop_corporate_name

        shop_id = self.shop_id

        shop_model = self.shop_model

        shop_name = self.shop_name

        shop_operator_internal_id = self.shop_operator_internal_id

        shop_tax_number = self.shop_tax_number

        state = self.state

        total_amount_excl_taxes = self.total_amount_excl_taxes

        total_amount_incl_taxes = self.total_amount_incl_taxes

        total_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.total_taxes, Unset):
            total_taxes = []
            for total_taxes_item_data in self.total_taxes:
                total_taxes_item = total_taxes_item_data.to_dict()
                total_taxes.append(total_taxes_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if details is not UNSET:
            field_dict["details"] = details
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if issuing_user is not UNSET:
            field_dict["issuing_user"] = issuing_user
        if pay_out_psp_code is not UNSET:
            field_dict["pay_out_psp_code"] = pay_out_psp_code
        if payment is not UNSET:
            field_dict["payment"] = payment
        if shop_address is not UNSET:
            field_dict["shop_address"] = shop_address
        if shop_corporate_name is not UNSET:
            field_dict["shop_corporate_name"] = shop_corporate_name
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if shop_model is not UNSET:
            field_dict["shop_model"] = shop_model
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if shop_operator_internal_id is not UNSET:
            field_dict["shop_operator_internal_id"] = shop_operator_internal_id
        if shop_tax_number is not UNSET:
            field_dict["shop_tax_number"] = shop_tax_number
        if state is not UNSET:
            field_dict["state"] = state
        if total_amount_excl_taxes is not UNSET:
            field_dict["total_amount_excl_taxes"] = total_amount_excl_taxes
        if total_amount_incl_taxes is not UNSET:
            field_dict["total_amount_incl_taxes"] = total_amount_incl_taxes
        if total_taxes is not UNSET:
            field_dict["total_taxes"] = total_taxes
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iv01_response_200_invoices_details import IV01Response200InvoicesDetails
        from ..models.iv01_response_200_invoices_issuing_user import IV01Response200InvoicesIssuingUser
        from ..models.iv01_response_200_invoices_payment import IV01Response200InvoicesPayment
        from ..models.iv01_response_200_invoices_shop_address import IV01Response200InvoicesShopAddress
        from ..models.iv01_response_200_invoices_total_taxes import IV01Response200InvoicesTotalTaxes

        d = dict(src_dict)
        currency_iso_code = d.pop("currency_iso_code", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = IV01Response200InvoicesDetails.from_dict(details_item_data)

            details.append(details_item)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        id = d.pop("id", UNSET)

        invoice_id = d.pop("invoice_id", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        _issuing_user = d.pop("issuing_user", UNSET)
        issuing_user: Union[Unset, IV01Response200InvoicesIssuingUser]
        if isinstance(_issuing_user, Unset):
            issuing_user = UNSET
        else:
            issuing_user = IV01Response200InvoicesIssuingUser.from_dict(_issuing_user)

        pay_out_psp_code = d.pop("pay_out_psp_code", UNSET)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, IV01Response200InvoicesPayment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = IV01Response200InvoicesPayment.from_dict(_payment)

        _shop_address = d.pop("shop_address", UNSET)
        shop_address: Union[Unset, IV01Response200InvoicesShopAddress]
        if isinstance(_shop_address, Unset):
            shop_address = UNSET
        else:
            shop_address = IV01Response200InvoicesShopAddress.from_dict(_shop_address)

        shop_corporate_name = d.pop("shop_corporate_name", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        shop_model = d.pop("shop_model", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        shop_operator_internal_id = d.pop("shop_operator_internal_id", UNSET)

        shop_tax_number = d.pop("shop_tax_number", UNSET)

        state = d.pop("state", UNSET)

        total_amount_excl_taxes = d.pop("total_amount_excl_taxes", UNSET)

        total_amount_incl_taxes = d.pop("total_amount_incl_taxes", UNSET)

        total_taxes = []
        _total_taxes = d.pop("total_taxes", UNSET)
        for total_taxes_item_data in _total_taxes or []:
            total_taxes_item = IV01Response200InvoicesTotalTaxes.from_dict(total_taxes_item_data)

            total_taxes.append(total_taxes_item)

        type_ = d.pop("type", UNSET)

        iv01_response_200_invoices = cls(
            currency_iso_code=currency_iso_code,
            date_created=date_created,
            details=details,
            due_date=due_date,
            id=id,
            invoice_id=invoice_id,
            issue_date=issue_date,
            issuing_user=issuing_user,
            pay_out_psp_code=pay_out_psp_code,
            payment=payment,
            shop_address=shop_address,
            shop_corporate_name=shop_corporate_name,
            shop_id=shop_id,
            shop_model=shop_model,
            shop_name=shop_name,
            shop_operator_internal_id=shop_operator_internal_id,
            shop_tax_number=shop_tax_number,
            state=state,
            total_amount_excl_taxes=total_amount_excl_taxes,
            total_amount_incl_taxes=total_amount_incl_taxes,
            total_taxes=total_taxes,
            type_=type_,
        )

        iv01_response_200_invoices.additional_properties = d
        return iv01_response_200_invoices

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
