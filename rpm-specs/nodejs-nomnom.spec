%global modname nomnom

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

Name:           nodejs-%{modname}
Version:        1.8.1
Release:        15%{?dist}
Summary:        Nodejs option parser with generated usage and commands
License:        MIT
URL:            https://github.com/harthur/nomnom
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(underscore)
BuildRequires:  npm(chalk)

%description
Nomnom is an option parser for Node. It noms your args and gives them back to 
you in a hash.

%prep
%setup -q -n package
%nodejs_fixdep chalk "1 - 2"
%nodejs_fixdep underscore "^1.6"

%build
# nothing to do

%check
%nodejs_symlink_deps --check
nodeunit test/*.js

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -p package.json nomnom.js %{buildroot}%{nodejs_sitelib}/%{modname}/
%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{modname}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.8.1-11
- Fix dependency on npm(underscore), thanks to RHBZ#1573064

* Mon Apr 30 2018 Dan Callaghan <dcallagh@redhat.com> - 1.8.1-10
- relax dependency on underscore further

* Mon Mar 12 2018 Dan Callaghan <dcallagh@redhat.com> - 1.8.1-9
- relax dependency on chalk

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Tom Hughes <tom@compton.nu> - 1.8.1-5
- Update npm(chalk) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Dan Callaghan <dcallagh@redhat.com> - 1.8.1-3
- enabled tests

* Wed Oct 07 2015 Dan Callaghan <dcallagh@redhat.com> - 1.8.1-2
- relaxed underscore version requirement

* Tue Sep 01 2015 Dan Callaghan <dcallagh@redhat.com> - 1.8.1-1
- upstream bug fix release 1.8.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 12 2014 Dan Callaghan <dcallagh@redhat.com> - 1.8.0-1
- initial version
