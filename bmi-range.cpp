#include <iostream>

using namespace std;

double BMI(double weight, double height);
void range(double BMI);

int main()
{
	double weight = 0;
	double height = 0;
	double BMInum = 0;

	BMInum = BMI(weight, height);
	range(BMInum);
	
	return 0;
}

/*Calculates BMI using metric values*/
double BMI(double weight, double height)
{
	double BMInum = 0;

	cout << "Enter weight (in kg): ";
	cin >> weight;
	cout << "Enter height (in m): ";
	cin >> height;
	cout << endl;

	BMInum = weight / (pow(height, 2));

	cout << "Your BMI is " << BMInum << endl;

	return BMInum;
}

/*Prints which range user is in*/
void range(double BMI)
{
	cout << "According to CDC guidelines, you are: ";

	if (BMI < 18.5)
	{
		cout << "Underweight";
	}
	else if (BMI >= 18.5 && BMI < 25)
	{
		cout << "Normal";
	}
	else if (BMI >= 25 && BMI < 30)
	{
		cout << "Overweight";
	}
	else if (BMI >= 30 && BMI < 35)
	{
		cout << "Obese Class 1";
	}
	else if (BMI >= 35 && BMI < 40)
	{
		cout << "Obese Class 2";
	}
	else if (BMI >= 40)
	{
		cout << "Obese Class 3 (Severe)";
	}
	else
	{
		cout << "Error";
	}

	cout << endl;
}
