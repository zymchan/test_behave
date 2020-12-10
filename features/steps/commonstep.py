import time

from behave import *

use_step_matcher("re")


@given("get current time as <time>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    return str(time.time())[0: 13]
