from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tl02_response_200_data_entities_channel import TL02Response200DataEntitiesChannel
    from ..models.tl02_response_200_data_entities_debit import TL02Response200DataEntitiesDebit
    from ..models.tl02_response_200_data_entities_fee import TL02Response200DataEntitiesFee
    from ..models.tl02_response_200_data_entities_manual_accounting_document import (
        TL02Response200DataEntitiesManualAccountingDocument,
    )
    from ..models.tl02_response_200_data_entities_order import TL02Response200DataEntitiesOrder
    from ..models.tl02_response_200_data_entities_order_fee import TL02Response200DataEntitiesOrderFee
    from ..models.tl02_response_200_data_entities_order_line import TL02Response200DataEntitiesOrderLine
    from ..models.tl02_response_200_data_entities_order_tax import TL02Response200DataEntitiesOrderTax
    from ..models.tl02_response_200_data_entities_refund import TL02Response200DataEntitiesRefund
    from ..models.tl02_response_200_data_entities_shipment import TL02Response200DataEntitiesShipment
    from ..models.tl02_response_200_data_entities_shop_tax import TL02Response200DataEntitiesShopTax
    from ..models.tl02_response_200_data_entities_transaction_info import TL02Response200DataEntitiesTransactionInfo


T = TypeVar("T", bound="TL02Response200DataEntities")


@_attrs_define
class TL02Response200DataEntities:
    """
    Attributes:
        channel (Union[Unset, TL02Response200DataEntitiesChannel]):
        debit (Union[Unset, TL02Response200DataEntitiesDebit]):
        domain (Union[Unset, str]): The domain of the entities related to the transaction line (PRODUCT or SERVICE)
        fee (Union[Unset, TL02Response200DataEntitiesFee]):
        manual_accounting_document (Union[Unset, TL02Response200DataEntitiesManualAccountingDocument]):
        order (Union[Unset, TL02Response200DataEntitiesOrder]):
        order_fee (Union[Unset, TL02Response200DataEntitiesOrderFee]):
        order_line (Union[Unset, TL02Response200DataEntitiesOrderLine]):
        order_tax (Union[Unset, TL02Response200DataEntitiesOrderTax]):
        refund (Union[Unset, TL02Response200DataEntitiesRefund]):
        shipment (Union[Unset, TL02Response200DataEntitiesShipment]):
        shop_tax (Union[Unset, TL02Response200DataEntitiesShopTax]):
        transaction_info (Union[Unset, TL02Response200DataEntitiesTransactionInfo]):
    """

    channel: Union[Unset, "TL02Response200DataEntitiesChannel"] = UNSET
    debit: Union[Unset, "TL02Response200DataEntitiesDebit"] = UNSET
    domain: Union[Unset, str] = UNSET
    fee: Union[Unset, "TL02Response200DataEntitiesFee"] = UNSET
    manual_accounting_document: Union[Unset, "TL02Response200DataEntitiesManualAccountingDocument"] = UNSET
    order: Union[Unset, "TL02Response200DataEntitiesOrder"] = UNSET
    order_fee: Union[Unset, "TL02Response200DataEntitiesOrderFee"] = UNSET
    order_line: Union[Unset, "TL02Response200DataEntitiesOrderLine"] = UNSET
    order_tax: Union[Unset, "TL02Response200DataEntitiesOrderTax"] = UNSET
    refund: Union[Unset, "TL02Response200DataEntitiesRefund"] = UNSET
    shipment: Union[Unset, "TL02Response200DataEntitiesShipment"] = UNSET
    shop_tax: Union[Unset, "TL02Response200DataEntitiesShopTax"] = UNSET
    transaction_info: Union[Unset, "TL02Response200DataEntitiesTransactionInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        debit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.debit, Unset):
            debit = self.debit.to_dict()

        domain = self.domain

        fee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fee, Unset):
            fee = self.fee.to_dict()

        manual_accounting_document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.manual_accounting_document, Unset):
            manual_accounting_document = self.manual_accounting_document.to_dict()

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        order_fee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_fee, Unset):
            order_fee = self.order_fee.to_dict()

        order_line: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_line, Unset):
            order_line = self.order_line.to_dict()

        order_tax: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_tax, Unset):
            order_tax = self.order_tax.to_dict()

        refund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund, Unset):
            refund = self.refund.to_dict()

        shipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        shop_tax: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shop_tax, Unset):
            shop_tax = self.shop_tax.to_dict()

        transaction_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction_info, Unset):
            transaction_info = self.transaction_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if debit is not UNSET:
            field_dict["debit"] = debit
        if domain is not UNSET:
            field_dict["domain"] = domain
        if fee is not UNSET:
            field_dict["fee"] = fee
        if manual_accounting_document is not UNSET:
            field_dict["manual_accounting_document"] = manual_accounting_document
        if order is not UNSET:
            field_dict["order"] = order
        if order_fee is not UNSET:
            field_dict["order_fee"] = order_fee
        if order_line is not UNSET:
            field_dict["order_line"] = order_line
        if order_tax is not UNSET:
            field_dict["order_tax"] = order_tax
        if refund is not UNSET:
            field_dict["refund"] = refund
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if shop_tax is not UNSET:
            field_dict["shop_tax"] = shop_tax
        if transaction_info is not UNSET:
            field_dict["transaction_info"] = transaction_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tl02_response_200_data_entities_channel import TL02Response200DataEntitiesChannel
        from ..models.tl02_response_200_data_entities_debit import TL02Response200DataEntitiesDebit
        from ..models.tl02_response_200_data_entities_fee import TL02Response200DataEntitiesFee
        from ..models.tl02_response_200_data_entities_manual_accounting_document import (
            TL02Response200DataEntitiesManualAccountingDocument,
        )
        from ..models.tl02_response_200_data_entities_order import TL02Response200DataEntitiesOrder
        from ..models.tl02_response_200_data_entities_order_fee import TL02Response200DataEntitiesOrderFee
        from ..models.tl02_response_200_data_entities_order_line import TL02Response200DataEntitiesOrderLine
        from ..models.tl02_response_200_data_entities_order_tax import TL02Response200DataEntitiesOrderTax
        from ..models.tl02_response_200_data_entities_refund import TL02Response200DataEntitiesRefund
        from ..models.tl02_response_200_data_entities_shipment import TL02Response200DataEntitiesShipment
        from ..models.tl02_response_200_data_entities_shop_tax import TL02Response200DataEntitiesShopTax
        from ..models.tl02_response_200_data_entities_transaction_info import TL02Response200DataEntitiesTransactionInfo

        d = dict(src_dict)
        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, TL02Response200DataEntitiesChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = TL02Response200DataEntitiesChannel.from_dict(_channel)

        _debit = d.pop("debit", UNSET)
        debit: Union[Unset, TL02Response200DataEntitiesDebit]
        if isinstance(_debit, Unset):
            debit = UNSET
        else:
            debit = TL02Response200DataEntitiesDebit.from_dict(_debit)

        domain = d.pop("domain", UNSET)

        _fee = d.pop("fee", UNSET)
        fee: Union[Unset, TL02Response200DataEntitiesFee]
        if isinstance(_fee, Unset):
            fee = UNSET
        else:
            fee = TL02Response200DataEntitiesFee.from_dict(_fee)

        _manual_accounting_document = d.pop("manual_accounting_document", UNSET)
        manual_accounting_document: Union[Unset, TL02Response200DataEntitiesManualAccountingDocument]
        if isinstance(_manual_accounting_document, Unset):
            manual_accounting_document = UNSET
        else:
            manual_accounting_document = TL02Response200DataEntitiesManualAccountingDocument.from_dict(
                _manual_accounting_document
            )

        _order = d.pop("order", UNSET)
        order: Union[Unset, TL02Response200DataEntitiesOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = TL02Response200DataEntitiesOrder.from_dict(_order)

        _order_fee = d.pop("order_fee", UNSET)
        order_fee: Union[Unset, TL02Response200DataEntitiesOrderFee]
        if isinstance(_order_fee, Unset):
            order_fee = UNSET
        else:
            order_fee = TL02Response200DataEntitiesOrderFee.from_dict(_order_fee)

        _order_line = d.pop("order_line", UNSET)
        order_line: Union[Unset, TL02Response200DataEntitiesOrderLine]
        if isinstance(_order_line, Unset):
            order_line = UNSET
        else:
            order_line = TL02Response200DataEntitiesOrderLine.from_dict(_order_line)

        _order_tax = d.pop("order_tax", UNSET)
        order_tax: Union[Unset, TL02Response200DataEntitiesOrderTax]
        if isinstance(_order_tax, Unset):
            order_tax = UNSET
        else:
            order_tax = TL02Response200DataEntitiesOrderTax.from_dict(_order_tax)

        _refund = d.pop("refund", UNSET)
        refund: Union[Unset, TL02Response200DataEntitiesRefund]
        if isinstance(_refund, Unset):
            refund = UNSET
        else:
            refund = TL02Response200DataEntitiesRefund.from_dict(_refund)

        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, TL02Response200DataEntitiesShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = TL02Response200DataEntitiesShipment.from_dict(_shipment)

        _shop_tax = d.pop("shop_tax", UNSET)
        shop_tax: Union[Unset, TL02Response200DataEntitiesShopTax]
        if isinstance(_shop_tax, Unset):
            shop_tax = UNSET
        else:
            shop_tax = TL02Response200DataEntitiesShopTax.from_dict(_shop_tax)

        _transaction_info = d.pop("transaction_info", UNSET)
        transaction_info: Union[Unset, TL02Response200DataEntitiesTransactionInfo]
        if isinstance(_transaction_info, Unset):
            transaction_info = UNSET
        else:
            transaction_info = TL02Response200DataEntitiesTransactionInfo.from_dict(_transaction_info)

        tl02_response_200_data_entities = cls(
            channel=channel,
            debit=debit,
            domain=domain,
            fee=fee,
            manual_accounting_document=manual_accounting_document,
            order=order,
            order_fee=order_fee,
            order_line=order_line,
            order_tax=order_tax,
            refund=refund,
            shipment=shipment,
            shop_tax=shop_tax,
            transaction_info=transaction_info,
        )

        tl02_response_200_data_entities.additional_properties = d
        return tl02_response_200_data_entities

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
