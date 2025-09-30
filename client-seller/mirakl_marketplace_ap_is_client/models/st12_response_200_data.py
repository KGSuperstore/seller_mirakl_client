import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st12_response_200_data_fulfillment import ST12Response200DataFulfillment
    from ..models.st12_response_200_data_references import ST12Response200DataReferences
    from ..models.st12_response_200_data_shipment_lines import ST12Response200DataShipmentLines
    from ..models.st12_response_200_data_shipping_address import ST12Response200DataShippingAddress


T = TypeVar("T", bound="ST12Response200Data")


@_attrs_define
class ST12Response200Data:
    """
    Attributes:
        fulfillment (Union[Unset, ST12Response200DataFulfillment]):
        order_id (Union[Unset, str]): Order id
        references (Union[Unset, ST12Response200DataReferences]):
        shipment_lines (Union[Unset, list['ST12Response200DataShipmentLines']]): Shipment lines
        shipping_address (Union[Unset, ST12Response200DataShippingAddress]):
        shipping_date (Union[Unset, datetime.datetime]): Shipping date
        shipping_deadline (Union[Unset, datetime.datetime]): Shipping deadline
        shipping_type_code (Union[Unset, str]): Code of shipping's type
        shipping_type_standard_code (Union[Unset, str]): Shipping type's standard code
    """

    fulfillment: Union[Unset, "ST12Response200DataFulfillment"] = UNSET
    order_id: Union[Unset, str] = UNSET
    references: Union[Unset, "ST12Response200DataReferences"] = UNSET
    shipment_lines: Union[Unset, list["ST12Response200DataShipmentLines"]] = UNSET
    shipping_address: Union[Unset, "ST12Response200DataShippingAddress"] = UNSET
    shipping_date: Union[Unset, datetime.datetime] = UNSET
    shipping_deadline: Union[Unset, datetime.datetime] = UNSET
    shipping_type_code: Union[Unset, str] = UNSET
    shipping_type_standard_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fulfillment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment, Unset):
            fulfillment = self.fulfillment.to_dict()

        order_id = self.order_id

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        shipment_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_lines, Unset):
            shipment_lines = []
            for shipment_lines_item_data in self.shipment_lines:
                shipment_lines_item = shipment_lines_item_data.to_dict()
                shipment_lines.append(shipment_lines_item)

        shipping_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        shipping_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_date, Unset):
            shipping_date = self.shipping_date.isoformat()

        shipping_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_deadline, Unset):
            shipping_deadline = self.shipping_deadline.isoformat()

        shipping_type_code = self.shipping_type_code

        shipping_type_standard_code = self.shipping_type_standard_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillment is not UNSET:
            field_dict["fulfillment"] = fulfillment
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if references is not UNSET:
            field_dict["references"] = references
        if shipment_lines is not UNSET:
            field_dict["shipment_lines"] = shipment_lines
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if shipping_date is not UNSET:
            field_dict["shipping_date"] = shipping_date
        if shipping_deadline is not UNSET:
            field_dict["shipping_deadline"] = shipping_deadline
        if shipping_type_code is not UNSET:
            field_dict["shipping_type_code"] = shipping_type_code
        if shipping_type_standard_code is not UNSET:
            field_dict["shipping_type_standard_code"] = shipping_type_standard_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st12_response_200_data_fulfillment import ST12Response200DataFulfillment
        from ..models.st12_response_200_data_references import ST12Response200DataReferences
        from ..models.st12_response_200_data_shipment_lines import ST12Response200DataShipmentLines
        from ..models.st12_response_200_data_shipping_address import ST12Response200DataShippingAddress

        d = dict(src_dict)
        _fulfillment = d.pop("fulfillment", UNSET)
        fulfillment: Union[Unset, ST12Response200DataFulfillment]
        if isinstance(_fulfillment, Unset):
            fulfillment = UNSET
        else:
            fulfillment = ST12Response200DataFulfillment.from_dict(_fulfillment)

        order_id = d.pop("order_id", UNSET)

        _references = d.pop("references", UNSET)
        references: Union[Unset, ST12Response200DataReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = ST12Response200DataReferences.from_dict(_references)

        shipment_lines = []
        _shipment_lines = d.pop("shipment_lines", UNSET)
        for shipment_lines_item_data in _shipment_lines or []:
            shipment_lines_item = ST12Response200DataShipmentLines.from_dict(shipment_lines_item_data)

            shipment_lines.append(shipment_lines_item)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, ST12Response200DataShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ST12Response200DataShippingAddress.from_dict(_shipping_address)

        _shipping_date = d.pop("shipping_date", UNSET)
        shipping_date: Union[Unset, datetime.datetime]
        if isinstance(_shipping_date, Unset):
            shipping_date = UNSET
        else:
            shipping_date = isoparse(_shipping_date)

        _shipping_deadline = d.pop("shipping_deadline", UNSET)
        shipping_deadline: Union[Unset, datetime.datetime]
        if isinstance(_shipping_deadline, Unset):
            shipping_deadline = UNSET
        else:
            shipping_deadline = isoparse(_shipping_deadline)

        shipping_type_code = d.pop("shipping_type_code", UNSET)

        shipping_type_standard_code = d.pop("shipping_type_standard_code", UNSET)

        st12_response_200_data = cls(
            fulfillment=fulfillment,
            order_id=order_id,
            references=references,
            shipment_lines=shipment_lines,
            shipping_address=shipping_address,
            shipping_date=shipping_date,
            shipping_deadline=shipping_deadline,
            shipping_type_code=shipping_type_code,
            shipping_type_standard_code=shipping_type_standard_code,
        )

        st12_response_200_data.additional_properties = d
        return st12_response_200_data

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
