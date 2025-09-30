import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TL03Request")


@_attrs_define
class TL03Request:
    """
    Attributes:
        accounting_document_id (Union[Unset, str]): Accounting document id for filtering. This parameter only filter
            documents requests of the type: <code>SHOP_BILLING_CYCLE_PURCHASE_ORDER</code>.
        accounting_document_number (Union[Unset, str]): Accounting document number for filtering.
        date_created_from (Union[Unset, datetime.datetime]): Creation date for filtering
        date_created_to (Union[Unset, datetime.datetime]): Creation date for filtering
        items_per_chunk (Union[Unset, int]): The maximum number of items per chunk.
        last_updated_from (Union[Unset, datetime.datetime]): Last updated date for filtering
        megabytes_per_chunk (Union[Unset, int]): The maximum size in megabytes of a chunk.
        order_id (Union[Unset, list[str]]): Order id for filtering. This parameter can be supplied multiple times.
        order_line_id (Union[Unset, list[str]]): Order line id for filtering. This parameter can be supplied multiple
            times.
        order_reference_for_customer (Union[Unset, list[str]]): A comma-separated list of order references for customer.
        order_reference_for_seller (Union[Unset, list[str]]): A comma-separated list of order references for seller.
        pay_out_psp_codes (Union[Unset, list[str]]): A comma-separated list of pay-out PSP codes for filtering. This
            parameter requires the Hybrid pay-out PSP feature to be enabled.
        payment_state (Union[Unset, list[str]]): Payment state for filtering. This parameter can be supplied multiple
            times.
        payment_voucher_number (Union[Unset, str]): Payment voucher for filtering
        shop_domain (Union[Unset, list[str]]): A shop domain for filtering. This parameter can be supplied multiple
            times.
        shop_id (Union[Unset, int]): Shop identifier
        shop_model (Union[Unset, list[str]]): Shop model for filtering. This parameter can be supplied multiple times.
        transaction_date_from (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_date_to (Union[Unset, datetime.datetime]): Transaction date for filtering
        transaction_type (Union[Unset, list[str]]): Transaction type for filtering. This parameter can be supplied
            multiple times.
    """

    accounting_document_id: Union[Unset, str] = UNSET
    accounting_document_number: Union[Unset, str] = UNSET
    date_created_from: Union[Unset, datetime.datetime] = UNSET
    date_created_to: Union[Unset, datetime.datetime] = UNSET
    items_per_chunk: Union[Unset, int] = UNSET
    last_updated_from: Union[Unset, datetime.datetime] = UNSET
    megabytes_per_chunk: Union[Unset, int] = UNSET
    order_id: Union[Unset, list[str]] = UNSET
    order_line_id: Union[Unset, list[str]] = UNSET
    order_reference_for_customer: Union[Unset, list[str]] = UNSET
    order_reference_for_seller: Union[Unset, list[str]] = UNSET
    pay_out_psp_codes: Union[Unset, list[str]] = UNSET
    payment_state: Union[Unset, list[str]] = UNSET
    payment_voucher_number: Union[Unset, str] = UNSET
    shop_domain: Union[Unset, list[str]] = UNSET
    shop_id: Union[Unset, int] = UNSET
    shop_model: Union[Unset, list[str]] = UNSET
    transaction_date_from: Union[Unset, datetime.datetime] = UNSET
    transaction_date_to: Union[Unset, datetime.datetime] = UNSET
    transaction_type: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_document_id = self.accounting_document_id

        accounting_document_number = self.accounting_document_number

        date_created_from: Union[Unset, str] = UNSET
        if not isinstance(self.date_created_from, Unset):
            date_created_from = self.date_created_from.isoformat()

        date_created_to: Union[Unset, str] = UNSET
        if not isinstance(self.date_created_to, Unset):
            date_created_to = self.date_created_to.isoformat()

        items_per_chunk = self.items_per_chunk

        last_updated_from: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_from, Unset):
            last_updated_from = self.last_updated_from.isoformat()

        megabytes_per_chunk = self.megabytes_per_chunk

        order_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = self.order_id

        order_line_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_line_id, Unset):
            order_line_id = self.order_line_id

        order_reference_for_customer: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_reference_for_customer, Unset):
            order_reference_for_customer = self.order_reference_for_customer

        order_reference_for_seller: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_reference_for_seller, Unset):
            order_reference_for_seller = self.order_reference_for_seller

        pay_out_psp_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pay_out_psp_codes, Unset):
            pay_out_psp_codes = self.pay_out_psp_codes

        payment_state: Union[Unset, list[str]] = UNSET
        if not isinstance(self.payment_state, Unset):
            payment_state = self.payment_state

        payment_voucher_number = self.payment_voucher_number

        shop_domain: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shop_domain, Unset):
            shop_domain = self.shop_domain

        shop_id = self.shop_id

        shop_model: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shop_model, Unset):
            shop_model = self.shop_model

        transaction_date_from: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date_from, Unset):
            transaction_date_from = self.transaction_date_from.isoformat()

        transaction_date_to: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date_to, Unset):
            transaction_date_to = self.transaction_date_to.isoformat()

        transaction_type: Union[Unset, list[str]] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_document_id is not UNSET:
            field_dict["accounting_document_id"] = accounting_document_id
        if accounting_document_number is not UNSET:
            field_dict["accounting_document_number"] = accounting_document_number
        if date_created_from is not UNSET:
            field_dict["date_created_from"] = date_created_from
        if date_created_to is not UNSET:
            field_dict["date_created_to"] = date_created_to
        if items_per_chunk is not UNSET:
            field_dict["items_per_chunk"] = items_per_chunk
        if last_updated_from is not UNSET:
            field_dict["last_updated_from"] = last_updated_from
        if megabytes_per_chunk is not UNSET:
            field_dict["megabytes_per_chunk"] = megabytes_per_chunk
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if order_reference_for_customer is not UNSET:
            field_dict["order_reference_for_customer"] = order_reference_for_customer
        if order_reference_for_seller is not UNSET:
            field_dict["order_reference_for_seller"] = order_reference_for_seller
        if pay_out_psp_codes is not UNSET:
            field_dict["pay_out_psp_codes"] = pay_out_psp_codes
        if payment_state is not UNSET:
            field_dict["payment_state"] = payment_state
        if payment_voucher_number is not UNSET:
            field_dict["payment_voucher_number"] = payment_voucher_number
        if shop_domain is not UNSET:
            field_dict["shop_domain"] = shop_domain
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if shop_model is not UNSET:
            field_dict["shop_model"] = shop_model
        if transaction_date_from is not UNSET:
            field_dict["transaction_date_from"] = transaction_date_from
        if transaction_date_to is not UNSET:
            field_dict["transaction_date_to"] = transaction_date_to
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_document_id = d.pop("accounting_document_id", UNSET)

        accounting_document_number = d.pop("accounting_document_number", UNSET)

        _date_created_from = d.pop("date_created_from", UNSET)
        date_created_from: Union[Unset, datetime.datetime]
        if isinstance(_date_created_from, Unset):
            date_created_from = UNSET
        else:
            date_created_from = isoparse(_date_created_from)

        _date_created_to = d.pop("date_created_to", UNSET)
        date_created_to: Union[Unset, datetime.datetime]
        if isinstance(_date_created_to, Unset):
            date_created_to = UNSET
        else:
            date_created_to = isoparse(_date_created_to)

        items_per_chunk = d.pop("items_per_chunk", UNSET)

        _last_updated_from = d.pop("last_updated_from", UNSET)
        last_updated_from: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_from, Unset):
            last_updated_from = UNSET
        else:
            last_updated_from = isoparse(_last_updated_from)

        megabytes_per_chunk = d.pop("megabytes_per_chunk", UNSET)

        order_id = cast(list[str], d.pop("order_id", UNSET))

        order_line_id = cast(list[str], d.pop("order_line_id", UNSET))

        order_reference_for_customer = cast(list[str], d.pop("order_reference_for_customer", UNSET))

        order_reference_for_seller = cast(list[str], d.pop("order_reference_for_seller", UNSET))

        pay_out_psp_codes = cast(list[str], d.pop("pay_out_psp_codes", UNSET))

        payment_state = cast(list[str], d.pop("payment_state", UNSET))

        payment_voucher_number = d.pop("payment_voucher_number", UNSET)

        shop_domain = cast(list[str], d.pop("shop_domain", UNSET))

        shop_id = d.pop("shop_id", UNSET)

        shop_model = cast(list[str], d.pop("shop_model", UNSET))

        _transaction_date_from = d.pop("transaction_date_from", UNSET)
        transaction_date_from: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date_from, Unset):
            transaction_date_from = UNSET
        else:
            transaction_date_from = isoparse(_transaction_date_from)

        _transaction_date_to = d.pop("transaction_date_to", UNSET)
        transaction_date_to: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date_to, Unset):
            transaction_date_to = UNSET
        else:
            transaction_date_to = isoparse(_transaction_date_to)

        transaction_type = cast(list[str], d.pop("transaction_type", UNSET))

        tl03_request = cls(
            accounting_document_id=accounting_document_id,
            accounting_document_number=accounting_document_number,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            items_per_chunk=items_per_chunk,
            last_updated_from=last_updated_from,
            megabytes_per_chunk=megabytes_per_chunk,
            order_id=order_id,
            order_line_id=order_line_id,
            order_reference_for_customer=order_reference_for_customer,
            order_reference_for_seller=order_reference_for_seller,
            pay_out_psp_codes=pay_out_psp_codes,
            payment_state=payment_state,
            payment_voucher_number=payment_voucher_number,
            shop_domain=shop_domain,
            shop_id=shop_id,
            shop_model=shop_model,
            transaction_date_from=transaction_date_from,
            transaction_date_to=transaction_date_to,
            transaction_type=transaction_type,
        )

        tl03_request.additional_properties = d
        return tl03_request

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
