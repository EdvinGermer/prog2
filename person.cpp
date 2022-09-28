#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fib();
		void set(int);
	private:
		int fib_aux(int);
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(){ 
	return fib_aux(age);
	}


int Person::fib_aux(int age){ 
	if(age<=1) {
      return(age);
   }else {
      return(fib_aux(age-1)+fib_aux(age-2));
   }
	}


 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}