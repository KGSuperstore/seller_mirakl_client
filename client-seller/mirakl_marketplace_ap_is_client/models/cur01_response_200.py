from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cur01_response_200_currencies import CUR01Response200Currencies


T = TypeVar("T", bound="CUR01Response200")


@_attrs_define
class CUR01Response200:
    """
    Attributes:
        currencies (Union[Unset, list['CUR01Response200Currencies']]): List of currencies
    """

    currencies: Union[Unset, list["CUR01Response200Currencies"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currencies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currencies is not UNSET:
            field_dict["currencies"] = currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cur01_response_200_currencies import CUR01Response200Currencies

        d = dict(src_dict)
        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = CUR01Response200Currencies.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        cur01_response_200 = cls(
            currencies=currencies,
        )

        cur01_response_200.additional_properties = d
        return cur01_response_200

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
