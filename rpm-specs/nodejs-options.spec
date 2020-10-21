%global npm_name options
# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       Light-weight in-code option parser for nodejs
Name:          nodejs-%{npm_name}
Version:       0.0.6
Release:       12%{?dist}
License:       MIT
URL:           https://github.com/einaros/options.js
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(expect.js)
%endif
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
A very light-weight in-code option parser for nodejs.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib Makefile package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%if 0%{?enable_tests}
%check
make test
%endif

%files
%doc README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.0.6-5
- update ExclusiveArch and BuildRequires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 0.0.6-1
- Updated to latest release

* Wed Jan 22 2014 Troy Dawson <tdawson@redhat.com> - 0.0.5-4
- Add exclusivearch on EL6

* Fri Jan 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-3
- add macro to invoke dependency generator on EL6

* Wed Jun 19 2013 Troy Dawson <tdawson@redhat.com> - 0.0.5-2
- Bump release number up (#975859)

* Wed May 29 2013 Troy Dawson <tdawson@redhat.com> - 0.0.5-1
- Update to version 0.0.5

* Fri Mar 01 2013 Troy Dawson <tdawson@redhat.com> - 0.0.3-2
- Update spec to Fedora nodejs standards

* Wed Nov 14 2012 Troy Dawson <tdawson@redhat.com> - 0.0.3-1
- Initial build using tchor spec template

