%{?nodejs_find_provides_and_requires}

Name:           nodejs-pgpass
Version:        1.0.2
Release:        7%{?dist}
Summary:        Module for reading .pgpass

License:        MIT
URL:            https://www.npmjs.com/package/pgpass
Source0:        https://github.com/hoegaarden/pgpass/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  lsof

BuildRequires:  npm(mocha)
BuildRequires:  npm(pg-escape)
BuildRequires:  npm(resumer)
BuildRequires:  npm(split)
BuildRequires:  npm(tmp)
BuildRequires:  npm(which)


%description
This module tries to read the ~/.pgpass file (or the equivalent
for windows systems). If the environment variable PGPASSFILE is
set, this file is used instead. If everything goes right, the
password from said file is passed to the callback; if the password
cannot be read undefined is passed to the callback.


%prep
%autosetup -p 1 -n pgpass-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pgpass
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/pgpass
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
chmod 600 test/_pgpass
%{nodejs_sitelib}/mocha/bin/mocha -R list


%files
%doc README.md
%{nodejs_sitelib}/pgpass


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug  2 2016 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Mon Aug  1 2016 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Thu Jul 28 2016 Tom Hughes <tom@compton.nu> - 0.0.6-3
- Remove npm(split) fixdep

* Thu Jul 28 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.6-2
- Remove fixed dependency on older version of npm(split)
- Add require test to check section

* Tue Jun  7 2016 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Update to 0.0.6 upstream release

* Mon Jun  6 2016 Tom Hughes <tom@compton.nu> - 0.0.5-2
- Change license from BSD to MIT

* Mon Jun  6 2016 Tom Hughes <tom@compton.nu> - 0.0.5-1
- Update to 0.0.5 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Hughes <tom@compton.nu> - 0.0.3-2
- Correct license

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.0.3-1
- Initial build of 0.0.3
