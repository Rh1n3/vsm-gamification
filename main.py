import time

class ConductorProfile:
    def __init__(self, name):
        self.name = name
        self.competence_points = 0
        self.passenger_loyalty = 50  # Старт с середины (0-100)
        self.safety_rating = 50      # Старт с середины (0-100)
        self.achievements = []

    def update_stats(self, loyalty_delta, safety_delta, points_delta):
        self.passenger_loyalty = max(0, min(100, self.passenger_loyalty + loyalty_delta))
        self.safety_rating = max(0, min(100, self.safety_rating + safety_delta))
        self.competence_points += points_delta
        self.check_achievements()

    def check_achievements(self):
        if self.safety_rating >= 90 and "Страж безопасности" not in self.achievements:
            self.achievements.append("Страж безопасности")
        if self.passenger_loyalty >= 90 and "Любимец пассажиров" not in self.achievements:
            self.achievements.append("Любимец пассажиров")

# Пример структуры сценария (Граф/Древо решений)
scenarios = {
    "start": {
        "text": "Пассажир бизнес-класса громко скандалит из-за того, что его кресло не раскладывается. Ваши действия?",
        "options": [
            {
                "text": "Спокойно извиниться, предложить перезагрузить модуль кресла и принести экспресс-комплимент (чай/кофе).",
                "loyalty_delta": 20, "safety_delta": 0, "points_delta": 15,
                "next_step": "success_resolved"
            },
            {
                "text": "Строго заявить, что поезд в движении, и ему придется подождать техников на конечной станции.",
                "loyalty_delta": -25, "safety_delta": -5, "points_delta": 0,
                "next_step": "escalation"
            },
            {
                "text": "Немедленно предложить пересесть на свободное место в этом же или соседнем вагоне обслуживания.",
                "loyalty_delta": 15, "safety_delta": 0, "points_delta": 10,
                "next_step": "success_resolved"
            }
        ]
    },
    "escalation": {
        "text": "Пассажир начинает переходить на личности и мешает остальным. Время на решение — 5 секунд!",
        "options": [
            {
                "text": "Вызвать начальника поезда и сотрудника транспортной безопасности для фиксации правонарушения.",
                "loyalty_delta": -5, "safety_delta": 25, "points_delta": 20,
                "next_step": "end_case"
            },
            {
                "text": "Вступить в спор и начать доказывать, что поломка произошла не по вашей вине.",
                "loyalty_delta": -40, "safety_delta": -20, "points_delta": -10,
                "next_step": "end_case"
            }
        ]
    },
    "success_resolved": {
        "text": "Конфликт исчерпан. Пассажир оставил позитивный отзыв в анкете качества. Кейс успешно пройден!",
        "options": []
    },
    "end_case": {
        "text": "Разбор инцидента завершен. Данные отправлены в личный кабинет для анализа инструктором.",
        "options": []
    }
}
