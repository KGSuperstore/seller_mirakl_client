from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesCatalog")


@_attrs_define
class PC01Response200FeaturesCatalog:
    """
    Attributes:
        allow_shop_contribution_to_all_channels (Union[Unset, bool]): Allows shops to contribute data to all sales
            channels when enabled; otherwise, data can only be pushed to channels the shop belongs to
        exclude_invalid_products (Union[Unset, bool]): When enabled, products with validation errors will be excluded
            from product imports and won't be transmitted to MCM
        list_of_multiple_values_separator (Union[Unset, str]): Character used to separate values in the 'Multiple Values
            List' type attributes
        product_acceptance_by_channel (Union[Unset, bool]): Allows operators to accept or reject products according to
            sales channels
        product_data_validation_by_channel (Union[Unset, bool]): Facilitates the management of attributes in a
            multilingual context
        product_import_only_on_leaf (Union[Unset, bool]): Prevents the import of products into non-leaf categories
    """

    allow_shop_contribution_to_all_channels: Union[Unset, bool] = UNSET
    exclude_invalid_products: Union[Unset, bool] = UNSET
    list_of_multiple_values_separator: Union[Unset, str] = UNSET
    product_acceptance_by_channel: Union[Unset, bool] = UNSET
    product_data_validation_by_channel: Union[Unset, bool] = UNSET
    product_import_only_on_leaf: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_shop_contribution_to_all_channels = self.allow_shop_contribution_to_all_channels

        exclude_invalid_products = self.exclude_invalid_products

        list_of_multiple_values_separator = self.list_of_multiple_values_separator

        product_acceptance_by_channel = self.product_acceptance_by_channel

        product_data_validation_by_channel = self.product_data_validation_by_channel

        product_import_only_on_leaf = self.product_import_only_on_leaf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_shop_contribution_to_all_channels is not UNSET:
            field_dict["allow_shop_contribution_to_all_channels"] = allow_shop_contribution_to_all_channels
        if exclude_invalid_products is not UNSET:
            field_dict["exclude_invalid_products"] = exclude_invalid_products
        if list_of_multiple_values_separator is not UNSET:
            field_dict["list_of_multiple_values_separator"] = list_of_multiple_values_separator
        if product_acceptance_by_channel is not UNSET:
            field_dict["product_acceptance_by_channel"] = product_acceptance_by_channel
        if product_data_validation_by_channel is not UNSET:
            field_dict["product_data_validation_by_channel"] = product_data_validation_by_channel
        if product_import_only_on_leaf is not UNSET:
            field_dict["product_import_only_on_leaf"] = product_import_only_on_leaf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_shop_contribution_to_all_channels = d.pop("allow_shop_contribution_to_all_channels", UNSET)

        exclude_invalid_products = d.pop("exclude_invalid_products", UNSET)

        list_of_multiple_values_separator = d.pop("list_of_multiple_values_separator", UNSET)

        product_acceptance_by_channel = d.pop("product_acceptance_by_channel", UNSET)

        product_data_validation_by_channel = d.pop("product_data_validation_by_channel", UNSET)

        product_import_only_on_leaf = d.pop("product_import_only_on_leaf", UNSET)

        pc01_response_200_features_catalog = cls(
            allow_shop_contribution_to_all_channels=allow_shop_contribution_to_all_channels,
            exclude_invalid_products=exclude_invalid_products,
            list_of_multiple_values_separator=list_of_multiple_values_separator,
            product_acceptance_by_channel=product_acceptance_by_channel,
            product_data_validation_by_channel=product_data_validation_by_channel,
            product_import_only_on_leaf=product_import_only_on_leaf,
        )

        pc01_response_200_features_catalog.additional_properties = d
        return pc01_response_200_features_catalog

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
