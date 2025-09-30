from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="P51Response200ProductImportTrackingsIntegrationDetails")


@_attrs_define
class P51Response200ProductImportTrackingsIntegrationDetails:
    """
    Attributes:
        invalid_products (Union[Unset, int]): Number of invalid products
        products_not_accepted_in_time (Union[Unset, int]): Number of products that haven't been accepted in the required
            time
        products_not_synchronized_in_time (Union[Unset, int]): Number of products that haven't been synchronized in the
            required time
        products_reimported (Union[Unset, int]): Number of products that have been reimported in a more recent file
        products_successfully_synchronized (Union[Unset, int]): Number of products successfully synchronized on operator
            system
        products_with_synchronization_issues (Union[Unset, int]): Number of products having synchronization issues with
            operator system
        products_with_wrong_identifiers (Union[Unset, int]): Number of products having wrong identifiers
        rejected_products (Union[Unset, int]): Number of rejected products by operator system
    """

    invalid_products: Union[Unset, int] = UNSET
    products_not_accepted_in_time: Union[Unset, int] = UNSET
    products_not_synchronized_in_time: Union[Unset, int] = UNSET
    products_reimported: Union[Unset, int] = UNSET
    products_successfully_synchronized: Union[Unset, int] = UNSET
    products_with_synchronization_issues: Union[Unset, int] = UNSET
    products_with_wrong_identifiers: Union[Unset, int] = UNSET
    rejected_products: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invalid_products = self.invalid_products

        products_not_accepted_in_time = self.products_not_accepted_in_time

        products_not_synchronized_in_time = self.products_not_synchronized_in_time

        products_reimported = self.products_reimported

        products_successfully_synchronized = self.products_successfully_synchronized

        products_with_synchronization_issues = self.products_with_synchronization_issues

        products_with_wrong_identifiers = self.products_with_wrong_identifiers

        rejected_products = self.rejected_products

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invalid_products is not UNSET:
            field_dict["invalid_products"] = invalid_products
        if products_not_accepted_in_time is not UNSET:
            field_dict["products_not_accepted_in_time"] = products_not_accepted_in_time
        if products_not_synchronized_in_time is not UNSET:
            field_dict["products_not_synchronized_in_time"] = products_not_synchronized_in_time
        if products_reimported is not UNSET:
            field_dict["products_reimported"] = products_reimported
        if products_successfully_synchronized is not UNSET:
            field_dict["products_successfully_synchronized"] = products_successfully_synchronized
        if products_with_synchronization_issues is not UNSET:
            field_dict["products_with_synchronization_issues"] = products_with_synchronization_issues
        if products_with_wrong_identifiers is not UNSET:
            field_dict["products_with_wrong_identifiers"] = products_with_wrong_identifiers
        if rejected_products is not UNSET:
            field_dict["rejected_products"] = rejected_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invalid_products = d.pop("invalid_products", UNSET)

        products_not_accepted_in_time = d.pop("products_not_accepted_in_time", UNSET)

        products_not_synchronized_in_time = d.pop("products_not_synchronized_in_time", UNSET)

        products_reimported = d.pop("products_reimported", UNSET)

        products_successfully_synchronized = d.pop("products_successfully_synchronized", UNSET)

        products_with_synchronization_issues = d.pop("products_with_synchronization_issues", UNSET)

        products_with_wrong_identifiers = d.pop("products_with_wrong_identifiers", UNSET)

        rejected_products = d.pop("rejected_products", UNSET)

        p51_response_200_product_import_trackings_integration_details = cls(
            invalid_products=invalid_products,
            products_not_accepted_in_time=products_not_accepted_in_time,
            products_not_synchronized_in_time=products_not_synchronized_in_time,
            products_reimported=products_reimported,
            products_successfully_synchronized=products_successfully_synchronized,
            products_with_synchronization_issues=products_with_synchronization_issues,
            products_with_wrong_identifiers=products_with_wrong_identifiers,
            rejected_products=rejected_products,
        )

        p51_response_200_product_import_trackings_integration_details.additional_properties = d
        return p51_response_200_product_import_trackings_integration_details

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
