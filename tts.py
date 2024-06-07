# Синтез речи

from speechkit import model_repository, configure_credentials, creds
import config


def synthesize(export_path, text):

    API_KEY = config.YANDEX_API_KEY

    # Аутентификация через API-ключ.
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key=API_KEY
        )
    )

    model = model_repository.synthesis_model()

    # Задайте настройки синтеза.
    model.voice = 'jane'
    model.role = 'good'

    # Синтез речи и создание аудио с результатом.
    result = model.synthesize(text, raw_format=False)
    result.export(f'{export_path}.wav', 'wav')


if __name__ == '__main__':
    synthesize()