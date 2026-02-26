from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнения.
    """
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на частичное обновление упражнения.
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class Exercises(TypedDict):
    """
    Описание структуры запроса на частичное обновление упражнения.
    """
    id: str | None
    title: str | None
    courseId: str | None
    maxScope: int | None
    minScope: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class GetExercisesResponseDict(TypedDict):
    exercises: Exercises


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь CreateExercisesRequestDict,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь UpdateExercisesRequestDict.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises{exercise_id}")

    def get_exercise(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения упражнения.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict
        """
        response = self.get_exercise_api(query)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> Exercises:
        """
        Метод создания упражнения.

        :param request: Словарь CreateExercisesRequestDict,
        :return: Ответ от сервера в виде объекта Exercises
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> GetExercisesResponseDict:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь UpdateExercisesRequestDict.
        :return: Ответ от сервера в виде объектаGetExercisesResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
