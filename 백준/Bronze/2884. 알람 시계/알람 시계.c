#include <stdio.h>



int main(void) {

	int h, m;

	scanf("%d %d", &h, &m);
	if (h >= 0 && h <= 23 && m >= 0 && m <= 59) {
		m = m - 45;
		if (m < 0) {
			m = 60+m;
			h--;
			if (h < 0) {
				h = 23;
			}
		}

		printf("%d %d", h, m);
	}
	return 0;
}