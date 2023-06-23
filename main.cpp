// Jack Tench 2023
// ScoreTallyPlus

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Define class for counter.
class Counter
{
public:

	int count;

	Counter()
	{
		count = 0;
	}

	void up()
	{
		count++;
	}
	void down()
	{
		count--;
	}

	void reset()
	{
		count = 0;
	}

	int getCount()
	{
		return count;
	}

};

int main()
{
	
	cout << "ScoreTallyPlus" << endl;

	cout << "Select how many counters: ";
	string strInitCounters;
	int intInitCounters;
	cin >> strInitCounters;
	intInitCounters = stoi(strInitCounters);

	// Init vector of Counters.
	vector<Counter> counters(intInitCounters);

	// Main loop. Just runs until you kill the program.
	while (true)
	{

		string command;
		int vecIndex;

		// Take user command input.
		cout << "Command: ";
		cin >> command;

		if (command.find('+') != string::npos)
		{
			vecIndex = command.find_first_of("+");
			vecIndex = stoi(command.substr(0, vecIndex)) - 1;
			counters[vecIndex].up();
		}
		else if (command.find('-') != string::npos)
		{
			vecIndex = command.find_first_of("-");
			vecIndex = stoi(command.substr(0, vecIndex)) - 1;
			counters[vecIndex].down();
		}
		else if (command.find('r') != string::npos)
		{
			vecIndex = command.find_first_of("r");
			vecIndex = stoi(command.substr(0, vecIndex)) - 1;
			counters[vecIndex].reset();
		}
		else
		{
			cout << "Please enter a valid command." << endl;
		}

		// Print table.
		for (Counter current : counters)
		{

			int currentCounterCount = current.getCount();
			cout << currentCounterCount << endl;

		}

	}

	// end
	return 0;

}
