$fn=100;

difference() {
	cylinder(r1=10, r2=12, h=20);
	translate([0,0,2])
		cylinder(r1=8, r2=10, h=18.1);
}