from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p51_response_200_product_import_trackings import P51Response200ProductImportTrackings


T = TypeVar("T", bound="P51Response200")


@_attrs_define
class P51Response200:
    """
    Attributes:
        product_import_trackings (Union[Unset, list['P51Response200ProductImportTrackings']]): List of product import
            status information
        total_count (Union[Unset, int]): Total count of product import status information
    """

    product_import_trackings: Union[Unset, list["P51Response200ProductImportTrackings"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_import_trackings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_import_trackings, Unset):
            product_import_trackings = []
            for product_import_trackings_item_data in self.product_import_trackings:
                product_import_trackings_item = product_import_trackings_item_data.to_dict()
                product_import_trackings.append(product_import_trackings_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_import_trackings is not UNSET:
            field_dict["product_import_trackings"] = product_import_trackings
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p51_response_200_product_import_trackings import P51Response200ProductImportTrackings

        d = dict(src_dict)
        product_import_trackings = []
        _product_import_trackings = d.pop("product_import_trackings", UNSET)
        for product_import_trackings_item_data in _product_import_trackings or []:
            product_import_trackings_item = P51Response200ProductImportTrackings.from_dict(
                product_import_trackings_item_data
            )

            product_import_trackings.append(product_import_trackings_item)

        total_count = d.pop("total_count", UNSET)

        p51_response_200 = cls(
            product_import_trackings=product_import_trackings,
            total_count=total_count,
        )

        p51_response_200.additional_properties = d
        return p51_response_200

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
