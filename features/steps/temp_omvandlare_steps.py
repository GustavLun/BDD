from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError

from behave.api.pending_step import StepNotImplementedError


@given(u'att jag har temperaturen 32°F')
def step_impl(context):
    context.f = 32


@when(u'jag omvandlar det')
def step_impl(context):
    if hasattr(context, 'f'):
        context.result = ((context.f - 32 )/ 1.8)
    elif hasattr(context, 'c'):
        context.result = ((context.c * 1.8 ) + 32)


@then(u'ska resultatet vara 0°C')
def step_impl(context):
    assert context.result == 0


@given(u'att jag har temperaturen 100°C')
def step_impl(context):
    context.c = 100


@then(u'ska resultatet vara 212°F')
def step_impl(context):
    assert context.result == 212
