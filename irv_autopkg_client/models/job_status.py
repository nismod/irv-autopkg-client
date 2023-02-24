from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_progress import JobProgress
    from ..models.job_result import JobResult


T = TypeVar("T", bound="JobStatus")


@attr.s(auto_attribs=True)
class JobStatus:
    """Status of a Submitted Job

    Attributes:
        job_id (str):
        processor_name (str):
        job_status (str):
        job_progress (Union[Unset, JobProgress]): Specifics about the progress of an individual Processors Job
        job_result (Union[Unset, JobResult]):
    """

    job_id: str
    processor_name: str
    job_status: str
    job_progress: Union[Unset, "JobProgress"] = UNSET
    job_result: Union[Unset, "JobResult"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        processor_name = self.processor_name
        job_status = self.job_status
        job_progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_progress, Unset):
            job_progress = self.job_progress.to_dict()

        job_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_result, Unset):
            job_result = self.job_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "processor_name": processor_name,
                "job_status": job_status,
            }
        )
        if job_progress is not UNSET:
            field_dict["job_progress"] = job_progress
        if job_result is not UNSET:
            field_dict["job_result"] = job_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_progress import JobProgress
        from ..models.job_result import JobResult

        d = src_dict.copy()
        job_id = d.pop("job_id")

        processor_name = d.pop("processor_name")

        job_status = d.pop("job_status")

        _job_progress = d.pop("job_progress", UNSET)
        job_progress: Union[Unset, JobProgress]
        if isinstance(_job_progress, Unset):
            job_progress = UNSET
        else:
            job_progress = JobProgress.from_dict(_job_progress)

        _job_result = d.pop("job_result", UNSET)
        job_result: Union[Unset, JobResult]
        if isinstance(_job_result, Unset):
            job_result = UNSET
        else:
            job_result = JobResult.from_dict(_job_result)

        job_status = cls(
            job_id=job_id,
            processor_name=processor_name,
            job_status=job_status,
            job_progress=job_progress,
            job_result=job_result,
        )

        job_status.additional_properties = d
        return job_status

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
