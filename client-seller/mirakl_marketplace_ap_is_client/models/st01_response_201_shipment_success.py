import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st01_response_201_shipment_success_payment_details import ST01Response201ShipmentSuccessPaymentDetails
    from ..models.st01_response_201_shipment_success_shipment_additional_information import (
        ST01Response201ShipmentSuccessShipmentAdditionalInformation,
    )
    from ..models.st01_response_201_shipment_success_shipment_lines import ST01Response201ShipmentSuccessShipmentLines
    from ..models.st01_response_201_shipment_success_shipping_from import ST01Response201ShipmentSuccessShippingFrom
    from ..models.st01_response_201_shipment_success_tracking import ST01Response201ShipmentSuccessTracking


T = TypeVar("T", bound="ST01Response201ShipmentSuccess")


@_attrs_define
class ST01Response201ShipmentSuccess:
    """
    Attributes:
        created_date (Union[Unset, datetime.datetime]): Shipment's creation date
        id (Union[Unset, str]): Shipment id
        invoice_reference (Union[Unset, str]): Shipment's invoice reference
        last_updated_date (Union[Unset, datetime.datetime]): Shipment's last updated date
        order_id (Union[Unset, str]): Order id
        payment_details (Union[Unset, ST01Response201ShipmentSuccessPaymentDetails]):
        shipment_additional_information (Union[Unset,
            list['ST01Response201ShipmentSuccessShipmentAdditionalInformation']]): Shipment's additional information
        shipment_lines (Union[Unset, list['ST01Response201ShipmentSuccessShipmentLines']]): Shipment lines
        shipped_date (Union[Unset, datetime.datetime]): Shipment's shipped date.
        shipping_from (Union[Unset, ST01Response201ShipmentSuccessShippingFrom]):
        status (Union[Unset, str]): Shipment status
        status_customer_debit (Union[Unset, str]): Shipment debit status
        tracking (Union[Unset, ST01Response201ShipmentSuccessTracking]):
    """

    created_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_reference: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    order_id: Union[Unset, str] = UNSET
    payment_details: Union[Unset, "ST01Response201ShipmentSuccessPaymentDetails"] = UNSET
    shipment_additional_information: Union[
        Unset, list["ST01Response201ShipmentSuccessShipmentAdditionalInformation"]
    ] = UNSET
    shipment_lines: Union[Unset, list["ST01Response201ShipmentSuccessShipmentLines"]] = UNSET
    shipped_date: Union[Unset, datetime.datetime] = UNSET
    shipping_from: Union[Unset, "ST01Response201ShipmentSuccessShippingFrom"] = UNSET
    status: Union[Unset, str] = UNSET
    status_customer_debit: Union[Unset, str] = UNSET
    tracking: Union[Unset, "ST01Response201ShipmentSuccessTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        id = self.id

        invoice_reference = self.invoice_reference

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        order_id = self.order_id

        payment_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_details, Unset):
            payment_details = self.payment_details.to_dict()

        shipment_additional_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_additional_information, Unset):
            shipment_additional_information = []
            for shipment_additional_information_item_data in self.shipment_additional_information:
                shipment_additional_information_item = shipment_additional_information_item_data.to_dict()
                shipment_additional_information.append(shipment_additional_information_item)

        shipment_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_lines, Unset):
            shipment_lines = []
            for shipment_lines_item_data in self.shipment_lines:
                shipment_lines_item = shipment_lines_item_data.to_dict()
                shipment_lines.append(shipment_lines_item)

        shipped_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_date, Unset):
            shipped_date = self.shipped_date.isoformat()

        shipping_from: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_from, Unset):
            shipping_from = self.shipping_from.to_dict()

        status = self.status

        status_customer_debit = self.status_customer_debit

        tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_reference is not UNSET:
            field_dict["invoice_reference"] = invoice_reference
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if payment_details is not UNSET:
            field_dict["payment_details"] = payment_details
        if shipment_additional_information is not UNSET:
            field_dict["shipment_additional_information"] = shipment_additional_information
        if shipment_lines is not UNSET:
            field_dict["shipment_lines"] = shipment_lines
        if shipped_date is not UNSET:
            field_dict["shipped_date"] = shipped_date
        if shipping_from is not UNSET:
            field_dict["shipping_from"] = shipping_from
        if status is not UNSET:
            field_dict["status"] = status
        if status_customer_debit is not UNSET:
            field_dict["status_customer_debit"] = status_customer_debit
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st01_response_201_shipment_success_payment_details import (
            ST01Response201ShipmentSuccessPaymentDetails,
        )
        from ..models.st01_response_201_shipment_success_shipment_additional_information import (
            ST01Response201ShipmentSuccessShipmentAdditionalInformation,
        )
        from ..models.st01_response_201_shipment_success_shipment_lines import (
            ST01Response201ShipmentSuccessShipmentLines,
        )
        from ..models.st01_response_201_shipment_success_shipping_from import ST01Response201ShipmentSuccessShippingFrom
        from ..models.st01_response_201_shipment_success_tracking import ST01Response201ShipmentSuccessTracking

        d = dict(src_dict)
        _created_date = d.pop("created_date", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        id = d.pop("id", UNSET)

        invoice_reference = d.pop("invoice_reference", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        order_id = d.pop("order_id", UNSET)

        _payment_details = d.pop("payment_details", UNSET)
        payment_details: Union[Unset, ST01Response201ShipmentSuccessPaymentDetails]
        if isinstance(_payment_details, Unset):
            payment_details = UNSET
        else:
            payment_details = ST01Response201ShipmentSuccessPaymentDetails.from_dict(_payment_details)

        shipment_additional_information = []
        _shipment_additional_information = d.pop("shipment_additional_information", UNSET)
        for shipment_additional_information_item_data in _shipment_additional_information or []:
            shipment_additional_information_item = (
                ST01Response201ShipmentSuccessShipmentAdditionalInformation.from_dict(
                    shipment_additional_information_item_data
                )
            )

            shipment_additional_information.append(shipment_additional_information_item)

        shipment_lines = []
        _shipment_lines = d.pop("shipment_lines", UNSET)
        for shipment_lines_item_data in _shipment_lines or []:
            shipment_lines_item = ST01Response201ShipmentSuccessShipmentLines.from_dict(shipment_lines_item_data)

            shipment_lines.append(shipment_lines_item)

        _shipped_date = d.pop("shipped_date", UNSET)
        shipped_date: Union[Unset, datetime.datetime]
        if isinstance(_shipped_date, Unset):
            shipped_date = UNSET
        else:
            shipped_date = isoparse(_shipped_date)

        _shipping_from = d.pop("shipping_from", UNSET)
        shipping_from: Union[Unset, ST01Response201ShipmentSuccessShippingFrom]
        if isinstance(_shipping_from, Unset):
            shipping_from = UNSET
        else:
            shipping_from = ST01Response201ShipmentSuccessShippingFrom.from_dict(_shipping_from)

        status = d.pop("status", UNSET)

        status_customer_debit = d.pop("status_customer_debit", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, ST01Response201ShipmentSuccessTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = ST01Response201ShipmentSuccessTracking.from_dict(_tracking)

        st01_response_201_shipment_success = cls(
            created_date=created_date,
            id=id,
            invoice_reference=invoice_reference,
            last_updated_date=last_updated_date,
            order_id=order_id,
            payment_details=payment_details,
            shipment_additional_information=shipment_additional_information,
            shipment_lines=shipment_lines,
            shipped_date=shipped_date,
            shipping_from=shipping_from,
            status=status,
            status_customer_debit=status_customer_debit,
            tracking=tracking,
        )

        st01_response_201_shipment_success.additional_properties = d
        return st01_response_201_shipment_success

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
