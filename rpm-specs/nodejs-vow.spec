# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename vow

Name:               nodejs-vow
Version:            0.4.9
Release:            11%{?dist}
Summary:            Promises/A+ proposal compatible promises library

# https://github.com/dfilatov/vow/issues/67
License:            MIT and GPLv3
URL:                https://www.npmjs.org/package/vow
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      nodejs-uglify-js
BuildRequires:      nodejs-jspath
BuildRequires:      nodejs-istanbul
BuildRequires:      nodejs-promises-aplus-tests
BuildRequires:      nodejs-marked
BuildRequires:      nodejs-highlight-js
BuildRequires:      nodejs-nodeunit
BuildRequires:      nodejs-bem-jsd
BuildRequires:      nodejs-yate
%endif


%description
A Promises/A+ implementation.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/vow

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
./node_modules/istanbul/lib/cli.js test test/utils/runner.js
%endif

%files
%{nodejs_sitelib}/vow/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Ralph Bean <rbean@redhat.com> - 0.4.9-1
- new version

* Sat Mar 21 2015 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- new version

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- Latest upstream.
- Specify arch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Initial packaging for Fedora.
