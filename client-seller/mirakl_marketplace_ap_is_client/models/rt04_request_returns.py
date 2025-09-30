from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt04_request_returns_tracking import RT04RequestReturnsTracking


T = TypeVar("T", bound="RT04RequestReturns")


@_attrs_define
class RT04RequestReturns:
    """Returns to be updated, maximum number of returns per call: 100

    Attributes:
        id (Union[Unset, str]): Return id
        label_url (Union[Unset, str]): Return label URL
        rma (Union[Unset, str]): Return RMA
        tracking (Union[Unset, RT04RequestReturnsTracking]): Tracking information
    """

    id: Union[Unset, str] = UNSET
    label_url: Union[Unset, str] = UNSET
    rma: Union[Unset, str] = UNSET
    tracking: Union[Unset, "RT04RequestReturnsTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label_url = self.label_url

        rma = self.rma

        tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label_url is not UNSET:
            field_dict["label_url"] = label_url
        if rma is not UNSET:
            field_dict["rma"] = rma
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt04_request_returns_tracking import RT04RequestReturnsTracking

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        label_url = d.pop("label_url", UNSET)

        rma = d.pop("rma", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, RT04RequestReturnsTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = RT04RequestReturnsTracking.from_dict(_tracking)

        rt04_request_returns = cls(
            id=id,
            label_url=label_url,
            rma=rma,
            tracking=tracking,
        )

        rt04_request_returns.additional_properties = d
        return rt04_request_returns

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
