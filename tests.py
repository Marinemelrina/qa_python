import pytest
from test_data import BOOKS_NAMES_AND_GENRE
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

    @pytest.mark.parametrize(
        "name", ["", "Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции"]
    )
    def test_add_new_book_empty_name_and_more_than_40_characters(self, name, books_collector):
        books_collector.add_new_book(name)
        assert name not in books_collector.get_books_genre()

    @pytest.mark.parametrize(
        "genre_and_expected", [["Фантастика", "Фантастика"], ["Трагедия", ""]]
    )
    def test_set_book_genre_1_set_and_1_not_set(
        self, books_collector, genre_and_expected
    ):
        genre, expected_result = genre_and_expected
        name = "Гордость и предубеждение и зомби"

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        genre_added = books_collector.get_book_genre(name)

        assert genre_added == expected_result

    def test_get_book_genre_return_genre_by_name(self, books_collector):
        name = "Гордость и предубеждение и зомби"
        books_collector.add_new_book(name)

        assert books_collector.get_book_genre(name) == ""

    def test_get_books_with_specific_genre_returned_5(self, books_collector, add_books):
        genre = "Фантастика"
        for book in books_collector.get_books_genre():
            books_collector.set_book_genre(book, genre)

        returned_books_list = books_collector.get_books_with_specific_genre(
            "Фантастика"
        )

        assert len(returned_books_list) == 5

    def test_get_books_genre_dict_books_genre_returned(
        self, books_collector, add_books, set_genre
    ):
        returned_books_genre_dict = books_collector.get_books_genre()
        expected_books_genre_dict = BOOKS_NAMES_AND_GENRE

        assert returned_books_genre_dict == expected_books_genre_dict

    def test_get_books_for_children_return_non_rating_books(
        self, books_collector, add_books, set_genre
    ):
        expected_books = [
            "Путешествия Гулливера",
            "Ледниковый период",
            "Дневник Бриджет Джонс",
        ]
        returned_books = books_collector.get_books_for_children()

        assert returned_books == expected_books

    def test_add_book_in_favorites_not_added_book(self, books_collector):
        books_collector.add_book_in_favorites("Гордость и предубеждение и зомби")

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 0

    def test_add_book_in_favorites_not_added_in_favorites_if_name_is_name(
        self, books_collector
    ):
        books_collector.add_new_book("Внутри Убийцы")

        books_collector.add_book_in_favorites("Внутри Убийцы")
        books_collector.add_book_in_favorites("Внутри Убийцы")

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 1

    def test_delete_book_from_favorites_not_deleted_book_with_invalid_name(
        self, books_collector
    ):
        books_collector.add_new_book("Гордость и предубеждение и зомби")

        books_collector.add_book_in_favorites("Гордость и предубеждение и зомби")
        books_collector.delete_book_from_favorites("Путешесвия Гулливера")

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 1




