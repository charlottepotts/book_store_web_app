from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http:/127.0.0.1:5001/team")
    h1 = page.locator('h1')
    expect(h1).to_have_text("Team")

def test_has_list_of_team(page:Page):
    page.goto("http://127.0.0.1:5001/team")
    team = page.locator('li')
    expected_members = [
        'Miffy',
        'Peter',
        'Bugs',
        'Thumper'
    ]
    actual_members = team.all_inner_texts()
    assert actual_members == expected_members