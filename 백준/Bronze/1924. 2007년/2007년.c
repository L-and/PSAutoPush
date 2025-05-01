#include <stdio.h>

void find_day(int total_days);

int main(void) {
	int x = 0, y = 0; //X:월 Y:일
	int total_days = 0;//1월1일~x월x일까지 일수

	scanf("%d %d", &x, &y);
	if (x <= 12 && x >= 1 && y <= 31 && y >= 1) {
		total_days += y; //총일수에 일수를더함
		switch (x-1) {
		case 12:
			total_days += 31;
		case 11:
			total_days += 30;
		case 10:
			total_days += 31;
		case 9:
			total_days += 30;
		case 8:
			total_days += 31;
		case 7:
			total_days += 31;
		case 6:
			total_days += 30;

		case 5:
			total_days += 31;
		case 4:
			total_days += 30;
		case 3:
			total_days += 31;
		case 2:
			total_days += 28;
		case 1:
			total_days += 31;
		}
	}

		find_day(total_days);

	return 0;
}

void find_day(int total_days) {
	int days = total_days; //요일
	char day[7][4] = {
		{"MON"},{"TUE"},{"WED"},{"THU"},{"FRI"},{"SAT"},{"SUN"}
	};
	while (days > 7) {
		days -= 7;
	}
	printf("%s", day[days-1]);
}