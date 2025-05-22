#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cctype>

class WordCounter {
private:
    struct FileStats {
        std::string filename;
        size_t lines;
        size_t words;
        size_t bytes;
        size_t chars;
    };

    bool count_lines = false;
    bool count_words = false;
    bool count_bytes = false;
    bool count_chars = false;
    bool show_all = true;
    std::vector<std::string> filenames;

public:
    WordCounter(int argc, char** argv) {
        parseArguments(argc, argv);
    }

    void run() {
        if (filenames.empty()) {
            std::cerr << "Ошибка: Не указаны файлы для анализа\n";
            return;
        }

        for (const auto& filename : filenames) {
            FileStats stats = processFile(filename);
            printStats(stats);
        }
    }

private:
    void parseArguments(int argc, char** argv) {
        for (int i = 1; i < argc; ++i) {
            std::string arg = argv[i];

            if (arg[0] == '-') {
                show_all = false;
                if (arg == "--lines" || arg == "-l") {
                    count_lines = true;
                }
                else if (arg == "--words" || arg == "-w") {
                    count_words = true;
                }
                else if (arg == "--bytes" || arg == "-c") {
                    count_bytes = true;
                }
                else if (arg == "--chars" || arg == "-m") {
                    count_chars = true;
                }
                else if (arg.size() > 1 && arg[0] == '-' && arg[1] != '-') {
                    for (size_t j = 1; j < arg.size(); ++j) {
                        switch (arg[j]) {
                        case 'l': count_lines = true; break;
                        case 'w': count_words = true; break;
                        case 'c': count_bytes = true; break;
                        case 'm': count_chars = true; break;
                        default:
                            std::cerr << "Ошибка: Неизвестная опция -" << arg[j] << "\n";
                        }
                    }
                }
            }
            else {
                filenames.push_back(arg);
            }
        }

        if (show_all) {
            count_lines = count_words = count_bytes = count_chars = true;
        }
    }

    FileStats processFile(const std::string& filename) {
        std::ifstream file(filename, std::ios::binary);
        if (!file) {
            std::cerr << "Ошибка: Не удалось открыть файл " << filename << "\n";
            return { filename, 0, 0, 0, 0 };
        }

        FileStats stats{ filename, 0, 0, 0, 0 };
        std::string line;
        bool in_word = false;

        file.seekg(0, std::ios::end);
        stats.bytes = file.tellg();
        file.seekg(0, std::ios::beg);

        while (std::getline(file, line)) {
            stats.lines++;

            for (char c : line) {
                if (std::isalpha(static_cast<unsigned char>(c))) {
                    stats.chars++;
                }

                if (std::isspace(static_cast<unsigned char>(c))) {
                    if (in_word) {
                        stats.words++;
                        in_word = false;
                    }
                }
                else {
                    in_word = true;
                }
            }

            if (in_word) {
                stats.words++;
                in_word = false;
            }
        }

        return stats;
    }

    void printStats(const FileStats& stats) {
        std::cout << "File analysis: " << stats.filename << "\n";

        if (count_lines) {
            std::cout << "• Lines: " << stats.lines << "\n";
        }
        if (count_words) {
            std::cout << "• Words: " << stats.words << "\n";
        }
        if (count_bytes) {
            std::cout << "• Bytes: " << stats.bytes << "\n";
        }
        if (count_chars) {
            std::cout << "• Letters: " << stats.chars << "\n";
        }

        std::cout << "----------------------------\n";
    }
};

int main(int argc, char** argv) {
    WordCounter wordCounter(argc, argv);
    wordCounter.run();
    return 0;
}
