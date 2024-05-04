from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000/2-index.html"

def test_cube(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")
    input.fill("5")

    page.get_by_role(
        "button", name="cube"
    ).click()

    result = page.locator("p#result")
    expect(result).to_contain_text("125")

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    page.get_by_role(
        "button", name="cube"
    ).click()

    result = page.locator("p#result")

    expect(result).to_have_text(
        "Enter something!"
    )
    