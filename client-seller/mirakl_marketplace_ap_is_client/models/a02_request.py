import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a02_request_address import A02RequestAddress
    from ..models.a02_request_payment_info import A02RequestPaymentInfo
    from ..models.a02_request_pro_details import A02RequestProDetails
    from ..models.a02_request_producer_identifiers import A02RequestProducerIdentifiers
    from ..models.a02_request_shop_additional_fields import A02RequestShopAdditionalFields


T = TypeVar("T", bound="A02Request")


@_attrs_define
class A02Request:
    """
    Attributes:
        address (Union[Unset, A02RequestAddress]): The address of the shop. Cannot be null.
        channels (Union[Unset, list[str]]): List of the channel codes associated to the shop. If new channel is
            associated without providing values for the required shop_additional_fields, default values will be set.
        closed_from (Union[Unset, datetime.datetime]): Date: if defined, this shop will be closed on this date.
            Nullable.
        closed_to (Union[Unset, datetime.datetime]): Date: if defined, this shop will be reopened on this date.
            Nullable.
        description (Union[Unset, str]): Description of the shop. Nullable.
        email (Union[Unset, str]): Email of the shop. Cannot be null.
        fax (Union[Unset, str]): Fax of the shop. Nullable.
        is_professional (Union[Unset, bool]): Whether or not the shop is professional. Cannot be null.
        payment_info (Union[Unset, A02RequestPaymentInfo]): Payment information of the shop. Nullable.
        pro_details (Union[Unset, A02RequestProDetails]): Professional details of the shop. Updated and not nullable if
            shop is declared as professional.
        producer_identifiers (Union[Unset, list['A02RequestProducerIdentifiers']]): List of shop’s producer identifiers
            per Extended Producer Responsibility (EPR) categories. Only available if the operator setting <em>Activate data
            collection related to circular economy regulations</em> is enabled.
        recycling_policy (Union[Unset, str]): Recycling policy - only available if the operator setting <em>Activate
            data collection related to circular economy regulations</em> has been enabled.
        return_policy (Union[Unset, str]): Return policy of the shop. Nullable.
        shipping_country (Union[Unset, str]): Shipping country of the shop. Nullable.
        shop_additional_fields (Union[Unset, list['A02RequestShopAdditionalFields']]): Additional fields of the shop.
            Note that if the 'value' field in the child structure is absent, the corresponding additional field value will
            be removed for this shop. Nullable.
        shop_name (Union[Unset, str]): The name of the shop. Cannot be null.
        web_site (Union[Unset, str]): Website of the shop. Nullable.
    """

    address: Union[Unset, "A02RequestAddress"] = UNSET
    channels: Union[Unset, list[str]] = UNSET
    closed_from: Union[Unset, datetime.datetime] = UNSET
    closed_to: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    is_professional: Union[Unset, bool] = UNSET
    payment_info: Union[Unset, "A02RequestPaymentInfo"] = UNSET
    pro_details: Union[Unset, "A02RequestProDetails"] = UNSET
    producer_identifiers: Union[Unset, list["A02RequestProducerIdentifiers"]] = UNSET
    recycling_policy: Union[Unset, str] = UNSET
    return_policy: Union[Unset, str] = UNSET
    shipping_country: Union[Unset, str] = UNSET
    shop_additional_fields: Union[Unset, list["A02RequestShopAdditionalFields"]] = UNSET
    shop_name: Union[Unset, str] = UNSET
    web_site: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        closed_from: Union[Unset, str] = UNSET
        if not isinstance(self.closed_from, Unset):
            closed_from = self.closed_from.isoformat()

        closed_to: Union[Unset, str] = UNSET
        if not isinstance(self.closed_to, Unset):
            closed_to = self.closed_to.isoformat()

        description = self.description

        email = self.email

        fax = self.fax

        is_professional = self.is_professional

        payment_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_info, Unset):
            payment_info = self.payment_info.to_dict()

        pro_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pro_details, Unset):
            pro_details = self.pro_details.to_dict()

        producer_identifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.producer_identifiers, Unset):
            producer_identifiers = []
            for producer_identifiers_item_data in self.producer_identifiers:
                producer_identifiers_item = producer_identifiers_item_data.to_dict()
                producer_identifiers.append(producer_identifiers_item)

        recycling_policy = self.recycling_policy

        return_policy = self.return_policy

        shipping_country = self.shipping_country

        shop_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shop_additional_fields, Unset):
            shop_additional_fields = []
            for shop_additional_fields_item_data in self.shop_additional_fields:
                shop_additional_fields_item = shop_additional_fields_item_data.to_dict()
                shop_additional_fields.append(shop_additional_fields_item)

        shop_name = self.shop_name

        web_site = self.web_site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if channels is not UNSET:
            field_dict["channels"] = channels
        if closed_from is not UNSET:
            field_dict["closed_from"] = closed_from
        if closed_to is not UNSET:
            field_dict["closed_to"] = closed_to
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if is_professional is not UNSET:
            field_dict["is_professional"] = is_professional
        if payment_info is not UNSET:
            field_dict["payment_info"] = payment_info
        if pro_details is not UNSET:
            field_dict["pro_details"] = pro_details
        if producer_identifiers is not UNSET:
            field_dict["producer_identifiers"] = producer_identifiers
        if recycling_policy is not UNSET:
            field_dict["recycling_policy"] = recycling_policy
        if return_policy is not UNSET:
            field_dict["return_policy"] = return_policy
        if shipping_country is not UNSET:
            field_dict["shipping_country"] = shipping_country
        if shop_additional_fields is not UNSET:
            field_dict["shop_additional_fields"] = shop_additional_fields
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if web_site is not UNSET:
            field_dict["web_site"] = web_site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a02_request_address import A02RequestAddress
        from ..models.a02_request_payment_info import A02RequestPaymentInfo
        from ..models.a02_request_pro_details import A02RequestProDetails
        from ..models.a02_request_producer_identifiers import A02RequestProducerIdentifiers
        from ..models.a02_request_shop_additional_fields import A02RequestShopAdditionalFields

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, A02RequestAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = A02RequestAddress.from_dict(_address)

        channels = cast(list[str], d.pop("channels", UNSET))

        _closed_from = d.pop("closed_from", UNSET)
        closed_from: Union[Unset, datetime.datetime]
        if isinstance(_closed_from, Unset):
            closed_from = UNSET
        else:
            closed_from = isoparse(_closed_from)

        _closed_to = d.pop("closed_to", UNSET)
        closed_to: Union[Unset, datetime.datetime]
        if isinstance(_closed_to, Unset):
            closed_to = UNSET
        else:
            closed_to = isoparse(_closed_to)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        is_professional = d.pop("is_professional", UNSET)

        _payment_info = d.pop("payment_info", UNSET)
        payment_info: Union[Unset, A02RequestPaymentInfo]
        if isinstance(_payment_info, Unset):
            payment_info = UNSET
        else:
            payment_info = A02RequestPaymentInfo.from_dict(_payment_info)

        _pro_details = d.pop("pro_details", UNSET)
        pro_details: Union[Unset, A02RequestProDetails]
        if isinstance(_pro_details, Unset):
            pro_details = UNSET
        else:
            pro_details = A02RequestProDetails.from_dict(_pro_details)

        producer_identifiers = []
        _producer_identifiers = d.pop("producer_identifiers", UNSET)
        for producer_identifiers_item_data in _producer_identifiers or []:
            producer_identifiers_item = A02RequestProducerIdentifiers.from_dict(producer_identifiers_item_data)

            producer_identifiers.append(producer_identifiers_item)

        recycling_policy = d.pop("recycling_policy", UNSET)

        return_policy = d.pop("return_policy", UNSET)

        shipping_country = d.pop("shipping_country", UNSET)

        shop_additional_fields = []
        _shop_additional_fields = d.pop("shop_additional_fields", UNSET)
        for shop_additional_fields_item_data in _shop_additional_fields or []:
            shop_additional_fields_item = A02RequestShopAdditionalFields.from_dict(shop_additional_fields_item_data)

            shop_additional_fields.append(shop_additional_fields_item)

        shop_name = d.pop("shop_name", UNSET)

        web_site = d.pop("web_site", UNSET)

        a02_request = cls(
            address=address,
            channels=channels,
            closed_from=closed_from,
            closed_to=closed_to,
            description=description,
            email=email,
            fax=fax,
            is_professional=is_professional,
            payment_info=payment_info,
            pro_details=pro_details,
            producer_identifiers=producer_identifiers,
            recycling_policy=recycling_policy,
            return_policy=return_policy,
            shipping_country=shipping_country,
            shop_additional_fields=shop_additional_fields,
            shop_name=shop_name,
            web_site=web_site,
        )

        a02_request.additional_properties = d
        return a02_request

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
