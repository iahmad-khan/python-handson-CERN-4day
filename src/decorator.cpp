// The C++ version is very limited in comparison to the Python one, in
// that you have to anticipate all the methods that you are going to
// add "dynamically" to your component AT COMPLIE TIME. When _I_ use
// the word "dynamic", I mean something considerably more dynamic than
// that; in Python you can add any methods at all, including ones that
// weren't even thought of when the interface of your component was
// written.

// Furthermore, because, in the C++ pattern, the decorations WRAP the
// original object (in C++ the object becomes an attribute of the
// decoration; in Python the decoration becomes an attribute of the
// object), decoration changes the identitiy of the object; existing
// references to the object do not pick up the decorations. Again,
// such limitations are absent in the Python version.

#include <iostream>

struct Component {
  virtual void bar() = 0;
};

class Decorator : public Component {
  Component* _component;
public:
  Decorator(Component* c): _component(c) {}
  void bar() {
    _component->bar();
  }
};

struct ZotDecorator : public Decorator {
  ZotDecorator(Component* c) :Decorator(c) {}
  void bar() {
    Decorator::bar();
    zot();
  }
  void zot() {
    std::cout << "This is the zot decoration" << std::endl;
  }
};

struct Foo : public Component {
  void bar() {
    std::cout << "This is Foo::bar's original behaviour" << std::endl;
  }
};
  

int main() {

  Foo* aFoo = new Foo;
  ZotDecorator* decoratedFoo = new ZotDecorator(aFoo);
  decoratedFoo->zot();

  return 0;
}

