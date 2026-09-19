from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from src.lagerhållning.lagerhållning import StockItem, Stock
from src.lagerhållning.lagerhållning import Stock


@given(u'att jag har 5 st gurkor')
def step_impl(context):
    context.StockItem = StockItem("gurkor", 5)
    context.stock = Stock()


@when(u'jag lägger till dem i lagret')
def step_impl(context):
    context.stock.add_product(context.StockItem)


@then(u'lagret fylls med 5 st gurkor')
def step_impl(context):
    assert context.StockItem in context.stock.items
