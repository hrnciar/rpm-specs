Name:               nodejs-co
Epoch:              1
Version:            4.6.0
Release:            9%{?dist}
Summary:            Generator async flow control goodness

License:            MIT
URL:                https://www.npmjs.org/package/co
Source0:            https://github.com/tj/co/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:          noarch
ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(mocha)
BuildRequires:      npm(mz)

%description
Generator based flow-control goodness for nodejs and the browser, using
thunks _or_ promises, letting you write non-blocking code in a nice-ish
way.

%prep
%autosetup -n co-%{version}
%nodejs_fixdep --caret
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/co
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/co
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
mocha --harmony


%files
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/co


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Tom Hughes <tom@compton.nu> - 1:4.6.0-7
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 10 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1:4.6.0-1
- update to 4.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 1:3.1.0-1
- Downgrade to 3.1.0, 4.x needs node 0.12 which is not in Fedora

* Sat Jul 25 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 4.5.1-3
- fixdep npm(engine)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Ralph Bean <rbean@redhat.com> - 4.5.1-1
- new version

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 4.4.0-2
- Apply fixdep on npm(engine).

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 4.4.0-1
- new version

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 3.0.6-1
- Initial packaging for Fedora.
