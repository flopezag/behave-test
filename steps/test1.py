from behave import *

use_step_matcher("re")


@given('I set the API at the url')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I set the API at the url "http//: :"')


@given("I Set POST posts api endpoint")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I Set POST posts api endpoint')


@when('I Set HEADER param request content type as "application/json\."')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I Set HEADER param request content type as "application/json."')


@step("Set request Body")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Set request Body')


@step("Send a POST HTTP request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Send a POST HTTP request')


@then("I receive valid HTTP response code 201")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I receive valid HTTP response code 201')


@step('Response BODY "POST" is non-empty\.')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Response BODY "POST" is non-empty.')


@given('I Set GET posts api endpoint ""')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I Set GET posts api endpoint ""')


@step("Send GET HTTP request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Send GET HTTP request')


@then('I receive valid HTTP response code 200 for "GET\."')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I receive valid HTTP response code 200 for "GET."')


@step('Response BODY "GET" is non-empty')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Response BODY "GET" is non-empty')


@given('I Set PUT posts api endpoint for ""')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I Set PUT posts api endpoint for ""')


@when("I Set Update request Body")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I Set Update request Body')


@step("Send PUT HTTP request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Send PUT HTTP request')


@given('I Set DELETE posts api endpoint for ""')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I Set DELETE posts api endpoint for ""')


@when("I Send DELETE HTTP request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I Send DELETE HTTP request')