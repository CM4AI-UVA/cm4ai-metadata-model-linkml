# Auto generated from cm4ai_metadata_model_linkml.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-05T12:42:09
# Schema: cm4ai-metadata-model-linkml
#
# id: https://w3id.org/cm4ai-uva/cm4ai-metadata-model-linkml
# description: Cell maps for AI metadata model in LinkML
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
CM4AI_METADATA_MODEL_LINKML = CurieNamespace('cm4ai_metadata_model_linkml', 'https://w3id.org/cm4ai-uva/cm4ai-metadata-model-linkml/')
EVI = CurieNamespace('evi', 'http://example.org/UNKNOWN/evi/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CM4AI_METADATA_MODEL_LINKML


# Types

# Class references
class DatasetId(extended_str):
    pass


class SoftwareId(extended_str):
    pass


class ComputationId(extended_str):
    pass


@dataclass
class Dataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Dataset
    class_class_curie: ClassVar[str] = "cm4ai_metadata_model_linkml:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Dataset

    id: Union[str, DatasetId] = None
    name: str = None
    type: str = None
    author: str = None
    datePublished: Union[str, XSDDate] = None
    version: str = None
    description: str = None
    format: str = None
    contentUrl: Union[str, URIorCURIE] = None
    context: Optional[str] = None
    keywords: Optional[str] = None
    associatedPublication: Optional[str] = None
    additionalDocumentation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    dataSchema: Optional[str] = None
    generatedBy: Optional[Union[str, List[str]]] = empty_list()
    derivedFrom: Optional[Union[str, List[str]]] = empty_list()
    usedBy: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.author):
            self.MissingRequiredField("author")
        if not isinstance(self.author, str):
            self.author = str(self.author)

        if self._is_empty(self.datePublished):
            self.MissingRequiredField("datePublished")
        if not isinstance(self.datePublished, XSDDate):
            self.datePublished = XSDDate(self.datePublished)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.contentUrl):
            self.MissingRequiredField("contentUrl")
        if not isinstance(self.contentUrl, URIorCURIE):
            self.contentUrl = URIorCURIE(self.contentUrl)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.associatedPublication is not None and not isinstance(self.associatedPublication, str):
            self.associatedPublication = str(self.associatedPublication)

        if not isinstance(self.additionalDocumentation, list):
            self.additionalDocumentation = [self.additionalDocumentation] if self.additionalDocumentation is not None else []
        self.additionalDocumentation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.additionalDocumentation]

        if self.dataSchema is not None and not isinstance(self.dataSchema, str):
            self.dataSchema = str(self.dataSchema)

        if not isinstance(self.generatedBy, list):
            self.generatedBy = [self.generatedBy] if self.generatedBy is not None else []
        self.generatedBy = [v if isinstance(v, str) else str(v) for v in self.generatedBy]

        if not isinstance(self.derivedFrom, list):
            self.derivedFrom = [self.derivedFrom] if self.derivedFrom is not None else []
        self.derivedFrom = [v if isinstance(v, str) else str(v) for v in self.derivedFrom]

        if not isinstance(self.usedBy, list):
            self.usedBy = [self.usedBy] if self.usedBy is not None else []
        self.usedBy = [v if isinstance(v, str) else str(v) for v in self.usedBy]

        super().__post_init__(**kwargs)


@dataclass
class Software(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Software
    class_class_curie: ClassVar[str] = "cm4ai_metadata_model_linkml:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Software

    id: Union[str, SoftwareId] = None
    name: str = None
    type: str = None
    author: str = None
    dateModified: Union[str, XSDDate] = None
    version: str = None
    description: str = None
    format: str = None
    contentUrl: Union[str, URIorCURIE] = None
    context: Optional[str] = None
    keywords: Optional[str] = None
    associatedPublication: Optional[str] = None
    additionalDocumentation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    usedByComputation: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.author):
            self.MissingRequiredField("author")
        if not isinstance(self.author, str):
            self.author = str(self.author)

        if self._is_empty(self.dateModified):
            self.MissingRequiredField("dateModified")
        if not isinstance(self.dateModified, XSDDate):
            self.dateModified = XSDDate(self.dateModified)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.contentUrl):
            self.MissingRequiredField("contentUrl")
        if not isinstance(self.contentUrl, URIorCURIE):
            self.contentUrl = URIorCURIE(self.contentUrl)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.associatedPublication is not None and not isinstance(self.associatedPublication, str):
            self.associatedPublication = str(self.associatedPublication)

        if not isinstance(self.additionalDocumentation, list):
            self.additionalDocumentation = [self.additionalDocumentation] if self.additionalDocumentation is not None else []
        self.additionalDocumentation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.additionalDocumentation]

        if not isinstance(self.usedByComputation, list):
            self.usedByComputation = [self.usedByComputation] if self.usedByComputation is not None else []
        self.usedByComputation = [v if isinstance(v, str) else str(v) for v in self.usedByComputation]

        super().__post_init__(**kwargs)


@dataclass
class Computation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Computation
    class_class_curie: ClassVar[str] = "cm4ai_metadata_model_linkml:Computation"
    class_name: ClassVar[str] = "Computation"
    class_model_uri: ClassVar[URIRef] = CM4AI_METADATA_MODEL_LINKML.Computation

    id: Union[str, ComputationId] = None
    name: str = None
    type: str = None
    runBy: str = None
    dateCreated: Union[str, XSDDate] = None
    description: str = None
    usedSoftware: Union[str, List[str]] = None
    context: Optional[str] = None
    keywords: Optional[str] = None
    associatedPublication: Optional[str] = None
    additionalDocumentation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    calledBy: Optional[str] = None
    usedDataset: Optional[Union[str, List[str]]] = empty_list()
    generated: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationId):
            self.id = ComputationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.runBy):
            self.MissingRequiredField("runBy")
        if not isinstance(self.runBy, str):
            self.runBy = str(self.runBy)

        if self._is_empty(self.dateCreated):
            self.MissingRequiredField("dateCreated")
        if not isinstance(self.dateCreated, XSDDate):
            self.dateCreated = XSDDate(self.dateCreated)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.usedSoftware):
            self.MissingRequiredField("usedSoftware")
        if not isinstance(self.usedSoftware, list):
            self.usedSoftware = [self.usedSoftware] if self.usedSoftware is not None else []
        self.usedSoftware = [v if isinstance(v, str) else str(v) for v in self.usedSoftware]

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.associatedPublication is not None and not isinstance(self.associatedPublication, str):
            self.associatedPublication = str(self.associatedPublication)

        if not isinstance(self.additionalDocumentation, list):
            self.additionalDocumentation = [self.additionalDocumentation] if self.additionalDocumentation is not None else []
        self.additionalDocumentation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.additionalDocumentation]

        if self.calledBy is not None and not isinstance(self.calledBy, str):
            self.calledBy = str(self.calledBy)

        if not isinstance(self.usedDataset, list):
            self.usedDataset = [self.usedDataset] if self.usedDataset is not None else []
        self.usedDataset = [v if isinstance(v, str) else str(v) for v in self.usedDataset]

        if not isinstance(self.generated, list):
            self.generated = [self.generated] if self.generated is not None else []
        self.generated = [v if isinstance(v, str) else str(v) for v in self.generated]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.context = Slot(uri=CM4AI_METADATA_MODEL_LINKML.context, name="context", curie=CM4AI_METADATA_MODEL_LINKML.curie('context'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.context, domain=None, range=Optional[str])

slots.id = Slot(uri=EVI.identifier, name="id", curie=EVI.curie('identifier'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.name, domain=None, range=str)

slots.type = Slot(uri=SCHEMA.Dataset, name="type", curie=SCHEMA.curie('Dataset'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.type, domain=None, range=str)

slots.keywords = Slot(uri=SCHEMA.keywords, name="keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.keywords, domain=None, range=Optional[str])

slots.author = Slot(uri=CM4AI_METADATA_MODEL_LINKML.author, name="author", curie=CM4AI_METADATA_MODEL_LINKML.curie('author'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.author, domain=None, range=str)

slots.datePublished = Slot(uri=SCHEMA.datePublished, name="datePublished", curie=SCHEMA.curie('datePublished'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.datePublished, domain=None, range=Union[str, XSDDate])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.version, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.description, domain=None, range=str)

slots.associatedPublication = Slot(uri=SCHEMA.citation, name="associatedPublication", curie=SCHEMA.curie('citation'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.associatedPublication, domain=None, range=Optional[str])

slots.additionalDocumentation = Slot(uri=RDFS.seeAlso, name="additionalDocumentation", curie=RDFS.curie('seeAlso'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.additionalDocumentation, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.format = Slot(uri=SCHEMA.encodingFormat, name="format", curie=SCHEMA.curie('encodingFormat'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.format, domain=None, range=str)

slots.dataSchema = Slot(uri=CM4AI_METADATA_MODEL_LINKML.dataSchema, name="dataSchema", curie=CM4AI_METADATA_MODEL_LINKML.curie('dataSchema'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.dataSchema, domain=None, range=Optional[str])

slots.generatedBy = Slot(uri=EVI.generatedBy, name="generatedBy", curie=EVI.curie('generatedBy'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.generatedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.derivedFrom = Slot(uri=EVI.derivedFrom, name="derivedFrom", curie=EVI.curie('derivedFrom'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.derivedFrom, domain=None, range=Optional[Union[str, List[str]]])

slots.usedBy = Slot(uri=EVI.usedBy, name="usedBy", curie=EVI.curie('usedBy'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.usedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.contentUrl = Slot(uri=SCHEMA.contentUrl, name="contentUrl", curie=SCHEMA.curie('contentUrl'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.contentUrl, domain=None, range=Union[str, URIorCURIE])

slots.dateModified = Slot(uri=SCHEMA.dateModified, name="dateModified", curie=SCHEMA.curie('dateModified'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.dateModified, domain=None, range=Union[str, XSDDate])

slots.usedByComputation = Slot(uri=EVI.sotwareUsedBy, name="usedByComputation", curie=EVI.curie('sotwareUsedBy'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.usedByComputation, domain=None, range=Optional[Union[str, List[str]]])

slots.runBy = Slot(uri=CM4AI_METADATA_MODEL_LINKML.runBy, name="runBy", curie=CM4AI_METADATA_MODEL_LINKML.curie('runBy'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.runBy, domain=None, range=str)

slots.dateCreated = Slot(uri=SCHEMA.dateCreated, name="dateCreated", curie=SCHEMA.curie('dateCreated'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.dateCreated, domain=None, range=Union[str, XSDDate])

slots.usedSoftware = Slot(uri=EVI.usedSoftware, name="usedSoftware", curie=EVI.curie('usedSoftware'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.usedSoftware, domain=None, range=Union[str, List[str]])

slots.calledBy = Slot(uri=EVI.calledBy, name="calledBy", curie=EVI.curie('calledBy'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.calledBy, domain=None, range=Optional[str])

slots.usedDataset = Slot(uri=EVI.usedDataset, name="usedDataset", curie=EVI.curie('usedDataset'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.usedDataset, domain=None, range=Optional[Union[str, List[str]]])

slots.generated = Slot(uri=EVI.generated, name="generated", curie=EVI.curie('generated'),
                   model_uri=CM4AI_METADATA_MODEL_LINKML.generated, domain=None, range=Optional[Union[str, List[str]]])