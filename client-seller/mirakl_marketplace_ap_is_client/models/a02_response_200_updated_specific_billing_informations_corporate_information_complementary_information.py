from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A02Response200UpdatedSpecificBillingInformationsCorporateInformationComplementaryInformation")


@_attrs_define
class A02Response200UpdatedSpecificBillingInformationsCorporateInformationComplementaryInformation:
    """
    Attributes:
        business_activity_code (Union[Unset, str]): The business activity code of the company, known as <code>APE
            code</code> in France.
            <br/><i>Applies only when the operator is registered in the <code>EU</code>, and the seller is registered in
            <code>France</code>.</i>
        company_registration_city (Union[Unset, str]): The city of the company's registry office.
            <br/><i>Applies only when the operator is registered in the <code>EU</code> and the seller is registered in
            <code>France</code> or <code>Luxembourg</code>.</i>
        company_registration_province (Union[Unset, str]): The initials of the company’s registry office province. Known
            as <code>Ufficio</code> in Italy.
            <br/><i>Applies only when the operator is registered in the <code>EU</code> and the seller is registered in
            <code>Italy</code>.</i>
        company_shareholders (Union[Unset, str]): Indicates if there is a single shareholder or several shareholders.
            Known as <code>Socio Unico</code> in Italy.
            <br/><i>Applies only when the operator is registered in the <code>EU</code> and the seller is registered in
            <code>Italy</code>.</i>
        is_in_liquidation (Union[Unset, bool]): Indicates whether the company is in liquidation or not.
            <br/><i>Applies only when the operator is registered in the <code>EU</code></i>
        legal_form (Union[Unset, str]): The legal form of the company.
            <br/><i>Applies only when the operator is registered in the <code>EU</code></i>
        share_capital (Union[Unset, float]): The share capital of the company.
            <br/><i>Applies only when the operator is registered in the <code>EU</code></i>
        share_capital_currency (Union[Unset, str]): The share capital currency of the company.
            <br/><i>Applies only when the operator is registered in the <code>EU</code></i>
        sole_trader (Union[Unset, bool]): Defines if the shop is a sole trader. When this option is set to true,
            additional information is asked to the shop. <i>Applies only when the operator is registered in the
            <code>EU</code></i>
    """

    business_activity_code: Union[Unset, str] = UNSET
    company_registration_city: Union[Unset, str] = UNSET
    company_registration_province: Union[Unset, str] = UNSET
    company_shareholders: Union[Unset, str] = UNSET
    is_in_liquidation: Union[Unset, bool] = UNSET
    legal_form: Union[Unset, str] = UNSET
    share_capital: Union[Unset, float] = UNSET
    share_capital_currency: Union[Unset, str] = UNSET
    sole_trader: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_activity_code = self.business_activity_code

        company_registration_city = self.company_registration_city

        company_registration_province = self.company_registration_province

        company_shareholders = self.company_shareholders

        is_in_liquidation = self.is_in_liquidation

        legal_form = self.legal_form

        share_capital = self.share_capital

        share_capital_currency = self.share_capital_currency

        sole_trader = self.sole_trader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_activity_code is not UNSET:
            field_dict["business_activity_code"] = business_activity_code
        if company_registration_city is not UNSET:
            field_dict["company_registration_city"] = company_registration_city
        if company_registration_province is not UNSET:
            field_dict["company_registration_province"] = company_registration_province
        if company_shareholders is not UNSET:
            field_dict["company_shareholders"] = company_shareholders
        if is_in_liquidation is not UNSET:
            field_dict["is_in_liquidation"] = is_in_liquidation
        if legal_form is not UNSET:
            field_dict["legal_form"] = legal_form
        if share_capital is not UNSET:
            field_dict["share_capital"] = share_capital
        if share_capital_currency is not UNSET:
            field_dict["share_capital_currency"] = share_capital_currency
        if sole_trader is not UNSET:
            field_dict["sole_trader"] = sole_trader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_activity_code = d.pop("business_activity_code", UNSET)

        company_registration_city = d.pop("company_registration_city", UNSET)

        company_registration_province = d.pop("company_registration_province", UNSET)

        company_shareholders = d.pop("company_shareholders", UNSET)

        is_in_liquidation = d.pop("is_in_liquidation", UNSET)

        legal_form = d.pop("legal_form", UNSET)

        share_capital = d.pop("share_capital", UNSET)

        share_capital_currency = d.pop("share_capital_currency", UNSET)

        sole_trader = d.pop("sole_trader", UNSET)

        a02_response_200_updated_specific_billing_informations_corporate_information_complementary_information = cls(
            business_activity_code=business_activity_code,
            company_registration_city=company_registration_city,
            company_registration_province=company_registration_province,
            company_shareholders=company_shareholders,
            is_in_liquidation=is_in_liquidation,
            legal_form=legal_form,
            share_capital=share_capital,
            share_capital_currency=share_capital_currency,
            sole_trader=sole_trader,
        )

        a02_response_200_updated_specific_billing_informations_corporate_information_complementary_information.additional_properties = d
        return a02_response_200_updated_specific_billing_informations_corporate_information_complementary_information

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
