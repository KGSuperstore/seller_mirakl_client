import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr11_response_200_data_document_details import DR11Response200DataDocumentDetails
    from ..models.dr11_response_200_data_entities import DR11Response200DataEntities
    from ..models.dr11_response_200_data_initial_documents import DR11Response200DataInitialDocuments
    from ..models.dr11_response_200_data_issuer import DR11Response200DataIssuer
    from ..models.dr11_response_200_data_payment import DR11Response200DataPayment
    from ..models.dr11_response_200_data_payment_destination import DR11Response200DataPaymentDestination
    from ..models.dr11_response_200_data_payment_terms import DR11Response200DataPaymentTerms
    from ..models.dr11_response_200_data_recipient import DR11Response200DataRecipient
    from ..models.dr11_response_200_data_taxes import DR11Response200DataTaxes


T = TypeVar("T", bound="DR11Response200Data")


@_attrs_define
class DR11Response200Data:
    """
    Attributes:
        currency_iso_code (Union[Unset, str]): The currency of the document request
        date_created (Union[Unset, datetime.datetime]): The document request creation date
        document_details (Union[Unset, list['DR11Response200DataDocumentDetails']]): The document details
        document_number (Union[Unset, str]): The accounting document number
        document_upload_date (Union[Unset, datetime.datetime]): The last upload date of the accounting document
        due_date (Union[Unset, datetime.datetime]): The document due date
        entities (Union[Unset, DR11Response200DataEntities]):
        entity_date_created (Union[Unset, datetime.datetime]): The entity creation date, not applicable for
            entity_type=SHOP_BILLING_CYCLE_PURCHASE_ORDER
        entity_id (Union[Unset, str]): The entity id the document request relates to
        entity_type (Union[Unset, str]): The entity type the document request relates to
        id (Union[Unset, str]): The document request unique identifier
        initial_documents (Union[Unset, list['DR11Response200DataInitialDocuments']]): In the case of
            <code>CREDIT_NOTE</code> or reissued <code>INVOICE</code>, information about the initial accounting documents
        initial_payment_state (Union[Unset, str]): The document request payment state at the time when the document
            request was created
        issue_date (Union[Unset, datetime.datetime]): The document issue date
        issuer (Union[Unset, DR11Response200DataIssuer]):
        last_updated (Union[Unset, datetime.datetime]): The document request last update date
        payment (Union[Unset, DR11Response200DataPayment]):
        payment_destination (Union[Unset, DR11Response200DataPaymentDestination]):
        payment_terms (Union[Unset, DR11Response200DataPaymentTerms]):
        recipient (Union[Unset, DR11Response200DataRecipient]):
        state (Union[Unset, str]): The document request state
        taxes (Union[Unset, list['DR11Response200DataTaxes']]): Total amount of taxes aggregated per tax code and rate
        total_amount_excluding_taxes (Union[Unset, float]): The total document amount (excluding taxes)
        total_amount_including_taxes (Union[Unset, float]): The total document amount (including taxes)
        total_tax_amount (Union[Unset, float]): The total taxes amount of the document
        type_ (Union[Unset, str]): The accounting document type
    """

    currency_iso_code: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    document_details: Union[Unset, list["DR11Response200DataDocumentDetails"]] = UNSET
    document_number: Union[Unset, str] = UNSET
    document_upload_date: Union[Unset, datetime.datetime] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    entities: Union[Unset, "DR11Response200DataEntities"] = UNSET
    entity_date_created: Union[Unset, datetime.datetime] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    initial_documents: Union[Unset, list["DR11Response200DataInitialDocuments"]] = UNSET
    initial_payment_state: Union[Unset, str] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    issuer: Union[Unset, "DR11Response200DataIssuer"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    payment: Union[Unset, "DR11Response200DataPayment"] = UNSET
    payment_destination: Union[Unset, "DR11Response200DataPaymentDestination"] = UNSET
    payment_terms: Union[Unset, "DR11Response200DataPaymentTerms"] = UNSET
    recipient: Union[Unset, "DR11Response200DataRecipient"] = UNSET
    state: Union[Unset, str] = UNSET
    taxes: Union[Unset, list["DR11Response200DataTaxes"]] = UNSET
    total_amount_excluding_taxes: Union[Unset, float] = UNSET
    total_amount_including_taxes: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_iso_code = self.currency_iso_code

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        document_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.document_details, Unset):
            document_details = []
            for document_details_item_data in self.document_details:
                document_details_item = document_details_item_data.to_dict()
                document_details.append(document_details_item)

        document_number = self.document_number

        document_upload_date: Union[Unset, str] = UNSET
        if not isinstance(self.document_upload_date, Unset):
            document_upload_date = self.document_upload_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        entities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        entity_date_created: Union[Unset, str] = UNSET
        if not isinstance(self.entity_date_created, Unset):
            entity_date_created = self.entity_date_created.isoformat()

        entity_id = self.entity_id

        entity_type = self.entity_type

        id = self.id

        initial_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.initial_documents, Unset):
            initial_documents = []
            for initial_documents_item_data in self.initial_documents:
                initial_documents_item = initial_documents_item_data.to_dict()
                initial_documents.append(initial_documents_item)

        initial_payment_state = self.initial_payment_state

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        issuer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = self.issuer.to_dict()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        payment_destination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_destination, Unset):
            payment_destination = self.payment_destination.to_dict()

        payment_terms: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_terms, Unset):
            payment_terms = self.payment_terms.to_dict()

        recipient: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        state = self.state

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        total_amount_excluding_taxes = self.total_amount_excluding_taxes

        total_amount_including_taxes = self.total_amount_including_taxes

        total_tax_amount = self.total_tax_amount

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if document_details is not UNSET:
            field_dict["document_details"] = document_details
        if document_number is not UNSET:
            field_dict["document_number"] = document_number
        if document_upload_date is not UNSET:
            field_dict["document_upload_date"] = document_upload_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if entities is not UNSET:
            field_dict["entities"] = entities
        if entity_date_created is not UNSET:
            field_dict["entity_date_created"] = entity_date_created
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if id is not UNSET:
            field_dict["id"] = id
        if initial_documents is not UNSET:
            field_dict["initial_documents"] = initial_documents
        if initial_payment_state is not UNSET:
            field_dict["initial_payment_state"] = initial_payment_state
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if payment is not UNSET:
            field_dict["payment"] = payment
        if payment_destination is not UNSET:
            field_dict["payment_destination"] = payment_destination
        if payment_terms is not UNSET:
            field_dict["payment_terms"] = payment_terms
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if state is not UNSET:
            field_dict["state"] = state
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total_amount_excluding_taxes is not UNSET:
            field_dict["total_amount_excluding_taxes"] = total_amount_excluding_taxes
        if total_amount_including_taxes is not UNSET:
            field_dict["total_amount_including_taxes"] = total_amount_including_taxes
        if total_tax_amount is not UNSET:
            field_dict["total_tax_amount"] = total_tax_amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr11_response_200_data_document_details import DR11Response200DataDocumentDetails
        from ..models.dr11_response_200_data_entities import DR11Response200DataEntities
        from ..models.dr11_response_200_data_initial_documents import DR11Response200DataInitialDocuments
        from ..models.dr11_response_200_data_issuer import DR11Response200DataIssuer
        from ..models.dr11_response_200_data_payment import DR11Response200DataPayment
        from ..models.dr11_response_200_data_payment_destination import DR11Response200DataPaymentDestination
        from ..models.dr11_response_200_data_payment_terms import DR11Response200DataPaymentTerms
        from ..models.dr11_response_200_data_recipient import DR11Response200DataRecipient
        from ..models.dr11_response_200_data_taxes import DR11Response200DataTaxes

        d = dict(src_dict)
        currency_iso_code = d.pop("currency_iso_code", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        document_details = []
        _document_details = d.pop("document_details", UNSET)
        for document_details_item_data in _document_details or []:
            document_details_item = DR11Response200DataDocumentDetails.from_dict(document_details_item_data)

            document_details.append(document_details_item)

        document_number = d.pop("document_number", UNSET)

        _document_upload_date = d.pop("document_upload_date", UNSET)
        document_upload_date: Union[Unset, datetime.datetime]
        if isinstance(_document_upload_date, Unset):
            document_upload_date = UNSET
        else:
            document_upload_date = isoparse(_document_upload_date)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _entities = d.pop("entities", UNSET)
        entities: Union[Unset, DR11Response200DataEntities]
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = DR11Response200DataEntities.from_dict(_entities)

        _entity_date_created = d.pop("entity_date_created", UNSET)
        entity_date_created: Union[Unset, datetime.datetime]
        if isinstance(_entity_date_created, Unset):
            entity_date_created = UNSET
        else:
            entity_date_created = isoparse(_entity_date_created)

        entity_id = d.pop("entity_id", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        id = d.pop("id", UNSET)

        initial_documents = []
        _initial_documents = d.pop("initial_documents", UNSET)
        for initial_documents_item_data in _initial_documents or []:
            initial_documents_item = DR11Response200DataInitialDocuments.from_dict(initial_documents_item_data)

            initial_documents.append(initial_documents_item)

        initial_payment_state = d.pop("initial_payment_state", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        _issuer = d.pop("issuer", UNSET)
        issuer: Union[Unset, DR11Response200DataIssuer]
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = DR11Response200DataIssuer.from_dict(_issuer)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, DR11Response200DataPayment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = DR11Response200DataPayment.from_dict(_payment)

        _payment_destination = d.pop("payment_destination", UNSET)
        payment_destination: Union[Unset, DR11Response200DataPaymentDestination]
        if isinstance(_payment_destination, Unset):
            payment_destination = UNSET
        else:
            payment_destination = DR11Response200DataPaymentDestination.from_dict(_payment_destination)

        _payment_terms = d.pop("payment_terms", UNSET)
        payment_terms: Union[Unset, DR11Response200DataPaymentTerms]
        if isinstance(_payment_terms, Unset):
            payment_terms = UNSET
        else:
            payment_terms = DR11Response200DataPaymentTerms.from_dict(_payment_terms)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, DR11Response200DataRecipient]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = DR11Response200DataRecipient.from_dict(_recipient)

        state = d.pop("state", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = DR11Response200DataTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        total_amount_excluding_taxes = d.pop("total_amount_excluding_taxes", UNSET)

        total_amount_including_taxes = d.pop("total_amount_including_taxes", UNSET)

        total_tax_amount = d.pop("total_tax_amount", UNSET)

        type_ = d.pop("type", UNSET)

        dr11_response_200_data = cls(
            currency_iso_code=currency_iso_code,
            date_created=date_created,
            document_details=document_details,
            document_number=document_number,
            document_upload_date=document_upload_date,
            due_date=due_date,
            entities=entities,
            entity_date_created=entity_date_created,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            initial_documents=initial_documents,
            initial_payment_state=initial_payment_state,
            issue_date=issue_date,
            issuer=issuer,
            last_updated=last_updated,
            payment=payment,
            payment_destination=payment_destination,
            payment_terms=payment_terms,
            recipient=recipient,
            state=state,
            taxes=taxes,
            total_amount_excluding_taxes=total_amount_excluding_taxes,
            total_amount_including_taxes=total_amount_including_taxes,
            total_tax_amount=total_tax_amount,
            type_=type_,
        )

        dr11_response_200_data.additional_properties = d
        return dr11_response_200_data

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
