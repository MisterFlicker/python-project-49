install: # создание или обновление виртуального окружения
	poetry install

brain-games: # запуск команды brain-games
	poetry run brain-games

brain-even: # запуск команды brain-even
	poetry run brain-even

brain-calc: # запуск команды brain-calc
	poetry run brain-calc

brain-gcd: # запуск команды brain-gcd
	poetry run brain-gcd

brain-progression: # запуск команды brain-progression
	poetry run brain-progression

brain-prime: # запуск команды brain-prime
	poetry run brain-prime

build: # выполнение сборки пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: # установка пакета в систему
	pip install --user --force-reinstall dist/*.whl

lint: # проверка brain_games по линтеру flake8
	poetry run flake8 brain_games
