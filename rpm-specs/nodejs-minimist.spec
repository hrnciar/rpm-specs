%{?nodejs_find_provides_and_requires}

# sometimes you might need to disable tests to get it to build since tap
# depends on this
%global enable_tests 1

Name:           nodejs-minimist
Version:        1.2.0
Release:        9%{?dist}
Summary:        Parse argument options in Node.js

License:        MIT
URL:            https://github.com/substack/minimist
Source0:        https://registry.npmjs.org/minimist/-/minimist-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
%endif

%description
%{summary}.

This module is the guts of nodejs-optimist's argument parser without all the 
fanciful decoration.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/minimist
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/minimist

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
%tap test/*.js
%endif

%files
%{nodejs_sitelib}/minimist
%doc readme.markdown example
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2.0-1
- Update to new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-2
- update to new nodejs standards

* Mon Aug 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package
