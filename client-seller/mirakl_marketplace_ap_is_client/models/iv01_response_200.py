from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iv01_response_200_invoices import IV01Response200Invoices


T = TypeVar("T", bound="IV01Response200")


@_attrs_define
class IV01Response200:
    """
    Attributes:
        invoices (Union[Unset, list['IV01Response200Invoices']]): Accounting documents
        total_count (Union[Unset, int]): Accounting documents total count
    """

    invoices: Union[Unset, list["IV01Response200Invoices"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iv01_response_200_invoices import IV01Response200Invoices

        d = dict(src_dict)
        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:
            invoices_item = IV01Response200Invoices.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        total_count = d.pop("total_count", UNSET)

        iv01_response_200 = cls(
            invoices=invoices,
            total_count=total_count,
        )

        iv01_response_200.additional_properties = d
        return iv01_response_200

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
