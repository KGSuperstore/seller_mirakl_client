import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tl02_response_200_data_entities import TL02Response200DataEntities


T = TypeVar("T", bound="TL02Response200Data")


@_attrs_define
class TL02Response200Data:
    """
    Attributes:
        accounting_document_creation_date (Union[Unset, datetime.datetime]): The billing cycle's accounting document
            creation date
        accounting_document_id (Union[Unset, str]): The billing cycle's accounting document id. This field is only
            available for documents requests of the type: <code>SHOP_BILLING_CYCLE_PURCHASE_ORDER</code>.
        accounting_document_number (Union[Unset, str]): The billing cycle's accounting document number
        amount (Union[Unset, int]): The amount.
        amount_credited (Union[Unset, int]): The amount credited.
        amount_debited (Union[Unset, int]): The amount debited.
        balance (Union[Unset, int]): The balance of the transaction.
        currency_iso_code (Union[Unset, str]): The currency of the shop (iso format)
        date_created (Union[Unset, datetime.datetime]): Creation date of the transaction line
        entities (Union[Unset, TL02Response200DataEntities]):
        id (Union[Unset, str]): Identifier of the transaction
        last_updated (Union[Unset, datetime.datetime]): Date of last update of the transaction line
        pay_out_psp_code (Union[Unset, str]): Pay-out PSP code associated with the transaction.
        payment_state (Union[Unset, str]): The payment state of the transaction.
        psp_balance (Union[Unset, int]): The Pay-out balance of the transaction.
        type_ (Union[Unset, str]): Type of transaction (refund, transaction fee, etc ...)
    """

    accounting_document_creation_date: Union[Unset, datetime.datetime] = UNSET
    accounting_document_id: Union[Unset, str] = UNSET
    accounting_document_number: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    amount_credited: Union[Unset, int] = UNSET
    amount_debited: Union[Unset, int] = UNSET
    balance: Union[Unset, int] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    entities: Union[Unset, "TL02Response200DataEntities"] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    pay_out_psp_code: Union[Unset, str] = UNSET
    payment_state: Union[Unset, str] = UNSET
    psp_balance: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_document_creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.accounting_document_creation_date, Unset):
            accounting_document_creation_date = self.accounting_document_creation_date.isoformat()

        accounting_document_id = self.accounting_document_id

        accounting_document_number = self.accounting_document_number

        amount = self.amount

        amount_credited = self.amount_credited

        amount_debited = self.amount_debited

        balance = self.balance

        currency_iso_code = self.currency_iso_code

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        entities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        pay_out_psp_code = self.pay_out_psp_code

        payment_state = self.payment_state

        psp_balance = self.psp_balance

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_document_creation_date is not UNSET:
            field_dict["accounting_document_creation_date"] = accounting_document_creation_date
        if accounting_document_id is not UNSET:
            field_dict["accounting_document_id"] = accounting_document_id
        if accounting_document_number is not UNSET:
            field_dict["accounting_document_number"] = accounting_document_number
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_credited is not UNSET:
            field_dict["amount_credited"] = amount_credited
        if amount_debited is not UNSET:
            field_dict["amount_debited"] = amount_debited
        if balance is not UNSET:
            field_dict["balance"] = balance
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if entities is not UNSET:
            field_dict["entities"] = entities
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if pay_out_psp_code is not UNSET:
            field_dict["pay_out_psp_code"] = pay_out_psp_code
        if payment_state is not UNSET:
            field_dict["payment_state"] = payment_state
        if psp_balance is not UNSET:
            field_dict["psp_balance"] = psp_balance
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tl02_response_200_data_entities import TL02Response200DataEntities

        d = dict(src_dict)
        _accounting_document_creation_date = d.pop("accounting_document_creation_date", UNSET)
        accounting_document_creation_date: Union[Unset, datetime.datetime]
        if isinstance(_accounting_document_creation_date, Unset):
            accounting_document_creation_date = UNSET
        else:
            accounting_document_creation_date = isoparse(_accounting_document_creation_date)

        accounting_document_id = d.pop("accounting_document_id", UNSET)

        accounting_document_number = d.pop("accounting_document_number", UNSET)

        amount = d.pop("amount", UNSET)

        amount_credited = d.pop("amount_credited", UNSET)

        amount_debited = d.pop("amount_debited", UNSET)

        balance = d.pop("balance", UNSET)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _entities = d.pop("entities", UNSET)
        entities: Union[Unset, TL02Response200DataEntities]
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = TL02Response200DataEntities.from_dict(_entities)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        pay_out_psp_code = d.pop("pay_out_psp_code", UNSET)

        payment_state = d.pop("payment_state", UNSET)

        psp_balance = d.pop("psp_balance", UNSET)

        type_ = d.pop("type", UNSET)

        tl02_response_200_data = cls(
            accounting_document_creation_date=accounting_document_creation_date,
            accounting_document_id=accounting_document_id,
            accounting_document_number=accounting_document_number,
            amount=amount,
            amount_credited=amount_credited,
            amount_debited=amount_debited,
            balance=balance,
            currency_iso_code=currency_iso_code,
            date_created=date_created,
            entities=entities,
            id=id,
            last_updated=last_updated,
            pay_out_psp_code=pay_out_psp_code,
            payment_state=payment_state,
            psp_balance=psp_balance,
            type_=type_,
        )

        tl02_response_200_data.additional_properties = d
        return tl02_response_200_data

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
