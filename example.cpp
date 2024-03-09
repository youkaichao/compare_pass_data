#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <map>
#include <iostream>

namespace py = pybind11;

class IntMap {
public:
    std::map<int64_t, int64_t> map;

    void insert(int64_t key, int64_t value) {
        map[key] = value;
    }
};

// void pass_data(std::map<int64_t, int64_t>& input_map) {
// // do nothing, just to test the argument passing time
// }

void pass_data(IntMap& input_obj) {
    std::map<int64_t, int64_t>& input_map = input_obj.map;
}

PYBIND11_MODULE(example, m) {
    m.def("pass_data", &pass_data, "A function that accepts a std::map<int64_t, int64_t>");
    py::class_<IntMap>(m, "IntMap")
        .def(py::init<>())
        .def("insert", &IntMap::insert);
}
