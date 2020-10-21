%global modname grunt-sed

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

# tests are disabled until grunt-exec is packaged
%bcond_with tests

Name:           nodejs-%{modname}
Version:        0.1.1
Release:        11%{?dist}
Summary:        Grunt task for search and replace
License:        MIT
URL:            https://github.com/jharding/grunt-sed
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
%if %{with tests}
BuildRequires:  npm(replace)
BuildRequires:  npm(grunt-contrib-jshint)
BuildRequires:  npm(grunt-exec)
%endif

%description
Built on top of replace, grunt-sed is a Grunt plugin for performing search and 
replace on files.

%prep
%setup -q -n package
%nodejs_fixdep replace

%build
# nothing to do

%check
%if %{with tests}
%nodejs_symlink_deps --check
grunt test
%endif

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -pr package.json tasks/ %{buildroot}%{nodejs_sitelib}/%{modname}/
%nodejs_symlink_deps

%files
%doc README.md LICENSE-MIT
%{nodejs_sitelib}/%{modname}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 12 2014 Dan Callaghan <dcallagh@redhat.com> - 0.1.1-1
- initial version
