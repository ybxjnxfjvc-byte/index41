# Supply-chain notes

Dependency inventory выполняется локально без запросов к внешней сети. Он показывает состав, но не заменяет полноценный vulnerability scanner. Для реального проекта дальше нужны lockfiles, проверка происхождения пакетов, pinning критичных CI actions и обновление зависимостей через review.
