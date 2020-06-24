Name:           nodejs-assert-plus
Version:        1.0.0
Release:        8%{?dist}
Summary:        Extra assertions on top of node's assert module
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# MIT license text in README.md
License:        MIT
URL:            https://github.com/mcavage/node-assert-plus
Source0:        https://github.com/mcavage/node-assert-plus/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  nodejs-packaging
BuildRequires:  npm(tape)

%description
This library is a super small wrapper over node's assert module that has two 
things: (1) the ability to disable assertions with the environment variable 
NODE_NDEBUG, and (2) some API wrappers for argument testing.

%prep
%setup -q -n node-assert-plus-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/assert-plus
cp -pr package.json assert.js %{buildroot}%{nodejs_sitelib}/assert-plus

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
tape tests/*.js

%files
%{nodejs_sitelib}/assert-plus
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 28 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-1
- update to 1.0.0

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.1.4-5
- Cleanup spec for newer guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-1
- new upstream release 0.1.4

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-2
- restrict to compatible arches

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- initial package
