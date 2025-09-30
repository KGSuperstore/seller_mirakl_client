from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_issuer_organization_address import DR11Response200DataIssuerOrganizationAddress
    from ..models.dr11_response_200_data_issuer_organization_fiscal_representative import (
        DR11Response200DataIssuerOrganizationFiscalRepresentative,
    )
    from ..models.dr11_response_200_data_issuer_organization_personal_information import (
        DR11Response200DataIssuerOrganizationPersonalInformation,
    )


T = TypeVar("T", bound="DR11Response200DataIssuerOrganization")


@_attrs_define
class DR11Response200DataIssuerOrganization:
    """
    Attributes:
        address (Union[Unset, DR11Response200DataIssuerOrganizationAddress]):
        business_activity_code (Union[Unset, str]): The business activity code of the organization.
        company_shareholders (Union[Unset, str]): Indicates if there is a single shareholder or several shareholders.
        fiscal_representative (Union[Unset, DR11Response200DataIssuerOrganizationFiscalRepresentative]):
        identification_number (Union[Unset, str]): The identification number of the organization.
        is_in_liquidation (Union[Unset, bool]): Indicates whether the company is in liquidation or not.
        legal_form (Union[Unset, str]): The legal form of the organization.
        local_tax_number (Union[Unset, str]): The VAT/GST number.
        local_tax_number_country (Union[Unset, str]): The local tax number country of the organization.
        name (Union[Unset, str]): The organization name.
        personal_information (Union[Unset, DR11Response200DataIssuerOrganizationPersonalInformation]):
        share_capital (Union[Unset, float]): The share capital of the organization.
        share_capital_currency (Union[Unset, str]): The share capital currency of the organization.
        sole_trader (Union[Unset, bool]): Indicates if the organization is a sole trader.
        tax_identification_number (Union[Unset, str]): The tax identification number of the organization.
        tax_number_country (Union[Unset, str]): The tax number country of the organization.
        trade_company_registration_location (Union[Unset, str]): The trade company registration location of the
            organization.
    """

    address: Union[Unset, "DR11Response200DataIssuerOrganizationAddress"] = UNSET
    business_activity_code: Union[Unset, str] = UNSET
    company_shareholders: Union[Unset, str] = UNSET
    fiscal_representative: Union[Unset, "DR11Response200DataIssuerOrganizationFiscalRepresentative"] = UNSET
    identification_number: Union[Unset, str] = UNSET
    is_in_liquidation: Union[Unset, bool] = UNSET
    legal_form: Union[Unset, str] = UNSET
    local_tax_number: Union[Unset, str] = UNSET
    local_tax_number_country: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    personal_information: Union[Unset, "DR11Response200DataIssuerOrganizationPersonalInformation"] = UNSET
    share_capital: Union[Unset, float] = UNSET
    share_capital_currency: Union[Unset, str] = UNSET
    sole_trader: Union[Unset, bool] = UNSET
    tax_identification_number: Union[Unset, str] = UNSET
    tax_number_country: Union[Unset, str] = UNSET
    trade_company_registration_location: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        business_activity_code = self.business_activity_code

        company_shareholders = self.company_shareholders

        fiscal_representative: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fiscal_representative, Unset):
            fiscal_representative = self.fiscal_representative.to_dict()

        identification_number = self.identification_number

        is_in_liquidation = self.is_in_liquidation

        legal_form = self.legal_form

        local_tax_number = self.local_tax_number

        local_tax_number_country = self.local_tax_number_country

        name = self.name

        personal_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personal_information, Unset):
            personal_information = self.personal_information.to_dict()

        share_capital = self.share_capital

        share_capital_currency = self.share_capital_currency

        sole_trader = self.sole_trader

        tax_identification_number = self.tax_identification_number

        tax_number_country = self.tax_number_country

        trade_company_registration_location = self.trade_company_registration_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if business_activity_code is not UNSET:
            field_dict["business_activity_code"] = business_activity_code
        if company_shareholders is not UNSET:
            field_dict["company_shareholders"] = company_shareholders
        if fiscal_representative is not UNSET:
            field_dict["fiscal_representative"] = fiscal_representative
        if identification_number is not UNSET:
            field_dict["identification_number"] = identification_number
        if is_in_liquidation is not UNSET:
            field_dict["is_in_liquidation"] = is_in_liquidation
        if legal_form is not UNSET:
            field_dict["legal_form"] = legal_form
        if local_tax_number is not UNSET:
            field_dict["local_tax_number"] = local_tax_number
        if local_tax_number_country is not UNSET:
            field_dict["local_tax_number_country"] = local_tax_number_country
        if name is not UNSET:
            field_dict["name"] = name
        if personal_information is not UNSET:
            field_dict["personal_information"] = personal_information
        if share_capital is not UNSET:
            field_dict["share_capital"] = share_capital
        if share_capital_currency is not UNSET:
            field_dict["share_capital_currency"] = share_capital_currency
        if sole_trader is not UNSET:
            field_dict["sole_trader"] = sole_trader
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number
        if tax_number_country is not UNSET:
            field_dict["tax_number_country"] = tax_number_country
        if trade_company_registration_location is not UNSET:
            field_dict["trade_company_registration_location"] = trade_company_registration_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_issuer_organization_address import (
            DR11Response200DataIssuerOrganizationAddress,
        )
        from ..models.dr11_response_200_data_issuer_organization_fiscal_representative import (
            DR11Response200DataIssuerOrganizationFiscalRepresentative,
        )
        from ..models.dr11_response_200_data_issuer_organization_personal_information import (
            DR11Response200DataIssuerOrganizationPersonalInformation,
        )

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, DR11Response200DataIssuerOrganizationAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DR11Response200DataIssuerOrganizationAddress.from_dict(_address)

        business_activity_code = d.pop("business_activity_code", UNSET)

        company_shareholders = d.pop("company_shareholders", UNSET)

        _fiscal_representative = d.pop("fiscal_representative", UNSET)
        fiscal_representative: Union[Unset, DR11Response200DataIssuerOrganizationFiscalRepresentative]
        if isinstance(_fiscal_representative, Unset):
            fiscal_representative = UNSET
        else:
            fiscal_representative = DR11Response200DataIssuerOrganizationFiscalRepresentative.from_dict(
                _fiscal_representative
            )

        identification_number = d.pop("identification_number", UNSET)

        is_in_liquidation = d.pop("is_in_liquidation", UNSET)

        legal_form = d.pop("legal_form", UNSET)

        local_tax_number = d.pop("local_tax_number", UNSET)

        local_tax_number_country = d.pop("local_tax_number_country", UNSET)

        name = d.pop("name", UNSET)

        _personal_information = d.pop("personal_information", UNSET)
        personal_information: Union[Unset, DR11Response200DataIssuerOrganizationPersonalInformation]
        if isinstance(_personal_information, Unset):
            personal_information = UNSET
        else:
            personal_information = DR11Response200DataIssuerOrganizationPersonalInformation.from_dict(
                _personal_information
            )

        share_capital = d.pop("share_capital", UNSET)

        share_capital_currency = d.pop("share_capital_currency", UNSET)

        sole_trader = d.pop("sole_trader", UNSET)

        tax_identification_number = d.pop("tax_identification_number", UNSET)

        tax_number_country = d.pop("tax_number_country", UNSET)

        trade_company_registration_location = d.pop("trade_company_registration_location", UNSET)

        dr11_response_200_data_issuer_organization = cls(
            address=address,
            business_activity_code=business_activity_code,
            company_shareholders=company_shareholders,
            fiscal_representative=fiscal_representative,
            identification_number=identification_number,
            is_in_liquidation=is_in_liquidation,
            legal_form=legal_form,
            local_tax_number=local_tax_number,
            local_tax_number_country=local_tax_number_country,
            name=name,
            personal_information=personal_information,
            share_capital=share_capital,
            share_capital_currency=share_capital_currency,
            sole_trader=sole_trader,
            tax_identification_number=tax_identification_number,
            tax_number_country=tax_number_country,
            trade_company_registration_location=trade_company_registration_location,
        )

        dr11_response_200_data_issuer_organization.additional_properties = d
        return dr11_response_200_data_issuer_organization

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
