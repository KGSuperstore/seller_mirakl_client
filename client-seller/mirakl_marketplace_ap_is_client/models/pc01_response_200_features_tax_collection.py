from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesTaxCollection")


@_attrs_define
class PC01Response200FeaturesTaxCollection:
    """
    Attributes:
        activated (Union[Unset, str]): Tax collection activated. NO: Not activated. YES: Activated for all stores.
            YES_PER_STORE: Activated for some stores.
        product_tax_code_mandatory (Union[Unset, bool]): Product tax code mandatory at offer level
        tax_collection_by_operator (Union[Unset, bool]): Operator in charge of tax collection on behalf of sellers
    """

    activated: Union[Unset, str] = UNSET
    product_tax_code_mandatory: Union[Unset, bool] = UNSET
    tax_collection_by_operator: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activated = self.activated

        product_tax_code_mandatory = self.product_tax_code_mandatory

        tax_collection_by_operator = self.tax_collection_by_operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activated is not UNSET:
            field_dict["activated"] = activated
        if product_tax_code_mandatory is not UNSET:
            field_dict["product_tax_code_mandatory"] = product_tax_code_mandatory
        if tax_collection_by_operator is not UNSET:
            field_dict["tax_collection_by_operator"] = tax_collection_by_operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activated = d.pop("activated", UNSET)

        product_tax_code_mandatory = d.pop("product_tax_code_mandatory", UNSET)

        tax_collection_by_operator = d.pop("tax_collection_by_operator", UNSET)

        pc01_response_200_features_tax_collection = cls(
            activated=activated,
            product_tax_code_mandatory=product_tax_code_mandatory,
            tax_collection_by_operator=tax_collection_by_operator,
        )

        pc01_response_200_features_tax_collection.additional_properties = d
        return pc01_response_200_features_tax_collection

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
