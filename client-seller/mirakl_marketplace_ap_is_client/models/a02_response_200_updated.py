import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a02_response_200_updated_address import A02Response200UpdatedAddress
    from ..models.a02_response_200_updated_default_billing_information import (
        A02Response200UpdatedDefaultBillingInformation,
    )
    from ..models.a02_response_200_updated_payment_info import A02Response200UpdatedPaymentInfo
    from ..models.a02_response_200_updated_pro_details import A02Response200UpdatedProDetails
    from ..models.a02_response_200_updated_producer_identifiers import A02Response200UpdatedProducerIdentifiers
    from ..models.a02_response_200_updated_shipping import A02Response200UpdatedShipping
    from ..models.a02_response_200_updated_shop_additional_fields import A02Response200UpdatedShopAdditionalFields
    from ..models.a02_response_200_updated_specific_billing_informations import (
        A02Response200UpdatedSpecificBillingInformations,
    )


T = TypeVar("T", bound="A02Response200Updated")


@_attrs_define
class A02Response200Updated:
    """
    Attributes:
        address (Union[Unset, A02Response200UpdatedAddress]):
        channels (Union[Unset, list[str]]): List of the channel codes associated to the shop
        closed_from (Union[Unset, datetime.datetime]): The start date of the closing of the shop
        closed_to (Union[Unset, datetime.datetime]): The end date of the closing of the shop
        default_billing_information (Union[Unset, A02Response200UpdatedDefaultBillingInformation]):
        description (Union[Unset, str]): Shop description
        email (Union[Unset, str]): Shop email
        fax (Union[Unset, str]): Shop fax
        is_professional (Union[Unset, bool]): Whether or not the shop is professional
        model (Union[Unset, str]): Shop platform model, current possible values :
            <ul>
                <li><code>MARKETPLACE</code></li>
                <li><code>DROPSHIP</code></li>
                <li><code>ONE_CREDITOR</code></li>
            </ul>
        payment_info (Union[Unset, A02Response200UpdatedPaymentInfo]):
        payment_method_mandatory (Union[Unset, bool]): Payment method is mandatory
        pro_details (Union[Unset, A02Response200UpdatedProDetails]):
        producer_identifiers (Union[Unset, list['A02Response200UpdatedProducerIdentifiers']]): List of shop’s producer
            identifiers per Extended Producer Responsibility (EPR) categories. Only available if the operator setting
            <em>Activate data collection related to circular economy regulations</em> is enabled.
        recycling_policy (Union[Unset, str]): <span>Recycling policy of the shop - only available if the operator
            setting </span><em>Activate data collection related to circular economy regulations</em><span> has been
            enabled.</span>
        return_policy (Union[Unset, str]): Return policy of the shop
        shipping (Union[Unset, A02Response200UpdatedShipping]):
        shipping_country (Union[Unset, str]): Shipping country of the shop
        shop_additional_fields (Union[Unset, list['A02Response200UpdatedShopAdditionalFields']]): Additional fields of
            the shop
        shop_name (Union[Unset, str]): Shop name
        specific_billing_informations (Union[Unset, list['A02Response200UpdatedSpecificBillingInformations']]): The list
            of specific billing information of the shop, used for invoicing and reporting purposes
            <br/><i>Applies only when the shop is <code>professional</code></i>
        web_site (Union[Unset, str]): Shop website
    """

    address: Union[Unset, "A02Response200UpdatedAddress"] = UNSET
    channels: Union[Unset, list[str]] = UNSET
    closed_from: Union[Unset, datetime.datetime] = UNSET
    closed_to: Union[Unset, datetime.datetime] = UNSET
    default_billing_information: Union[Unset, "A02Response200UpdatedDefaultBillingInformation"] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    is_professional: Union[Unset, bool] = UNSET
    model: Union[Unset, str] = UNSET
    payment_info: Union[Unset, "A02Response200UpdatedPaymentInfo"] = UNSET
    payment_method_mandatory: Union[Unset, bool] = UNSET
    pro_details: Union[Unset, "A02Response200UpdatedProDetails"] = UNSET
    producer_identifiers: Union[Unset, list["A02Response200UpdatedProducerIdentifiers"]] = UNSET
    recycling_policy: Union[Unset, str] = UNSET
    return_policy: Union[Unset, str] = UNSET
    shipping: Union[Unset, "A02Response200UpdatedShipping"] = UNSET
    shipping_country: Union[Unset, str] = UNSET
    shop_additional_fields: Union[Unset, list["A02Response200UpdatedShopAdditionalFields"]] = UNSET
    shop_name: Union[Unset, str] = UNSET
    specific_billing_informations: Union[Unset, list["A02Response200UpdatedSpecificBillingInformations"]] = UNSET
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

        default_billing_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_billing_information, Unset):
            default_billing_information = self.default_billing_information.to_dict()

        description = self.description

        email = self.email

        fax = self.fax

        is_professional = self.is_professional

        model = self.model

        payment_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_info, Unset):
            payment_info = self.payment_info.to_dict()

        payment_method_mandatory = self.payment_method_mandatory

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

        shipping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        shipping_country = self.shipping_country

        shop_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shop_additional_fields, Unset):
            shop_additional_fields = []
            for shop_additional_fields_item_data in self.shop_additional_fields:
                shop_additional_fields_item = shop_additional_fields_item_data.to_dict()
                shop_additional_fields.append(shop_additional_fields_item)

        shop_name = self.shop_name

        specific_billing_informations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.specific_billing_informations, Unset):
            specific_billing_informations = []
            for specific_billing_informations_item_data in self.specific_billing_informations:
                specific_billing_informations_item = specific_billing_informations_item_data.to_dict()
                specific_billing_informations.append(specific_billing_informations_item)

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
        if default_billing_information is not UNSET:
            field_dict["default_billing_information"] = default_billing_information
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if is_professional is not UNSET:
            field_dict["is_professional"] = is_professional
        if model is not UNSET:
            field_dict["model"] = model
        if payment_info is not UNSET:
            field_dict["payment_info"] = payment_info
        if payment_method_mandatory is not UNSET:
            field_dict["payment_method_mandatory"] = payment_method_mandatory
        if pro_details is not UNSET:
            field_dict["pro_details"] = pro_details
        if producer_identifiers is not UNSET:
            field_dict["producer_identifiers"] = producer_identifiers
        if recycling_policy is not UNSET:
            field_dict["recycling_policy"] = recycling_policy
        if return_policy is not UNSET:
            field_dict["return_policy"] = return_policy
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if shipping_country is not UNSET:
            field_dict["shipping_country"] = shipping_country
        if shop_additional_fields is not UNSET:
            field_dict["shop_additional_fields"] = shop_additional_fields
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if specific_billing_informations is not UNSET:
            field_dict["specific_billing_informations"] = specific_billing_informations
        if web_site is not UNSET:
            field_dict["web_site"] = web_site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a02_response_200_updated_address import A02Response200UpdatedAddress
        from ..models.a02_response_200_updated_default_billing_information import (
            A02Response200UpdatedDefaultBillingInformation,
        )
        from ..models.a02_response_200_updated_payment_info import A02Response200UpdatedPaymentInfo
        from ..models.a02_response_200_updated_pro_details import A02Response200UpdatedProDetails
        from ..models.a02_response_200_updated_producer_identifiers import A02Response200UpdatedProducerIdentifiers
        from ..models.a02_response_200_updated_shipping import A02Response200UpdatedShipping
        from ..models.a02_response_200_updated_shop_additional_fields import A02Response200UpdatedShopAdditionalFields
        from ..models.a02_response_200_updated_specific_billing_informations import (
            A02Response200UpdatedSpecificBillingInformations,
        )

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, A02Response200UpdatedAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = A02Response200UpdatedAddress.from_dict(_address)

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

        _default_billing_information = d.pop("default_billing_information", UNSET)
        default_billing_information: Union[Unset, A02Response200UpdatedDefaultBillingInformation]
        if isinstance(_default_billing_information, Unset):
            default_billing_information = UNSET
        else:
            default_billing_information = A02Response200UpdatedDefaultBillingInformation.from_dict(
                _default_billing_information
            )

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        is_professional = d.pop("is_professional", UNSET)

        model = d.pop("model", UNSET)

        _payment_info = d.pop("payment_info", UNSET)
        payment_info: Union[Unset, A02Response200UpdatedPaymentInfo]
        if isinstance(_payment_info, Unset):
            payment_info = UNSET
        else:
            payment_info = A02Response200UpdatedPaymentInfo.from_dict(_payment_info)

        payment_method_mandatory = d.pop("payment_method_mandatory", UNSET)

        _pro_details = d.pop("pro_details", UNSET)
        pro_details: Union[Unset, A02Response200UpdatedProDetails]
        if isinstance(_pro_details, Unset):
            pro_details = UNSET
        else:
            pro_details = A02Response200UpdatedProDetails.from_dict(_pro_details)

        producer_identifiers = []
        _producer_identifiers = d.pop("producer_identifiers", UNSET)
        for producer_identifiers_item_data in _producer_identifiers or []:
            producer_identifiers_item = A02Response200UpdatedProducerIdentifiers.from_dict(
                producer_identifiers_item_data
            )

            producer_identifiers.append(producer_identifiers_item)

        recycling_policy = d.pop("recycling_policy", UNSET)

        return_policy = d.pop("return_policy", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, A02Response200UpdatedShipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = A02Response200UpdatedShipping.from_dict(_shipping)

        shipping_country = d.pop("shipping_country", UNSET)

        shop_additional_fields = []
        _shop_additional_fields = d.pop("shop_additional_fields", UNSET)
        for shop_additional_fields_item_data in _shop_additional_fields or []:
            shop_additional_fields_item = A02Response200UpdatedShopAdditionalFields.from_dict(
                shop_additional_fields_item_data
            )

            shop_additional_fields.append(shop_additional_fields_item)

        shop_name = d.pop("shop_name", UNSET)

        specific_billing_informations = []
        _specific_billing_informations = d.pop("specific_billing_informations", UNSET)
        for specific_billing_informations_item_data in _specific_billing_informations or []:
            specific_billing_informations_item = A02Response200UpdatedSpecificBillingInformations.from_dict(
                specific_billing_informations_item_data
            )

            specific_billing_informations.append(specific_billing_informations_item)

        web_site = d.pop("web_site", UNSET)

        a02_response_200_updated = cls(
            address=address,
            channels=channels,
            closed_from=closed_from,
            closed_to=closed_to,
            default_billing_information=default_billing_information,
            description=description,
            email=email,
            fax=fax,
            is_professional=is_professional,
            model=model,
            payment_info=payment_info,
            payment_method_mandatory=payment_method_mandatory,
            pro_details=pro_details,
            producer_identifiers=producer_identifiers,
            recycling_policy=recycling_policy,
            return_policy=return_policy,
            shipping=shipping,
            shipping_country=shipping_country,
            shop_additional_fields=shop_additional_fields,
            shop_name=shop_name,
            specific_billing_informations=specific_billing_informations,
            web_site=web_site,
        )

        a02_response_200_updated.additional_properties = d
        return a02_response_200_updated

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
