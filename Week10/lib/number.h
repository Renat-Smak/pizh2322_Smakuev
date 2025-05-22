#pragma once
#include <iostream>
#include <cstring> // для работы с C-строками

// Структура для большого числа
struct uint2022_t {
    // Массив для хранения разрядов числа
    uint32_t data[10]; // пусть будет максимум 10 элементов (для 320 бит)
    int size;           // количество "разрядов"

    // Конструктор по умолчанию
    uint2022_t() : size(0) {
        memset(data, 0, sizeof(data)); // обнуляем массив
    }
};

// Функция для конвертации из uint32_t в uint2022_t
uint2022_t from_uint(uint32_t i);

// Функция для конвертации из строки в uint2022_t
uint2022_t from_string(const char* buff);

// Операторы для сложения, вычитания, умножения и деления
uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs);

// Операторы для сравнения
bool operator==(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator<(const uint2022_t& lhs, const uint2022_t& rhs);


// Оператор для вывода в консоль
std::ostream& operator<<(std::ostream& stream, const uint2022_t& value);
