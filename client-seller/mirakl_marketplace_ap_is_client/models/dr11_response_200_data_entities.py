from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_entities_delivery_bill_information import (
        DR11Response200DataEntitiesDeliveryBillInformation,
    )
    from ..models.dr11_response_200_data_entities_shipping_information import (
        DR11Response200DataEntitiesShippingInformation,
    )
    from ..models.dr11_response_200_data_entities_shop_billing_cycle import DR11Response200DataEntitiesShopBillingCycle


T = TypeVar("T", bound="DR11Response200DataEntities")


@_attrs_define
class DR11Response200DataEntities:
    """
    Attributes:
        delivery_bill_information (Union[Unset, list['DR11Response200DataEntitiesDeliveryBillInformation']]): A list of
            delivery bill information
        ship_to_iso_country_code (Union[Unset, str]): Ship to ISO country code
        shipping_information (Union[Unset, DR11Response200DataEntitiesShippingInformation]):
        shop_billing_cycle (Union[Unset, DR11Response200DataEntitiesShopBillingCycle]):
    """

    delivery_bill_information: Union[Unset, list["DR11Response200DataEntitiesDeliveryBillInformation"]] = UNSET
    ship_to_iso_country_code: Union[Unset, str] = UNSET
    shipping_information: Union[Unset, "DR11Response200DataEntitiesShippingInformation"] = UNSET
    shop_billing_cycle: Union[Unset, "DR11Response200DataEntitiesShopBillingCycle"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_bill_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delivery_bill_information, Unset):
            delivery_bill_information = []
            for delivery_bill_information_item_data in self.delivery_bill_information:
                delivery_bill_information_item = delivery_bill_information_item_data.to_dict()
                delivery_bill_information.append(delivery_bill_information_item)

        ship_to_iso_country_code = self.ship_to_iso_country_code

        shipping_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_information, Unset):
            shipping_information = self.shipping_information.to_dict()

        shop_billing_cycle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shop_billing_cycle, Unset):
            shop_billing_cycle = self.shop_billing_cycle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_bill_information is not UNSET:
            field_dict["delivery_bill_information"] = delivery_bill_information
        if ship_to_iso_country_code is not UNSET:
            field_dict["ship_to_iso_country_code"] = ship_to_iso_country_code
        if shipping_information is not UNSET:
            field_dict["shipping_information"] = shipping_information
        if shop_billing_cycle is not UNSET:
            field_dict["shop_billing_cycle"] = shop_billing_cycle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_entities_delivery_bill_information import (
            DR11Response200DataEntitiesDeliveryBillInformation,
        )
        from ..models.dr11_response_200_data_entities_shipping_information import (
            DR11Response200DataEntitiesShippingInformation,
        )
        from ..models.dr11_response_200_data_entities_shop_billing_cycle import (
            DR11Response200DataEntitiesShopBillingCycle,
        )

        d = dict(src_dict)
        delivery_bill_information = []
        _delivery_bill_information = d.pop("delivery_bill_information", UNSET)
        for delivery_bill_information_item_data in _delivery_bill_information or []:
            delivery_bill_information_item = DR11Response200DataEntitiesDeliveryBillInformation.from_dict(
                delivery_bill_information_item_data
            )

            delivery_bill_information.append(delivery_bill_information_item)

        ship_to_iso_country_code = d.pop("ship_to_iso_country_code", UNSET)

        _shipping_information = d.pop("shipping_information", UNSET)
        shipping_information: Union[Unset, DR11Response200DataEntitiesShippingInformation]
        if isinstance(_shipping_information, Unset):
            shipping_information = UNSET
        else:
            shipping_information = DR11Response200DataEntitiesShippingInformation.from_dict(_shipping_information)

        _shop_billing_cycle = d.pop("shop_billing_cycle", UNSET)
        shop_billing_cycle: Union[Unset, DR11Response200DataEntitiesShopBillingCycle]
        if isinstance(_shop_billing_cycle, Unset):
            shop_billing_cycle = UNSET
        else:
            shop_billing_cycle = DR11Response200DataEntitiesShopBillingCycle.from_dict(_shop_billing_cycle)

        dr11_response_200_data_entities = cls(
            delivery_bill_information=delivery_bill_information,
            ship_to_iso_country_code=ship_to_iso_country_code,
            shipping_information=shipping_information,
            shop_billing_cycle=shop_billing_cycle,
        )

        dr11_response_200_data_entities.additional_properties = d
        return dr11_response_200_data_entities

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
