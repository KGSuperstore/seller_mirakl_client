from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="OF01Body")


@_attrs_define
class OF01Body:
    """
    Attributes:
        file (Union[Unset, File]): Import file (CSV or XML or XLSX) to upload. Use <code>multipart/form-data</code> with
            name <code>file</code>.<br/> Csv format:<br/><pre>"sku";"product-id";"product-id-type";"description";"internal-
            description";"price";"price-additional-info";"quantity";"min-quantity-alert";"state";"available-start-
            date";"available-end-date";"discount-price";"discount-start-date";"discount-end-date";"discount-ranges";"allow-
            quote-requests";"leadtime-to-ship";"min-order-quantity";"max-order-quantity";"package-quantity";"update-
            delete";"price-ranges";"ecotax";"gift-wrap";"min-quantity-ordered"</pre><br/><br/>If you use specific sales
            channels, use: <pre>"price[channel=channel code]";"discount-price[channel=channel code]";"discount-start-
            date[channel=channel code]";"discount-end-date[channel=channel code]";"discount-ranges[channel=channel
            code]";"price-ranges[channel=channel code]"</pre><br/>If you use the price per measurement unit feature, use
            <code>pricing-unit</code> to specify the unit corresponding to the submitted <code>price</code>.<br/><br/>If US
            Tax options are activated on the platform, use: <code>product-tax-code</code> to facilitate tax
            calculations.<br/><br/>If <i>Data collection related to circular economy regulations</i> is enabled,
            use:<br/><pre>"producer-id[EPR category code]"; "eco-contribution-amount[EPR category code]"</pre>EPR category
            code must be one of: <pre>FR-AGROPACK, FR-ASL, FR-DASRIPAT, FR-DBPS, FR-DDS, FR-DEA, FR-DEEE, FR-DISPMED, FR-
            DIY, FR-EMBM, FR-GF, FR-JOUETS, FR-LUB, FR-MH, FR-MNU, FR-PA, FR-PAP, FR-PCHIM, FR-PMCB, FR-PNEU, FR-TABAC, FR-
            TLC, FR-VEHICULE, FR-VHU, DE-BATTG, DE-PACK, DE-WEEE, ES-PACK, ES-GPACK, ES-WEEE</pre><br/>
        import_mode (Union[Unset, str]):
        operator_format (Union[Unset, bool]): Force the use of the operator product format Default: False.
        with_products (Union[Unset, bool]): This file also contains product information Default: False.
    """

    file: Union[Unset, File] = UNSET
    import_mode: Union[Unset, str] = UNSET
    operator_format: Union[Unset, bool] = False
    with_products: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        import_mode = self.import_mode

        operator_format = self.operator_format

        with_products = self.with_products

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if import_mode is not UNSET:
            field_dict["import_mode"] = import_mode
        if operator_format is not UNSET:
            field_dict["operator_format"] = operator_format
        if with_products is not UNSET:
            field_dict["with_products"] = with_products

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.import_mode, Unset):
            files.append(("import_mode", (None, str(self.import_mode).encode(), "text/plain")))

        if not isinstance(self.operator_format, Unset):
            files.append(("operator_format", (None, str(self.operator_format).encode(), "text/plain")))

        if not isinstance(self.with_products, Unset):
            files.append(("with_products", (None, str(self.with_products).encode(), "text/plain")))

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

        import_mode = d.pop("import_mode", UNSET)

        operator_format = d.pop("operator_format", UNSET)

        with_products = d.pop("with_products", UNSET)

        of01_body = cls(
            file=file,
            import_mode=import_mode,
            operator_format=operator_format,
            with_products=with_products,
        )

        of01_body.additional_properties = d
        return of01_body

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
