from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt21_request_returns import RT21RequestReturns


T = TypeVar("T", bound="RT21Request")


@_attrs_define
class RT21Request:
    """
    Attributes:
        returns (Union[Unset, list['RT21RequestReturns']]): Returns to be accepted, maximum number of returns per call:
            100
    """

    returns: Union[Unset, list["RT21RequestReturns"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        returns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.returns, Unset):
            returns = []
            for returns_item_data in self.returns:
                returns_item = returns_item_data.to_dict()
                returns.append(returns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if returns is not UNSET:
            field_dict["returns"] = returns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt21_request_returns import RT21RequestReturns

        d = dict(src_dict)
        returns = []
        _returns = d.pop("returns", UNSET)
        for returns_item_data in _returns or []:
            returns_item = RT21RequestReturns.from_dict(returns_item_data)

            returns.append(returns_item)

        rt21_request = cls(
            returns=returns,
        )

        rt21_request.additional_properties = d
        return rt21_request

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
