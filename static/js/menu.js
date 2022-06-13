document.addEventListener('DOMContentLoaded', function () {
	var elems = document.querySelectorAll('.sidenav');
	var instances = M.Sidenav.init(elems, {});
	M.AutoInit();
});

document.addEventListener('DOMContentLoaded', function () {
	var elems = document.querySelectorAll('.dropdown-trigger');
	var instances = M.Dropdown.init(elems, { constrainWidth: false, inDuration: 600 });
});

document.addEventListener('DOMContentLoaded', function () {
	var options = {
		format: 'dd/mm/yyyy',
		i18n: {
			monthsShort: [
				'Jan',
				'Fev',
				'Mar',
				'Abr',
				'Mai',
				'Jun',
				'Jul',
				'Ago',
				'Set',
				'Out',
				'Nov',
				'Dez',
			],
			weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
			weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
		},
	};
	var elems = document.querySelectorAll('.datepicker');
	var instances = M.Datepicker.init(elems, options);
});
