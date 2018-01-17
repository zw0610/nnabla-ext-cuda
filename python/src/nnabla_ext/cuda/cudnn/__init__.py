# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import nnabla
from . import init

from nnabla.variable import Context
from ._version import (
    __version__,
    __author__,
    __email__
)

from nnabla_ext.cuda import (
    clear_memory_cache,
    array_classes,
    device_synchronize,
    get_device_count,
    get_devices,
    synchronize,
)


def context(device_id=0, *kw):
    """CUDNN context"""
    from nnabla_ext.cuda import array_classes
    return Context(['cudnn:float', 'cuda:float', 'cpu:float'],
                   array_classes()[0], device_id=str(device_id))
