import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p11_response_200_products_offers_shipping_types_delivery_time import (
        P11Response200ProductsOffersShippingTypesDeliveryTime,
    )


T = TypeVar("T", bound="P11Response200ProductsOffersShippingTypes")


@_attrs_define
class P11Response200ProductsOffersShippingTypes:
    """
    Attributes:
        code (Union[Unset, str]): Shipping type code
        cut_off_next_date (Union[Unset, datetime.datetime]): Next cutoff date
        cut_off_time (Union[Unset, str]): Shipping type Cutoff time
        delivery_time (Union[Unset, P11Response200ProductsOffersShippingTypesDeliveryTime]):
        label (Union[Unset, str]): Shipping type label
        shipping_deadline (Union[Unset, datetime.datetime]): Estimated shipping date, that includes business closing
            days and cut-off configured on the platform. Add the earliest and latest delivery times to calculate the
            estimated delivery date to customers
        shipping_price_type (Union[Unset, str]): Shipping price type of the offer for a given zone method
        shipping_price_unit (Union[Unset, float]): Shipping price of the offer
        shipping_zone_code (Union[Unset, str]): Shipping zone code
        shipping_zone_label (Union[Unset, str]): Shipping zone label
        standard_code (Union[Unset, str]): Shipping type standard code
    """

    code: Union[Unset, str] = UNSET
    cut_off_next_date: Union[Unset, datetime.datetime] = UNSET
    cut_off_time: Union[Unset, str] = UNSET
    delivery_time: Union[Unset, "P11Response200ProductsOffersShippingTypesDeliveryTime"] = UNSET
    label: Union[Unset, str] = UNSET
    shipping_deadline: Union[Unset, datetime.datetime] = UNSET
    shipping_price_type: Union[Unset, str] = UNSET
    shipping_price_unit: Union[Unset, float] = UNSET
    shipping_zone_code: Union[Unset, str] = UNSET
    shipping_zone_label: Union[Unset, str] = UNSET
    standard_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        cut_off_next_date: Union[Unset, str] = UNSET
        if not isinstance(self.cut_off_next_date, Unset):
            cut_off_next_date = self.cut_off_next_date.isoformat()

        cut_off_time = self.cut_off_time

        delivery_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.delivery_time, Unset):
            delivery_time = self.delivery_time.to_dict()

        label = self.label

        shipping_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_deadline, Unset):
            shipping_deadline = self.shipping_deadline.isoformat()

        shipping_price_type = self.shipping_price_type

        shipping_price_unit = self.shipping_price_unit

        shipping_zone_code = self.shipping_zone_code

        shipping_zone_label = self.shipping_zone_label

        standard_code = self.standard_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if cut_off_next_date is not UNSET:
            field_dict["cut_off_next_date"] = cut_off_next_date
        if cut_off_time is not UNSET:
            field_dict["cut_off_time"] = cut_off_time
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if label is not UNSET:
            field_dict["label"] = label
        if shipping_deadline is not UNSET:
            field_dict["shipping_deadline"] = shipping_deadline
        if shipping_price_type is not UNSET:
            field_dict["shipping_price_type"] = shipping_price_type
        if shipping_price_unit is not UNSET:
            field_dict["shipping_price_unit"] = shipping_price_unit
        if shipping_zone_code is not UNSET:
            field_dict["shipping_zone_code"] = shipping_zone_code
        if shipping_zone_label is not UNSET:
            field_dict["shipping_zone_label"] = shipping_zone_label
        if standard_code is not UNSET:
            field_dict["standard_code"] = standard_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p11_response_200_products_offers_shipping_types_delivery_time import (
            P11Response200ProductsOffersShippingTypesDeliveryTime,
        )

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _cut_off_next_date = d.pop("cut_off_next_date", UNSET)
        cut_off_next_date: Union[Unset, datetime.datetime]
        if isinstance(_cut_off_next_date, Unset):
            cut_off_next_date = UNSET
        else:
            cut_off_next_date = isoparse(_cut_off_next_date)

        cut_off_time = d.pop("cut_off_time", UNSET)

        _delivery_time = d.pop("delivery_time", UNSET)
        delivery_time: Union[Unset, P11Response200ProductsOffersShippingTypesDeliveryTime]
        if isinstance(_delivery_time, Unset):
            delivery_time = UNSET
        else:
            delivery_time = P11Response200ProductsOffersShippingTypesDeliveryTime.from_dict(_delivery_time)

        label = d.pop("label", UNSET)

        _shipping_deadline = d.pop("shipping_deadline", UNSET)
        shipping_deadline: Union[Unset, datetime.datetime]
        if isinstance(_shipping_deadline, Unset):
            shipping_deadline = UNSET
        else:
            shipping_deadline = isoparse(_shipping_deadline)

        shipping_price_type = d.pop("shipping_price_type", UNSET)

        shipping_price_unit = d.pop("shipping_price_unit", UNSET)

        shipping_zone_code = d.pop("shipping_zone_code", UNSET)

        shipping_zone_label = d.pop("shipping_zone_label", UNSET)

        standard_code = d.pop("standard_code", UNSET)

        p11_response_200_products_offers_shipping_types = cls(
            code=code,
            cut_off_next_date=cut_off_next_date,
            cut_off_time=cut_off_time,
            delivery_time=delivery_time,
            label=label,
            shipping_deadline=shipping_deadline,
            shipping_price_type=shipping_price_type,
            shipping_price_unit=shipping_price_unit,
            shipping_zone_code=shipping_zone_code,
            shipping_zone_label=shipping_zone_label,
            standard_code=standard_code,
        )

        p11_response_200_products_offers_shipping_types.additional_properties = d
        return p11_response_200_products_offers_shipping_types

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
