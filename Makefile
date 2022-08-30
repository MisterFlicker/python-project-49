install: # создание или обновление виртуального окружения
	poetry install

brain-games: # запуск команды brain-games
	poetry run brain-games

build: # выполнение сборки пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: # установка пакета в систему
	python3 -m pip install --user dist/*.whl

lint: # проверка brain_games по линтеру flake8
	poetry run flake8 brain_games
