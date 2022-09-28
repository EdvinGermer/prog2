#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fib();  // Public method
		void set(int);
	private:
		int fib_aux(int);  // Private method
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(){   // Publicfib method that calls auxilary recursive fib method
	return fib_aux(age);
	}


int Person::fib_aux(int age){    // Private fib method that calculates and returns fib value
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
	int Person_fib(Person* person) {return person->fib();}    // Added fib method to C bridging code
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}