def pytest_configure(config):
    config.addinivalue_line(
        "markers", "allure_label(name): добавить кастомный label для Allure отчёта"
    )
