
- Хуки pytest
  - Примерное дерево хуков - https://github.com/pytest-dev/pytest/issues/3261#issuecomment-369740536
  - pytest_addoption - добавляем новые опции
  - pytest_configure - меняем что-нибудь в конфигурации
  - pytest_sessionstart - делаем что-нибудь перед стартом всех тестов
  - pytest_generate_tests - изменяем параметризацию тестов
  - pytest_collection_modifyitems - редактируем собранные тесты
  - pytest_runtestloop - хуки во время выполнения тестов
  - pytest_sessionfinish - все тесты завершились

- xdist
  - -n аргумент
  - фикстуры xdist
  - как себя ведут session scope фикстуры?
  - Как заставить session scope фикстуру выполниться один раз https://pytest-xdist.readthedocs.io/en/latest/how-to.html
