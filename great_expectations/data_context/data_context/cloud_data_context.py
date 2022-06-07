from typing import Mapping, Optional, Union

from great_expectations.data_context.data_context.abstract_data_context import (
    AbstractDataContext,
)
from great_expectations.data_context.types.base import DataContextConfig, GeCloudConfig


class CloudDataContext(AbstractDataContext):
    """
    Subclass of AbstractDataContext that contains functionality necessary to hydrate state from cloud
    """

    def __init__(
        self,
        project_config: Union[DataContextConfig, Mapping],
        runtime_environment: Optional[dict] = None,
        ge_cloud_mode: bool = False,
        ge_cloud_config: Optional[GeCloudConfig] = None,
    ) -> None:

        self._ge_cloud_mode = ge_cloud_mode
        self._ge_cloud_config = ge_cloud_config

        # config overrides with cloud configs
        self._project_config = project_config
        # TODO: this is actually unnecessary technically speaking. see if it can actually be removed
        super()._apply_global_config_overrides()
        super().__init__(
            project_config=project_config, runtime_environment=runtime_environment
        )