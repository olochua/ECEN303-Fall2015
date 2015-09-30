#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

// random generator
int ngrandom (int i) { return rand() % i; }

int main() {
  srand ( unsigned ( std::time(NULL) ) );

  // initialize vector with student names.
  vector<string> ecen303names
  ecen303names.push_back("George Anthony");
  ecen303names.push_back("Allison Ruth Badgett");
  ecen303names.push_back("Bailey Katherine Barksdale");
  ecen303names.push_back("Logan Allen Barnard");
  ecen303names.push_back("Kaitlin Le'Ann Basham");
  ecen303names.push_back("Philip Bowie");
  ecen303names.push_back("Kevin Bradshaw");
  ecen303names.push_back("Jui Yen Chua");
  ecen303names.push_back("Phillip Conor Cryer");
  ecen303names.push_back("Stephanie Demco");
  ecen303names.push_back("Pablo Dominguez");
  ecen303names.push_back("Andrew Douglass");
  ecen303names.push_back("Isach Duka");
  ecen303names.push_back("David Fawcett");
  ecen303names.push_back("Morgan Glen Frakes");
  ecen303names.push_back("Alexander Garcia");
  ecen303names.push_back("Gissel Gardea");
  ecen303names.push_back("Matthew David Grogan");
  ecen303names.push_back("Brandon Haskovec");
  ecen303names.push_back("Derek Heidtke");
  ecen303names.push_back("Tyler Henderson");
  ecen303names.push_back("Caleb Aaron-Rale Holley");
  ecen303names.push_back("Benjamin Johnston");
  ecen303names.push_back("Madeline Kinnaird");
  ecen303names.push_back("Benjamin Ledesma");
  ecen303names.push_back("Jordan Lewallen");
  ecen303names.push_back("Justin Tyler Lewis");
  ecen303names.push_back("Chu Ming Liang");
  ecen303names.push_back("Trevor Kyle Malota");
  ecen303names.push_back("Jonathan Moore");
  ecen303names.push_back("Shannon Morrissey");
  ecen303names.push_back("Bijan Nekovei");
  ecen303names.push_back("Katy Alaine Nix");
  ecen303names.push_back("Eric Niyigaba");
  ecen303names.push_back("Nirmal Pradipkumar Patel");
  ecen303names.push_back("Alejandro Penaloza Rodriguez");
  ecen303names.push_back("Colbie James Prestwood");
  ecen303names.push_back("Jacoby Prestwood");
  ecen303names.push_back("Wenkui Ren");
  ecen303names.push_back("Ruben Dario Rodriguez Espinoza");
  ecen303names.push_back("Christian Alberto Rodriguez Fuenmayor");
  ecen303names.push_back("Fernando Romo Diaz De Leon");
  ecen303names.push_back("Joshua Ruff");
  ecen303names.push_back("Stephen Michael Sattler");
  ecen303names.push_back("Rodney Connery Siders");
  ecen303names.push_back("Zachary Smadi");
  ecen303names.push_back("Michael Snowden");
  ecen303names.push_back("Eloi Fabian Tarango");
  ecen303names.push_back("Weston Torti");
  ecen303names.push_back("Clarissa Tovias");
  ecen303names.push_back("Charles Alexander Wallace");
  ecen303names.push_back("Fletcher Watts");
  ecen303names.push_back("Craig Wolf");
  ecen303names.push_back("Jesse Phillip Yancy");
  ecen303names.push_back("Seungwon Yoon");


  // initialize vector with grader names.
  vector<string> ecen303graders;
  ecen303graders = ecen303names;

  // generate a derangement using the rejection method.
  bool derangement = false;
  vector<string>::iterator niterator;
  vector<string>::iterator giterator;

  while (derangement == false) {
    // permute grader names using built-in random generator.
    random_shuffle ( ecen303graders.begin(), ecen303graders.end(), ngrandom);
    // checking that permuation is derangement.
    derangement = true;
    niterator = ecen303names.begin();
    giterator = ecen303graders.begin();
    while ((niterator != ecen303names.end()) && (derangement == true)) {
      if (*niterator == *giterator) {
        derangement = false;
      }
      niterator++;
      giterator++;
    }
  }

  cout << endl << "==== Graders and Students ===="  << endl << endl;
  giterator = ecen303graders.begin();
  for (string name : ecen303names) {
    cout << "Grader: " << *giterator << ";    Student: " << name << endl;
    giterator++;
  }
  cout << endl;

  cout << endl << "==== Students and Graders ===="  << endl << endl;
  giterator = ecen303graders.begin();
  for (string name : ecen303names) {
    cout << "Student: " << name << ";    Grader: " << *giterator << endl;
    giterator++;
  }
  cout << endl;
}

