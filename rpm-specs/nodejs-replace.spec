%global modname replace

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

Name:           nodejs-%{modname}
Version:        1.1.1
Release:        4%{?dist}
Summary:        Command line search and replace utility using Nodejs
License:        MIT
URL:            https://github.com/ALMaclaine/replace
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
BuildRequires:  npm(yargs)
BuildRequires:  npm(colors)
BuildRequires:  npm(minimatch)

%description
replace is a command line utility for performing search-and-replace on files. 
It's similar to sed but there are a few differences:
* Modifies files when matches are found
* Recursive search on directories with -r
* Uses JavaScript syntax for regular expressions and replacement strings.

%prep
%setup -q -n package
%nodejs_fixdep yargs
%nodejs_fixdep colors
%nodejs_fixdep minimatch

%build
# nothing to do

%check
%nodejs_symlink_deps --check
tap test

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -pr package.json replace.js defaultignore bin/ \
    %{buildroot}%{nodejs_sitelib}/%{modname}/
# Not installing to /usr/bin for now, because search and replace both conflict 
# with existing packages:
# https://github.com/harthur/replace/issues/34
%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{modname}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Dan Callaghan <djc@djc.id.au> - 1.1.1-1
- upstream bug fix release 1.1.1: fixes -r recursive replacement

* Wed Aug 14 2019 Dan Callaghan <djc@djc.id.au> - 1.1.0-1
- new upstream release 1.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Dan Callaghan <dcallagh@redhat.com> - 1.0.0-1
- new upstream release with new maintainer

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-2
- using LICENSE file committed upstream

* Sun Oct 12 2014 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-1
- initial version
