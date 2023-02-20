from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.boundary import Boundary
    from ..models.datapackage import Datapackage
    from ..models.processor import Processor


T = TypeVar("T", bound="Package")


@attr.s(auto_attribs=True)
class Package:
    """Detailed information about a package

    Attributes:
        boundary_name (str):
        uri (str):
        boundary (Boundary): Complete boundary information
        processors (List['Processor']):
        datapackage (Datapackage):
    """

    boundary_name: str
    uri: str
    boundary: "Boundary"
    processors: List["Processor"]
    datapackage: "Datapackage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boundary_name = self.boundary_name
        uri = self.uri
        boundary = self.boundary.to_dict()

        processors = []
        for processors_item_data in self.processors:
            processors_item = processors_item_data.to_dict()

            processors.append(processors_item)

        datapackage = self.datapackage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boundary_name": boundary_name,
                "uri": uri,
                "boundary": boundary,
                "processors": processors,
                "datapackage": datapackage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.boundary import Boundary
        from ..models.datapackage import Datapackage
        from ..models.processor import Processor

        d = src_dict.copy()
        boundary_name = d.pop("boundary_name")

        uri = d.pop("uri")

        boundary = Boundary.from_dict(d.pop("boundary"))

        processors = []
        _processors = d.pop("processors")
        for processors_item_data in _processors:
            processors_item = Processor.from_dict(processors_item_data)

            processors.append(processors_item)

        datapackage = Datapackage.from_dict(d.pop("datapackage"))

        package = cls(
            boundary_name=boundary_name,
            uri=uri,
            boundary=boundary,
            processors=processors,
            datapackage=datapackage,
        )

        package.additional_properties = d
        return package

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
