from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PRI01Body")


@_attrs_define
class PRI01Body:
    """
    Attributes:
        file (Union[Unset, File]): Import CSV file to upload. Use <code>multipart/form-data</code> with name
            <code>file</code>.<br/>
            Csv format:<br/>
            <ul>
            <li><code>"offer-sku";"price";"discount-price";"discount-start-date";"discount-end-date"</code></li>
            <ul>
                <li>1 line = 1 offer price</li>
                <li>List prices for the same offer together</li>
                <li>Limits: 50 prices can be created for an offer</li>
            </ul>
            <li><b>Volume Pricing users</b>: use additional columns <code>price-ranges</code> and <code>discount-
            ranges</code></li>
            <li><b>Channel Pricing users</b>: use additional column <code>channels</code></li>
            <li><b>Scheduled Pricing users</b>: use additional columns <code>start-date</code> and <code>end-
            date</code></li>
            <li><b>Customer Pricing users</b>: use additional columns <code>customer-organization-ids</code> and
            <code>customer-group-ids</code></li>
            </ul>
    """

    file: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        pri01_body = cls(
            file=file,
        )

        pri01_body.additional_properties = d
        return pri01_body

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
