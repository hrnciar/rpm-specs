Name:           nodejs-mapnik-pool
Version:        0.1.3
Release:        9%{?dist}
Summary:        Manage a pool of mapnik instances

License:        ISC
URL:            https://github.com/mapbox/mapnik-pool
Source0:        https://github.com/mapbox/mapnik-pool/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(generic-pool)
BuildRequires:  npm(mapnik)
BuildRequires:  npm(xtend)

%description
If you want to use node-mapnik in an app with concurrency, you'll
want to use a map pool.

Concurrently using a single map instance can crash your app, and
several map instances will give you a significant speedup. mapnik-pool
manages a generic-pool of mapnik.Map instances so you don't have to.


%prep
%setup -q -n mapnik-pool-%{version}
%nodejs_fixdep generic-pool "^2.0.3"
%nodejs_fixdep xtend "^4.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mapnik-pool
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/mapnik-pool
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/mapnik-pool


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 0.1.3-1
- Update to 0.1.3 upstream release

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 0.1.2-1
- Update to 0.1.2 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Tom Hughes <tom@compton.nu> - 0.1.1-1
- Update to 0.1.1 upstream release

* Tue Nov 25 2014 Tom Hughes <tom@compton.nu> - 0.1.0-2
- Add license text

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Initial build of 0.1.0
