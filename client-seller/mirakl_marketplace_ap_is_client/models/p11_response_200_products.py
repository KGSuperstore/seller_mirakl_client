from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p11_response_200_products_measurement import P11Response200ProductsMeasurement
    from ..models.p11_response_200_products_offers import P11Response200ProductsOffers
    from ..models.p11_response_200_products_product_media import P11Response200ProductsProductMedia
    from ..models.p11_response_200_products_product_references import P11Response200ProductsProductReferences


T = TypeVar("T", bound="P11Response200Products")


@_attrs_define
class P11Response200Products:
    """
    Attributes:
        category_code (Union[Unset, str]): Code of the product category
        category_label (Union[Unset, str]): Label of the product category
        measurement (Union[Unset, P11Response200ProductsMeasurement]):
        offers (Union[Unset, list['P11Response200ProductsOffers']]): List of offers for the product
        product_brand (Union[Unset, str]): Brand of the product
        product_description (Union[Unset, str]): Description of the product
        product_media (Union[Unset, P11Response200ProductsProductMedia]):
        product_references (Union[Unset, list['P11Response200ProductsProductReferences']]): List of product's references
        product_sku (Union[Unset, str]): SKU of the product
        product_title (Union[Unset, str]): Title of the product
        total_count (Union[Unset, int]): Number of offers for this product
    """

    category_code: Union[Unset, str] = UNSET
    category_label: Union[Unset, str] = UNSET
    measurement: Union[Unset, "P11Response200ProductsMeasurement"] = UNSET
    offers: Union[Unset, list["P11Response200ProductsOffers"]] = UNSET
    product_brand: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    product_media: Union[Unset, "P11Response200ProductsProductMedia"] = UNSET
    product_references: Union[Unset, list["P11Response200ProductsProductReferences"]] = UNSET
    product_sku: Union[Unset, str] = UNSET
    product_title: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_code = self.category_code

        category_label = self.category_label

        measurement: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        offers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        product_brand = self.product_brand

        product_description = self.product_description

        product_media: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_media, Unset):
            product_media = self.product_media.to_dict()

        product_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_references, Unset):
            product_references = []
            for product_references_item_data in self.product_references:
                product_references_item = product_references_item_data.to_dict()
                product_references.append(product_references_item)

        product_sku = self.product_sku

        product_title = self.product_title

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if category_label is not UNSET:
            field_dict["category_label"] = category_label
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if offers is not UNSET:
            field_dict["offers"] = offers
        if product_brand is not UNSET:
            field_dict["product_brand"] = product_brand
        if product_description is not UNSET:
            field_dict["product_description"] = product_description
        if product_media is not UNSET:
            field_dict["product_media"] = product_media
        if product_references is not UNSET:
            field_dict["product_references"] = product_references
        if product_sku is not UNSET:
            field_dict["product_sku"] = product_sku
        if product_title is not UNSET:
            field_dict["product_title"] = product_title
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p11_response_200_products_measurement import P11Response200ProductsMeasurement
        from ..models.p11_response_200_products_offers import P11Response200ProductsOffers
        from ..models.p11_response_200_products_product_media import P11Response200ProductsProductMedia
        from ..models.p11_response_200_products_product_references import P11Response200ProductsProductReferences

        d = dict(src_dict)
        category_code = d.pop("category_code", UNSET)

        category_label = d.pop("category_label", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: Union[Unset, P11Response200ProductsMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = P11Response200ProductsMeasurement.from_dict(_measurement)

        offers = []
        _offers = d.pop("offers", UNSET)
        for offers_item_data in _offers or []:
            offers_item = P11Response200ProductsOffers.from_dict(offers_item_data)

            offers.append(offers_item)

        product_brand = d.pop("product_brand", UNSET)

        product_description = d.pop("product_description", UNSET)

        _product_media = d.pop("product_media", UNSET)
        product_media: Union[Unset, P11Response200ProductsProductMedia]
        if isinstance(_product_media, Unset):
            product_media = UNSET
        else:
            product_media = P11Response200ProductsProductMedia.from_dict(_product_media)

        product_references = []
        _product_references = d.pop("product_references", UNSET)
        for product_references_item_data in _product_references or []:
            product_references_item = P11Response200ProductsProductReferences.from_dict(product_references_item_data)

            product_references.append(product_references_item)

        product_sku = d.pop("product_sku", UNSET)

        product_title = d.pop("product_title", UNSET)

        total_count = d.pop("total_count", UNSET)

        p11_response_200_products = cls(
            category_code=category_code,
            category_label=category_label,
            measurement=measurement,
            offers=offers,
            product_brand=product_brand,
            product_description=product_description,
            product_media=product_media,
            product_references=product_references,
            product_sku=product_sku,
            product_title=product_title,
            total_count=total_count,
        )

        p11_response_200_products.additional_properties = d
        return p11_response_200_products

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
