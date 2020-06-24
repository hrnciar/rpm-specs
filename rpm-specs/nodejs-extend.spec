Name:           nodejs-extend
Version:        3.0.2
Release:        3%{?dist}
Summary:        Port of jQuery.extend for node.js and the browser

License:        MIT
URL:            https://www.npmjs.org/package/extend
Source0:        https://github.com/justmoon/node-extend/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging >= 6

BuildRequires:  npm(tape)

%description
nodejs-extend is a port of the classic extend() method from jQuery. It behaves
as you expect.  It is simple, tried and true.


%prep
%autosetup -n node-extend-%{version}
%nodejs_fixdep --caret
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/extend
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/extend
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test/index.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/extend/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 3.0.2-1
- Update to 3.0.2 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.0-1
- new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- new version

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- Initial packaging for Fedora.
