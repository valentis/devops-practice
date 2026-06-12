import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:3000"

def test_signup_and_login(page: Page):
    page.goto(f"{BASE_URL}/signup")
    page.fill("[name=email]", "test@example.com")
    page.fill("[name=password]", "SecurePass123!")
    page.click("button[type=submit]")
    expect(page).to_have_url(f"{BASE_URL}/dashboard")

def test_login_invalid_credentials(page: Page):
    page.goto(f"{BASE_URL}/login")
    page.fill("[name=email]", "wrong@example.com")
    page.fill("[name=password]", "wrongpass")
    page.click("button[type=submit]")
    expect(page.locator(".error-message")).to_be_visible()
