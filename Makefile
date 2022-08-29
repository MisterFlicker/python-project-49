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
