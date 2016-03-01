#include <iostream>

struct FooBarState {
  virtual void hello() = 0;
};

struct FooState : FooBarState {
  void hello() {
    std::cout << "This is foo going about its business" << std::endl;
  }
};

struct BarState : FooBarState {
  void hello() {
    std::cout << "This is bar going about its business" << std::endl;
  }
};

class FooBar {
  FooBarState *_state; 
public:
  FooBar(FooBarState* initial_state):_state(initial_state) {}
  void ChangeState(FooBarState* new_state) {
    _state = new_state;
  }
  void hello() {
    _state->hello();
  }
};

int main() {

  FooState aFooState;
  BarState aBarState;

  FooBar instance(&aFooState);
  instance.hello();
  instance.ChangeState(&aBarState);
  instance.hello();

  return 0;

}

