from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr12_response_200_data_delivery_bill_information import DR12Response200DataDeliveryBillInformation
    from ..models.dr12_response_200_data_eco_contributions import DR12Response200DataEcoContributions
    from ..models.dr12_response_200_data_fees_excluding_taxes import DR12Response200DataFeesExcludingTaxes
    from ..models.dr12_response_200_data_order import DR12Response200DataOrder
    from ..models.dr12_response_200_data_order_line import DR12Response200DataOrderLine
    from ..models.dr12_response_200_data_product import DR12Response200DataProduct
    from ..models.dr12_response_200_data_shipping_from import DR12Response200DataShippingFrom
    from ..models.dr12_response_200_data_shipping_taxes import DR12Response200DataShippingTaxes
    from ..models.dr12_response_200_data_shipping_to import DR12Response200DataShippingTo
    from ..models.dr12_response_200_data_shop import DR12Response200DataShop
    from ..models.dr12_response_200_data_taxes import DR12Response200DataTaxes


T = TypeVar("T", bound="DR12Response200Data")


@_attrs_define
class DR12Response200Data:
    """
    Attributes:
        delivery_bill_information (Union[Unset, list['DR12Response200DataDeliveryBillInformation']]): Delivery bill
            information
        eco_contributions (Union[Unset, list['DR12Response200DataEcoContributions']]): List of eco-contribution amounts
            and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        entity_id (Union[Unset, str]): The entity id the document line relates to
        entity_type (Union[Unset, str]): The entity type the document line relates to
        fees_excluding_taxes (Union[Unset, list['DR12Response200DataFeesExcludingTaxes']]): List of fees applied on the
            order line
        order (Union[Unset, DR12Response200DataOrder]):
        order_line (Union[Unset, DR12Response200DataOrderLine]):
        origin_unit_price_excluding_taxes (Union[Unset, float]): The original unit price excluding tax of the offer
            associated with the order line
        origin_unit_price_including_taxes (Union[Unset, float]): The original unit price including tax of the offer
            associated with the order line
        payment_state (Union[Unset, str]): Document request line payment status
        price_excluding_taxes (Union[Unset, float]): The price excluding taxes after promotions
        product (Union[Unset, DR12Response200DataProduct]):
        quantity (Union[Unset, int]): The quantity of the document line
        shipping_from (Union[Unset, DR12Response200DataShippingFrom]):
        shipping_price_excluding_taxes (Union[Unset, float]): The shipping price excluding taxes
        shipping_taxes (Union[Unset, list['DR12Response200DataShippingTaxes']]): The shipping taxes
        shipping_to (Union[Unset, DR12Response200DataShippingTo]):
        shop (Union[Unset, DR12Response200DataShop]):
        tax_legal_notice (Union[Unset, str]): The legal notice applying to the offer’s tax calculation
        taxes (Union[Unset, list['DR12Response200DataTaxes']]): The taxes
        total_price_including_taxes (Union[Unset, float]): The total price
        unit_price_excluding_taxes (Union[Unset, float]): The unit price excluding taxes after promotions
    """

    delivery_bill_information: Union[Unset, list["DR12Response200DataDeliveryBillInformation"]] = UNSET
    eco_contributions: Union[Unset, list["DR12Response200DataEcoContributions"]] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    fees_excluding_taxes: Union[Unset, list["DR12Response200DataFeesExcludingTaxes"]] = UNSET
    order: Union[Unset, "DR12Response200DataOrder"] = UNSET
    order_line: Union[Unset, "DR12Response200DataOrderLine"] = UNSET
    origin_unit_price_excluding_taxes: Union[Unset, float] = UNSET
    origin_unit_price_including_taxes: Union[Unset, float] = UNSET
    payment_state: Union[Unset, str] = UNSET
    price_excluding_taxes: Union[Unset, float] = UNSET
    product: Union[Unset, "DR12Response200DataProduct"] = UNSET
    quantity: Union[Unset, int] = UNSET
    shipping_from: Union[Unset, "DR12Response200DataShippingFrom"] = UNSET
    shipping_price_excluding_taxes: Union[Unset, float] = UNSET
    shipping_taxes: Union[Unset, list["DR12Response200DataShippingTaxes"]] = UNSET
    shipping_to: Union[Unset, "DR12Response200DataShippingTo"] = UNSET
    shop: Union[Unset, "DR12Response200DataShop"] = UNSET
    tax_legal_notice: Union[Unset, str] = UNSET
    taxes: Union[Unset, list["DR12Response200DataTaxes"]] = UNSET
    total_price_including_taxes: Union[Unset, float] = UNSET
    unit_price_excluding_taxes: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_bill_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delivery_bill_information, Unset):
            delivery_bill_information = []
            for delivery_bill_information_item_data in self.delivery_bill_information:
                delivery_bill_information_item = delivery_bill_information_item_data.to_dict()
                delivery_bill_information.append(delivery_bill_information_item)

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        entity_id = self.entity_id

        entity_type = self.entity_type

        fees_excluding_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fees_excluding_taxes, Unset):
            fees_excluding_taxes = []
            for fees_excluding_taxes_item_data in self.fees_excluding_taxes:
                fees_excluding_taxes_item = fees_excluding_taxes_item_data.to_dict()
                fees_excluding_taxes.append(fees_excluding_taxes_item)

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        order_line: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_line, Unset):
            order_line = self.order_line.to_dict()

        origin_unit_price_excluding_taxes = self.origin_unit_price_excluding_taxes

        origin_unit_price_including_taxes = self.origin_unit_price_including_taxes

        payment_state = self.payment_state

        price_excluding_taxes = self.price_excluding_taxes

        product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        quantity = self.quantity

        shipping_from: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_from, Unset):
            shipping_from = self.shipping_from.to_dict()

        shipping_price_excluding_taxes = self.shipping_price_excluding_taxes

        shipping_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_taxes, Unset):
            shipping_taxes = []
            for shipping_taxes_item_data in self.shipping_taxes:
                shipping_taxes_item = shipping_taxes_item_data.to_dict()
                shipping_taxes.append(shipping_taxes_item)

        shipping_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_to, Unset):
            shipping_to = self.shipping_to.to_dict()

        shop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shop, Unset):
            shop = self.shop.to_dict()

        tax_legal_notice = self.tax_legal_notice

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        total_price_including_taxes = self.total_price_including_taxes

        unit_price_excluding_taxes = self.unit_price_excluding_taxes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_bill_information is not UNSET:
            field_dict["delivery_bill_information"] = delivery_bill_information
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if fees_excluding_taxes is not UNSET:
            field_dict["fees_excluding_taxes"] = fees_excluding_taxes
        if order is not UNSET:
            field_dict["order"] = order
        if order_line is not UNSET:
            field_dict["order_line"] = order_line
        if origin_unit_price_excluding_taxes is not UNSET:
            field_dict["origin_unit_price_excluding_taxes"] = origin_unit_price_excluding_taxes
        if origin_unit_price_including_taxes is not UNSET:
            field_dict["origin_unit_price_including_taxes"] = origin_unit_price_including_taxes
        if payment_state is not UNSET:
            field_dict["payment_state"] = payment_state
        if price_excluding_taxes is not UNSET:
            field_dict["price_excluding_taxes"] = price_excluding_taxes
        if product is not UNSET:
            field_dict["product"] = product
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if shipping_from is not UNSET:
            field_dict["shipping_from"] = shipping_from
        if shipping_price_excluding_taxes is not UNSET:
            field_dict["shipping_price_excluding_taxes"] = shipping_price_excluding_taxes
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if shipping_to is not UNSET:
            field_dict["shipping_to"] = shipping_to
        if shop is not UNSET:
            field_dict["shop"] = shop
        if tax_legal_notice is not UNSET:
            field_dict["tax_legal_notice"] = tax_legal_notice
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total_price_including_taxes is not UNSET:
            field_dict["total_price_including_taxes"] = total_price_including_taxes
        if unit_price_excluding_taxes is not UNSET:
            field_dict["unit_price_excluding_taxes"] = unit_price_excluding_taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr12_response_200_data_delivery_bill_information import DR12Response200DataDeliveryBillInformation
        from ..models.dr12_response_200_data_eco_contributions import DR12Response200DataEcoContributions
        from ..models.dr12_response_200_data_fees_excluding_taxes import DR12Response200DataFeesExcludingTaxes
        from ..models.dr12_response_200_data_order import DR12Response200DataOrder
        from ..models.dr12_response_200_data_order_line import DR12Response200DataOrderLine
        from ..models.dr12_response_200_data_product import DR12Response200DataProduct
        from ..models.dr12_response_200_data_shipping_from import DR12Response200DataShippingFrom
        from ..models.dr12_response_200_data_shipping_taxes import DR12Response200DataShippingTaxes
        from ..models.dr12_response_200_data_shipping_to import DR12Response200DataShippingTo
        from ..models.dr12_response_200_data_shop import DR12Response200DataShop
        from ..models.dr12_response_200_data_taxes import DR12Response200DataTaxes

        d = dict(src_dict)
        delivery_bill_information = []
        _delivery_bill_information = d.pop("delivery_bill_information", UNSET)
        for delivery_bill_information_item_data in _delivery_bill_information or []:
            delivery_bill_information_item = DR12Response200DataDeliveryBillInformation.from_dict(
                delivery_bill_information_item_data
            )

            delivery_bill_information.append(delivery_bill_information_item)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = DR12Response200DataEcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        entity_id = d.pop("entity_id", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        fees_excluding_taxes = []
        _fees_excluding_taxes = d.pop("fees_excluding_taxes", UNSET)
        for fees_excluding_taxes_item_data in _fees_excluding_taxes or []:
            fees_excluding_taxes_item = DR12Response200DataFeesExcludingTaxes.from_dict(fees_excluding_taxes_item_data)

            fees_excluding_taxes.append(fees_excluding_taxes_item)

        _order = d.pop("order", UNSET)
        order: Union[Unset, DR12Response200DataOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = DR12Response200DataOrder.from_dict(_order)

        _order_line = d.pop("order_line", UNSET)
        order_line: Union[Unset, DR12Response200DataOrderLine]
        if isinstance(_order_line, Unset):
            order_line = UNSET
        else:
            order_line = DR12Response200DataOrderLine.from_dict(_order_line)

        origin_unit_price_excluding_taxes = d.pop("origin_unit_price_excluding_taxes", UNSET)

        origin_unit_price_including_taxes = d.pop("origin_unit_price_including_taxes", UNSET)

        payment_state = d.pop("payment_state", UNSET)

        price_excluding_taxes = d.pop("price_excluding_taxes", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, DR12Response200DataProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = DR12Response200DataProduct.from_dict(_product)

        quantity = d.pop("quantity", UNSET)

        _shipping_from = d.pop("shipping_from", UNSET)
        shipping_from: Union[Unset, DR12Response200DataShippingFrom]
        if isinstance(_shipping_from, Unset):
            shipping_from = UNSET
        else:
            shipping_from = DR12Response200DataShippingFrom.from_dict(_shipping_from)

        shipping_price_excluding_taxes = d.pop("shipping_price_excluding_taxes", UNSET)

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = DR12Response200DataShippingTaxes.from_dict(shipping_taxes_item_data)

            shipping_taxes.append(shipping_taxes_item)

        _shipping_to = d.pop("shipping_to", UNSET)
        shipping_to: Union[Unset, DR12Response200DataShippingTo]
        if isinstance(_shipping_to, Unset):
            shipping_to = UNSET
        else:
            shipping_to = DR12Response200DataShippingTo.from_dict(_shipping_to)

        _shop = d.pop("shop", UNSET)
        shop: Union[Unset, DR12Response200DataShop]
        if isinstance(_shop, Unset):
            shop = UNSET
        else:
            shop = DR12Response200DataShop.from_dict(_shop)

        tax_legal_notice = d.pop("tax_legal_notice", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = DR12Response200DataTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        total_price_including_taxes = d.pop("total_price_including_taxes", UNSET)

        unit_price_excluding_taxes = d.pop("unit_price_excluding_taxes", UNSET)

        dr12_response_200_data = cls(
            delivery_bill_information=delivery_bill_information,
            eco_contributions=eco_contributions,
            entity_id=entity_id,
            entity_type=entity_type,
            fees_excluding_taxes=fees_excluding_taxes,
            order=order,
            order_line=order_line,
            origin_unit_price_excluding_taxes=origin_unit_price_excluding_taxes,
            origin_unit_price_including_taxes=origin_unit_price_including_taxes,
            payment_state=payment_state,
            price_excluding_taxes=price_excluding_taxes,
            product=product,
            quantity=quantity,
            shipping_from=shipping_from,
            shipping_price_excluding_taxes=shipping_price_excluding_taxes,
            shipping_taxes=shipping_taxes,
            shipping_to=shipping_to,
            shop=shop,
            tax_legal_notice=tax_legal_notice,
            taxes=taxes,
            total_price_including_taxes=total_price_including_taxes,
            unit_price_excluding_taxes=unit_price_excluding_taxes,
        )

        dr12_response_200_data.additional_properties = d
        return dr12_response_200_data

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
