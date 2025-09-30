import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of52_request_rename_fields import OF52RequestRenameFields


T = TypeVar("T", bound="OF52Request")


@_attrs_define
class OF52Request:
    """
    Attributes:
        channel_codes (Union[Unset, list[str]]): List of the channel codes to filter with. If specified, only offers
            that can be sold on the specified channel(s) will be returned. If not, offers will be returned regardless of
            their channels.
        export_type (Union[Unset, str]): Format of the generated files: CSV or JSON (value is either
            <code>text/csv</code> or <code>application/json</code>). Default to <code>text/csv</code>.
        include_fields (Union[Unset, list[str]]): Specify which columns (CSV) or fields (JSON) will be returned. If
            specified, only the listed columns/fields will be returned, otherwise all will be returned. If combined with
            <em>rename_fields</em>, <em>include_fields</em> must use the original header/field names.
        include_inactive_offers (Union[Unset, bool]): When calling the API in full mode (i.e. when no
            <i>last_request_date</i> is provided), inactive offers are not returned. To retrieve both active and inactive
            offers, set this field to true.<br />When calling the API in differential mode (i.e. when the
            <i>last_request_date</i> is provided), both active and inactive offers are returned. This field cannot be used
            in differential mode otherwise the call fails. Default: False.
        items_per_chunk (Union[Unset, int]): The maximum number of items per chunk
        last_request_date (Union[Unset, datetime.datetime]): Date and time of your last request.<br />If provided,
            retrieves all offers updated since this date and time, including deleted and inactive offers.<br />If not
            provided, retrieves all active offers only, unless otherwise specified in the <i>include_inactive_offers</i>
            field.
        megabytes_per_chunk (Union[Unset, int]): The maximum size in megabytes of a chunk
        rename_fields (Union[Unset, OF52RequestRenameFields]): This is only supported for CSV export. Can be used to
            modify the name of the CSV headers. The expected format is a JSON object with the original fields as keys and
            the substitute as value. <pre>{"offer-id": "offerId", "shop-name":"shopName"}</pre>
        shipping_zones (Union[Unset, list[str]]): If the setting <i>Export shipping charges and delivery times</i> has
            been enabled, list of the shipping zones codes to filter with. If specified, only shipping information linked to
            the given zones will be returned. Otherwise, all shipping information for all zones will be returned.
    """

    channel_codes: Union[Unset, list[str]] = UNSET
    export_type: Union[Unset, str] = UNSET
    include_fields: Union[Unset, list[str]] = UNSET
    include_inactive_offers: Union[Unset, bool] = False
    items_per_chunk: Union[Unset, int] = UNSET
    last_request_date: Union[Unset, datetime.datetime] = UNSET
    megabytes_per_chunk: Union[Unset, int] = UNSET
    rename_fields: Union[Unset, "OF52RequestRenameFields"] = UNSET
    shipping_zones: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channel_codes, Unset):
            channel_codes = self.channel_codes

        export_type = self.export_type

        include_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.include_fields, Unset):
            include_fields = self.include_fields

        include_inactive_offers = self.include_inactive_offers

        items_per_chunk = self.items_per_chunk

        last_request_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_request_date, Unset):
            last_request_date = self.last_request_date.isoformat()

        megabytes_per_chunk = self.megabytes_per_chunk

        rename_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rename_fields, Unset):
            rename_fields = self.rename_fields.to_dict()

        shipping_zones: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shipping_zones, Unset):
            shipping_zones = self.shipping_zones

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_codes is not UNSET:
            field_dict["channel_codes"] = channel_codes
        if export_type is not UNSET:
            field_dict["export_type"] = export_type
        if include_fields is not UNSET:
            field_dict["include_fields"] = include_fields
        if include_inactive_offers is not UNSET:
            field_dict["include_inactive_offers"] = include_inactive_offers
        if items_per_chunk is not UNSET:
            field_dict["items_per_chunk"] = items_per_chunk
        if last_request_date is not UNSET:
            field_dict["last_request_date"] = last_request_date
        if megabytes_per_chunk is not UNSET:
            field_dict["megabytes_per_chunk"] = megabytes_per_chunk
        if rename_fields is not UNSET:
            field_dict["rename_fields"] = rename_fields
        if shipping_zones is not UNSET:
            field_dict["shipping_zones"] = shipping_zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of52_request_rename_fields import OF52RequestRenameFields

        d = dict(src_dict)
        channel_codes = cast(list[str], d.pop("channel_codes", UNSET))

        export_type = d.pop("export_type", UNSET)

        include_fields = cast(list[str], d.pop("include_fields", UNSET))

        include_inactive_offers = d.pop("include_inactive_offers", UNSET)

        items_per_chunk = d.pop("items_per_chunk", UNSET)

        _last_request_date = d.pop("last_request_date", UNSET)
        last_request_date: Union[Unset, datetime.datetime]
        if isinstance(_last_request_date, Unset):
            last_request_date = UNSET
        else:
            last_request_date = isoparse(_last_request_date)

        megabytes_per_chunk = d.pop("megabytes_per_chunk", UNSET)

        _rename_fields = d.pop("rename_fields", UNSET)
        rename_fields: Union[Unset, OF52RequestRenameFields]
        if isinstance(_rename_fields, Unset):
            rename_fields = UNSET
        else:
            rename_fields = OF52RequestRenameFields.from_dict(_rename_fields)

        shipping_zones = cast(list[str], d.pop("shipping_zones", UNSET))

        of52_request = cls(
            channel_codes=channel_codes,
            export_type=export_type,
            include_fields=include_fields,
            include_inactive_offers=include_inactive_offers,
            items_per_chunk=items_per_chunk,
            last_request_date=last_request_date,
            megabytes_per_chunk=megabytes_per_chunk,
            rename_fields=rename_fields,
            shipping_zones=shipping_zones,
        )

        of52_request.additional_properties = d
        return of52_request

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
